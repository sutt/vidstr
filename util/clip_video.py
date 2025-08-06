import argparse
import sys

from moviepy import VideoFileClip


def clip_video(input_path: str, output_path: str, start: float, end: float):
    """
    Clips a video file between a start and end time.

    Args:
        input_path (str): Path to the input video file.
        output_path (str): Path to save the clipped video file.
        start (float): Start time of the clip in seconds.
        end (float): End time of the clip in seconds.
    """
    try:
        with VideoFileClip(input_path) as video:
            sub_clip = video.subclipped(start, end)
            sub_clip.write_videofile(output_path)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(description="Clip a video file.")
    parser.add_argument("input_path", type=str, help="Path to the input video file.")
    parser.add_argument("output_path", type=str, help="Path to the output video file.")
    parser.add_argument(
        "--start", type=float, required=True, help="Start time in seconds."
    )
    parser.add_argument(
        "--end", type=float, required=True, help="End time in seconds."
    )

    args = parser.parse_args()

    clip_video(args.input_path, args.output_path, args.start, args.end)


if __name__ == "__main__":
    main()
