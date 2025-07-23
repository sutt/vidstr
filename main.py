import argparse
import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types
from get_frame import get_frame
from client import get_client
# from PIL import Image

load_dotenv()


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


IMAGE_MODEL = "imagen-4.0-ultra-generate-preview-06-06"
VIDEO_MODEL = "veo-2.0-generate-001"


def generate_images(
    client: genai.Client, prompt: str, output_dir: str, number_of_images: int
):
    """Generates images from a prompt and saves them to a directory."""
    print(f"Generating {number_of_images} image(s) for prompt: '{prompt}'")

    os.makedirs(output_dir, exist_ok=True)

    response = client.models.generate_images(
        model=IMAGE_MODEL,
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=number_of_images,
        ),
    )

    for i, generated_image in enumerate(response.generated_images):
        image_path = os.path.join(output_dir, f"image_{i}.png")
        unique_image_path = get_unique_filepath(image_path)
        generated_image.image.save(unique_image_path)
        print(f"Saved image to {unique_image_path}")


def generate_video(
    client: genai.Client,
    prompt: str,
    output_dir: str,
    input_image_path: str | None,
    input_video_path: str | None,
):
    """Generates a video from a prompt and saves it to a directory."""
    print(f"Generating video for prompt: '{prompt}'")

    os.makedirs(output_dir, exist_ok=True)

    input_image = None
    if input_image_path:
        print(f"Using initial image from: {input_image_path}")
        input_image = types.Image.from_file(location=input_image_path)

    input_video = None
    if input_video_path:
        print(f"Using initial video from: {input_video_path}")
        input_video = types.Video.from_file(location=input_video_path)

    operation = client.models.generate_videos(
        model=VIDEO_MODEL,
        prompt=prompt,
        image=input_image,
        video=input_video,
    )

    print("Waiting for video generation to complete...")
    while not operation.done:
        time.sleep(10)
        operation = client.operations.get(operation)

    print("\n--- DEBUG: Operation object ---")
    print(operation)
    print("--- END DEBUG ---\n")

    if operation.error:
        print(f"ERROR: Video generation failed: {operation.error.message}")
        return

    if not operation.response:
        print("ERROR: Video generation completed but returned no response.")
        print(
            "This can happen if using Vertex AI with local files, which is not supported."
        )
        return

    is_vertex = os.environ.get("GOOGLE_GENAI_USE_VERTEXAI") == "true"

    if is_vertex:
        # For Vertex AI, the result is in `operation.result` and is a GCS URI.
        video = operation.result.generated_videos[0]
        print(f"Video generated at GCS URI: {video.video.uri}")
        print("Manual download required from the GCS bucket.")
    else:
        # For Gemini API, the result is in `operation.response` and is downloadable.
        video = operation.response.generated_videos[0]
        video_path = os.path.join(output_dir, "video.mp4")
        unique_video_path = get_unique_filepath(video_path)
        print(f"Downloading video to {unique_video_path}...")
        client.files.download(file=video.video)
        video.video.save(unique_video_path)
        print(f"Saved video to {unique_video_path}")


def continue_video(client: genai.Client, prompt: str, output_dir: str, input_video_path: str):
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
        default=1,
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

    if args.command == "image":
        generate_images(
            client=client,
            prompt=args.prompt,
            output_dir=args.output_dir,
            number_of_images=args.number_of_images,
        )
    elif args.command == "video":
        generate_video(
            client=client,
            prompt=args.prompt,
            output_dir=args.output_dir,
            input_image_path=args.input_image,
            input_video_path=args.input_video,
        )
    elif args.command == "continue-video":
        continue_video(
            client=client,
            prompt=args.prompt,
            output_dir=args.output_dir,
            input_video_path=args.input_video,
        )


if __name__ == "__main__":
    main()
