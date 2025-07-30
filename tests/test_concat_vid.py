"""
Tests for the concat_vid module.
"""

import os
import tempfile
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from concat_vid import (
    get_mp4_files_from_directory,
    validate_video_files,
    concatenate_videos,
    concat_videos_from_files,
    concat_videos_from_dir,
    main
)


class TestGetMp4FilesFromDirectory:
    """Test the get_mp4_files_from_directory function."""
    
    def test_nonexistent_directory(self):
        """Test with a directory that doesn't exist."""
        with pytest.raises(ValueError, match="Directory does not exist"):
            get_mp4_files_from_directory("/nonexistent/directory")
    
    def test_file_instead_of_directory(self):
        """Test with a file path instead of directory."""
        with tempfile.NamedTemporaryFile(suffix=".mp4") as tmp_file:
            with pytest.raises(ValueError, match="Path is not a directory"):
                get_mp4_files_from_directory(tmp_file.name)
    
    def test_empty_directory(self):
        """Test with a directory containing no MP4 files."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Create a non-MP4 file
            Path(tmp_dir) / "test.txt"
            with pytest.raises(ValueError, match="No MP4 files found"):
                get_mp4_files_from_directory(tmp_dir)
    
    def test_directory_with_mp4_files(self):
        """Test with a directory containing MP4 files."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Create test MP4 files
            files = ["vid-1.mp4", "vid-3.mp4", "vid-2.mp4", "not-video.txt"]
            for filename in files:
                (Path(tmp_dir) / filename).touch()
            
            result = get_mp4_files_from_directory(tmp_dir)
            
            # Should return only MP4 files, sorted alphabetically
            expected = [
                str(Path(tmp_dir) / "vid-1.mp4"),
                str(Path(tmp_dir) / "vid-2.mp4"),
                str(Path(tmp_dir) / "vid-3.mp4"),
            ]
            assert result == expected


class TestValidateVideoFiles:
    """Test the validate_video_files function."""
    
    def test_nonexistent_file(self):
        """Test with a file that doesn't exist."""
        with pytest.raises(ValueError, match="File does not exist"):
            validate_video_files(["/nonexistent/file.mp4"])
    
    def test_directory_instead_of_file(self):
        """Test with a directory path instead of file."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            with pytest.raises(ValueError, match="Path is not a file"):
                validate_video_files([tmp_dir])
    
    def test_valid_files(self):
        """Test with valid files."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Create test files
            file1 = Path(tmp_dir) / "test1.mp4"
            file2 = Path(tmp_dir) / "test2.mp4"
            file1.touch()
            file2.touch()
            
            result = validate_video_files([str(file1), str(file2)])
            
            # Should return absolute paths
            assert len(result) == 2
            assert str(file1.resolve()) in result
            assert str(file2.resolve()) in result
    
    def test_non_mp4_file_warning(self, capsys):
        """Test that non-MP4 files generate a warning."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "test.avi"
            file_path.touch()
            
            result = validate_video_files([str(file_path)])
            
            captured = capsys.readouterr()
            assert "Warning: File" in captured.out
            assert "is not an MP4 file" in captured.out
            assert len(result) == 1


class TestConcatenateVideos:
    """Test the concatenate_videos function."""
    
    def test_empty_video_list(self):
        """Test with empty video files list."""
        with pytest.raises(ValueError, match="No video files provided"):
            concatenate_videos([], "output.mp4")
    
    @patch('concat_vid.VideoFileClip')
    @patch('concat_vid.concatenate_videoclips')
    def test_single_video_warning(self, mock_concat, mock_clip, capsys):
        """Test warning when only one video is provided."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            video_file = Path(tmp_dir) / "test.mp4"
            video_file.touch()
            output_file = Path(tmp_dir) / "output.mp4"
            
            # Mock MoviePy components
            mock_video_clip = MagicMock()
            mock_clip.return_value = mock_video_clip
            mock_final_clip = MagicMock()
            mock_concat.return_value = mock_final_clip
            
            concatenate_videos([str(video_file)], str(output_file))
            
            captured = capsys.readouterr()
            assert "Warning: Only one video file provided" in captured.out
    
    @patch('concat_vid.VideoFileClip')
    @patch('concat_vid.concatenate_videoclips')
    def test_successful_concatenation(self, mock_concat, mock_clip):
        """Test successful video concatenation."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Create test files
            video1 = Path(tmp_dir) / "test1.mp4"
            video2 = Path(tmp_dir) / "test2.mp4"
            video1.touch()
            video2.touch()
            output_file = Path(tmp_dir) / "output.mp4"
            
            # Mock MoviePy components
            mock_video_clip = MagicMock()
            mock_clip.return_value = mock_video_clip
            mock_final_clip = MagicMock()
            mock_concat.return_value = mock_final_clip
            
            concatenate_videos([str(video1), str(video2)], str(output_file))
            
            # Verify MoviePy methods were called
            assert mock_clip.call_count == 2
            mock_concat.assert_called_once()
            mock_final_clip.write_videofile.assert_called_once()


class TestPublicFunctions:
    """Test the public API functions."""
    
    @patch('concat_vid.concatenate_videos')
    def test_concat_videos_from_files(self, mock_concat):
        """Test concat_videos_from_files function."""
        files = ["video1.mp4", "video2.mp4"]
        output = "output.mp4"
        
        concat_videos_from_files(files, output)
        
        mock_concat.assert_called_once_with(files, output)
    
    @patch('concat_vid.get_mp4_files_from_directory')
    @patch('concat_vid.concatenate_videos')
    def test_concat_videos_from_dir(self, mock_concat, mock_get_files):
        """Test concat_videos_from_dir function."""
        directory = "/test/dir"
        output = "output.mp4"
        mock_files = ["video1.mp4", "video2.mp4"]
        mock_get_files.return_value = mock_files
        
        concat_videos_from_dir(directory, output)
        
        mock_get_files.assert_called_once_with(directory)
        mock_concat.assert_called_once_with(mock_files, output)


class TestMainCLI:
    """Test the main CLI function."""
    
    @patch('concat_vid.concatenate_videos')
    @patch('sys.argv')
    def test_files_argument(self, mock_argv, mock_concat):
        """Test CLI with --files argument."""
        mock_argv.__getitem__.side_effect = lambda i: [
            'concat_vid.py', '--files', 'video1.mp4', 'video2.mp4'
        ][i]
        mock_argv.__len__.return_value = 4
        
        with tempfile.TemporaryDirectory() as tmp_dir:
            video1 = Path(tmp_dir) / "video1.mp4"
            video2 = Path(tmp_dir) / "video2.mp4"
            video1.touch()
            video2.touch()
            
            # Mock sys.argv for argparse
            with patch('sys.argv', ['concat_vid.py', '--files', str(video1), str(video2)]):
                result = main()
                
                assert result == 0
                mock_concat.assert_called_once()
    
    @patch('concat_vid.concat_videos_from_dir')
    @patch('sys.argv')
    def test_dir_argument(self, mock_argv, mock_concat_dir):
        """Test CLI with --dir argument."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            with patch('sys.argv', ['concat_vid.py', '--dir', tmp_dir]):
                result = main()
                
                assert result == 0
                mock_concat_dir.assert_called_once_with(tmp_dir, 'concatenated_video.mp4')
    
    
    @patch('concat_vid.concatenate_videos')
    def test_comma_separated_files(self, mock_concat):
        """Test CLI with comma-separated files."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            video1 = Path(tmp_dir) / "video1.mp4"
            video2 = Path(tmp_dir) / "video2.mp4"
            video1.touch()
            video2.touch()
            
            files_arg = f"{video1},{video2}"
            with patch('sys.argv', ['concat_vid.py', '--files', files_arg]):
                result = main()
                
                assert result == 0
                mock_concat.assert_called_once()
                call_args = mock_concat.call_args[0]
                assert len(call_args[0]) == 2  # Should have parsed 2 files
    
    def test_keyboard_interrupt(self):
        """Test CLI handles KeyboardInterrupt gracefully."""
        with patch('concat_vid.concatenate_videos', side_effect=KeyboardInterrupt):
            with tempfile.TemporaryDirectory() as tmp_dir:
                video = Path(tmp_dir) / "video.mp4"
                video.touch()
                
                with patch('sys.argv', ['concat_vid.py', '--files', str(video)]):
                    result = main()
                    assert result == 1