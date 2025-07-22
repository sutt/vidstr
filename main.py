import argparse
import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

load_dotenv()


IMAGE_MODEL = "imagen-4.0-ultra-generate-preview-06-06"
VIDEO_MODEL = "veo-2.0-generate-001"

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)


def generate_images(prompt: str, output_dir: str, number_of_images: int):
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
        generated_image.image.save(image_path)
        print(f"Saved image to {image_path}")


def generate_video(prompt: str, output_dir: str, input_image_path: str | None):
    """Generates a video from a prompt and saves it to a directory."""
    print(f"Generating video for prompt: '{prompt}'")

    os.makedirs(output_dir, exist_ok=True)

    input_image = None
    if input_image_path:
        print(f"Using initial image from: {input_image_path}")
        input_image = Image.open(input_image_path)

    operation = client.models.generate_videos(
        model=VIDEO_MODEL,
        prompt=prompt,
        image=input_image,
    )

    print("Waiting for video generation to complete...")
    while not operation.done:
        time.sleep(10)
        operation = client.operations.get(operation)

    video = operation.response.generated_videos[0]
    video_path = os.path.join(output_dir, "video.mp4")
    print(f"Downloading video to {video_path}...")
    client.files.download(file=video.video)
    video.video.save(video_path)
    print(f"Saved video to {video_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate images or video from a text prompt."
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
        "-o",
        "--output-dir",
        type=str,
        default="data/tmp",
        help="Directory to save generated video.",
    )

    args = parser.parse_args()

    if args.command == "image":
        generate_images(
            prompt=args.prompt,
            output_dir=args.output_dir,
            number_of_images=args.number_of_images,
        )
    elif args.command == "video":
        generate_video(
            prompt=args.prompt,
            output_dir=args.output_dir,
            input_image_path=args.input_image,
        )


if __name__ == "__main__":
    main()
