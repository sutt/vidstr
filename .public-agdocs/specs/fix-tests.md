Fix the tests, with output included below:

============================= test session starts ==============================
platform linux -- Python 3.12.11, pytest-8.4.1, pluggy-1.6.0
rootdir: /home/user/dev/smol-projs/vidstr
configfile: pyproject.toml
testpaths: tests
plugins: anyio-4.9.0
collected 4 items

tests/test_config.py FFFF                                                [100%]

=================================== FAILURES ===================================
______________ test_load_config_and_create_generate_videos_config ______________

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
>           assert loaded_config == config_data["video_generation"]
E           AssertionError: assert {'aspect_rati...': False, ...} == {'aspect_rati...': False, ...}
E             
E             Omitting 9 identical items, use -vv to show
E             Left contains 1 more item:
E             {'model': 'veo-2.0-generate-001'}
E             Use -v to get more diff

tests/test_config.py:39: AssertionError
----------------------------- Captured stdout call -----------------------------
Loading profile settings from: /tmp/tmp7a50y6w9.yaml
______________ test_load_config_and_create_generate_images_config ______________

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
>           assert loaded_config == config_data["image_generation"]
E           AssertionError: assert {'aspect_rati...e': 'ja', ...} == {'aspect_rati...e': 'ja', ...}
E             
E             Omitting 9 identical items, use -vv to show
E             Left contains 1 more item:
E             {'model': 'imagen-4.0-generate-preview-06-06'}
E             Use -v to get more diff

tests/test_config.py:87: AssertionError
----------------------------- Captured stdout call -----------------------------
Loading profile settings from: /tmp/tmpsl20d634.yaml
_________________________ test_load_config_empty_file __________________________

    def test_load_config_empty_file():
        """Tests loading an empty config file."""
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".yaml") as tmp:
            config_path = tmp.name
    
        try:
            loaded_config = load_config("video_generation", config_path)
>           assert loaded_config == {}
E           AssertionError: assert {'aspect_rati...ate-001', ...} == {}
E             
E             Left contains 5 more items:
E             {'aspect_ratio': '16:9',
E              'duration_seconds': 8,
E              'enhance_prompt': True,
E              'model': 'veo-2.0-generate-001',
E              'number_of_videos': 1}
E             Use -v to get more diff

tests/test_config.py:117: AssertionError
----------------------------- Captured stdout call -----------------------------
Loading profile settings from: /tmp/tmpjthsz39g.yaml
___________________________ test_load_config_no_file ___________________________

    def test_load_config_no_file():
        """Tests loading when config file does not exist."""
        loaded_config = load_config("video_generation", "non_existent_file.yaml")
>       assert loaded_config == {}
E       AssertionError: assert {'aspect_rati...ate-001', ...} == {}
E         
E         Left contains 5 more items:
E         {'aspect_ratio': '16:9',
E          'duration_seconds': 8,
E          'enhance_prompt': True,
E          'model': 'veo-2.0-generate-001',
E          'number_of_videos': 1}
E         Use -v to get more diff

tests/test_config.py:125: AssertionError
=========================== short test summary info ============================
FAILED tests/test_config.py::test_load_config_and_create_generate_videos_config
FAILED tests/test_config.py::test_load_config_and_create_generate_images_config
FAILED tests/test_config.py::test_load_config_empty_file - AssertionError: as...
FAILED tests/test_config.py::test_load_config_no_file - AssertionError: asser...
============================== 4 failed in 0.50s ===============================
