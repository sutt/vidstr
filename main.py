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
from client import get_client, download_from_gcs
# from PIL import Image

load_dotenv()


def load_config(
    section: str, profile_path: str | None = None, default_config_path="config.yaml"
):
    """Loads a config section from YAML files, with profile overriding defaults."""
    # Load defaults
    config = {}
    if os.path.exists(default_config_path):
        with open(default_config_path, "r") as f:
            default_yaml = yaml.safe_load(f)
            if default_yaml:
                config = default_yaml.get(section, {})

    # Load profile and override
    if profile_path and os.path.exists(profile_path):
        print(f"Loading profile settings from: {profile_path}")
        with open(profile_path, "r") as f:
            profile_yaml = yaml.safe_load(f)
            if profile_yaml:
                profile_section = profile_yaml.get(section, {})
                config.update(profile_section)

    return config


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




def generate_images(client: genai.Client, prompt: str, output_dir: str, config: dict):
    """Generates images from a prompt and saves them to a directory."""
    config = config.copy()
    image_model = config.pop("model", "imagen-4.0-generate-preview-06-06")
    number_of_images = config.get("number_of_images", 1)
    print(f"Generating {number_of_images} image(s) for prompt: '{prompt}'")

    os.makedirs(output_dir, exist_ok=True)

    response = client.models.generate_images(
        model=image_model,
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
    gcs_output_bucket: str,
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
    bucket_output_uri = f"{gcs_output_bucket}/{prefix}-{unique_id}"

    # Configure operation based on whether we're using Vertex AI
    video_config = config.copy()
    video_model = video_config.pop("model", "veo-2.0-generate-001")
    if last_frame:
        video_config["last_frame"] = last_frame

    if is_vertex:
        video_config["output_gcs_uri"] = bucket_output_uri
        operation = client.models.generate_videos(
            model=video_model,
            prompt=prompt,
            image=input_image,
            video=input_video,
            config=types.GenerateVideosConfig(**video_config),
        )
        print(f"Using bucket output: {bucket_output_uri}")
    else:
        operation = client.models.generate_videos(
            model=video_model,
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
        gcs_uri = video.video.uri
        print(f"Video generated and saved to GCS bucket: {gcs_uri}")

        video_path = os.path.join(output_dir, "video.mp4")
        unique_video_path = get_unique_filepath(video_path)
        print(f"Downloading video from GCS to {unique_video_path}...")
        download_from_gcs(gcs_uri, unique_video_path)
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
    gcs_output_bucket: str,
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
        gcs_output_bucket=gcs_output_bucket,
    )


def main():
    workspace_config = load_config("workspace_setting")
    gcs_output_bucket = workspace_config.get("gcs_output_bucket", "gs://default-bucket")
    local_output_dir = workspace_config.get("local_output_dir", "data/tmp")

    parser = argparse.ArgumentParser(
        description="Generate images or video from a text prompt."
    )
    parser.add_argument(
        "--vertex", action="store_true", help="Use Vertex AI instead of Gemini API."
    )
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        help="Path to a profile.yaml for custom configuration.",
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
        default=local_output_dir,
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
        default=local_output_dir,
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
        default=local_output_dir,
        help="Directory to save generated video and last frame.",
    )

    args = parser.parse_args()

    if args.vertex:
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "true"
    else:
        # CLI flag takes precedence, default to Gemini API
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "false"

    # Determine profile path
    profile_path = None
    if args.config:
        if os.path.exists(args.config):
            profile_path = args.config
        else:
            print(f"Warning: Specified profile file not found: {args.config}")
    else:
        # Search in output_dir then root
        search_paths = []
        if hasattr(args, "output_dir") and args.output_dir:
            search_paths.append(os.path.join(args.output_dir, "profile.yaml"))
        search_paths.append("profile.yaml")

        for p in search_paths:
            if os.path.exists(p):
                profile_path = p
                break

    client = get_client()
    video_config = load_config("video_generation", profile_path=profile_path)
    image_config = load_config("image_generation", profile_path=profile_path)

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
            gcs_output_bucket=gcs_output_bucket,
        )
    elif args.command == "continue-video":
        continue_video(
            client=client,
            prompt=args.prompt,
            output_dir=args.output_dir,
            input_video_path=args.input_video,
            config=video_config,
            gcs_output_bucket=gcs_output_bucket,
        )


if __name__ == "__main__":
    main()
