"""
Tests for the mp4_to_gif module.
"""

import os
import tempfile
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mp4_to_gif import (
    get_unique_filepath,
    validate_mp4_file,
    mp4_to_gif,
    main
)


class TestGetUniqueFilepath:
    """Test the get_unique_filepath function."""
    
    def test_nonexistent_file(self):
        """Test with a file that doesn't exist."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            filepath = os.path.join(tmp_dir, "test.gif")
            result = get_unique_filepath(filepath)
            assert result == filepath
    
    def test_existing_file(self):
        """Test with a file that exists."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Create an existing file
            existing_file = Path(tmp_dir) / "test.gif"
            existing_file.touch()
            
            result = get_unique_filepath(str(existing_file))
            
            # Should return path with counter
            expected = os.path.join(tmp_dir, "test-001.gif")
            assert result == expected
    
    def test_multiple_existing_files(self):
        """Test with multiple existing files with counters."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Create multiple existing files
            files = ["test.gif", "test-001.gif", "test-002.gif"]
            for filename in files:
                (Path(tmp_dir) / filename).touch()
            
            filepath = os.path.join(tmp_dir, "test.gif")
            result = get_unique_filepath(filepath)
            
            # Should return the next available counter
            expected = os.path.join(tmp_dir, "test-003.gif")
            assert result == expected


class TestValidateMp4File:
    """Test the validate_mp4_file function."""
    
    def test_nonexistent_file(self):
        """Test with a file that doesn't exist."""
        with pytest.raises(ValueError, match="File does not exist"):
            validate_mp4_file("/nonexistent/file.mp4")
    
    def test_directory_instead_of_file(self):
        """Test with a directory path instead of file."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            with pytest.raises(ValueError, match="Path is not a file"):
                validate_mp4_file(tmp_dir)
    
    def test_valid_mp4_file(self):
        """Test with a valid MP4 file."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "test.mp4"
            file_path.touch()
            
            result = validate_mp4_file(str(file_path))
            
            # Should return absolute path
            assert result == str(file_path.resolve())
    
    def test_non_mp4_file_warning(self, capsys):
        """Test that non-MP4 files generate a warning."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = Path(tmp_dir) / "test.avi"
            file_path.touch()
            
            result = validate_mp4_file(str(file_path))
            
            captured = capsys.readouterr()
            assert "Warning: File" in captured.out
            assert "is not an MP4 file" in captured.out
            assert result == str(file_path.resolve())


class TestMp4ToGif:
    """Test the mp4_to_gif function."""
    
    def test_nonexistent_input_file(self):
        """Test with input file that doesn't exist."""
        with pytest.raises(ValueError, match="File does not exist"):
            mp4_to_gif("/nonexistent/file.mp4", "output.gif")
    
    @patch('mp4_to_gif.VideoFileClip')
    def test_successful_conversion_without_fps(self, mock_clip):
        """Test successful MP4 to GIF conversion without fps parameter."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Create input and output files
            input_file = Path(tmp_dir) / "test.mp4"
            input_file.touch()
            output_file = Path(tmp_dir) / "output.gif"
            
            # Mock MoviePy VideoFileClip
            mock_video_clip = MagicMock()
            mock_clip.return_value = mock_video_clip
            
            # Mock output file creation
            with patch('os.path.exists', return_value=True), \
                 patch('os.path.getsize', return_value=1024):
                
                mp4_to_gif(str(input_file), str(output_file))
                
                # Verify MoviePy methods were called correctly
                mock_clip.assert_called_once_with(str(input_file.resolve()))
                mock_video_clip.write_gif.assert_called_once_with(str(output_file), loop=0)
                mock_video_clip.close.assert_called_once()
    
    @patch('mp4_to_gif.VideoFileClip')
    def test_successful_conversion_with_fps(self, mock_clip):
        """Test successful MP4 to GIF conversion with fps parameter."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Create input and output files
            input_file = Path(tmp_dir) / "test.mp4"
            input_file.touch()
            output_file = Path(tmp_dir) / "output.gif"
            
            # Mock MoviePy VideoFileClip
            mock_video_clip = MagicMock()
            mock_clip.return_value = mock_video_clip
            
            # Mock output file creation
            with patch('os.path.exists', return_value=True), \
                 patch('os.path.getsize', return_value=1024):
                
                mp4_to_gif(str(input_file), str(output_file), fps=2)
                
                # Verify MoviePy methods were called correctly with fps
                mock_clip.assert_called_once_with(str(input_file.resolve()))
                mock_video_clip.write_gif.assert_called_once_with(
                    str(output_file), fps=2, loop=0
                )
                mock_video_clip.close.assert_called_once()
    
    @patch('mp4_to_gif.VideoFileClip')
    def test_output_directory_creation(self, mock_clip):
        """Test that output directory is created if it doesn't exist."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Create input file
            input_file = Path(tmp_dir) / "test.mp4"
            input_file.touch()
            
            # Output in a subdirectory that doesn't exist
            output_subdir = Path(tmp_dir) / "subdir"
            output_file = output_subdir / "output.gif"
            
            # Mock MoviePy VideoFileClip
            mock_video_clip = MagicMock()
            mock_clip.return_value = mock_video_clip
            
            # Mock output file creation
            with patch('os.path.exists', return_value=True), \
                 patch('os.path.getsize', return_value=1024):
                
                mp4_to_gif(str(input_file), str(output_file))
                
                # Verify output directory was created
                assert output_subdir.exists()
                mock_video_clip.write_gif.assert_called_once()
    
    @patch('mp4_to_gif.VideoFileClip')
    def test_empty_output_file_error(self, mock_clip):
        """Test error when output file is empty."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            input_file = Path(tmp_dir) / "test.mp4"
            input_file.touch()
            output_file = Path(tmp_dir) / "output.gif"
            
            # Mock MoviePy VideoFileClip
            mock_video_clip = MagicMock()
            mock_clip.return_value = mock_video_clip
            
            # Mock empty output file
            with patch('os.path.exists', return_value=True), \
                 patch('os.path.getsize', return_value=0):
                
                with pytest.raises(RuntimeError, match="Output GIF file is empty"):
                    mp4_to_gif(str(input_file), str(output_file))
    
    @patch('mp4_to_gif.VideoFileClip')
    def test_conversion_failure(self, mock_clip):
        """Test handling of conversion failure."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            input_file = Path(tmp_dir) / "test.mp4"
            input_file.touch()
            output_file = Path(tmp_dir) / "output.gif"
            
            # Mock MoviePy VideoFileClip to raise an exception
            mock_clip.side_effect = Exception("MoviePy error")
            
            with pytest.raises(RuntimeError, match="Failed to convert MP4 to GIF"):
                mp4_to_gif(str(input_file), str(output_file))


class TestMainCLI:
    """Test the main CLI function."""
    
    @patch('mp4_to_gif.mp4_to_gif')
    @patch('mp4_to_gif.get_unique_filepath')
    def test_basic_conversion(self, mock_unique, mock_convert):
        """Test basic CLI conversion."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            input_file = Path(tmp_dir) / "test.mp4"
            input_file.touch()
            output_file = Path(tmp_dir) / "test.gif"
            
            mock_unique.return_value = str(output_file)
            
            with patch('sys.argv', ['mp4_to_gif.py', str(input_file)]):
                result = main()
                
                assert result == 0
                mock_convert.assert_called_once_with(str(input_file), str(output_file), None)
    
    @patch('mp4_to_gif.mp4_to_gif')
    @patch('mp4_to_gif.get_unique_filepath')
    def test_custom_output_and_fps(self, mock_unique, mock_convert):
        """Test CLI with custom output path and fps."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            input_file = Path(tmp_dir) / "test.mp4"
            input_file.touch()
            output_file = Path(tmp_dir) / "custom.gif"
            
            mock_unique.return_value = str(output_file)
            
            with patch('sys.argv', [
                'mp4_to_gif.py', str(input_file), 
                '--output', str(output_file), 
                '--fps', '2'
            ]):
                result = main()
                
                assert result == 0
                mock_convert.assert_called_once_with(str(input_file), str(output_file), 2)
    
    @patch.dict(os.environ, {'VIDSTR_CALLER_DIR': '/caller/dir'})
    @patch('mp4_to_gif.mp4_to_gif')
    @patch('mp4_to_gif.get_unique_filepath')
    def test_caller_dir_resolution(self, mock_unique, mock_convert):
        """Test VIDSTR_CALLER_DIR path resolution."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Use relative paths that should be resolved against VIDSTR_CALLER_DIR
            input_rel = "test.mp4"
            output_rel = "output.gif"
            
            # Expected absolute paths
            input_abs = "/caller/dir/test.mp4"
            output_abs = "/caller/dir/output.gif"
            
            mock_unique.return_value = output_abs
            
            with patch('sys.argv', [
                'mp4_to_gif.py', input_rel, 
                '--output', output_rel
            ]):
                result = main()
                
                assert result == 0
                mock_convert.assert_called_once_with(input_abs, output_abs, None)
    
    @patch('mp4_to_gif.mp4_to_gif')
    def test_conversion_error_handling(self, mock_convert):
        """Test CLI error handling."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            input_file = Path(tmp_dir) / "test.mp4"
            input_file.touch()
            
            # Mock conversion to raise an error
            mock_convert.side_effect = ValueError("Test error")
            
            with patch('sys.argv', ['mp4_to_gif.py', str(input_file)]):
                result = main()
                
                assert result == 1
    
    @patch('mp4_to_gif.mp4_to_gif')
    def test_keyboard_interrupt(self, mock_convert):
        """Test CLI handles KeyboardInterrupt gracefully."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            input_file = Path(tmp_dir) / "test.mp4"
            input_file.touch()
            
            # Mock conversion to raise KeyboardInterrupt
            mock_convert.side_effect = KeyboardInterrupt()
            
            with patch('sys.argv', ['mp4_to_gif.py', str(input_file)]):
                result = main()
                
                assert result == 1


# Integration test that can be marked as xfail if moviepy isn't working properly
@pytest.mark.xfail(reason="May fail if moviepy/system dependencies are not properly configured")
class TestIntegration:
    """Integration tests with actual video processing (marked as xfail)."""
    
    def test_actual_conversion_if_demo_exists(self):
        """Test actual conversion with demo file if it exists."""
        demo_path = Path(__file__).parent.parent / "docs" / "test-assets" / "demo.mp4"
        
        if demo_path.exists():
            with tempfile.TemporaryDirectory() as tmp_dir:
                output_path = Path(tmp_dir) / "test_output.gif"
                
                try:
                    mp4_to_gif(str(demo_path), str(output_path), fps=2)
                    
                    # Check if output file was created and has content
                    assert output_path.exists()
                    assert output_path.stat().st_size > 0
                    
                except Exception as e:
                    pytest.fail(f"Integration test failed: {e}")
        else:
            pytest.skip("Demo file not found")