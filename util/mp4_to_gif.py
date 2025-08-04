import argparse
import os

from moviepy import VideoFileClip


def convert_mp4_to_gif(mp4_path: str, gif_path: str, fps: int = 10):
    """Converts an mp4 video to a gif."""
    with VideoFileClip(mp4_path) as clip:
        clip.write_gif(gif_path, fps=fps, loop=0)


def main():
    """CLI for converting mp4 to gif."""
    parser = argparse.ArgumentParser(description="Convert an MP4 file to a GIF.")
    parser.add_argument("input_file", help="The input MP4 file path.")
    parser.add_argument(
        "-o",
        "--output_file",
        help="The output GIF file path. Defaults to input file with .gif extension.",
    )
    parser.add_argument(
        "--fps", type=int, default=10, help="Frames per second for the GIF."
    )
    args = parser.parse_args()

    output_file = args.output_file
    if not output_file:
        output_file = f"{os.path.splitext(args.input_file)[0]}.gif"

    try:
        convert_mp4_to_gif(args.input_file, output_file, args.fps)
        print(f"Successfully converted {args.input_file} to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
