import argparse
import os
import cv2


def get_frame(video_path: str, frame_type: str, output_path: str):
    """Extracts the first or last frame from a video and saves it as an image."""
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    if frame_type == "first":
        success, image = cap.read()
        if not success:
            print("Error: Could not read the first frame.")
            cap.release()
            return
    elif frame_type == "last":
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if frame_count == 0:
            print("Error: Video has no frames.")
            cap.release()
            return
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count - 1)
        success, image = cap.read()
        if not success:
            print("Error: Could not read the last frame.")
            cap.release()
            return
    else:
        # This case should not be reached if called from main() due to argparse choices.
        print(f"Error: Invalid frame type '{frame_type}'. Choose 'first' or 'last'.")
        cap.release()
        return

    cap.release()

    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    cv2.imwrite(output_path, image)
    print(f"Saved {frame_type} frame to {output_path}")


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
        help="Which frame to extract ('first' or 'last').",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Path to save the output image. Defaults to a path in the same directory as the video.",
    )
    args = parser.parse_args()

    if not args.output:
        video_dir = os.path.dirname(args.video_path)
        video_filename = os.path.splitext(os.path.basename(args.video_path))[0]
        args.output = os.path.join(
            video_dir, f"{video_filename}_{args.frame}_frame.png"
        )

    get_frame(args.video_path, args.frame, args.output)


if __name__ == "__main__":
    main()
