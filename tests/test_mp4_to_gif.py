import os
import tempfile
from unittest.mock import patch

from PIL import Image

from util.mp4_to_gif import convert_mp4_to_gif, main


class TestMp4ToGif:
    def test_convert_mp4_to_gif(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            input_file = "media/bitmap.mp4"
            output_file = os.path.join(tmpdir, "output.gif")

            convert_mp4_to_gif(input_file, output_file)

            assert os.path.exists(output_file)

            # Check if it's a valid GIF
            with Image.open(output_file) as img:
                assert img.format == "GIF"
                assert img.is_animated
                assert "loop" in img.info and img.info["loop"] == 0

    @patch("sys.argv", ["mp4_to_gif.py", "media/bitmap.mp4"])
    def test_main_cli_default_output(self):
        with patch("util.mp4_to_gif.convert_mp4_to_gif") as mock_convert:
            main()
            expected_output = "media/bitmap.gif"
            mock_convert.assert_called_once_with(
                "media/bitmap.mp4", expected_output, 10
            )
            if os.path.exists(expected_output):
                os.remove(expected_output)

    @patch("sys.argv", ["mp4_to_gif.py", "media/bitmap.mp4", "-o", "custom.gif"])
    def test_main_cli_custom_output(self):
        with patch("util.mp4_to_gif.convert_mp4_to_gif") as mock_convert:
            main()
            mock_convert.assert_called_once_with("media/bitmap.mp4", "custom.gif", 10)

    @patch("sys.argv", ["mp4_to_gif.py", "media/bitmap.mp4", "--fps", "15"])
    def test_main_cli_custom_fps(self):
        with patch("util.mp4_to_gif.convert_mp4_to_gif") as mock_convert:
            main()
            expected_output = "media/bitmap.gif"
            mock_convert.assert_called_once_with(
                "media/bitmap.mp4", expected_output, 15
            )
            if os.path.exists(expected_output):
                os.remove(expected_output)
