import argparse
import os
import cv2


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


def get_frame(
    video_path: str,
    output_path: str,
    frame_type: str | None = None,
    frame_num: int | None = None,
):
    """Extracts a specific frame from a video and saves it as an image."""
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if frame_count == 0:
        print("Error: Video has no frames.")
        cap.release()
        return

    target_frame = -1
    frame_desc = ""

    if frame_num is not None:
        if 0 <= frame_num < frame_count:
            target_frame = frame_num
            frame_desc = f"frame {frame_num}"
        else:
            print(
                f"Error: Invalid frame number {frame_num}. Video has {frame_count} frames (0 to {frame_count-1})."
            )
            cap.release()
            return
    elif frame_type == "first":
        target_frame = 0
        frame_desc = "first frame"
    elif frame_type == "last":
        target_frame = frame_count - 1
        frame_desc = "last frame"
    else:
        # This case should not be reached if called from main() due to argparse choices.
        print(f"Error: Invalid frame type '{frame_type}'. Choose 'first' or 'last'.")
        cap.release()
        return

    cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame)
    success, image = cap.read()
    if not success:
        print(f"Error: Could not read {frame_desc}.")
        cap.release()
        return

    cap.release()

    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    cv2.imwrite(output_path, image)
    print(f"Saved {frame_desc} to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Extract the first or last frame from a video."
    )
    parser.add_argument("video_path", type=str, help="Path to the input video file.")
    parser.add_argument(
        "--frame",
        type=str,
        choices=["first", "last"],
        default="first",
        help="Which frame to extract ('first' or 'last'). Is ignored if --num-frame is used.",
    )
    parser.add_argument(
        "-n",
        "--num-frame",
        type=int,
        help="Frame number to extract. Overrides --frame.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Path to save the output image. Defaults to a path in the same directory as the video.",
    )
    args = parser.parse_args()

    video_filename = os.path.splitext(os.path.basename(args.video_path))[0]
    if args.num_frame is not None:
        output_filename = f"{video_filename}_frame_{args.num_frame}.png"
    else:
        output_filename = f"{video_filename}_{args.frame}_frame.png"

    if not args.output:
        video_dir = os.path.dirname(args.video_path)
        args.output = os.path.join(video_dir, output_filename)
    elif os.path.isdir(args.output):
        args.output = os.path.join(args.output, output_filename)

    output_path = get_unique_filepath(args.output)
    if args.num_frame is not None:
        get_frame(args.video_path, output_path, frame_num=args.num_frame)
    else:
        get_frame(args.video_path, output_path, frame_type=args.frame)


if __name__ == "__main__":
    main()
