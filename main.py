import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


MODEL = "imagen-4.0-ultra-generate-preview-06-06"

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)


def generate_images(prompt: str, output_dir: str, number_of_images: int):
    """Generates images from a prompt and saves them to a directory."""
    print(f"Generating {number_of_images} image(s) for prompt: '{prompt}'")

    os.makedirs(output_dir, exist_ok=True)

    response = client.models.generate_images(
        model=MODEL,
        prompt=prompt,
        config=types.GenerateImagesConfig(
            number_of_images=number_of_images,
        ),
    )

    for i, generated_image in enumerate(response.generated_images):
        image_path = os.path.join(output_dir, f"image_{i}.png")
        generated_image.image.save(image_path)
        print(f"Saved image to {image_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate images from a text prompt.")
    parser.add_argument("prompt", type=str, help="The text prompt for image generation.")
    parser.add_argument(
        "-n",
        "--number-of-images",
        type=int,
        default=1,
        help="Number of images to generate.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=str,
        default="data/tmp",
        help="Directory to save generated images.",
    )
    args = parser.parse_args()

    generate_images(
        prompt=args.prompt,
        output_dir=args.output_dir,
        number_of_images=args.number_of_images,
    )


if __name__ == "__main__":
    main()
