import argparse
import os
import time
import uuid
import yaml
import json

from dotenv import load_dotenv
from google import genai
from google.genai import types
from get_frame import get_frame
from client import get_client
# from PIL import Image

load_dotenv()


def load_config(section: str, config_path="config.yaml"):
    """Loads a config section from a YAML file."""
    if not os.path.exists(config_path):
        return {}
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    if config is not None:
        return config.get(section, {})
    else:
        return {}


def get_unique_filepath(filepath):
    """
    If a file exists at the given path, appends an incremental counter
    to the filename until a unique path is found.
    e.g., 'image.png' -> 'image-0001.png', 'image-0002.png'
    """
    if not os.path.exists(filepath):
        return filepath

    directory, filename = os.path.split(filepath)
    name, ext = os.path.splitext(filename)
    counter = 1

    while True:
        new_filename = f"{name}-{counter:04d}{ext}"
        new_filepath = os.path.join(directory, new_filename)
        if not os.path.exists(new_filepath):
            return new_filepath
        counter += 1


IMAGE_MODEL = "imagen-4.0-generate-preview-06-06" 
VIDEO_MODEL = "veo-2.0-generate-001"


def generate_images(client: genai.Client, prompt: str, output_dir: str, config: dict):
    """Generates images from a prompt and saves them to a directory."""
    number_of_images = config.get("number_of_images", 1)
    print(f"Generating {number_of_images} image(s) for prompt: '{prompt}'")

    os.makedirs(output_dir, exist_ok=True)

    response = client.models.generate_images(
        model=IMAGE_MODEL,
        prompt=prompt,
        config=types.GenerateImagesConfig(**config),
    )

    mime_type_ext = {
        "image/png": ".png",
        "image/jpeg": ".jpg",
    }
    ext = mime_type_ext.get(config.get("output_mime_type"), ".png")

    for i, generated_image in enumerate(response.generated_images):
        image_path = os.path.join(output_dir, f"image_{i}{ext}")
        unique_image_path = get_unique_filepath(image_path)
        generated_image.image.save(unique_image_path)
        print(f"Saved image to {unique_image_path}")


def generate_video(
    client: genai.Client,
    prompt: str,
    output_dir: str,
    input_image_path: str | None,
    input_video_path: str | None,
    last_frame_path: str | None,
    config: dict,
):
    """Generates a video from a prompt and saves it to a directory."""
    print(f"Generating video for prompt: '{prompt}'")

    os.makedirs(output_dir, exist_ok=True)

    input_image = None
    if input_image_path:
        print(f"Using initial image from: {input_image_path}")
        input_image = types.Image.from_file(location=input_image_path)

    last_frame = None
    if last_frame_path:
        print(f"Using last frame from: {last_frame_path}")
        last_frame = types.Image.from_file(location=last_frame_path)

    input_video = None
    if input_video_path:
        print(f"Using initial video from: {input_video_path}")
        input_video = types.Video.from_file(location=input_video_path)

    is_vertex = os.environ.get("GOOGLE_GENAI_USE_VERTEXAI") == "true"
    
    # Generate unique filename for bucket output
    prefix = "video"
    if input_video_path:
        prefix = os.path.splitext(os.path.basename(input_video_path))[0]
    elif input_image_path:
        prefix = os.path.splitext(os.path.basename(input_image_path))[0]
    unique_id = str(uuid.uuid4())[:8]
    bucket_output_uri = f"gs://hello-world-123/{prefix}-{unique_id}"

    # Configure operation based on whether we're using Vertex AI
    video_config = config.copy()
    if last_frame:
        video_config["last_frame"] = last_frame

    if is_vertex:
        video_config["output_gcs_uri"] = bucket_output_uri
        operation = client.models.generate_videos(
            model=VIDEO_MODEL,
            prompt=prompt,
            image=input_image,
            video=input_video,
            config=types.GenerateVideosConfig(**video_config),
        )
        print(f"Using bucket output: {bucket_output_uri}")
    else:
        operation = client.models.generate_videos(
            model=VIDEO_MODEL,
            prompt=prompt,
            image=input_image,
            video=input_video,
            config=types.GenerateVideosConfig(**video_config),
        )

    print("Waiting for video generation to complete...")
    while not operation.done:
        time.sleep(10)
        operation = client.operations.get(operation)


    if operation.error:
        print(f"ERROR: Video generation failed: {json.dumps(operation.error)}")
        return

    if is_vertex:
        # For Vertex AI with bucket output, the video is in the GCS bucket
        video = operation.result.generated_videos[0]
        print(f"Video generated and saved to GCS bucket: {video.video.uri}")
        return
    else:
        # For Gemini API, check operation.response
        if not operation.response:
            print("ERROR: Video generation completed but returned no response.")
            return
            
        video = operation.response.generated_videos[0]
        video_path = os.path.join(output_dir, "video.mp4")
        unique_video_path = get_unique_filepath(video_path)
        print(f"Downloading video to {unique_video_path}...")
        client.files.download(file=video.video)
        video.video.save(unique_video_path)
        print(f"Saved video to {unique_video_path}")


def continue_video(
    client: genai.Client,
    prompt: str,
    output_dir: str,
    input_video_path: str,
    config: dict,
):
    """Continues a video from a prompt and an existing video."""
    print(f"Continuing video from '{input_video_path}' with prompt: '{prompt}'")

    os.makedirs(output_dir, exist_ok=True)

    last_frame_path = os.path.join(output_dir, "last_frame.png")
    print(f"Extracting last frame to {last_frame_path}...")
    get_frame(
        video_path=input_video_path, frame_type="last", output_path=last_frame_path
    )

    # Now call generate_video with the extracted frame
    generate_video(
        client=client,
        prompt=prompt,
        output_dir=output_dir,
        input_image_path=last_frame_path,
        input_video_path=None,
        last_frame_path=None,
        config=config,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Generate images or video from a text prompt."
    )
    parser.add_argument(
        "--vertex", action="store_true", help="Use Vertex AI instead of Gemini API."
    )
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="sub-command help"
    )

    # Image generation subcommand
    parser_image = subparsers.add_parser("image", help="Generate images.")
    parser_image.add_argument(
        "prompt", type=str, help="The text prompt for image generation."
    )
    parser_image.add_argument(
        "-n",
        "--number-of-images",
        type=int,
        default=None,
        help="Number of images to generate.",
    )
    parser_image.add_argument(
        "-o",
        "--output-dir",
        type=str,
        default="data/tmp",
        help="Directory to save generated images.",
    )

    # Video generation subcommand
    parser_video = subparsers.add_parser("video", help="Generate a video.")
    parser_video.add_argument(
        "prompt", type=str, help="The text prompt for video generation."
    )
    parser_video.add_argument(
        "-i",
        "--input-image",
        type=str,
        help="Path to an initial image for the video.",
    )
    parser_video.add_argument(
        "-v",
        "--input-video",
        type=str,
        help="Path to an initial video for video extension.",
    )
    parser_video.add_argument(
        "-l",
        "--last-frame",
        type=str,
        help="Path to an image to use as the last frame for interpolation.",
    )
    parser_video.add_argument(
        "-o",
        "--output-dir",
        type=str,
        default="data/tmp",
        help="Directory to save generated video.",
    )

    # Video continuation subcommand
    parser_continue_video = subparsers.add_parser(
        "continue-video", help="Continue a video from its last frame."
    )
    parser_continue_video.add_argument(
        "prompt", type=str, help="The text prompt for video generation."
    )
    parser_continue_video.add_argument(
        "-i",
        "--input-video",
        type=str,
        required=True,
        help="Path to an existing video to continue from.",
    )
    parser_continue_video.add_argument(
        "-o",
        "--output-dir",
        type=str,
        default="data/tmp",
        help="Directory to save generated video and last frame.",
    )

    args = parser.parse_args()

    if args.vertex:
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "true"
    else:
        # CLI flag takes precedence, default to Gemini API
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "false"

    client = get_client()
    video_config = load_config("video_generation")
    image_config = load_config("image_generation")

    if args.command == "image":
        if args.number_of_images is not None:
            image_config["number_of_images"] = args.number_of_images

        generate_images(
            client=client,
            prompt=args.prompt,
            output_dir=args.output_dir,
            config=image_config,
        )
    elif args.command == "video":
        generate_video(
            client=client,
            prompt=args.prompt,
            output_dir=args.output_dir,
            input_image_path=args.input_image,
            input_video_path=args.input_video,
            last_frame_path=args.last_frame,
            config=video_config,
        )
    elif args.command == "continue-video":
        continue_video(
            client=client,
            prompt=args.prompt,
            output_dir=args.output_dir,
            input_video_path=args.input_video,
            config=video_config,
        )


if __name__ == "__main__":
    main()
