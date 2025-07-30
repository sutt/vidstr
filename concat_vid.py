#!/usr/bin/env python3
"""
Video concatenation module using MoviePy.

This module can be used as a CLI script or imported for use in other modules.
It concatenates MP4 videos either from a list of specific files or from all
MP4 files in a directory.
"""

import argparse
import os
import sys
from pathlib import Path
from typing import List, Optional

try:
    from moviepy import VideoFileClip, concatenate_videoclips
except ImportError:
    print("Error: moviepy is required. Install it with: pip install moviepy")
    sys.exit(1)


def get_mp4_files_from_directory(directory: str) -> List[str]:
    """
    Get all MP4 files from a directory, sorted alphabetically.
    
    Args:
        directory: Path to the directory containing MP4 files
        
    Returns:
        List of MP4 file paths sorted alphabetically
        
    Raises:
        ValueError: If directory doesn't exist or contains no MP4 files
    """
    dir_path = Path(directory)
    if not dir_path.exists():
        raise ValueError(f"Directory does not exist: {directory}")
    
    if not dir_path.is_dir():
        raise ValueError(f"Path is not a directory: {directory}")
    
    mp4_files = sorted([
        str(f) for f in dir_path.glob("*.mp4")
        if f.is_file()
    ])
    
    if not mp4_files:
        raise ValueError(f"No MP4 files found in directory: {directory}")
    
    return mp4_files


def validate_video_files(file_paths: List[str]) -> List[str]:
    """
    Validate that all provided files exist and are accessible.
    
    Args:
        file_paths: List of video file paths to validate
        
    Returns:
        List of validated file paths
        
    Raises:
        ValueError: If any file doesn't exist or is not accessible
    """
    validated_files = []
    
    for file_path in file_paths:
        path = Path(file_path)
        if not path.exists():
            raise ValueError(f"File does not exist: {file_path}")
        
        if not path.is_file():
            raise ValueError(f"Path is not a file: {file_path}")
        
        # Check file extension
        if path.suffix.lower() != '.mp4':
            print(f"Warning: File {file_path} is not an MP4 file")
        
        validated_files.append(str(path.resolve()))
    
    return validated_files


def concatenate_videos(video_files: List[str], output_path: str, method: str = "chain") -> None:
    """
    Concatenate video files using MoviePy.
    
    Args:
        video_files: List of video file paths to concatenate
        output_path: Path for the output concatenated video
        method: MoviePy concatenation method ("chain" or "compose")
        
    Raises:
        ValueError: If video_files is empty or contains invalid files
        RuntimeError: If concatenation fails
    """
    if not video_files:
        raise ValueError("No video files provided for concatenation")
    
    if len(video_files) == 1:
        print("Warning: Only one video file provided. Output will be a copy of the input.")
    
    validated_files = validate_video_files(video_files)
    
    print(f"Concatenating {len(validated_files)} video files using method '{method}':")
    for i, file_path in enumerate(validated_files, 1):
        print(f"  {i}. {file_path}")
    
    clips = []
    try:
        # Load video clips
        for file_path in validated_files:
            print(f"Loading: {file_path}")
            clip = VideoFileClip(file_path)
            clips.append(clip)
        
        # Concatenate clips
        print("Concatenating videos...")
        final_clip = concatenate_videoclips(clips, method=method)
        
        # Write output
        print(f"Writing output to: {output_path}")
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        
        print(f"Successfully created concatenated video: {output_path}")
        
    except Exception as e:
        raise RuntimeError(f"Failed to concatenate videos: {str(e)}")
    
    finally:
        # Clean up clips to free memory
        for clip in clips:
            try:
                clip.close()
            except:
                pass
        try:
            final_clip.close()
        except:
            pass


def concat_videos_from_files(files: List[str], output: str = "concatenated_video.mp4") -> None:
    """
    Concatenate videos from a list of file paths.
    
    Args:
        files: List of video file paths in the order they should be concatenated
        output: Output file path for the concatenated video
    """
    concatenate_videos(files, output)


def concat_videos_from_dir(directory: str, output: str = "concatenated_video.mp4") -> None:
    """
    Concatenate all MP4 videos from a directory in alphabetical order.
    
    Args:
        directory: Directory containing MP4 files to concatenate
        output: Output file path for the concatenated video
    """
    mp4_files = get_mp4_files_from_directory(directory)
    concatenate_videos(mp4_files, output)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Concatenate MP4 video files using MoviePy",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --files video1.mp4,video2.mp4,video3.mp4
  %(prog)s --files video1.mp4 video2.mp4 video3.mp4 --output combined.mp4
  %(prog)s --dir /path/to/videos/ --output directory_concat.mp4
        """
    )
    
    # Mutually exclusive group for input source
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "--files",
        nargs='+',
        help="List of video files to concatenate (space-separated or comma-separated)"
    )
    input_group.add_argument(
        "--dir",
        help="Directory containing MP4 files to concatenate (alphabetical order)"
    )
    
    parser.add_argument(
        "--output", "-o",
        default="concatenated_video.mp4",
        help="Output file path (default: concatenated_video.mp4)"
    )
    
    parser.add_argument(
        "--method",
        choices=["chain", "compose"],
        default="chain",
        help="Concatenation method: 'chain' (simple) or 'compose' (handles different resolutions)"
    )
    
    args = parser.parse_args()
    
    try:
        if args.files:
            # Handle comma-separated input
            files = []
            for file_arg in args.files:
                if ',' in file_arg:
                    files.extend([f.strip() for f in file_arg.split(',') if f.strip()])
                else:
                    files.append(file_arg)
            
            if not files:
                print("Error: No valid files provided")
                return 1
            
            print(f"Concatenating {len(files)} files from command line arguments")
            concatenate_videos(files, args.output, args.method)
            
        elif args.dir:
            print(f"Concatenating all MP4 files from directory: {args.dir}")
            concat_videos_from_dir(args.dir, args.output)
        
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