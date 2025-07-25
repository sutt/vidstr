import os
import sys
import tempfile
import yaml
import pytest
from google.genai import types

# Add project root to path to allow importing main
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import load_config


def test_load_config_and_create_generate_videos_config():
    """
    Tests that the config loaded from YAML can be used to instantiate
    a GenerateVideosConfig object.
    """
    config_data = {
        "video_generation": {
            "number_of_videos": 2,
            "duration_seconds": 10,
            "aspect_ratio": "9:16",
            "enhance_prompt": False,
            # only for vertex-api
            "resolution": "720p",
            "person_generation": "disallow",
            "generate_audio": True,
            "fps": 30,
            "compression_quality": "OPTIMIZED",
        }
    }

    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".yaml") as tmp:
        yaml.dump(config_data, tmp)
        config_path = tmp.name

    try:
        loaded_config = load_config("video_generation", config_path)
        assert loaded_config == config_data["video_generation"]

        # Test instantiation of GenerateVideosConfig
        try:
            video_config_obj = types.GenerateVideosConfig(**loaded_config)
            assert video_config_obj.number_of_videos == 2
            assert video_config_obj.fps == 30
            assert video_config_obj.duration_seconds == 10
            assert video_config_obj.aspect_ratio == "9:16"
            assert video_config_obj.resolution == "720p"
            assert video_config_obj.person_generation == "disallow"
            assert not video_config_obj.enhance_prompt
            assert video_config_obj.generate_audio
            assert video_config_obj.compression_quality == "OPTIMIZED"
        except Exception as e:
            pytest.fail(
                f"Failed to instantiate GenerateVideosConfig with loaded config: {e}"
            )

    finally:
        os.remove(config_path)


def test_load_config_and_create_generate_images_config():
    """
    Tests that the config loaded from YAML can be used to instantiate
    a GenerateImagesConfig object.
    """
    config_data = {
        "image_generation": {
            "number_of_images": 2,
            "aspect_ratio": "4:3",
            "guidance_scale": 8.0,
            "seed": 12345,
            "negative_prompt": "blurry",
            "person_generation": "ALLOW_ADULT",
            "enhance_prompt": False,
            "output_mime_type": "image/jpeg",
            "language": "ja",
        }
    }

    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".yaml") as tmp:
        yaml.dump(config_data, tmp)
        config_path = tmp.name

    try:
        loaded_config = load_config("image_generation", config_path)
        assert loaded_config == config_data["image_generation"]

        # Test instantiation of GenerateImagesConfig
        try:
            image_config_obj = types.GenerateImagesConfig(**loaded_config)
            assert image_config_obj.number_of_images == 2
            assert image_config_obj.aspect_ratio == "4:3"
            assert image_config_obj.guidance_scale == 8.0
            assert image_config_obj.seed == 12345
            assert image_config_obj.negative_prompt == "blurry"
            assert image_config_obj.person_generation == "ALLOW_ADULT"
            assert not image_config_obj.enhance_prompt
            assert image_config_obj.output_mime_type == "image/jpeg"
            assert image_config_obj.language == "ja"
        except Exception as e:
            pytest.fail(
                f"Failed to instantiate GenerateImagesConfig with loaded config: {e}"
            )

    finally:
        os.remove(config_path)


def test_load_config_empty_file():
    """Tests loading an empty config file."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".yaml") as tmp:
        config_path = tmp.name

    try:
        loaded_config = load_config("video_generation", config_path)
        assert loaded_config == {}
    finally:
        os.remove(config_path)


def test_load_config_no_file():
    """Tests loading when config file does not exist."""
    loaded_config = load_config("video_generation", "non_existent_file.yaml")
    assert loaded_config == {}
