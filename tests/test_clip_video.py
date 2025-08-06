import os
import tempfile
from unittest.mock import patch
import pytest

from moviepy import VideoFileClip
import pytest

from util.clip_video import clip_video, main


class TestClipVideo:
    @pytest.mark.skip()
    def test_clip_video(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            input_file = "media/bitmap.mp4"
            output_file = os.path.join(tmpdir, "output.mp4")
            start_time = 1
            end_time = 3
            expected_duration = end_time - start_time

            clip_video(input_file, output_file, start_time, end_time)

            assert os.path.exists(output_file)

            with VideoFileClip(output_file) as clip:
                assert abs(clip.duration - expected_duration) < 0.1

    def test_main_cli(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            input_file = "media/bitmap.mp4"
            output_file = os.path.join(tmpdir, "output.mp4")
            start_time = "1"
            end_time = "3"

            with patch(
                "sys.argv",
                [
                    "clip_video.py",
                    input_file,
                    output_file,
                    "--start",
                    start_time,
                    "--end",
                    end_time,
                ],
            ):
                with patch("util.clip_video.clip_video") as mock_clip_video:
                    main()
                    mock_clip_video.assert_called_once_with(
                        input_file, output_file, float(start_time), float(end_time)
                    )
