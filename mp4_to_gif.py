#!/usr/bin/env python3
"""
MP4 to GIF conversion module using MoviePy.

This module can be used as a CLI script or imported for use in other modules.
It converts MP4 videos to GIF format with configurable frame rate and infinite loop.
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Optional

try:
    from moviepy import VideoFileClip
except ImportError:
    print("Error: moviepy is required. Install it with: pip install moviepy")
    sys.exit(1)


def get_unique_filepath(filepath: str) -> str:
    """
    If a file exists at the given path, appends an incremental counter
    to the filename until a unique path is found.
    e.g., 'demo.gif' -> 'demo-001.gif', 'demo-002.gif'
    """
    if not os.path.exists(filepath):
        return filepath

    directory, filename = os.path.split(filepath)
    name, ext = os.path.splitext(filename)
    counter = 1

    while True:
        new_filename = f"{name}-{counter:03d}{ext}"
        new_filepath = os.path.join(directory, new_filename)
        if not os.path.exists(new_filepath):
            return new_filepath
        counter += 1


def validate_mp4_file(file_path: str) -> str:
    """
    Validate that the provided file exists and is accessible.
    
    Args:
        file_path: Path to the MP4 file to validate
        
    Returns:
        Validated and resolved file path
        
    Raises:
        ValueError: If file doesn't exist or is not accessible
    """
    path = Path(file_path)
    if not path.exists():
        raise ValueError(f"File does not exist: {file_path}")
    
    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    # Check file extension
    if path.suffix.lower() != '.mp4':
        print(f"Warning: File {file_path} is not an MP4 file")
    
    return str(path.resolve())


def mp4_to_gif(input_path: str, output_path: str, fps: Optional[int] = None) -> None:
    """
    Convert MP4 video to GIF format using MoviePy.
    
    Args:
        input_path: Path to the input MP4 file
        output_path: Path for the output GIF file
        fps: Frame rate for the output GIF (optional)
        
    Raises:
        ValueError: If input file is invalid
        RuntimeError: If conversion fails
    """
    validated_input = validate_mp4_file(input_path)
    
    print(f"Converting MP4 to GIF:")
    print(f"  Input:  {validated_input}")
    print(f"  Output: {output_path}")
    if fps:
        print(f"  FPS:    {fps}")
    
    clip = None
    try:
        # Load video clip
        print("Loading video...")
        clip = VideoFileClip(validated_input)
        
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        
        # Convert to GIF with infinite loop
        print("Converting to GIF...")
        if fps:
            clip.write_gif(output_path, fps=fps, loop=0)
        else:
            clip.write_gif(output_path, loop=0)
        
        print(f"Successfully created GIF: {output_path}")
        
        # Check if output file was created and has content
        if os.path.exists(output_path):
            file_size = os.path.getsize(output_path)
            print(f"Output file size: {file_size} bytes")
            if file_size == 0:
                raise RuntimeError("Output GIF file is empty")
        else:
            raise RuntimeError("Output GIF file was not created")
        
    except Exception as e:
        raise RuntimeError(f"Failed to convert MP4 to GIF: {str(e)}")
    
    finally:
        # Clean up clip to free memory
        if clip:
            try:
                clip.close()
            except:
                pass


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Convert MP4 video files to GIF format using MoviePy",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.mp4
  %(prog)s input.mp4 --output output.gif
  %(prog)s input.mp4 --fps 2 --output slow.gif
        """
    )
    
    parser.add_argument(
        "input",
        help="Input MP4 file path"
    )
    
    parser.add_argument(
        "--output", "-o",
        help="Output GIF file path (default: same name as input with .gif extension)"
    )
    
    parser.add_argument(
        "--fps",
        type=int,
        help="Frame rate for the output GIF (optional, uses video's original fps if not specified)"
    )
    
    args = parser.parse_args()

    # Resolve relative paths against caller's directory
    if "VIDSTR_CALLER_DIR" in os.environ:
        caller_dir = os.environ["VIDSTR_CALLER_DIR"]
        
        # Resolve input path
        if args.input and not os.path.isabs(args.input):
            args.input = os.path.join(caller_dir, args.input)
        
        # Resolve output path
        if args.output and not os.path.isabs(args.output):
            args.output = os.path.join(caller_dir, args.output)
    
    # Set default output path if not provided
    if not args.output:
        input_path = Path(args.input)
        args.output = str(input_path.with_suffix('.gif'))
    
    # Use unique filepath to avoid overwriting
    unique_output = get_unique_filepath(args.output)
    
    try:
        mp4_to_gif(args.input, unique_output, args.fps)
        return 0
        
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
        return 1
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())