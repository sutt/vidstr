This file is a merged representation of the entire codebase, combined into a single document by Repomix.
The content has been processed where security check has been disabled.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Security check has been disabled - content may contain sensitive information
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
.github/
  ISSUE_TEMPLATE/
    bug-report.md
    feature-request.md
    question.md
  workflows/
    build-docs.yml
    codeql-analysis.yml
    formatting_linting.yml
    publish.yml
    test_suite.yml
    update-version.yml
  PULL_REQUEST_TEMPLATE.md
docs/
  _static/
    code/
      getting_started/
        moviepy_10_minutes/
          trailer.py
        quick_presentation/
          basic_example.py
      user_guide/
        compositing/
          CompositeAudioClip.py
          CompositeVideoClip.py
          concatenate.py
          crossfadein.py
          juxtaposing.py
          with_position.py
          with_start.py
        effects/
          custom_effect.py
          image_transform.py
          modify_copy_example.py
          time_transform.py
          transform.py
          using_effects.py
          using_with_methods.py
        loading/
          AudioArrayClip.py
          AudioClip.py
          AudioFileClip.py
          closing.py
          ColorClip.py
          DataVideoClip.py
          ImageClip.py
          ImageSequenceClip.py
          loading.py
          masks.py
          TextClip.py
          UpdatedVideoClip.py
          VideoClip.py
          VideoFileClip.py
        rendering/
          display_in_notebook.py
          preview.py
          save_frame.py
          show.py
          write_gif.py
          write_images_sequence.py
          write_videofile_duration.py
          write_videofile.py
    medias/
      index_api.svg
      index_contribute.svg
      index_getting_started.svg
      index_user_guide.svg
    moviepy.css
  _templates/
    custom_autosummary/
      class.rst
      module.rst
  _themes/
    .gitignore
  developer_guide/
    contribution_guidelines.rst
    developers_install.rst
    index.rst
    maintainers_publish.rst
  getting_started/
    docker.rst
    FAQ.rst
    index.rst
    install.rst
    moviepy_10_minutes.rst
    quick_presentation.rst
    updating_to_v2.rst
  reference/
    reference/
      moviepy.audio.AudioClip.AudioArrayClip.rst
      moviepy.audio.AudioClip.AudioClip.rst
      moviepy.audio.AudioClip.CompositeAudioClip.rst
      moviepy.audio.AudioClip.concatenate_audioclips.rst
      moviepy.audio.AudioClip.rst
      moviepy.audio.fx.AudioDelay.rst
      moviepy.audio.fx.AudioFadeIn.rst
      moviepy.audio.fx.AudioFadeOut.rst
      moviepy.audio.fx.AudioLoop.rst
      moviepy.audio.fx.AudioNormalize.rst
      moviepy.audio.fx.MultiplyStereoVolume.rst
      moviepy.audio.fx.MultiplyVolume.rst
      moviepy.audio.fx.rst
      moviepy.audio.io.AudioFileClip.AudioFileClip.rst
      moviepy.audio.io.AudioFileClip.rst
      moviepy.audio.io.ffmpeg_audiowriter.ffmpeg_audiowrite.rst
      moviepy.audio.io.ffmpeg_audiowriter.FFMPEG_AudioWriter.rst
      moviepy.audio.io.ffmpeg_audiowriter.rst
      moviepy.audio.io.ffplay_audiopreviewer.ffplay_audiopreview.rst
      moviepy.audio.io.ffplay_audiopreviewer.FFPLAY_AudioPreviewer.rst
      moviepy.audio.io.ffplay_audiopreviewer.rst
      moviepy.audio.io.readers.FFMPEG_AudioReader.rst
      moviepy.audio.io.readers.rst
      moviepy.audio.io.rst
      moviepy.audio.rst
      moviepy.audio.tools.cuts.find_audio_period.rst
      moviepy.audio.tools.cuts.rst
      moviepy.audio.tools.rst
      moviepy.Clip.Clip.rst
      moviepy.Clip.rst
      moviepy.config.check.rst
      moviepy.config.rst
      moviepy.config.try_cmd.rst
      moviepy.decorators.add_mask_if_none.rst
      moviepy.decorators.apply_to_audio.rst
      moviepy.decorators.apply_to_mask.rst
      moviepy.decorators.audio_video_effect.rst
      moviepy.decorators.convert_masks_to_RGB.rst
      moviepy.decorators.convert_parameter_to_seconds.rst
      moviepy.decorators.convert_path_to_string.rst
      moviepy.decorators.outplace.rst
      moviepy.decorators.preprocess_args.rst
      moviepy.decorators.requires_duration.rst
      moviepy.decorators.requires_fps.rst
      moviepy.decorators.rst
      moviepy.decorators.use_clip_fps_by_default.rst
      moviepy.Effect.rst
      moviepy.rst
      moviepy.tools.close_all_clips.rst
      moviepy.tools.convert_to_seconds.rst
      moviepy.tools.cross_platform_popen_params.rst
      moviepy.tools.deprecated_version_of.rst
      moviepy.tools.find_extension.rst
      moviepy.tools.no_display_available.rst
      moviepy.tools.rst
      moviepy.tools.subprocess_call.rst
      moviepy.video.compositing.CompositeVideoClip.clips_array.rst
      moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip.rst
      moviepy.video.compositing.CompositeVideoClip.concatenate_videoclips.rst
      moviepy.video.compositing.CompositeVideoClip.rst
      moviepy.video.compositing.rst
      moviepy.video.fx.AccelDecel.rst
      moviepy.video.fx.BlackAndWhite.rst
      moviepy.video.fx.Blink.rst
      moviepy.video.fx.Crop.rst
      moviepy.video.fx.CrossFadeIn.rst
      moviepy.video.fx.CrossFadeOut.rst
      moviepy.video.fx.EvenSize.rst
      moviepy.video.fx.FadeIn.rst
      moviepy.video.fx.FadeOut.rst
      moviepy.video.fx.Freeze.rst
      moviepy.video.fx.FreezeRegion.rst
      moviepy.video.fx.GammaCorrection.rst
      moviepy.video.fx.HeadBlur.rst
      moviepy.video.fx.InvertColors.rst
      moviepy.video.fx.Loop.rst
      moviepy.video.fx.LumContrast.rst
      moviepy.video.fx.MakeLoopable.rst
      moviepy.video.fx.Margin.rst
      moviepy.video.fx.MaskColor.rst
      moviepy.video.fx.MasksAnd.rst
      moviepy.video.fx.MasksOr.rst
      moviepy.video.fx.MirrorX.rst
      moviepy.video.fx.MirrorY.rst
      moviepy.video.fx.MultiplyColor.rst
      moviepy.video.fx.MultiplySpeed.rst
      moviepy.video.fx.Painting.rst
      moviepy.video.fx.Resize.rst
      moviepy.video.fx.Rotate.rst
      moviepy.video.fx.rst
      moviepy.video.fx.Scroll.rst
      moviepy.video.fx.SlideIn.rst
      moviepy.video.fx.SlideOut.rst
      moviepy.video.fx.SuperSample.rst
      moviepy.video.fx.TimeMirror.rst
      moviepy.video.fx.TimeSymmetrize.rst
      moviepy.video.io.display_in_notebook.display_in_notebook.rst
      moviepy.video.io.display_in_notebook.html_embed.rst
      moviepy.video.io.display_in_notebook.HTML2.rst
      moviepy.video.io.display_in_notebook.rst
      moviepy.video.io.ffmpeg_reader.ffmpeg_parse_infos.rst
      moviepy.video.io.ffmpeg_reader.ffmpeg_read_image.rst
      moviepy.video.io.ffmpeg_reader.FFMPEG_VideoReader.rst
      moviepy.video.io.ffmpeg_reader.FFmpegInfosParser.rst
      moviepy.video.io.ffmpeg_reader.rst
      moviepy.video.io.ffmpeg_tools.ffmpeg_extract_audio.rst
      moviepy.video.io.ffmpeg_tools.ffmpeg_extract_subclip.rst
      moviepy.video.io.ffmpeg_tools.ffmpeg_merge_video_audio.rst
      moviepy.video.io.ffmpeg_tools.ffmpeg_resize.rst
      moviepy.video.io.ffmpeg_tools.ffmpeg_stabilize_video.rst
      moviepy.video.io.ffmpeg_tools.rst
      moviepy.video.io.ffmpeg_writer.FFMPEG_VideoWriter.rst
      moviepy.video.io.ffmpeg_writer.ffmpeg_write_image.rst
      moviepy.video.io.ffmpeg_writer.ffmpeg_write_video.rst
      moviepy.video.io.ffmpeg_writer.rst
      moviepy.video.io.ffplay_previewer.ffplay_preview_video.rst
      moviepy.video.io.ffplay_previewer.FFPLAY_VideoPreviewer.rst
      moviepy.video.io.ffplay_previewer.rst
      moviepy.video.io.gif_writers.rst
      moviepy.video.io.gif_writers.write_gif_with_imageio.rst
      moviepy.video.io.ImageSequenceClip.ImageSequenceClip.rst
      moviepy.video.io.ImageSequenceClip.rst
      moviepy.video.io.rst
      moviepy.video.io.VideoFileClip.rst
      moviepy.video.io.VideoFileClip.VideoFileClip.rst
      moviepy.video.rst
      moviepy.video.tools.credits.CreditsClip.rst
      moviepy.video.tools.credits.rst
      moviepy.video.tools.cuts.detect_scenes.rst
      moviepy.video.tools.cuts.find_video_period.rst
      moviepy.video.tools.cuts.FramesMatch.rst
      moviepy.video.tools.cuts.FramesMatches.rst
      moviepy.video.tools.cuts.rst
      moviepy.video.tools.drawing.blit.rst
      moviepy.video.tools.drawing.circle.rst
      moviepy.video.tools.drawing.color_gradient.rst
      moviepy.video.tools.drawing.color_split.rst
      moviepy.video.tools.drawing.rst
      moviepy.video.tools.interpolators.Interpolator.rst
      moviepy.video.tools.interpolators.rst
      moviepy.video.tools.interpolators.Trajectory.rst
      moviepy.video.tools.rst
      moviepy.video.tools.subtitles.file_to_subtitles.rst
      moviepy.video.tools.subtitles.rst
      moviepy.video.tools.subtitles.SubtitlesClip.rst
      moviepy.video.VideoClip.BitmapClip.rst
      moviepy.video.VideoClip.ColorClip.rst
      moviepy.video.VideoClip.DataVideoClip.rst
      moviepy.video.VideoClip.ImageClip.rst
      moviepy.video.VideoClip.rst
      moviepy.video.VideoClip.TextClip.rst
      moviepy.video.VideoClip.UpdatedVideoClip.rst
      moviepy.video.VideoClip.VideoClip.rst
    index.rst
  user_guide/
    compositing.rst
    create_effects.rst
    index.rst
    loading.rst
    modifying.rst
    rendering.rst
  conf.py
  index.rst
  make.bat
  Makefile
  makehtml.sh
examples/
  soundtrack.py
media/
  doc_medias/
    example.txt
  subtitles-unicode.srt
  subtitles.srt
  traj.txt
moviepy/
  audio/
    fx/
      __init__.py
      AudioDelay.py
      AudioFadeIn.py
      AudioFadeOut.py
      AudioLoop.py
      AudioNormalize.py
      MultiplyStereoVolume.py
      MultiplyVolume.py
    io/
      __init__.py
      AudioFileClip.py
      ffmpeg_audiowriter.py
      ffplay_audiopreviewer.py
      readers.py
    tools/
      __init__.py
      cuts.py
    __init__.py
    AudioClip.py
  video/
    compositing/
      __init__.py
      CompositeVideoClip.py
    fx/
      __init__.py
      AccelDecel.py
      BlackAndWhite.py
      Blink.py
      Crop.py
      CrossFadeIn.py
      CrossFadeOut.py
      EvenSize.py
      FadeIn.py
      FadeOut.py
      Freeze.py
      FreezeRegion.py
      GammaCorrection.py
      HeadBlur.py
      InvertColors.py
      Loop.py
      LumContrast.py
      MakeLoopable.py
      Margin.py
      MaskColor.py
      MasksAnd.py
      MasksOr.py
      MirrorX.py
      MirrorY.py
      MultiplyColor.py
      MultiplySpeed.py
      Painting.py
      Resize.py
      Rotate.py
      Scroll.py
      SlideIn.py
      SlideOut.py
      SuperSample.py
      TimeMirror.py
      TimeSymmetrize.py
    io/
      __init__.py
      display_in_notebook.py
      errors.py
      ffmpeg_reader.py
      ffmpeg_tools.py
      ffmpeg_writer.py
      ffplay_previewer.py
      gif_writers.py
      ImageSequenceClip.py
      VideoFileClip.py
    tools/
      credits.py
      cuts.py
      drawing.py
      interpolators.py
      subtitles.py
    __init__.py
    VideoClip.py
  __init__.py
  Clip.py
  config.py
  decorators.py
  Effect.py
  tools.py
  version.py
tests/
  conftest.py
  README.rst
  test_AudioClips.py
  test_BitmapClip.py
  test_Clip.py
  test_compositing.py
  test_doc_examples.py
  test_ffmpeg_reader.py
  test_ffmpeg_tools.py
  test_ffmpeg_writer.py
  test_fx.py
  test_ImageSequenceClip.py
  test_issues.py
  test_PR.py
  test_SubtitlesClip.py
  test_TextClip.py
  test_tools.py
  test_VideoClip.py
  test_VideoFileClip.py
  test_videotools.py
.gitignore
.pre-commit-config.yaml
.readthedocs.yml
appveyor.yml
CHANGELOG.md
CONTRIBUTING.md
Dockerfile
LICENCE.txt
MANIFEST.in
pyproject.toml
README.md
setup.cfg
```

# Files

## File: .github/ISSUE_TEMPLATE/bug-report.md
````markdown
---
name: Bug Report
about: Report a bug with MoviePy
title: ''
labels: bug
assignees: ''

---

<!--
You can format code by putting ``` (that's 3 backticks) on a line by itself at the beginning and end of each code block. For example:

```
from moviepy import *
clip = ColorClip((600, 400), color=(255, 100, 0), duration=2)
```

Please, include runnable working example of code that can trigger the bug so we can easily reproduce and investigate the bug.
-->


#### Expected Behavior


#### Actual Behavior


#### Steps and code to Reproduce the Problem
<!-- Please include code that demonstrates this problem so that we can reproduce it. For advice on how to do this, see https://stackoverflow.com/help/mcve

It's higlhy helpfull if you can provide an exact and complete code reproducing the bug, *along with all necessary medias (videos, images, sounds, etc.).* 

Ideally you should provide a functional code snippet that maintainers can run to investigate the bug.
-->


#### Used medias
<!-- If you use any external media in the code triggering the bug, please include them in this issue so we can easily reproduce -->


#### Specifications

  - Python Version:
  - MoviePy Version:
  - Platform Name:
  - Platform Version:
````

## File: .github/ISSUE_TEMPLATE/feature-request.md
````markdown
---
name: Feature Request
about: Suggest an idea for MoviePy
title: ''
labels: feature-request
assignees: ''

---
````

## File: .github/ISSUE_TEMPLATE/question.md
````markdown
---
name: Question
about: Ask a question about an unexpected behavior of MoviePy
title: ''
labels: question
assignees: ''

---

<!--
If possible, please prioritize using discussions (https://github.com/Zulko/moviepy/discussions) or online forums for asking questions on how to use MoviePy, issues should be used mainly for questions about a specific behavior that seem incoherent and could possibly be a bug.
 
--------------------

You can format code by putting ``` (that's 3 backticks) on a line by itself at the beginning and end of each code block. For example:

```
from moviepy import *
clip = ColorClip((600, 400), color=(255, 100, 0), duration=2)
```
-->
````

## File: .github/workflows/build-docs.yml
````yaml
name: Build and Deploy Sphinx Documentation

on:
  push:
    branches:
      - "master" # Trigger on version tags

jobs:
  build-docs:
    # This job builds the documentation and deploys it to GitHub Pages
    # it is automatically triggered by the update-version job via the commit
    # made in the update-version job that contains the commit message
    # '[bot] Update version to <version>'
    if: startsWith(github.event.head_commit.message, '[bot] Update version to')
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'  # Specify Python version as needed

    - name: Build current documentation
      run: |
        git fetch --tags
        echo "Latest tag: $latest_tag"
        git checkout "$latest_tag"
        pip install -e .
        pip install -e ".[doc]"
        
        cd docs

        make html
        mkdir -p "../build/html/$latest_tag"
        cp -r build/html/* "../build/html/$latest_tag/"
        rm -rf build/html
        git stash

    - name: Install dependencies
      run: |
        git checkout master  
        python -m pip install --upgrade pip
        pip install -e .
        pip install -e .[doc]

    - name: Build current documentation
      run: |
        cd docs
        make html
        cp -r build/html/* ../build/html/

    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v4
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./build/html/  # Adjusted path since we're copying docs to root build directory
````

## File: .github/workflows/codeql-analysis.yml
````yaml
name: Code scanning with CodeQL

on:
  push:
    branches: [master]
  pull_request:
    # The branches below must be a subset of the branches above
    branches: [master]
  schedule:
    - cron: '0 3 * * 3'

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        # Override automatic language detection by changing the below list
        # Supported options are ['csharp', 'cpp', 'go', 'java', 'javascript', 'python']
        language: ['python']
        # Learn more...
        # https://docs.github.com/en/github/finding-security-vulnerabilities-and-errors-in-your-code/configuring-code-scanning#overriding-automatic-language-detection

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4.1.6

    # Initializes the CodeQL tools for scanning.
    - name: Initialize CodeQL
      uses: github/codeql-action/init@v3
      with:
        languages: ${{ matrix.language }}
        # If you wish to specify custom queries, you can do so here or in a config file.
        # By default, queries listed here will override any specified in a config file. 
        # Prefix the list here with "+" to use these queries and those in the config file.
        # queries: ./path/to/local/query, your-org/your-repo/queries@main

    # Autobuild attempts to build any compiled languages  (C/C++, C#, or Java).
    # If this step fails, then you should remove it and run the build manually (see below)
    - name: Autobuild
      uses: github/codeql-action/autobuild@v3

    # ℹ️ Command-line programs to run using the OS shell.
    # 📚 https://git.io/JvXDl

    # ✏️ If the Autobuild fails above, remove it and uncomment the following three lines
    #    and modify them (or add more) to build your code if your project
    #    uses a compiled language

    #- run: |
    #   make bootstrap
    #   make release

    - name: Perform CodeQL Analysis
      uses: github/codeql-action/analyze@v3
````

## File: .github/workflows/formatting_linting.yml
````yaml
# SPDX-FileCopyrightText: 2024 K Kollmann
# SPDX-License-Identifier: MIT

name: Code formatting and linting

on:
  pull_request:
  push:
    branches:
      - master
      - main
  workflow_dispatch:

env:
  PYTHON_VERSION: "3.9"

jobs:
  black:
    name: Black code formatter
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4.1.6
        with:
          ref: ${{ github.event.pull_request.head.sha }}
      - name: Run Black
        uses: psf/black@24.4.2
        with:
          options: "--version --check --diff --color" # default: "--check --diff"

  flake8:
    name: Flake8 linter
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4.1.6
        with:
          ref: ${{ github.event.pull_request.head.sha }}
      - name: Set up Python environment – ${{ env.PYTHON_VERSION }}
        uses: actions/setup-python@v5.1.0
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade wheel pip
          pip install .[lint]
      - name: Show Flake8 version
        run: flake8 --version
      - name: Run Flake8
        run: flake8 -v --show-source --ignore=E501 moviepy docs/conf.py examples tests

  isort:
    name: isort import sorter
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4.1.6
        with:
          ref: ${{ github.event.pull_request.head.sha }}
      - name: Set up Python environment – ${{ env.PYTHON_VERSION }}
        uses: actions/setup-python@v5.1.0
        with:
          python-version: ${{ env.PYTHON_VERSION }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade wheel pip
          pip install .[lint]
      - name: Run isort
        run: isort --check-only --diff moviepy scripts docs/conf.py examples tests
````

## File: .github/workflows/publish.yml
````yaml
name: Publish to PyPI

on:
  release:
    types: [published]
  workflow_dispatch:
    inputs:

permissions:
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: release
    permissions:
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip
      - name: Install dependencies
        run: |
          pip install setuptools wheel build

      - name: Build
        run: |
          python -m build
      - name: Publish
        uses: pypa/gh-action-pypi-publish@release/v1
````

## File: .github/workflows/test_suite.yml
````yaml
# This workflow installs Python dependencies, runs tests and lints
# using a variety of Python versions.
# For more information see:
# https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Run Test Suite

on:
  push:
    branches:
      - master
  pull_request:

jobs:
  # Uses Python Framework build because on macOS, Matplotlib requires it
  macos:
    runs-on: macos-13
    # Do not ignore bash profile files. From:
    # https://github.com/marketplace/actions/setup-miniconda
    defaults:
      run:
        shell: bash -l {0}
    strategy:
      matrix:
        python-version: ["3.9", "3.10", "3.11"]
    steps:
    - uses: actions/checkout@v4.1.6
    - uses: conda-incubator/setup-miniconda@v3
      with:
        auto-update-conda: true
        python-version: ${{ matrix.python-version }}
        auto-activate-base: true

    - name: Install pythonw
      run: conda install python.app

    - name: Python Version Info
      run: |
        pythonw --version
        which python
        pythonw -m site --user-site
        echo $PYTHONPATH
        echo $PYTHONHOME

    - name: Install dependencies
      run: |
        # needed for installing matplotlib
        brew install pkg-config
        python -m pip install --upgrade wheel setuptools coveralls
        python -m pip install ".[test, optional]"

    - name: Test with pytest
      run: |
        pythonw -m pytest --doctest-glob "moviepy/**/**.py" -v --cov moviepy --cov-report term-missing


  windows:
    runs-on: windows-latest
    strategy:
      matrix:
        python-version: ["3.9", "3.10", "3.11"]
      fail-fast: false
    steps:
      - uses: actions/checkout@v4.1.6
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5.1.0
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade wheel setuptools coveralls
          python -m pip install ".[test]"

      - name: Check third party dependencies
        run: |
          python moviepy\config.py

      - name: PyTest
        shell: cmd
        run: |
          python -m pytest --cov moviepy --cov-report term-missing

  linux:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.9", "3.10", "3.11"]
      fail-fast: false
    steps:
      - uses: actions/checkout@v4.1.6

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5.1.0
        with:
          python-version: ${{ matrix.python-version }}

      - name: Python Version Info
        run: |
          python --version
          which python
          python -m site --user-site

      - name: Install common requirements
        run: |
          python -m pip install --upgrade wheel setuptools

      - name: Install test requirements
        if: ${{ matrix.python-version == '3.7' }}
        run: |
          python -m pip install ".[test, doc]"
          python -m pip install python-dotenv

      - name: Install test and optional requirements
        if: ${{ matrix.python-version != '3.7' }}
        run: |
          python -m pip install ".[test, optional, doc]"

      - name: PyTest
        run: |
          python -m pytest --doctest-glob "moviepy/**/**.py" --cov moviepy --cov-report term-missing

      - name: Test pip installation
        run: |
          pip install -e .
          pip install -e .[optional]
          pip install -e .[test]
          pip install -e .[doc]
````

## File: .github/workflows/update-version.yml
````yaml
name: Update Version on Tag

on:
  push:
    tags:
      - 'v*.*.*'  # Trigger on version tags

jobs:
  update-version:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0  # ensures tags are fetched

      - name: Extract version from tag
        id: get_version
        run: |
          TAG=${GITHUB_REF#refs/tags/}
          VERSION=${TAG#v}
          echo "version=$VERSION" >> $GITHUB_OUTPUT

      - name: Update version in pyproject.toml
        run: |
          sed -i "s/^version = \".*\"/version = \"${{ steps.get_version.outputs.version }}\"/" pyproject.toml

      - name: Update __version__ in source code
        run: |
          VERSION=${{ steps.get_version.outputs.version }}
          sed -i "s/^__version__ = \".*\"/__version__ = \"${VERSION}\"/" moviepy/version.py

      - name: Update version in docs/conf.py
        run: |  
          VERSION=${{ steps.get_version.outputs.version }}
          sed -i "s/^version = \".*\"/version = \"${VERSION}\"/" docs/conf.py

      - name: Commit and push changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "moviepy[bot]@users.noreply.github.com"
          git commit -am "[bot] Update version to ${{ steps.get_version.outputs.version }}"
          git push origin HEAD:${GITHUB_REF_NAME}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
````

## File: .github/PULL_REQUEST_TEMPLATE.md
````markdown
<!--
Please tick when you have done these. They don't need to all be completed before the PR is submitted.
Delete them if they are not appropriate for this pull request.
-->
- [ ] I have provided code that clearly demonstrates the bug and that only works correctly when applying this fix
- [ ] I have added suitable tests demonstrating a fixed bug or new/changed feature to the test suite in `tests/`
- [ ] I have properly documented new or changed features in the documentation or in the docstrings
- [ ] I have properly explained unusual or unexpected code in the comments around it
````

## File: docs/_static/code/getting_started/moviepy_10_minutes/trailer.py
````python
# Lets import moviepy, lets also import numpy we will use it a some point
import numpy as np

from moviepy import *


#################
# VIDEO LOADING #
#################
# We load our video
video = VideoFileClip("./resources/bbb.mp4")


#####################
# SCENES EXTRACTION #
#####################
# We extract the scenes we want to use

# First the characters
intro_clip = video.subclipped(1, 11)
bird_clip = video.subclipped(16, 20)
bunny_clip = video.subclipped(37, 55)
rodents_clip = video.subclipped(
    "00:03:34.75", "00:03:56"
)  # we can also use string notation with format HH:MM:SS.uS
rambo_clip = video.subclipped("04:41.5", "04:44.70")


#####################
# SCENES PREVIEWING #
#####################
# Now, lets have a first look at our clips
# Warning: you need ffplay installed for preview to work
# We set a low fps so our machine can render in real time without slowing down
intro_clip.preview(fps=20)
bird_clip.preview(fps=20)
bunny_clip.preview(fps=20)
rodents_clip.preview(fps=20)
rambo_clip.preview(fps=20)


##############################
# CLIPS MODIFICATION CUTTING #
##############################
# Well, looking at the rodent scene it is a bit long isn't?
# Let's see how we modify the clip with one of the many clip manipulation method starting by with_*
# in that case by removing of the clip the part between 00:06:00 to 00:10:00 of the clip, using with_section_cut_out
rodents_clip = rodents_clip.with_section_cut_out(start_time=4, end_time=10)

# Note: You may have noticed that we have reassign rodents_clip, this is because all with_* methods return a modified *copy* of the
# original clip instead of modifying it directly. In MoviePy any function starting by with_* is out-place instead of in-place
# meaning it does not modify the original data, but instead copy it and modify/return the copy

# Lets check the result
rodents_clip.preview(fps=10)

############################
# TEXT/LOGO CLIPS CREATION #
############################
# Lets create the texts to put between our clips
font = "./resources/font/font.ttf"
intro_text = TextClip(
    font=font,
    text="The Blender Foundation and\nPeach Project presents",
    font_size=50,
    color="#fff",
    text_align="center",
)
bird_text = TextClip(font=font, text="An unlucky bird", font_size=50, color="#fff")
bunny_text = TextClip(
    font=font, text="A (slightly overweight) bunny", font_size=50, color="#fff"
)
rodents_text = TextClip(
    font=font, text="And three rodent pests", font_size=50, color="#fff"
)
revenge_text = TextClip(
    font=font, text="Revenge is coming...", font_size=50, color="#fff"
)
made_with_text = TextClip(font=font, text="Made with", font_size=50, color="#fff")

# We will also need the big buck bunny logo, so lets load it and resize it
logo_clip = ImageClip("./resources/logo_bbb.png").resized(width=400)
moviepy_clip = ImageClip("./resources/logo_moviepy.png").resized(width=300)


################
# CLIPS TIMING #
################
# We have all the clips we need, but if we was to turn all the clips into a single one with composition (we will see that during next step)
# all our clips would start at the same time and play on top of each other, which is obviously not what we want.
# To fix that, we need to say when a clip should start and stop in the final clip.
# So, lets start by telling when each clip must start and end with appropriate with_* methods
intro_text = intro_text.with_duration(6).with_start(
    3
)  # Intro for 6 seconds, start after 3 seconds
logo_clip = logo_clip.with_start(intro_text.start + 2).with_end(
    intro_text.end
)  # Logo start 2 second after intro text and stop with it
bird_clip = bird_clip.with_start(
    intro_clip.end
)  # Make bird clip start after intro, duration already known
bird_text = bird_text.with_start(bird_clip.start).with_end(
    bird_clip.end
)  # Make text synchro with clip
bunny_clip = bunny_clip.with_start(bird_clip.end)  # Make bunny clip follow bird clip
bunny_text = bunny_text.with_start(bunny_clip.start + 2).with_duration(7)
rodents_clip = rodents_clip.with_start(bunny_clip.end)
rodents_text = rodents_text.with_start(rodents_clip.start).with_duration(4)
rambo_clip = rambo_clip.with_start(rodents_clip.end - 1.5)
revenge_text = revenge_text.with_start(rambo_clip.start + 1.5).with_duration(4)
made_with_text = made_with_text.with_start(rambo_clip.end).with_duration(3)
moviepy_clip = moviepy_clip.with_start(made_with_text.start).with_duration(3)


########################
# CLIPS TIMING PREVIEW #
########################
# Lets make a first compositing of the clips into one single clip and do a quick preview to see if everything is synchro

quick_compo = CompositeVideoClip(
    [
        intro_clip,
        intro_text,
        logo_clip,
        bird_clip,
        bird_text,
        bunny_clip,
        bunny_text,
        rodents_clip,
        rodents_text,
        rambo_clip,
        revenge_text,
        made_with_text,
        moviepy_clip,
    ]
)
quick_compo.preview(fps=10)


######################
# CLIPS POSITIONNING #
######################
# Now that we have set the timing of our different clips, we need to make sure they are in the right position
# We will keep things simple, and almost always set center center for every texts
bird_text = bird_text.with_position(("center", "center"))
bunny_text = bunny_text.with_position(("center", "center"))
rodents_text = rodents_text.with_position(("center", "center"))
revenge_text = revenge_text.with_position(("center", "center"))

# For the logos and intro/end, we will use pixel position instead of center
top = intro_clip.h // 2
intro_text = intro_text.with_position(("center", 200))
logo_clip = logo_clip.with_position(("center", top))
made_with_text = made_with_text.with_position(("center", 300))
moviepy_clip = moviepy_clip.with_position(("center", 360))

# Lets take another look to check positions
quick_compo = CompositeVideoClip(
    [
        intro_clip,
        intro_text,
        logo_clip,
        bird_clip,
        bird_text,
        bunny_clip,
        bunny_text,
        rodents_clip,
        rodents_text,
        rambo_clip,
        revenge_text,
        made_with_text,
        moviepy_clip,
    ]
)
quick_compo.preview(fps=10)


################################
# CLIPS TRANSITION AND EFFECTS #
################################
# Now that our clip are timed and positionned, lets add some transition to make it more natural
# To do so we use the with_effects method and the video effects in vfx
# We call with_effects on our clip and pass it an array of effect objects to apply
# We'll keep it simple, nothing fancy just cross fading
intro_text = intro_text.with_effects([vfx.CrossFadeIn(1), vfx.CrossFadeOut(1)])
logo_clip = logo_clip.with_effects([vfx.CrossFadeIn(1), vfx.CrossFadeOut(1)])
bird_text = bird_text.with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
bunny_text = bunny_text.with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
rodents_text = rodents_text.with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])

# Also add cross fading on video clips and video clips audio
# See how video effects are under vfx and audio ones under afx
intro_clip = intro_clip.with_effects(
    [vfx.FadeIn(1), vfx.FadeOut(1), afx.AudioFadeIn(1), afx.AudioFadeOut(1)]
)
bird_clip = bird_clip.with_effects(
    [vfx.FadeIn(1), vfx.FadeOut(1), afx.AudioFadeIn(1), afx.AudioFadeOut(1)]
)
bunny_clip = bunny_clip.with_effects(
    [vfx.FadeIn(1), vfx.FadeOut(1), afx.AudioFadeIn(1), afx.AudioFadeOut(1)]
)
rodents_clip = rodents_clip.with_effects(
    [
        vfx.FadeIn(1),
        vfx.CrossFadeOut(1.5),
        afx.AudioFadeIn(1),
        afx.AudioFadeOut(1.5),
    ]
)  # Just fade in, rambo clip will do the cross fade
rambo_clip = rambo_clip.with_effects(
    [
        vfx.CrossFadeIn(1.5),
        vfx.FadeOut(1),
        afx.AudioFadeIn(1.5),
        afx.AudioFadeOut(1),
    ]
)
rambo_clip = rambo_clip.with_effects(
    [
        vfx.CrossFadeIn(1.5),
        vfx.FadeOut(1),
        afx.AudioFadeIn(1.5),
        afx.AudioFadeOut(1),
    ]
)

# Effects are not only for transition, they can also change a clip timing or appearance
# To show that, lets also modify the Rambo-like part of our clip to be in slow motion
# PS: We do it for effect, but this is one of the few effects that have a direct shortcut, with_speed_scaled
# the others are with_volume_scaled, resized, cropped and rotated
rambo_clip = rambo_clip.with_effects([vfx.MultiplySpeed(0.5)])

# Because we modified timing of rambo_clip with our MultiplySpeed effect, we must re-assign the following clips timing
made_with_text = made_with_text.with_start(rambo_clip.end).with_duration(3)
moviepy_clip = moviepy_clip.with_start(made_with_text.start).with_duration(3)

# Let's have a last look at the result to make sure everything is working as expected
quick_comp = CompositeVideoClip(
    [
        intro_clip,
        intro_text,
        logo_clip,
        bird_clip,
        bird_text,
        bunny_clip,
        bunny_text,
        rodents_clip,
        rodents_text,
        rambo_clip,
        revenge_text,
        made_with_text,
        moviepy_clip,
    ]
)
quick_comp.preview(fps=10)


###############
# CLIP FILTER #
###############
# Lets finish by modifying our rambo clip to make it sepia


# We will start by defining a function that turn a numpy image into sepia
# It takes the image as numpy array in entry and return the modified image as output
def sepia_filter(frame: np.ndarray):
    # Sepia filter transformation matrix
    # Sepia transform works by applying to each pixel of the image the following rules
    # res_R = (R * .393) + (G *.769) + (B * .189)
    # res_G = (R * .349) + (G *.686) + (B * .168)
    # res_B = (R * .272) + (G *.534) + (B * .131)
    #
    # With numpy we can do that very efficiently by multiplying the image matrix by a transformation matrix
    sepia_matrix = np.array(
        [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
    )

    # Convert the image to float32 format for matrix multiplication
    frame = frame.astype(np.float32)

    # Apply the sepia transformation
    # .T is needed because multiplying matrix of shape (n,m) * (m,k) result in a matrix of shape (n,k)
    # what we want is (n,m), so we must transpose matrix (m,k) to (k,m)
    sepia_image = np.dot(frame, sepia_matrix.T)

    # Because final result can be > 255, we limit the result to range [0, 255]
    sepia_image = np.clip(sepia_image, 0, 255)

    # Convert the image back to uint8 format, because we need integer not float
    sepia_image = sepia_image.astype(np.uint8)

    return sepia_image


# Now, we simply apply the filter to our clip by calling image_transform, which will call our filter on every frame
rambo_clip = rambo_clip.image_transform(sepia_filter)

# Let's see how our filter look
rambo_clip.preview(fps=10)


##################
# CLIP RENDERING #
##################
# Everything is good and ready, we can finally render our clip into a file
final_clip = CompositeVideoClip(
    [
        intro_clip,
        intro_text,
        logo_clip,
        bird_clip,
        bird_text,
        bunny_clip,
        bunny_text,
        rodents_clip,
        rodents_text,
        rambo_clip,
        revenge_text,
        made_with_text,
        moviepy_clip,
    ]
)
final_clip.write_videofile("./result.mp4")
````

## File: docs/_static/code/getting_started/quick_presentation/basic_example.py
````python
# Import everything needed to edit video clips
from moviepy import *

# Load file example.mp4 and extract only the subclip from 00:00:10 to 00:00:20
clip = VideoFileClip("long_examples/example2.mp4").subclipped(10, 20)

# Reduce the audio volume to 80% of his original volume
clip = clip.with_volume_scaled(0.8)

# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip(
    font="example.ttf", text="Big Buck Bunny", font_size=70, color="white"
)

# Say that you want it to appear for 10s at the center of the screen
txt_clip = txt_clip.with_position("center").with_duration(10)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([clip, txt_clip])

# Write the result to a file (many options available!)
video.write_videofile("result.mp4")
````

## File: docs/_static/code/user_guide/compositing/CompositeAudioClip.py
````python
"""Let's first concatenate (one after the other) then composite
(on top of each other) three audio clips."""

from moviepy import AudioFileClip, CompositeAudioClip, concatenate_audioclips

# We load all the clips we want to compose
clip1 = AudioFileClip("example.wav")
clip2 = AudioFileClip("example2.wav")
clip3 = AudioFileClip("example3.wav")

# All clip will play one after the other
concat = concatenate_audioclips([clip1, clip2, clip3])

# We will play clip1, then on top of it clip2 starting at t=5s,
# and clip3 on top of both starting t=9s
compo = CompositeAudioClip(
    [
        clip1.with_volume_scaled(1.2),
        clip2.with_start(5),  # start at t=5s
        clip3.with_start(9),
    ]
)
````

## File: docs/_static/code/user_guide/compositing/CompositeVideoClip.py
````python
"""Let's stack three video clips on top of each other with
CompositeVideoClip."""

from moviepy import VideoFileClip, CompositeVideoClip

# We load all the clips we want to compose
clip1 = VideoFileClip("example.mp4")
clip2 = VideoFileClip("example2.mp4").subclipped(0, 1)
clip3 = VideoFileClip("example.mp4")

# We concatenate them and write theme stacked on top of each other,
# with clip3 over clip2 over clip1
final_clip = CompositeVideoClip([clip1, clip2, clip3])
final_clip.write_videofile("final_clip.mp4")
````

## File: docs/_static/code/user_guide/compositing/concatenate.py
````python
"""Let's concatenate (play one after the other) three video clips."""

from moviepy import VideoFileClip, concatenate_videoclips

# We load all the clips we want to concatenate
clip1 = VideoFileClip("example.mp4")
clip2 = VideoFileClip("example2.mp4").subclipped(0, 1)
clip3 = VideoFileClip("example3.mp4")

# We concatenate them and write the result
final_clip = concatenate_videoclips([clip1, clip2, clip3])
final_clip.write_videofile("final_clip.mp4")
````

## File: docs/_static/code/user_guide/compositing/crossfadein.py
````python
"""In this example, we will concatenate two clips with a 1-second
crossfadein of the second clip."""

from moviepy import VideoFileClip, CompositeVideoClip, vfx

# We load all the clips we want to compose
clip1 = VideoFileClip("example.mp4")
clip2 = VideoFileClip("example2.mp4")

clips = [
    clip1.with_end(2),
    clip2.with_start(1).with_effects([vfx.CrossFadeIn(1)]),
]
final_clip = CompositeVideoClip(clips)
final_clip.write_videofile("final_clip.mp4")
````

## File: docs/_static/code/user_guide/compositing/juxtaposing.py
````python
"""Let's juxtapose four video clips in a 2x2 grid."""

from moviepy import VideoFileClip, clips_array, vfx


# We will use the same clip and transform it in 3 ways
clip1 = VideoFileClip("example.mp4").with_effects([vfx.Margin(10)])  # add 10px contour
clip2 = clip1.with_effects([vfx.MirrorX()])  # Flip horizontaly
clip3 = clip1.with_effects([vfx.MirrorY()])  # Flip verticaly
clip4 = clip1.resized(0.6)  # downsize to 60% of original

# The form of the final clip will depend of the shape of the array
# We want our clip to be our 4 videos, 2x2, so we make an array of 2x2
array = [
    [clip1, clip2],
    [clip3, clip4],
]
final_clip = clips_array(array)
# let's resize the final clip so it has 480px of width
final_clip = final_clip.resized(width=480)

final_clip.write_videofile("final_clip.mp4")
````

## File: docs/_static/code/user_guide/compositing/with_position.py
````python
"""Let's position some text and images on a video."""

from moviepy import CompositeVideoClip, ImageClip, TextClip, VideoFileClip


# We load all the clips we want to compose
background = VideoFileClip("example2.mp4").subclipped(0, 2)
title = TextClip(
    "./example.ttf",
    text="Big Buck Bunny",
    font_size=80,
    color="#fff",
    text_align="center",
    duration=1,
)
author = TextClip(
    "./example.ttf",
    text="Blender Foundation",
    font_size=40,
    color="#fff",
    text_align="center",
    duration=1,
)
copyright = TextClip(
    "./example.ttf",
    text="© CC BY 3.0",
    font_size=20,
    color="#fff",
    text_align="center",
    duration=1,
)
logo = ImageClip("./example2.png", duration=1).resized(height=50)

# We want our title to be at the center horizontaly and start at 25%
# of the video verticaly. We can set as "center", "left", "right",
# "top" and "bottom", and % relative from the clip size
title = title.with_position(("center", 0.25), relative=True)

# We want the author to be in the center, 30px under the title
# We can set as pixels
top = background.h * 0.25 + title.h + 30
left = (background.w - author.w) / 2
author = author.with_position((left, top))

# We want the copyright to be 30px before bottom
copyright = copyright.with_position(("center", background.h - copyright.h - 30))

# Finally, we want the logo to be in the center, but to drop as time pass
# We can do so by setting position as a function that take time as argument,
# a lot like frame_function
top = (background.h - logo.h) / 2
logo = logo.with_position(lambda t: ("center", top + t * 30))

# We write the result
final_clip = CompositeVideoClip([background, title, author, copyright, logo])
final_clip.write_videofile("final_clip.mp4")
````

## File: docs/_static/code/user_guide/compositing/with_start.py
````python
from moviepy import VideoFileClip, CompositeVideoClip

# We load all the clips we want to compose
clip1 = VideoFileClip("example.mp4")
clip2 = VideoFileClip("example2.mp4").subclipped(0, 1)
clip3 = VideoFileClip("example3.mp4")

# We want to stop clip1 after 1s
clip1 = clip1.with_end(1)

# We want to play clip2 after 1.5s
clip2 = clip2.with_start(1.5)

# We want to play clip3 at the end of clip2, and so for 3 seconds only
# Some times its more practical to modify the duration of a clip instead
# of his end
clip3 = clip3.with_start(clip2.end).with_duration(1)

# We write the result
final_clip = CompositeVideoClip([clip1, clip2, clip3])
final_clip.write_videofile("final_clip.mp4")
````

## File: docs/_static/code/user_guide/effects/custom_effect.py
````python
"""Let's write a custom effect that will add a basic progress bar
at the bottom of our clip."""

from moviepy import VideoClip
from moviepy.decorators import requires_duration


# Here you see a decorator that will verify if our clip have a duration
# MoviePy offer a few of them that may come handy when writing your own effects
@requires_duration
def progress_bar(clip: VideoClip, color: tuple, height: int = 10):
    """
    Add a progress bar at the bottom of our clip

     Parameters
    ----------

      color: Color of the bar as a RGB tuple
      height: The height of the bar in pixels. Default = 10
    """

    # Because we have define the filter func inside our global effect,
    # it have access to global effect scope and can use clip from inside filter
    def filter(get_frame, t):
        progression = t / clip.duration
        bar_width = int(progression * clip.w)

        # Showing a progress bar is just replacing bottom pixels
        # on some part of our frame
        frame = get_frame(t)
        frame[-height:, 0:bar_width] = color

        return frame

    return clip.transform(filter, apply_to="mask")
````

## File: docs/_static/code/user_guide/effects/image_transform.py
````python
"""Let's invert the green and blue channels of a video."""

from moviepy import VideoFileClip
import numpy

my_clip = VideoFileClip("example.mp4")


def invert_green_blue(image: numpy.ndarray) -> numpy.ndarray:
    return image[:, :, [0, 2, 1]]


modified_clip1 = my_clip.image_transform(invert_green_blue)
````

## File: docs/_static/code/user_guide/effects/modify_copy_example.py
````python
# Import everything needed to edit video clips
from moviepy import VideoFileClip

# Load example.mp4
clip = VideoFileClip("example.mp4")

# This does nothing, as multiply_volume will return a copy of clip
# which you will loose immediatly as you don't store it
# If you was to render clip now, the audio would still be at full volume
clip.with_volume_scaled(0.1)

# This create a copy of clip in clip_whisper with a volume of only 10% the original,
# but does not modify the original clip
# If you was to render clip right now, the audio would still be at full volume
# If you was to render clip_whisper, the audio would be a 10% of the original volume
clip_whisper = clip.with_volume_scaled(0.1)

# This replace the original clip with a copy of it where volume is only 10% of
# the original. If you was to render clip now, the audio would be at 10%
# The original clip is now lost
clip = clip.with_volume_scaled(0.1)
````

## File: docs/_static/code/user_guide/effects/time_transform.py
````python
from moviepy import VideoFileClip
import math

my_clip = VideoFileClip("example.mp4")

# Let's accelerate the video by a factor of 3
modified_clip1 = my_clip.time_transform(lambda t: t * 3)
# Let's play the video back and forth with a "sine" time-warping effect
modified_clip2 = my_clip.time_transform(lambda t: 1 + math.sin(t))
````

## File: docs/_static/code/user_guide/effects/transform.py
````python
"""Let's create a scolling video effect from scratch."""

from moviepy import VideoFileClip

my_clip = VideoFileClip("example.mp4")


def scroll(get_frame, t):
    """
    This function returns a 'region' of the current frame.
    The position of this region depends on the time.
    """
    frame = get_frame(t)
    frame_region = frame[int(t) : int(t) + 360, :]
    return frame_region


modified_clip1 = my_clip.transform(scroll)
````

## File: docs/_static/code/user_guide/effects/using_effects.py
````python
from moviepy import VideoFileClip
from moviepy import vfx, afx

myclip = VideoFileClip("example.mp4")
# resize clip to be 460px in width, keeping aspect ratio
myclip = myclip.with_effects([vfx.Resize(width=460)])

# fx method return a copy of the clip, so we can easily chain them
# double the speed and half the audio volume
myclip = myclip.with_effects([vfx.MultiplySpeed(2), afx.MultiplyVolume(0.5)])

# because effects are added to Clip at runtime, you can also call
# them directly from your clip as methods
myclip = myclip.with_effects([vfx.MultiplyColor(0.5)])  # darken the clip
````

## File: docs/_static/code/user_guide/effects/using_with_methods.py
````python
from moviepy import VideoFileClip

myclip = VideoFileClip("example.mp4")
myclip = myclip.with_end(5)  # stop the clip after 5 sec
myclip = myclip.without_audio()  # remove the audio of the clip
````

## File: docs/_static/code/user_guide/loading/AudioArrayClip.py
````python
"""Let's create an audioclip from values in a numpy array."""

import numpy as np
from moviepy import AudioArrayClip

# We want to play these notes
notes = {"A": 440, "B": 494, "C": 523, "D": 587, "E": 659, "F": 698}

note_duration = 0.5
total_duration = len(notes) * note_duration
sample_rate = 44100  # Number of samples per second

note_size = int(note_duration * sample_rate)
n_frames = note_size * len(notes)


def frame_function(t, note_frequency):
    return np.sin(note_frequency * 2 * np.pi * t)


# At this point one could use this audioclip which generates the audio on the fly
# clip = AudioFileClip(frame_function)

# We generate all frames timepoints

audio_frame_values = [
    2 * [frame_function(t, freq)]
    for freq in notes.values()
    for t in np.arange(0, note_duration, 1.0 / sample_rate)
]
# Create an AudioArrayClip from the audio samples
audio_clip = AudioArrayClip(np.array(audio_frame_values), fps=sample_rate)

# Write the audio clip to a WAV file
audio_clip.write_audiofile("result.wav", fps=44100)
````

## File: docs/_static/code/user_guide/loading/AudioClip.py
````python
from moviepy import AudioClip
import numpy as np


def audio_frame(t):
    """Producing a sinewave of 440 Hz -> note A"""
    return np.sin(440 * 2 * np.pi * t)


audio_clip = AudioClip(frame_function=audio_frame, duration=3)
````

## File: docs/_static/code/user_guide/loading/AudioFileClip.py
````python
from moviepy import *

# Works for audio files, but also videos file where you only want the keep the audio track
clip = AudioFileClip("example.wav")
clip.write_audiofile("./result.wav")
````

## File: docs/_static/code/user_guide/loading/closing.py
````python
from moviepy import *

# clip.close() is implicitly called, so the lock on my_audiofile.mp3 file
# is immediately released.
try:
    with AudioFileClip("example.wav") as clip:
        raise Exception("Let's simulate an exception")
except Exception as e:
    print("{}".format(e))
````

## File: docs/_static/code/user_guide/loading/ColorClip.py
````python
from moviepy import ColorClip

# Color is passed as a RGB tuple
myclip = ColorClip(size=(200, 100), color=(255, 0, 0), duration=1)
# We really don't need more than 1 fps do we ?
myclip.write_videofile("result.mp4", fps=1)
````

## File: docs/_static/code/user_guide/loading/DataVideoClip.py
````python
"""Let's make a clip where frames depend on values in a list"""

from moviepy import DataVideoClip
import numpy as np

# Dataset will just be a list of colors as RGB
dataset = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (0, 255, 255),
    (255, 0, 255),
    (255, 255, 0),
]


# The function make frame take data and create an image of 200x100 px
# filled with the color given in the dataset
def frame_function(data):
    frame = np.full((100, 200, 3), data, dtype=np.uint8)
    return frame


# We create the DataVideoClip, and we set FPS at 2, making a 3s clip
# (because len(dataset) = 6, so 6/2=3)
myclip = DataVideoClip(data=dataset, data_to_frame=frame_function, fps=2)

# Modifying fps here will change video FPS, not clip FPS
myclip.write_videofile("result.mp4", fps=30)
````

## File: docs/_static/code/user_guide/loading/ImageClip.py
````python
"""Here's how you transform a VideoClip into an ImageClip from an image, from
arbitrary data, or by extracting a frame at a given time"""

from moviepy import ImageClip, VideoFileClip
import numpy as np

# Random RGB noise image of 200x100
noise_image = np.random.randint(low=0, high=255, size=(100, 200, 3))

myclip1 = ImageClip("example.png")  # You can create it from a path
myclip2 = ImageClip(noise_image)  # from a (height x width x 3) RGB numpy array
# Or load videoclip and extract frame at a given time
myclip3 = VideoFileClip("./example.mp4").to_ImageClip(t="00:00:01")
````

## File: docs/_static/code/user_guide/loading/ImageSequenceClip.py
````python
from moviepy import ImageSequenceClip

# A clip with a list of images showed for 1 second each
myclip = ImageSequenceClip(
    [
        "example_img_dir/image_0001.jpg",
        "example_img_dir/image_0002.jpg",
        "example_img_dir/image_0003.jpg",
    ],
    durations=[1, 1, 1],
)
# 3 images, 1 seconds each, duration = 3
print("Clip duration: {}".format(myclip.duration))
# 3 seconds, 3 images, fps is 3/3 = 1
print("Clip fps: {}".format(myclip.fps))

# This time we will load all images in the dir, and instead of showing theme
# for X seconds, we will define FPS
myclip2 = ImageSequenceClip("./example_img_dir", fps=30)
# fps = 30, so duration = nb images in dir / 30
print("Clip duration: {}".format(myclip2.duration))
print("Clip fps: {}".format(myclip2.fps))  # fps = 30

# the gif will be 30 fps, its duration will depend on the number of
# images in dir
myclip.write_gif("result.gif")  # the gif will be 3 sec and 1 fps
myclip2.write_gif("result2.gif")
````

## File: docs/_static/code/user_guide/loading/loading.py
````python
import numpy as np

from moviepy import (
    AudioClip,
    AudioFileClip,
    ColorClip,
    ImageClip,
    ImageSequenceClip,
    TextClip,
    VideoClip,
    VideoFileClip,
)


# Define some constants for later use
black = (255, 255, 255)  # RGB for black


def frame_function(t):
    """Random noise image of 200x100"""
    return np.random.randint(low=0, high=255, size=(100, 200, 3))


def frame_function_audio(t):
    """A note by producing a sinewave of 440 Hz"""
    return np.sin(440 * 2 * np.pi * t)


# Now lets see how to load different type of resources !

# VIDEO CLIPS
# for custom animations, where frame_function is a function returning an image
# as numpy array for a given time
clip = VideoClip(frame_function, duration=5)
clip = VideoFileClip("example.mp4")  # for videos
# for a list or directory of images to be used as a video sequence
clip = ImageSequenceClip("example_img_dir", fps=24)
clip = ImageClip("example.png")  # For a picture
# To create the image of a text
clip = TextClip(font="./example.ttf", text="Hello!", font_size=70, color="black")
# a clip of a single unified color, where color is a RGB tuple/array/list
clip = ColorClip(size=(460, 380), color=black)

# AUDIO CLIPS
# for audio files, but also videos where you only want the keep the audio track
clip = AudioFileClip("example.wav")
# for custom audio, where frame_function is a function returning a
# float (or tuple for stereo) for a given time
clip = AudioClip(frame_function_audio, duration=3)
````

## File: docs/_static/code/user_guide/loading/masks.py
````python
import numpy as np

from moviepy import ImageClip, VideoClip, VideoFileClip


# Random RGB noise image of 200x100
frame_function = lambda t: np.random.rand(100, 200)

# To define the VideoClip as a mask, just pass parameter is_mask as True
maskclip1 = VideoClip(frame_function, duration=4, is_mask=True)  # A random noise mask
maskclip2 = ImageClip("example_mask.jpg", is_mask=True)  # A fixed mask as jpeg
maskclip3 = VideoFileClip("example_mask.mp4", is_mask=True)  # A video as a mask

# Load our basic clip, resize to 200x100 and apply each mask
clip = VideoFileClip("example.mp4")
clip_masked1 = clip.with_mask(maskclip1)
clip_masked2 = clip.with_mask(maskclip2)
clip_masked3 = clip.with_mask(maskclip3)
````

## File: docs/_static/code/user_guide/loading/TextClip.py
````python
from moviepy import TextClip

font = "./example.ttf"

# First we use as string and let system autocalculate clip dimensions to fit the text
# we set clip duration to 2 secs, if we do not, it got an infinite duration
txt_clip1 = TextClip(
    font=font,
    text="Hello World !",
    font_size=30,
    color="#FF0000",  # Red
    bg_color="#FFFFFF",
    duration=2,
)
# This time we load text from a file, we set a fixed size for clip and let the system find best font size,
# allowing for line breaking
txt_clip2 = TextClip(
    font=font,
    filename="./example.txt",
    size=(500, 200),
    bg_color="#FFFFFF",
    method="caption",
    color=(0, 0, 255, 127),
)  # Blue with 50% transparency

# we set duration, because by default image clip are infinite, and we cannot render infinite
txt_clip2 = txt_clip2.with_duration(2)
# ImageClip have no FPS either, so we must defined it
txt_clip1.write_videofile("result1.mp4", fps=24)
txt_clip2.write_videofile("result2.mp4", fps=24)
````

## File: docs/_static/code/user_guide/loading/UpdatedVideoClip.py
````python
import random

import numpy as np

from moviepy import UpdatedVideoClip


class CoinFlipWorld:
    """A simulation of coin flipping.

    Imagine we want to make a video that become more and more red as we repeat same face
    on coinflip in a row because coinflip are done in real time, we need to wait
    until a winning row is done to be able to make the next frame.
    This is a world simulating that. Sorry, it's hard to come up with examples...
    """

    def __init__(self, fps):
        """
        FPS is usefull because we must increment clip_t by 1/FPS to have
        UpdatedVideoClip run with a certain FPS
        """
        self.clip_t = 0
        self.win_strike = 0
        self.reset = False
        self.fps = fps

    def update(self):
        if self.reset:
            self.win_strike = 0
            self.reset = False

        print("strike : {}, clip_t : {}".format(self.win_strike, self.clip_t))
        print(self.win_strike)

        # 0 tails, 1 heads, this is our simulation of coinflip
        choice = random.randint(0, 1)
        face = random.randint(0, 1)

        # We win, we increment our serie and retry
        if choice == face:
            self.win_strike += 1
            return

        # Different face, we increment clip_t and set reset so we will reset on next update.
        # We don't reset immediately because we will need current state to make frame
        self.reset = True
        self.clip_t += 1 / self.fps

    def to_frame(self):
        """Return a frame of a 200x100 image with red more or less intense based
        on number of victories in a row."""
        red_intensity = 255 * (self.win_strike / 10)
        red_intensity = min(red_intensity, 255)

        # A 200x100 image with red more or less intense based on number of victories in a row
        return np.full((100, 200, 3), (red_intensity, 0, 0), dtype=np.uint8)


world = CoinFlipWorld(fps=5)

myclip = UpdatedVideoClip(world=world, duration=10)
# We will set FPS to same as world, if we was to use a different FPS,
# the lowest from world.fps and our write_videofile fps param
# will be the real visible fps
myclip.write_videofile("result.mp4", fps=5)
````

## File: docs/_static/code/user_guide/loading/VideoClip.py
````python
import math

import numpy as np
from PIL import Image, ImageDraw

from moviepy import VideoClip


WIDTH, HEIGHT = (128, 128)
RED = (255, 0, 0)


def frame_function(t):
    frequency = 1  # One pulse per second
    coef = 0.5 * (1 + math.sin(2 * math.pi * frequency * t))  # radius varies over time
    radius = WIDTH * coef

    x1 = WIDTH / 2 - radius / 2
    y1 = HEIGHT / 2 - radius / 2
    x2 = WIDTH / 2 + radius / 2
    y2 = HEIGHT / 2 + radius / 2

    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    draw.ellipse((x1, y1, x2, y2), fill=RED)

    return np.array(img)  # returns a 8-bit RGB array


# we define a 2s duration for the clip to be able to render it later
clip = VideoClip(frame_function, duration=2)
# we must set a framerate because VideoClip have no framerate by default
clip.write_gif("circle.gif", fps=15)
````

## File: docs/_static/code/user_guide/loading/VideoFileClip.py
````python
from moviepy import VideoFileClip


myclip = VideoFileClip("example.mp4")

# video file clips already have fps and duration
print("Clip duration: {}".format(myclip.duration))
print("Clip fps: {}".format(myclip.fps))

myclip = myclip.subclipped(0.5, 2)  # Cutting the clip between 0.5 and 2 secs.
print("Clip duration: {}".format(myclip.duration))  # Cuting will update duration
print("Clip fps: {}".format(myclip.fps))  # and keep fps
# the output video will be 1.5 sec long and use original fps
myclip.write_videofile("result.mp4")
````

## File: docs/_static/code/user_guide/rendering/display_in_notebook.py
````python
from moviepy import *

# ...
# ... some jupyter specifics stuff
# ...

my_video_clip = VideoFileClip("./example.mp4")
my_image_clip = ImageClip("./example.png")
my_audio_clip = AudioFileClip("./example.wav")

# We can show any type of clip
my_video_clip.display_in_notebook()  # embeds a video
my_image_clip.display_in_notebook()  # embeds an image
my_audio_clip.display_in_notebook()  # embeds a sound

# We can display only a snaphot of a video
my_video_clip.display_in_notebook(t=1)

# We can provide any valid HTML5 option as keyword argument
# For instance, if the clip is too big, we can set width
my_video_clip.display_in_notebook(width=400)

# We can also make it loop, for example to check if a GIF is
# looping as expected
my_video_clip.display_in_notebook(autoplay=1, loop=1)
````

## File: docs/_static/code/user_guide/rendering/preview.py
````python
from moviepy import *


myclip = VideoFileClip("./example.mp4").subclipped(0, 1)  # Keep only 0 to 1 sec

# We preview our clip as a video, inheriting FPS and audio of the original clip
myclip.preview()

# We preview our clip as video, but with a custom FPS for video and audio
# making it less consuming for our computer
myclip.preview(fps=5, audio_fps=11000)

# Now we preview without audio
myclip.preview(audio=False)
````

## File: docs/_static/code/user_guide/rendering/save_frame.py
````python
from moviepy import *

# We load all the clips we want to compose
myclip = VideoFileClip("example.mp4")
myclip.save_frame("result.png", t=1)  # Save frame at 1 sec
````

## File: docs/_static/code/user_guide/rendering/show.py
````python
from moviepy import *

myclip = VideoFileClip("./example.mp4")

# We show the first frame of our clip
myclip.show()

# We show the frame at point 00:00:01.5 of our clip
myclip.show(1.5)

# We want to see our clip without applying his mask
myclip.show(1.5, with_mask=False)
````

## File: docs/_static/code/user_guide/rendering/write_gif.py
````python
from moviepy import *

myclip = VideoFileClip("example.mp4").subclipped(0, 2)

# Here we just save as GIF
myclip.write_gif("result.gif")

# Here we save as GIF, but we set the FPS of our GIF at 10
myclip.write_gif("result.gif", fps=10)
````

## File: docs/_static/code/user_guide/rendering/write_images_sequence.py
````python
from moviepy import *
import os

myclip = VideoFileClip("example.mp4")

# Here we just save in dir output with filename being his index (start at 0, then +1 for each frame)
os.mkdir("./output")
myclip.write_images_sequence("./output/%d.jpg")

# We set the FPS of our GIF at 10, and we leftpad name with 0 up to 4 digits
myclip.write_images_sequence("./output/%04d.jpg")
````

## File: docs/_static/code/user_guide/rendering/write_videofile_duration.py
````python
from moviepy import *

# By default an ImageClip has no duration
my_clip = ImageClip("example.png")

try:
    # This will fail! We cannot write a clip with no duration!
    my_clip.write_videofile("result.mp4")
except:
    print("Cannot write a video without duration")

# By calling with_duration on our clip, we fix the problem! We also need to set fps
my_clip.with_duration(2).write_videofile("result.mp4", fps=1)
````

## File: docs/_static/code/user_guide/rendering/write_videofile.py
````python
from moviepy import *

# We load all the clips we want to compose
background = VideoFileClip("long_examples/example2.mp4").subclipped(0, 10)
title = TextClip(
    "./example.ttf",
    text="Big Buck Bunny",
    font_size=80,
    color="#fff",
    text_align="center",
    duration=3,
).with_position(("center", "center"))

# We make our final clip through composition
final_clip = CompositeVideoClip([background, title])

# And finally we can write the result into a file

# Here we just save as MP4, inheriting FPS, etc. from final_clip
final_clip.write_videofile("result.mp4")

# Here we save as MP4, but we set the FPS of the clip to our own, here 24 fps, like cinema
final_clip.write_videofile("result24fps.mp4", fps=24)

# Now we save as WEBM instead, and we want tu use codec libvpx-vp9 (usefull when mp4 + transparency).
# We also want ffmpeg compression optimisation as minimal as possible. This will not change
# the video quality and it will decrease time for encoding, but increase final file size a lot.
# Finally, we want ffmpeg to use 4 threads for video encoding. You should probably leave that
# to default, as ffmpeg is already quite good at using the best setting on his own.
final_clip.write_videofile(
    "result.webm", codec="libvpx-vp9", fps=24, preset="ultrafast", threads=4
)
````

## File: docs/_static/medias/index_api.svg
````
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="99.058548mm"
   height="89.967583mm"
   viewBox="0 0 99.058554 89.967582"
   version="1.1"
   id="svg1040"
   inkscape:version="0.92.4 (f8dce91, 2019-08-02)"
   sodipodi:docname="index_api.svg">
  <defs
     id="defs1034" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.35"
     inkscape:cx="533.74914"
     inkscape:cy="10.90433"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     showgrid="false"
     fit-margin-top="0"
     fit-margin-left="0"
     fit-margin-right="0"
     fit-margin-bottom="0"
     inkscape:window-width="930"
     inkscape:window-height="472"
     inkscape:window-x="2349"
     inkscape:window-y="267"
     inkscape:window-maximized="0" />
  <metadata
     id="metadata1037">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(195.19933,-1.0492759)">
    <g
       id="g1008"
       transform="matrix(1.094977,0,0,1.094977,-521.5523,-198.34055)">
      <path
         inkscape:connector-curvature="0"
         id="path899"
         d="M 324.96812,187.09499 H 303.0455 v 72.1639 h 22.67969"
         style="fill:none;stroke:#459DB9;stroke-width:10;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
      <path
         inkscape:connector-curvature="0"
         id="path899-3"
         d="m 361.58921,187.09499 h 21.92262 v 72.1639 h -22.67969"
         style="fill:none;stroke:#459DB9;stroke-width:10;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
      <g
         transform="translate(415.87139,46.162126)"
         id="g944">
        <circle
           style="fill:#459DB9;fill-opacity:1;stroke:#459DB9;stroke-width:4.53704548;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path918"
           cx="-84.40152"
           cy="189.84375"
           r="2.2293637" />
        <circle
           style="fill:#459DB9;fill-opacity:1;stroke:#459DB9;stroke-width:4.53704548;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path918-5"
           cx="-72.949402"
           cy="189.84375"
           r="2.2293637" />
        <circle
           style="fill:#459DB9;fill-opacity:1;stroke:#459DB9;stroke-width:4.53704548;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path918-6"
           cx="-61.497284"
           cy="189.84375"
           r="2.2293637" />
      </g>
    </g>
  </g>
</svg>
````

## File: docs/_static/medias/index_contribute.svg
````
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="89.624855mm"
   height="89.96759mm"
   viewBox="0 0 89.62486 89.96759"
   version="1.1"
   id="svg1040"
   inkscape:version="0.92.4 (f8dce91, 2019-08-02)"
   sodipodi:docname="index_contribute.svg">
  <defs
     id="defs1034" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.35"
     inkscape:cx="683.11893"
     inkscape:cy="-59.078181"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     showgrid="false"
     fit-margin-top="0"
     fit-margin-left="0"
     fit-margin-right="0"
     fit-margin-bottom="0"
     inkscape:window-width="930"
     inkscape:window-height="472"
     inkscape:window-x="2349"
     inkscape:window-y="267"
     inkscape:window-maximized="0" />
  <metadata
     id="metadata1037">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(234.72009,17.466935)">
    <g
       id="g875"
       transform="matrix(0.99300176,0,0,0.99300176,-133.24106,-172.58804)">
      <path
         sodipodi:nodetypes="ccc"
         inkscape:connector-curvature="0"
         id="path869"
         d="m -97.139881,161.26069 47.247024,40.25446 -47.247024,40.25446"
         style="fill:none;stroke:#459DB9;stroke-width:10;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
      <path
         inkscape:connector-curvature="0"
         id="path871"
         d="m -49.514879,241.81547 h 32.505951"
         style="fill:none;stroke:#459DB9;stroke-width:10;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
    </g>
  </g>
</svg>
````

## File: docs/_static/medias/index_getting_started.svg
````
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="101.09389mm"
   height="89.96759mm"
   viewBox="0 0 101.09389 89.96759"
   version="1.1"
   id="svg1040"
   inkscape:version="0.92.4 (f8dce91, 2019-08-02)"
   sodipodi:docname="index_getting_started.svg">
  <defs
     id="defs1034" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.35"
     inkscape:cx="-93.242129"
     inkscape:cy="-189.9825"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     showgrid="false"
     fit-margin-top="0"
     fit-margin-left="0"
     fit-margin-right="0"
     fit-margin-bottom="0"
     inkscape:window-width="1875"
     inkscape:window-height="1056"
     inkscape:window-x="1965"
     inkscape:window-y="0"
     inkscape:window-maximized="1" />
  <metadata
     id="metadata1037">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(2.9219487,-8.5995374)">
    <path
       style="fill:#459DB9;fill-opacity:1;stroke-width:0.20233451"
       d="M 37.270955,98.335591 C 33.358064,97.07991 31.237736,92.52319 32.964256,89.08022 c 0.18139,-0.361738 4.757999,-5.096629 10.17021,-10.521968 l 9.84041,-9.864254 -4.03738,-4.041175 -4.037391,-4.041172 -4.96415,4.916665 c -3.61569,3.581096 -5.238959,5.04997 -5.975818,5.407377 l -1.011682,0.490718 H 17.267525 1.5866055 L 0.65034544,70.96512 C -2.2506745,69.535833 -3.5952145,66.18561 -2.5925745,62.884631 c 0.53525,-1.762217 1.61699004,-3.050074 3.22528014,-3.839847 l 1.15623996,-0.56778 13.2591094,-0.05613 13.259111,-0.05613 11.5262,-11.527539 11.526199,-11.527528 H 40.622647 c -12.145542,0 -12.189222,-0.0046 -13.752801,-1.445851 -2.229871,-2.055423 -2.162799,-5.970551 0.135998,-7.938238 1.475193,-1.262712 1.111351,-1.238469 18.588522,-1.238469 12.899229,0 16.035311,0.05193 16.692589,0.276494 0.641832,0.219264 2.590731,2.051402 9.416301,8.852134 l 8.606941,8.575638 h 6.848168 c 4.837422,0 7.092281,0.07311 7.679571,0.249094 0.48064,0.144008 1.22985,0.634863 1.77578,1.163429 2.383085,2.307333 1.968685,6.539886 -0.804989,8.221882 -0.571871,0.346781 -1.38284,0.687226 -1.80217,0.756523 -0.41933,0.06928 -4.2741,0.127016 -8.56615,0.128238 -6.56998,0.0016 -7.977492,-0.04901 -8.902732,-0.321921 -0.975569,-0.287742 -1.400468,-0.622236 -3.783999,-2.978832 l -2.685021,-2.654679 -5.05411,5.051071 -5.0541,5.051081 3.926292,3.947202 c 2.365399,2.378001 4.114289,4.309171 4.399158,4.857713 0.39266,0.75606 0.47311,1.219412 0.474321,2.731516 0.003,3.083647 0.620779,2.331942 -13.598011,16.531349 -10.273768,10.259761 -12.679778,12.563171 -13.500979,12.92519 -1.267042,0.55857 -3.156169,0.681342 -4.390271,0.285321 z m 40.130741,-65.45839 c -2.212909,-0.579748 -3.782711,-1.498393 -5.51275,-3.226063 -2.522111,-2.518633 -3.633121,-5.181304 -3.633121,-8.707194 0,-3.530699 1.11238,-6.197124 3.631161,-8.704043 4.866751,-4.8438383 12.324781,-4.8550953 17.211791,-0.026 3.908758,3.862461 4.818578,9.377999 2.372188,14.380771 -0.846209,1.730481 -3.39493,4.326384 -5.143839,5.239072 -2.69708,1.407492 -6.042829,1.798628 -8.92543,1.043434 z"
       id="path1000"
       inkscape:connector-curvature="0" />
  </g>
</svg>
````

## File: docs/_static/medias/index_user_guide.svg
````
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="123.72241mm"
   height="89.96759mm"
   viewBox="0 0 123.72242 89.96759"
   version="1.1"
   id="svg1040"
   inkscape:version="0.92.4 (f8dce91, 2019-08-02)"
   sodipodi:docname="index_userguide.svg">
  <defs
     id="defs1034" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.35"
     inkscape:cx="332.26618"
     inkscape:cy="83.744004"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     showgrid="false"
     fit-margin-top="0"
     fit-margin-left="0"
     fit-margin-right="0"
     fit-margin-bottom="0"
     inkscape:window-width="930"
     inkscape:window-height="472"
     inkscape:window-x="2349"
     inkscape:window-y="267"
     inkscape:window-maximized="0" />
  <metadata
     id="metadata1037">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     transform="translate(141.8903,-20.32143)">
    <path
       style="fill:#459DB9;fill-opacity:1;stroke-width:0.20483544"
       d="m -139.53374,110.1657 c -0.80428,-0.24884 -1.71513,-1.11296 -2.07107,-1.96486 -0.23905,-0.57214 -0.28453,-6.28104 -0.28453,-35.720988 0,-38.274546 -0.079,-35.840728 1.19849,-36.91568 0.58869,-0.495345 4.63766,-2.187548 8.47998,-3.544073 l 1.58749,-0.560453 v -3.309822 c 0,-3.025538 0.0396,-3.388179 0.46086,-4.222122 0.68808,-1.362003 1.38671,-1.714455 4.60319,-2.322195 4.12797,-0.779966 5.13304,-0.912766 8.81544,-1.16476 11.80964,-0.808168 22.80911,2.509277 30.965439,9.3392 1.750401,1.465747 3.840861,3.5635 5.0903,5.108065 l 0.659122,0.814805 0.659109,-0.814805 c 1.249431,-1.544565 3.33988,-3.642318 5.09029,-5.108065 8.156331,-6.829923 19.155791,-10.147368 30.965441,-9.3392 3.682389,0.251994 4.68748,0.384794 8.81544,1.16476 3.21647,0.60774 3.91511,0.960192 4.60318,2.322195 0.4213,0.833943 0.46087,1.196584 0.46087,4.222122 v 3.309822 l 1.58748,0.560453 c 4.10165,1.448077 7.98852,3.072753 8.5259,3.563743 1.22643,1.120567 1.15258,-1.245868 1.15258,36.927177 0,34.567591 -0.005,35.083151 -0.40663,35.903991 -0.22365,0.45804 -0.73729,1.05665 -1.14143,1.33024 -1.22281,0.82783 -2.17721,0.70485 -5.86813,-0.7561 -9.19595,-3.63998 -18.956011,-6.38443 -26.791332,-7.53353 -3.02827,-0.44412 -9.26189,-0.61543 -11.77821,-0.3237 -5.19357,0.60212 -8.736108,2.05527 -11.700039,4.79936 -0.684501,0.63371 -1.466141,1.23646 -1.736979,1.33942 -0.63859,0.2428 -4.236521,0.2428 -4.875112,0 -0.27083,-0.10296 -1.05247,-0.70571 -1.73696,-1.33942 -2.96395,-2.74409 -6.50648,-4.19724 -11.700058,-4.79936 -2.516312,-0.29173 -8.749941,-0.12042 -11.778201,0.3237 -7.78194,1.14127 -17.39965,3.83907 -26.73341,7.49883 -3.38325,1.32658 -4.15525,1.50926 -5.11851,1.21125 z m 4.2107,-5.34052 c 5.86759,-2.29858 14.40398,-4.922695 20.2018,-6.210065 6.31584,-1.402418 8.5236,-1.646248 14.91592,-1.647338 4.68699,-7.94e-4 6.013661,0.0632 7.257809,0.3497 0.837332,0.19286 1.561052,0.312028 1.60828,0.264819 0.147111,-0.147119 -1.803289,-1.307431 -4.154879,-2.471801 -8.12511,-4.023029 -18.27311,-4.986568 -29.0861,-2.761718 -1.09536,0.22538 -2.32708,0.40827 -2.73715,0.406418 -1.12787,-0.005 -2.3054,-0.76382 -2.84516,-1.8332 l -0.46086,-0.913098 V 62.99179 35.97471 l -0.56331,0.138329 c -0.30981,0.07608 -1.89985,0.665075 -3.5334,1.308881 -2.27551,0.896801 -2.96414,1.252878 -2.94452,1.522563 0.014,0.193604 0.0372,15.284513 0.0512,33.535345 0.014,18.250839 0.0538,33.183322 0.0884,33.183322 0.0346,0 1.02543,-0.3771 2.20198,-0.83801 z m 113.006991,-32.697216 -0.0518,-33.535203 -3.17495,-1.272156 c -1.74623,-0.699685 -3.33627,-1.278755 -3.53341,-1.286819 -0.33966,-0.01389 -0.35847,1.401778 -0.35847,26.980216 v 26.994863 l -0.46087,0.913112 c -0.53976,1.06939 -1.71729,1.828088 -2.84515,1.833189 -0.41008,0.0021 -1.6418,-0.181031 -2.73716,-0.406421 -11.888201,-2.446089 -22.84337,-1.046438 -31.491022,4.02332 -1.68175,0.985941 -2.216748,1.467501 -1.36534,1.228942 1.575181,-0.441362 4.990592,-0.73864 8.524862,-0.742011 5.954408,-0.005 11.43046,0.791951 19.10874,2.78333 3.9516,1.024874 12.1555,3.687454 15.6699,5.085704 1.23926,0.49306 2.36869,0.90517 2.50985,0.9158 0.20489,0.0155 0.2462,-6.745894 0.20483,-33.515866 z m -59.76135,-2.233777 V 40.065438 l -0.95972,-1.357442 c -1.380522,-1.952627 -5.376262,-5.847994 -7.64336,-7.45136 -3.778692,-2.672401 -9.063392,-4.943324 -13.672511,-5.875304 -3.19731,-0.646503 -5.23069,-0.833103 -9.05886,-0.831312 -4.37716,0.0021 -7.70223,0.349169 -11.83461,1.235469 l -1.07538,0.230645 v 31.242342 c 0,26.565778 0.0426,31.226011 0.28429,31.133261 0.15637,-0.06 1.42379,-0.297169 2.81648,-0.527026 12.37657,-2.042634 23.21658,-0.346861 32.521639,5.087596 2.10018,1.226558 5.20202,3.618878 6.880942,5.30692 0.788609,0.792909 1.502978,1.446609 1.587468,1.452679 0.0845,0.006 0.153622,-13.411893 0.153622,-29.817719 z m 5.80221,28.3766 c 6.21476,-6.141601 15.08488,-10.061509 25.025529,-11.05933 4.262419,-0.427849 11.579921,-0.0054 16.017661,0.924912 0.75932,0.15916 1.45259,0.244888 1.54058,0.190498 0.088,-0.05434 0.16003,-14.060382 0.16003,-31.124436 V 26.176883 l -0.52136,-0.198219 c -0.66893,-0.254325 -4.77649,-0.95482 -7.159981,-1.221048 -2.41372,-0.269605 -8.559851,-0.266589 -10.759229,0.0052 -6.458111,0.798299 -12.584091,3.083792 -17.405651,6.49374 -2.267091,1.603366 -6.262831,5.498733 -7.64336,7.45136 l -0.959721,1.357438 v 29.828747 c 0,16.405812 0.0532,29.828746 0.11802,29.828746 0.065,0 0.77928,-0.65347 1.587482,-1.452149 z"
       id="path845"
       inkscape:connector-curvature="0"
       sodipodi:nodetypes="csscccscsssscsssssscscsccsccsccscsscccccccscccccccccsccscscscccscccsccssccsscccscccccsccccsccscsccsscc" />
  </g>
</svg>
````

## File: docs/_static/moviepy.css
````css
@import url(flasky.css)
/* Override some aspects of the pydata-sphinx-theme */

.indexwrapper .sphinxsidebar { visibility: hidden; }

.logo img.logo { width: 120px; height: 120px; padding-right: 30px; }

div.body h1, div.body h2, div.body h3, div.body h4, div.body h5, div.body h6
  { font-family: 'Times New Roman', 'Garamond', 'Georgia', serif; }


:root {
  /* Use softer blue from bootstrap's default info color */
  --pst-color-info: 23, 162, 184;
}

table {
  width: auto; /* Override fit-content which breaks Styler user guide ipynb */
}

/* Main index page overview cards */

.intro-card {
  padding: 30px 10px 20px 10px;
}

.intro-card .sd-card-img-top {
  margin: 10px;
  height: 52px;
  background: none !important;
}

.intro-card .sd-card-title {
  color: var(--pst-color-primary);
  font-size: var(--pst-font-size-h5);
  padding: 1rem 0rem 0.5rem 0rem;
}

.intro-card .sd-card-footer {
  border: none !important;
}

.intro-card .sd-card-footer p.sd-card-text {
  max-width: 220px;
  margin-left: auto;
  margin-right: auto;
}

.intro-card .sd-btn-secondary {
  background-color: #6c757d !important;
  border-color: #6c757d !important;
}

.intro-card .sd-btn-secondary:hover {
  background-color: #5a6268 !important;
  border-color: #545b62 !important;
}

.card, .card img {
  background-color: var(--pst-color-background);
}
````

## File: docs/_templates/custom_autosummary/class.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}
   :members:
````

## File: docs/_templates/custom_autosummary/module.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
{{ fullname | escape | underline}}

{% if fullname in ['moviepy.Effect'] or '.fx.' in fullname %} {# Fix for autosummary to document abstract class #}
.. automodule:: {{ fullname }}
   :inherited-members:
{% else %}
.. automodule:: {{ fullname }}
{% endif %}
   

   {% block classes %}
   {% if classes %}
   .. rubric:: {{ _('Classes') }}

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   {% for item in classes %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}


   {% block functions %}
   {% if functions %}
   .. rubric:: {{ _('Functions') }}

   .. autosummary::
      :toctree:
   {% for item in functions %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}


   {% block exceptions %}
   {% if exceptions %}
   .. rubric:: {{ _('Exceptions') }}

   .. autosummary::
   {% for item in exceptions %}
      {{ item }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

{% block modules %}
{% if modules %}
.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: custom_autosummary/module.rst
   :recursive:
{% for item in modules %}
{% if not item in ['moviepy.version'] %}
   {{ item }}
{% endif %}
{%- endfor %}
{% endif %}
{% endblock %}
````

## File: docs/_themes/.gitignore
````
*.pyc
*.pyo
.DS_Store
````

## File: docs/developer_guide/contribution_guidelines.rst
````
.. _contribution_guidelines:

MoviePy's Contribution Guidelines
=================================

Communication on GitHub
-----------------------

- Keep messages on GitHub issues and pull requests on-topic and to the point. Be aware that each comment triggers a notification which gets sent out to a number of people.
    - Opinions are OK.
    - For longer or more in-depth discussions, use the `MoviePy Gitter <https://gitter.im/Movie-py>`_. If these discussions lead to a decision, like a merge/reject, please leave a message on the relevant MoviePy issue to document the outcome of the discussion/the reason for the decision.
- Do not push any commit that changes the API without prior discussion.

Preparing for development
-------------------------

- Fork the official MoviePy repository to your own GitHub account:  
  Use the "Fork" button in the top right corner of the GitHub interface while viewing `the official MoviePy <https://github.com/Zulko/moviepy>`_ repository.
- Use your fork as the basis for cloning the repository to your local machine: ``$ git clone URL_TO_YOUR_FORK``  
  You can get the appropriate URL (SSH- or HTTPS-based) by using the green "Code" button located at the top right of the repository view while looking at your fork. By default, Git refers to any remote you clone from – i.e. in this case your fork on GitHub – as ``origin``.
- Enter your local clone and add the official MoviePy repository as a second remote, with alias ``upstream``:  
  ``$ git remote add upstream git@github.com:Zulko/moviepy.git`` (using SSL) _or_   
  ``$ git remote add upstream https://github.com/Zulko/moviepy.git`` (using HTTPS).
- Install the library inside a `virtual environment <https://docs.python.org/3/tutorial/venv.html>`_ with all dependencies included using ``$ pip install -e ".[optional,doc,test,lint]"``
- Configure pre-commit hooks running ``$ pre-commit install``

Coding conventions, code quality
--------------------------------

- Respect `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ conventions.
- Add just the "right" amount of comments. Try to write auto-documented code with very explicit variable names.
- If you introduce new functionality or fix a bug, document it in the docstring or with code comments.
- MoviePy's team adopted `pre-commit <https://pre-commit.com/>`_ to run code checks using black, flake8 and isort, so make sure that you've configured the pre-commit hooks with ``pre-commit install``. 

Standard contribution workflow
------------------------------

Local development
~~~~~~~~~~~~~~~~~

- Keep your local ``master`` branch up-to-date with the official repo's master by periodically fetching/pulling it:  
  ``$ git pull upstream master``
- Never make changes on ``master`` directly, but branch off into separate develop branches:  
  ``$ git checkout --branch YOUR_DEVELOP_BRANCH``  
  Ideally, these are given names which function as keywords for what you are working on, and are prefixed with ``fix_`` (for bug fixes), ``feature_`` or something similarly appropriate and descriptive.
- Base any changes you submit on the most recent ``master``.

More detailed explanation of the last point:

It is likely that the official repo's ``master`` branch will move on (get updated, have other PRs merged into it) while you are working on your changes. Before creating a pull request, you will have to make sure your changes are not based on outdated code. For this reason, it makes sense to avoid falling "too much behind" while developing by rebasing your local ``master`` branch at intervals. Make sure your ``master`` branch is in sync with the official ``master`` branch (as per the first point), then, while checked into your develop branch, run: ``$ git rebase master``

If you **haven't rebased before**, make sure to **familiarise yourself** with the concept.

Submitting Pull Requests
~~~~~~~~~~~~~~~~~~~~~~~~

You do not have to have finished your feature or bug fix before submitting a PR; just mention that it still is a work in progress.

Before submitting PRs:

- run the test suite over your code to expose any problems: ``$ pytest``
- push your local develop branch to your GitHub fork ``$ git push origin YOUR_DEVELOP_BRANCH``

When you now look at your forked repo on your GitHub account, you will see GitHub suggest branches for sending pull requests to the official ``Zulko/moviepy`` repository.

Once you open a PR, you will be presented with a template which you are asked to fill out. You are encouraged to add any additional information which helps provide further context to your changes, and to link to any issues or PRs which your pull request references or is informed by.

On submitting your PR, an automated test suite runs over your submission, which might take a few minutes to complete. In a next step, a MoviePy maintainer will review your code and, if necessary, help you to get it merge-ready.
````

## File: docs/developer_guide/developers_install.rst
````
.. _developers_install:

Installation for MoviePy developers
======================================

.. warning::
    This part is only destined to people who want to build the MoviePy documentation by themselves, or to contribute to MoviePy. Normal users don't need it.

In addition to MoviePy main libraries, MoviePy developers will also need to install additional libraries to be able to run MoviePy tests and build the MoviePy documentation.

Libraries for documentation
-----------------------------

You can install the libraries required to build documentation with: 

.. code:: bash

    $ (sudo) pip install moviepy[doc]

Once libraries installed you can build the documentation with:

.. code:: bash

    $ python setup.py build_docs


Libraries for testing and linting
-------------------------------------

You can install the libraries required for testing and linting with:

.. code:: bash

    $ (sudo) pip install moviepy[test]
    $ (sudo) pip install moviepy[lint]

Once libraries installed you can test with:

.. code:: bash

    $ python -m pytest

And you can lint with:

.. code:: bash

    $ python -m black .

and 

.. code:: bash

    $ python3 -m flake8 -v --show-source --ignore=E501 moviepy docs/conf.py examples tests

Adding Git pre-commit hooks
-----------------------------

Running linter manually is painfull and error prone, instead you should consider adding a pre-commit hook.
To do so you can simply go in your local moviepy directory, and run :

.. code:: bash
    $ pre-commit install

This will enable a git hooks using python pre-commit framework.
````

## File: docs/developer_guide/index.rst
````
.. _developer_guide:

The MoviePy Developer's Guide
-----------------------------

This guide covers most of the things people wanting to participate in MoviePy development need to know.

.. toctree::
   :maxdepth: 1
   
   developers_install
   contribution_guidelines
   maintainers_publish
````

## File: docs/developer_guide/maintainers_publish.rst
````
.. _maintainers_publish:

Publishing a New Version of MoviePy
===================================

This section is for maintainers responsible for publishing new versions of MoviePy. Follow these steps to ensure the process is smooth and consistent:

**Pre-requisites**
------------------
- Ensure you have proper permissions to push changes and create releases in the MoviePy repository.

Steps to Publish a New Version
------------------------------

1. **Update the `CHANGELOG.md`**

   - Add a new section for the upcoming version, respecting the format used in previous entries.
   - Summarize all changes, fixes, and new features.

2. **Update the version in `pyproject.toml`**

   - Open the `pyproject.toml` file.
   - Update the `version` field to the new version, following `Semantic Versioning <https://semver.org/>`_.

3. **Commit and Push**

   - Stage your changes::

        git add CHANGELOG.md pyproject.toml

   - Commit your changes::

        git commit -m "Release vX.Y.Z"

   - Push your changes::

        git push

4. **Create a New Tag**

   - Create a tag for the new version (replace ``vX.Y.Z`` with the actual version number)::

        git tag -a vX.Y.Z -m "Release vX.Y.Z"

   - Push the tag to the remote repository::

        git push origin vX.Y.Z

5. **Create a New Release**

   - Go to the repository's page on GitHub (or the relevant hosting platform).
   - Navigate to the "Releases" section and create a new release.
   - Use the new tag (``vX.Y.Z``) and provide a description for the release.
     - Copy the changelog for this version into the release description.
   - Publish the release.

GitHub actions will automatically build and publish the new release on PyPi.

By following these steps, you ensure that each MoviePy release is well-documented, correctly versioned, and accessible to users.
````

## File: docs/getting_started/docker.rst
````
MoviePy Docker
===============

Prerequisites
-------------

Docker installed: `Docker Engine for Linux <https://docs.docker.com/engine/install/>`_ or `Docker Desktop for Windows/Mac/Linux <https://docs.docker.com/desktop/>`_.

Build the docker
-----------------
1. Move into the moviepy root dir
2. Build the Dockerfile ::
     
     docker build -t moviepy -f Dockerfile .


How to run the unittests from docker
------------------------------------------------

Run pytest inside the container with the following command ::

     docker run -w /moviepy -it moviepy python -m pytest

Running your own moviepy script from docker
--------------------------------------------

Change directory to where your script is located

If moviepy docker container is already running, you can connect by: ::

     docker exec -it moviepy python myscript.py

If the container isn't running already ::

     docker run -it moviepy bash
     python myscript.py

You can also start a container and run a script in one command: ::

     docker run -it -v `pwd`:/code moviepy python myscript.py
````

## File: docs/getting_started/FAQ.rst
````
FAQ and troubleshooting
=========================

This section intend to answer the most common questions and errors.

Common errors that are not bugs
--------------------------------

These are very common errors which are not considered as bugs to be
solved (but you can still ask for this to change). If these answers
don't work for you, please open a bug report on Github_, or on the dedicated Subreddit_.


MoviePy generated a video that cannot be read by my favorite player.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Known reason: one of the video's dimensions were not even,
for instance 720x405, and you used a MPEG4 codec like libx264 (default
in MoviePy). In this case the video generated uses a format that is
readable only on some readers like VLC.


I can't seem to read any video with MoviePy
""""""""""""""""""""""""""""""""""""""""""""""

Known reason: you have a deprecated version of FFmpeg, install a recent version from the
website, not from your OS's repositories! (see :ref:`install`).


Previewing videos make them slower than they are
"""""""""""""""""""""""""""""""""""""""""""""""""

It means that your computer is not good enough to render the clip in real time. Don't hesitate to play with the options of ``preview``: for instance, lower the fps of the sound (11000 Hz is still fine) and the video. Also, downsizing your video with ``resize`` can help.

.. _Github: https://github.com/Zulko/moviepy
.. _Subreddit: https://www.reddit.com/r/moviepy/
````

## File: docs/getting_started/index.rst
````
.. _getting_started:

Getting started with MoviePy
------------------------------

This section explain everything you need to start editing with MoviePy. To go further, have a look at the :ref:`user_guide` and the :ref:`reference_manual`.


.. toctree::
   :maxdepth: 1

   install
   quick_presentation
   moviepy_10_minutes
   docker
   updating_to_v2
   FAQ
````

## File: docs/getting_started/install.rst
````
.. _install:

Installation
============

Installation is done with ``pip``. If you don't have ``pip``, take a look at `how to install it <https://pip.pypa.io/en/stable/installation/>`_.

With ``pip`` installed, just type this in a terminal:

.. code:: bash

    $ (sudo) pip install moviepy

.. _install-binaries:

Installation of Additional Binaries
-----------------------------------

MoviePy depends on the software ffmpeg_ for video reading and writing and on ``ffplay`` for video previewing.

You don't need to worry about ffmpeg_, as it should be automatically downloaded/installed by ImageIO during your first use of MoviePy (it takes a few seconds).

You do need to worry about ``ffplay`` if you plan on using video/audio previewing. For these cases, make sure to have ``ffplay`` installed (it can usually be found alongside ``ffmpeg``) and ensure it is accessible to Python, or define a custom path (see below).

Define Custom Paths to Binaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to use a specific version of FFmpeg and FFplay, you can do so using environment variables.

There are a couple of environment variables used by MoviePy that allow you to configure custom paths to the external tools.

To set up any of these variables, the easiest way is to do it in Python before importing objects from MoviePy. For example:

.. code-block:: python

    import os
    os.environ["FFMPEG_BINARY"] = "/path/to/custom/ffmpeg"
    os.environ["FFPLAY_BINARY"] = "/path/to/custom/ffplay"

Alternatively, after installing the optional dependencies, you can create
a ``.env`` file in your working directory that will be automatically read.
For example

.. code-block:: ini

    FFMPEG_BINARY=/path/to/custom/ffmpeg
    FFPLAY_BINARY=/path/to/custom/ffplay

Environment Variables
---------------------

There are two available environment variables for external binaries:

``FFMPEG_BINARY``
    Normally you can leave it at its default ('ffmpeg-imageio'), in which
    case imageio will download the correct ffmpeg binary (on first use) and then always use that binary.

    The second option is ``"auto-detect"``. In this case, ffmpeg will be whatever
    binary is found on the computer: generally ``ffmpeg`` (on Linux/macOS) or ``ffmpeg.exe`` (on Windows).

    Lastly, you can set it to use a binary at a specific location on your disk by specifying the exact path.

``FFPLAY_BINARY``
    The default is ``"auto-detect"``. MoviePy will try to find and use the installed ``ffplay`` binary.

    You can set it to use a binary at a specific location on your disk. On Windows, this might look like:

    .. code-block:: python

        os.environ["FFPLAY_BINARY"] = r"C:\Program Files\ffmpeg\ffplay.exe"

Verify if MoviePy Finds Binaries
--------------------------------

To test if FFmpeg and FFplay are found by MoviePy, in a Python console, you can run:

.. code:: python

    from moviepy.config import check
    check()

.. _ffmpeg: https://www.ffmpeg.org/download.html
````

## File: docs/getting_started/moviepy_10_minutes.rst
````
.. _moviepy_10_minutes:

MoviePy in 10 Minutes: Creating a Trailer from "Big Buck Bunny"
===============================================================

.. note::
   This tutorial aims to be a simple and short introduction for new users wishing to use MoviePy. For a more in-depth exploration of the concepts seen in this tutorial, see :ref:`user_guide`.

In this tutorial, you will learn the basics of how to use the MoviePy library in just 10 minutes. As an example project for this tutorial, we will create the following trailer for the movie `"Big Buck Bunny." <https://peach.blender.org/>`_

.. raw:: html

   <div style="position: relative; padding-bottom: 56.25%; padding-top: 30px; margin-bottom:30px; height: 0; overflow: hidden; margin-left: 5%;">
      <video controls>
         <source src="/moviepy/_static/medias/getting_started/moviepy_10_minutes/trailer_bbb.mp4" type="video/mp4">
         <p>Your browser does not support HTML5 video in MP4 format.</p>
      </video>
   </div>

Prerequisites
-------------

Before we start, make sure you have MoviePy installed. You can install it using pip:

.. code-block:: shell

   pip install moviepy

Additionally, we will need to gather a few resources such as the original movie, font files, images, etc. To make it easy, we have prepared a template project you can download directly:

1. Download :download:`the project template </_static/medias/getting_started/moviepy_10_minutes/moviepy_10_minutes.zip>` and unzip it.
2. Take a look at the resources inside the folder to familiarize yourself.
3. Create a Python script file named ``trailer.py`` in the project directory.

Now, you are ready to proceed to the next steps.

Step 1: Import MoviePy and Load the Video
-----------------------------------------

Let's start by importing the necessary modules and loading the "Big Buck Bunny" video into our Python program:

.. literalinclude:: /_static/code/getting_started/moviepy_10_minutes/trailer.py
   :language: python
   :lines: 1-10

As you can see, loading a video file is really easy, but MoviePy isn't limited to video. It can handle images, audio, text, and even custom animations.

No matter the kind of resources, ultimately any clip will be either a :py:class:`~moviepy.video.VideoClip.VideoClip` for any visual element, and an :py:class:`~moviepy.audio.AudioClip.AudioClip` for any audio element.

In this tutorial, we will only see a few of those, but if you want to explore more, you can find an exhaustive list in the user guide about :ref:`loading`.

Step 2: Extract the Best Scenes
-------------------------------

To create our trailer, we will focus on presenting the main characters, so we need to extract parts of the movie. This is a very classic task, so let's turn our main clip into multiple subclips:

.. literalinclude:: /_static/code/getting_started/moviepy_10_minutes/trailer.py
   :language: python
   :lines: 13-25

Here, we use the ``subclip`` method to extract specific scenes from the main video. We provide the start and end times (in seconds or as text with the format ``HH:MM:SS.µS``) for each scene. The extracted clips are stored in their respective variables (``intro_clip``, ``bird_clip``, etc.).

Step 3: Take a First Look with Preview
--------------------------------------

When editing videos, it's often essential to preview the clips to ensure they meet our vision. This allows you to watch the segment you're working on and make any necessary adjustments for the perfect result.

To do so using MoviePy, you can utilize the ``preview()`` function available for each clip (the complementary ``audio_preview()`` is also available for :py:class:`~moviepy.audio.AudioClip.AudioClip`).

.. note::
   Note that you will need ``ffplay`` installed and accessible to MoviePy for preview to work. You can check if ``ffplay`` is available by running the command ``python3 -c "from moviepy.config import check; check()"``.
   If not, please see :ref:`install#binaries`.

.. literalinclude:: /_static/code/getting_started/moviepy_10_minutes/trailer.py
   :language: python
   :lines: 28-38

By using the preview, you may have noticed that our clips not only contain video but also audio. This is because when loading a video, you not only load the image but also the audio tracks that are turned into :py:class:`~moviepy.audio.AudioClip.AudioClip` and added to your video clip.

.. note::
   When previewing, you may encounter video slowing or video/audio shifting. This is not a bug; it's due to the fact that your computer cannot render the preview in real-time. In such a case, the best course of action is to set the ``fps`` parameter for the ``preview()`` at a lower value to make things easier on your machine.

Step 4: Modify a Clip by Cutting Out a Part of It
--------------------------------------------------

After previewing the clips, we notice that the rodents' scene is a bit long. Let's modify the clip by removing a specific part. It would be nice to remove parts of the scene that we don't need. This is also quite a common task in video editing. To do so, we are going to use the ``with_effects`` method to remove a portion of the clip between ``00:06:00`` to ``00:10:00``.

.. literalinclude:: /_static/code/getting_started/moviepy_10_minutes/trailer.py
   :language: python
   :lines: 41-54

In that particular case, we have used the ``with_effects``, but this is only one of the many clip manipulation methods starting with ``with_``. We will see a few others in this tutorial, but we will miss a lot more. If you want an exhaustive list, go see :ref:`reference_manual`.

.. note::
   You may have noticed that we have reassigned the ``rodents_clip`` variable instead of just calling a method on it. This is because in MoviePy, any function starting with ``with_`` is out-of-place instead of in-place, meaning it does not modify the original data but instead copies it and modifies/returns the copy. So you need to store the result of the method and, if necessary, reassign the original variable to update your clip.

Step 5: Creating Text/Logo Clips
------------------------------------

In addition to videos, we often need to work with images and texts. MoviePy offers some specialized kinds of :py:class:`~moviepy.video.VideoClip.VideoClip` specifically for that purpose: ``ImageClip`` and ``TextClip``.

In our case, we want to create text clips to add text overlays between the video clips. We'll define the font, text content, font size, and color for each text clip. We also want to create image clips for the "Big Buck Bunny" logo and the "Made with MoviePy" logo and resize them as needed.

.. literalinclude:: /_static/code/getting_started/moviepy_10_minutes/trailer.py
    :language: python
    :lines: 56-82

As you can see, ``ImageClip`` is quite simple, but ``TextClip`` is a rather complicated object. Don't hesitate to explore the arguments it accepts.

.. note::
   In our example, we have used the ``resize`` method to resize our image clips. This method works just like any ``with_*`` method, but because resizing is such a common task, the name has been shortened to ``resize``. The same is true for ``crop`` and ``rotate``.

Feel free to experiment with different effects and transitions to achieve the desired trailer effect.

Step 6: Timing the Clips
------------------------

We have all the clips we need, but if we were to combine all the clips into a single one using composition (we will see that in the next step), all our clips would start at the same time and play on top of each other, which is obviously not what we want. Also, some video clips, like images and texts, have no endpoint/duration at creation (unless you have provided a duration parameter), which means trying to render them will throw an error as it would result in an infinite video.

To fix that, we need to specify when a clip should start and stop in the final clip. So, let's start by indicating when each clip must start and end using the appropriate ``with_*`` methods.

.. literalinclude:: /_static/code/getting_started/moviepy_10_minutes/trailer.py
    :language: python
    :lines: 85-111

.. note::
   By default, all clips have a start point at ``0``. If a clip has no ``duration`` but you set the ``end_time``, then the ``duration`` will be calculated for you. The reciprocity is also true.

   So in our case, we either use ``duration`` or ``end_time``, depending on what is more practical for each specific case.

Step 7: Seeing How All Clips Combine
------------------------------------

Now that all our clips are timed, let's get a first idea of how our final clip will look. In video editing, the act of assembling multiple videos into a single one is known as composition. So, MoviePy offers a special kind of :py:class:`~moviepy.video.VideoClip.VideoClip` dedicated to the act of combining multiple clips into one, the :py:class:`~moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip`.

:py:class:`~moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip` takes an array of clips as input and will play them on top of each other at render time, starting and stopping each clip at its start and end points.

.. note::
   If possible, :py:class:`~moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip` will extract endpoint and size from the biggest/last ending clip. If a clip in the list has no duration, then you will have to manually set the duration of :py:class:`~moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip` before rendering.

.. literalinclude:: /_static/code/getting_started/moviepy_10_minutes/trailer.py
    :language: python
    :lines: 114-136

Step 8: Positioning Our Clips
-----------------------------

By looking at this first preview, we see that our clips are pretty well timed, but that the positions of our texts and logo are not satisfying.

This is because, for now, we have only specified when our clips should appear, and not the position at which they should appear. By default, all clips are positioned from the top left of the video, at ``(0, 0)``.

All our clips do not have the same sizes (the texts and images are smaller than the videos), and the :py:class:`~moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip` takes the size of the biggest clip (so in our case, the size of the videos), so the texts and images are all in the top left portion of the clip.

To fix this, we simply have to define the position of our clips in the composition with the method ``with_position``.

.. literalinclude:: /_static/code/getting_started/moviepy_10_minutes/trailer.py
    :language: python
    :lines: 139-174

.. note::
   The position is a tuple with horizontal and vertical position. You can give them as pixels, as strings (``top``, ``left``, ``right``, ``bottom``, ``center``), and even as a percentage by providing a float and passing the argument ``relative=True``.

Now, all our clips are in the right place and timed as expected.

Step 9: Adding Transitions and Effects
--------------------------------------

So, our clips are timed and placed, but for now, the result is quite raw. It would be nice to have smoother transitions between the clips. In MoviePy, this is achieved through the use of effects.

Effects play a crucial role in enhancing the visual and auditory appeal of your video clips. Effects are applied to clips to create transitions, transformations, or modifications, resulting in better-looking videos. Whether you want to add smooth transitions between clips, alter visual appearance, or manipulate audio properties, MoviePy comes with many existing effects to help you bring your creative vision to life with ease.

You can find these effects under the namespace ``vfx`` for video effects and ``afx`` for audio effects.

.. note::
   You can use audio effects on both audio and video clips because when applying audio effects to a video clip, the effect will actually be applied to the video clip's embedded audio clip instead.

Using an effect is very simple. You just have to call the method ``with_effects`` on your clip and pass an array of effect objects to apply.

In our case, we will add simple fade-in/out and cross-fade-in/out transitions between our clips, as well as slow down the ``rambo_clip``.

.. literalinclude:: /_static/code/getting_started/moviepy_10_minutes/trailer.py
    :language: python
    :lines: 177-239

Well, this looks a lot nicer! For this tutorial, we want to keep things simple, so we mostly used transitions. However, you can find many different effects and even create your own. For a more in-depth presentation, see :py:mod:`moviepy.video.fx`, :py:mod:`moviepy.audio.fx`, and :ref:`create_effects`.

.. note::
   Looking at the result, you may notice that cross-fading makes clips go from transparent to opaque, and reciprocally, and wonder how it works.

   We won't get into details, but know that in MoviePy, you can declare some sections of a video clip to be transparent by using masks. Masks are nothing more than special kinds of video clips that are made of values ranging from ``0`` for a transparent pixel to ``1`` for a fully opaque one.

   For more info, see :ref:`loading#masks`.

Step 10: Modifying the Appearance of a Clip Using Filters
---------------------------------------------------------

Finally, to make it more epic, we will apply a custom filter to our Rambo clip to make the image sepia. MoviePy does not come with a sepia effect out of the box, and creating a full custom effect is beyond the scope of this tutorial. However, we will see how we can apply a simple filter to our clip using the :py:meth:`~moviepy.video.VideoClip.VideoClip.image_transform` method.

To understand how filters work, you first need to understand that in MoviePy, a clip frame is nothing more than a numpy ``ndarray`` of shape ``HxWx3``. This means we can modify how a frame looks like by applying simple math operations. Doing that on all the frames allows us to apply a filter to our clip!

The "apply to all frames" part is done by the ``image_transform`` method. This method takes a callback function as an argument, and at render time, it will trigger the callback for each frame of the clip, passing the current frame.

.. warning::
   This is a bit of an advanced usage, and the example involves matrix multiplication. If this is too much for you, you can simply ignore it until you really need to make custom filters, then go look for a more detailed explanation on how to do filtering (:ref:`modifying#filters`) and create custom effects (:ref:`create_effects`) in the user guide.

   What you need to remember is just that we can apply filters on images. Here we do it mathematically, but you could very well use a library such as Pillow (provided it can understand numpy images) to do the maths for you!

.. literalinclude:: /_static/code/getting_started/moviepy_10_minutes/trailer.py
    :language: python
    :lines: 242-283

Step 11: Rendering the Final Clip to a File
-------------------------------------------

So, our final clip is ready, and we have made all the cutting and modifications we want. We are now ready to save the final result into a file. In video editing, this operation is known as rendering.

Again, we will keep things simple and just do video rendering without much tweaking. In most cases, MoviePy and FFmpeg will automatically find the best settings. Take a look at :py:meth:`~moviepy.video.VideoClip.VideoClip.write_videofile` for more info.

.. literalinclude:: /_static/code/getting_started/moviepy_10_minutes/trailer.py
    :language: python
    :lines: 286-307

Conclusion
----------

Congratulations! You have successfully created a trailer for the movie "Big Buck Bunny" using the MoviePy library. This tutorial covered the basics of MoviePy, including loading videos, trimming scenes, adding effects and transitions, overlaying text, and even a little bit of filtering.

If you want to dig deeper into MoviePy, we encourage you to try and experiment with this base example by using different effects, transitions, and audio elements to make your trailer truly captivating. We also encourage you to go and read the :ref:`user_guide`, as well as looking directly at the :ref:`reference_manual`.
````

## File: docs/getting_started/quick_presentation.rst
````
.. _quick_presentation:

Quick presentation
===================

This section explains when MoviePy can be used and how it works.

Do I need MoviePy?
~~~~~~~~~~~~~~~~~~~

Here are a few reasons why you may want to edit videos in Python:

- You have many videos to process or to compose in a complicated way.
- You want to automate the creation of videos or GIFs on a web server (Django, Flask, etc.)
- You want to automate tedious tasks, like title insertions tracking objects, cutting scenes, making end credits, subtitles, etc...
- You want to code your own video effects to do something no existing video editor can.
- You want to create animations from images generated by another python library (Matplotlib, Mayavi, Gizeh, scikit-images...)

And here are a few uses for which MoviePy is NOT the best solution:

- You only need to do frame-by-frame video analysis (with face detection or other fancy stuff). This could be done with MoviePy in association with other libraries, but really, just use imageio_, OpenCV_ or SimpleCV, these are libraries that specialize in these tasks.
- You only want to convert a video file, or turn a series of image files into a movie. In this case it is better to directly call ``ffmpeg`` (or ``avconv`` or ``mencoder``...) as it will be faster and more memory-efficient than going through MoviePy.


Advantages and limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

MoviePy has been developed with the following goals in mind:

- **Simple and intuitive**. Basic operations can be done in one line. The code is easy to learn and easy to understand for newcomers.
- **Flexible**. You have total control over the frames of the video and audio, and creating your own effects is easy as Py.
- **Portable**. The code uses very common software (Numpy and FFmpeg) and can run on (almost) any machine with (almost) any version of Python.

Limitations:
- MoviePy cannot stream videos (e.g. reading from a webcam, or rendering a video live on a distant machine).
- MoviePy is not really designed for video processing involving many successive frames of a movie (e.g. video stabilization - there is other software better suited for that).
- You can also have memory problems if you use many video, audio, and image sources at the same time (>100).

Example code
~~~~~~~~~~~~~~

In a typical MoviePy script, you load video or audio files, modify them, put them together, and write the final result to a new video file. As an example, let us load a video, lower the volume, add a title in the center of the video for the first ten seconds, and write the result in a file: 

.. literalinclude:: /_static/code/getting_started/quick_presentation/basic_example.py
    :language: python


How MoviePy works
~~~~~~~~~~~~~~~~~~~

MoviePy uses the software ``ffmpeg`` to read and to export video and audio files. It also (optionally) uses ``ffplay`` to allow for video previewing.

Internally, the representation and manipulation of the different media is done using Python's fast numerical library Numpy. Advanced effects and enhancements also use ``pillow`` library.

.. image:: /_static/medias/getting_started/explanations.jpeg
    :width: 570px
    :align: center


The central concept, the clips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The central object of MoviePy is the the :py:class:`Clip <moviepy.Clip.Clip>`, with either :py:class:`~moviepy.audio.AudioClip.AudioClip` for any audio element, or :py:class:`~moviepy.video.VideoClip.VideoClip` for any visual element. Clips really are the base unit of MoviePy, everything you do is with and on them.

Clips can be created from more than just videos or audios though. They can also be created from an image, a text, a custom animation, a folder of images, and even a simple lambda function!

To create your final video, what you will do is essentially:   

#. Load different resources as clips (see :ref:`loading`)
#. Modify them (see :ref:`modifying`)
#. Mixing them into one final clip (see :ref:`compositing`)
#. Render them into a file (see :ref:`rendering`)

Of course, MoviePy offer multiple handy solution and tools to facilitate all these steps, and lets you add new ones by writing your own effects (see :ref:`create_effects`)!


.. _imageio: https://imageio.github.io/
.. _OpenCV: http://opencv.org/
````

## File: docs/getting_started/updating_to_v2.rst
````
.. _updating_to_v2:

Updating from v1.X to v2.X
==========================

MoviePy v2.0 has undergone some large changes with the aim of making the API more consistent
and intuitive. As a result, multiple breaking changes have been made.
Therefore, there is a high likelihood that your pre-v2.0 programs will not run without
some changes.

Dropping support for Python 2
-----------------------------
Starting with version 2.0, MoviePy **no longer supports Python 2**, since Python 2 reached its end of life in 2020. 
Focusing on Python 3.7+ allows MoviePy to take advantage of the latest language features and improvements while maintaining code quality and security. 

Users are encouraged to upgrade to a supported version of Python to continue using MoviePy.

Suppression of ``moviepy.editor`` and simplified importation
------------------------------------------------------------
Before v2.0, it was advised to import from ``moviepy.editor`` whenever you needed to perform some manual operations,
such as previewing or hand editing, because the ``editor`` package handled a lot of magic and initialization, making your life
easier, at the cost of initializing some complex modules like ``pygame``.

With version 2.0, the ``moviepy.editor`` namespace no longer exists. Instead, you should import everything from ``moviepy`` like this:

.. code-block:: python

    from moviepy import *  # Simple and clean; the __all__ is set in moviepy, so only useful things will be loaded
    from moviepy import VideoFileClip  # You can also import only the things you really need

Renaming and API unification
-----------------------------

One of the most significant changes is the renaming of all ``.set_`` methods to ``.with_``. More generally, almost all methods that modify a clip now start
with ``with_``, indicating that they work 'out-of-place', meaning they do not directly modify the clip, but instead copy it, modify the copy, and return the updated copy,
leaving the original clip untouched.

We advise you to check your code for any calls to methods from ``Clip`` objects and verify if there is a matching ``.with_`` equivalent.

Massive refactoring of effects
------------------------------

With version 2.0, effects have undergone significant changes and refactoring. Although the logic of when and why to apply effects remains largely the same, 
the implementation has changed considerably.

If you used any kind of effects, you will need to update your code!

Moving effects from functions to classes
""""""""""""""""""""""""""""""""""""""""""""""

MoviePy version 2.0 introduces a more structured and object-oriented approach to handling effects. Previously, effects were simple Python functions that manipulated video clips or images. 
However, in version 2.0 and onwards, effects are now represented as classes.

This shift allows for better organization, encapsulation, and reusability of code, as well as more comprehensible code. Each effect is now encapsulated within its own class, making it easier to manage and modify. 

All effects now implement the :py:class:`~moviepy.Effect.Effect` abstract class, so if you ever wrote a custom effect.

If you ever wrote your own effect, you will have to migrate to the new object-based implementation. For more information, see :ref:`create_effects`.

Moving from ``clip.fx`` to :py:meth:`~moviepy.Clip.Clip.with_effects`
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The move from functions to objects also meant that MoviePy dropped the method ``Clip.fx`` previously used to apply effects in favor of the new :py:meth:`~moviepy.Clip.Clip.with_effects`.

For more information on how to use effects with v2.0, see :ref:`modifying#effects`.

Removing effects as clip methods
""""""""""""""""""""""""""""""""""

Before version 2.0, when importing from ``moviepy.editor``, effects were added as clip class methods at runtime. This is no longer the case.

If you previously used effects by calling them as clip methods, you must now use :py:meth:`~moviepy.Clip.Clip.with_effects`.

Dropping many external dependencies and unifying the environment
-------------------------------------------------------------

With v1.0, MoviePy relied on many optional external dependencies, attempting to gracefully fall back from one library to another in the event one of them was missing, eventually dropping some features when no library was available.
This resulted in complex and hard-to-maintain code for the MoviePy team, as well as fragmented and hard-to-understand environments for users.

With v2.0, the MoviePy team aimed to offer a simpler, smaller, and more unified dependency list, focusing on ``Pillow`` for all complex image manipulation, and dropping altogether the usage of ``ImageMagick``, ``PyGame``, ``OpenCV``, ``scipy``, ``scikit``, and a few others.

Removed features
-----------------

Unfortunately, reducing the scope of MoviePy and limiting external libraries means that some features had to be removed. If you used any of the following features, you will have to create your own replacements:

- ``moviepy.video.tools.tracking``
- ``moviepy.video.tools.segmenting``
- ``moviepy.video.io.sliders``

Miscellaneous signature changes
-------------------------------

When updating the API and moving from previous libraries to ``Pillow``, some miscellaneous changes also occurred, meaning some method signatures may have changed.

You should check the new signatures if you used any of the following:

- ``TextClip``: Some argument names have changed, and a path to a font file is now needed at object instantiation.
- ``clip.resize`` is now ``clip.resized``.
- ``clip.crop`` is now ``clip.cropped``.
- ``clip.rotate`` is now ``clip.rotated``.
- Any previous ``Clip`` method not starting with ``with_`` now probably starts with it.

Why all these changes and updating from v1.0 to v2.0?
-----------------------------------------------------

You might wonder why all these changes were introduced. The answer is: time.

MoviePy has seen many evolutions since its first release and has become a complex project, with ambitions sometimes too large in relation to the available manpower on the development team.
Over time, as in any project, inconsistencies were introduced to support new functionalities without breaking the current API, and some initial choices no longer reflected the current state of things.

Due to multiple factors, MoviePy underwent a long period during which the main version distributed through PyPi diverged from the GitHub distributed version, causing confusion and chaos.

In an effort to simplify future development and limit confusion by providing a unified environment, it was decided to release a new major version including the many evolutions that happened over the years, which meant breaking changes, and thus a new major version was required.

For anyone interested in how and why all of these decisions were made, you can find much of the discussion in GitHub issues `#1874 <https://github.com/Zulko/moviepy/issues/1874>`_, `#1089 <https://github.com/Zulko/moviepy/issues/1089>`_ and `#2012 <https://github.com/Zulko/moviepy/issues/2012>`_.
````

## File: docs/reference/reference/moviepy.audio.AudioClip.AudioArrayClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.audio.AudioClip.AudioArrayClip
======================================

.. currentmodule:: moviepy.audio.AudioClip

.. autoclass:: AudioArrayClip
   :members:
````

## File: docs/reference/reference/moviepy.audio.AudioClip.AudioClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.audio.AudioClip.AudioClip
=================================

.. currentmodule:: moviepy.audio.AudioClip

.. autoclass:: AudioClip
   :members:
````

## File: docs/reference/reference/moviepy.audio.AudioClip.CompositeAudioClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.audio.AudioClip.CompositeAudioClip
==========================================

.. currentmodule:: moviepy.audio.AudioClip

.. autoclass:: CompositeAudioClip
   :members:
````

## File: docs/reference/reference/moviepy.audio.AudioClip.concatenate_audioclips.rst
````
moviepy.audio.AudioClip.concatenate\_audioclips
===============================================

.. currentmodule:: moviepy.audio.AudioClip

.. autofunction:: concatenate_audioclips
````

## File: docs/reference/reference/moviepy.audio.AudioClip.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.AudioClip
=======================


.. automodule:: moviepy.audio.AudioClip

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      AudioArrayClip
      AudioClip
      CompositeAudioClip
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      concatenate_audioclips
````

## File: docs/reference/reference/moviepy.audio.fx.AudioDelay.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.fx.AudioDelay
===========================

 
.. automodule:: moviepy.audio.fx.AudioDelay
   :inherited-members:
````

## File: docs/reference/reference/moviepy.audio.fx.AudioFadeIn.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.fx.AudioFadeIn
============================

 
.. automodule:: moviepy.audio.fx.AudioFadeIn
   :inherited-members:
````

## File: docs/reference/reference/moviepy.audio.fx.AudioFadeOut.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.fx.AudioFadeOut
=============================

 
.. automodule:: moviepy.audio.fx.AudioFadeOut
   :inherited-members:
````

## File: docs/reference/reference/moviepy.audio.fx.AudioLoop.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.fx.AudioLoop
==========================

 
.. automodule:: moviepy.audio.fx.AudioLoop
   :inherited-members:
````

## File: docs/reference/reference/moviepy.audio.fx.AudioNormalize.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.fx.AudioNormalize
===============================

 
.. automodule:: moviepy.audio.fx.AudioNormalize
   :inherited-members:
````

## File: docs/reference/reference/moviepy.audio.fx.MultiplyStereoVolume.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.fx.MultiplyStereoVolume
=====================================

 
.. automodule:: moviepy.audio.fx.MultiplyStereoVolume
   :inherited-members:
````

## File: docs/reference/reference/moviepy.audio.fx.MultiplyVolume.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.fx.MultiplyVolume
===============================

 
.. automodule:: moviepy.audio.fx.MultiplyVolume
   :inherited-members:
````

## File: docs/reference/reference/moviepy.audio.fx.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.fx
================


.. automodule:: moviepy.audio.fx

   

   
   
   


   
   
   


   
   
   



.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: custom_autosummary/module.rst
   :recursive:


   moviepy.audio.fx.AudioDelay


   moviepy.audio.fx.AudioFadeIn


   moviepy.audio.fx.AudioFadeOut


   moviepy.audio.fx.AudioLoop


   moviepy.audio.fx.AudioNormalize


   moviepy.audio.fx.MultiplyStereoVolume


   moviepy.audio.fx.MultiplyVolume
````

## File: docs/reference/reference/moviepy.audio.io.AudioFileClip.AudioFileClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.audio.io.AudioFileClip.AudioFileClip
============================================

.. currentmodule:: moviepy.audio.io.AudioFileClip

.. autoclass:: AudioFileClip
   :members:
````

## File: docs/reference/reference/moviepy.audio.io.AudioFileClip.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.io.AudioFileClip
==============================


.. automodule:: moviepy.audio.io.AudioFileClip

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      AudioFileClip
````

## File: docs/reference/reference/moviepy.audio.io.ffmpeg_audiowriter.ffmpeg_audiowrite.rst
````
moviepy.audio.io.ffmpeg\_audiowriter.ffmpeg\_audiowrite
=======================================================

.. currentmodule:: moviepy.audio.io.ffmpeg_audiowriter

.. autofunction:: ffmpeg_audiowrite
````

## File: docs/reference/reference/moviepy.audio.io.ffmpeg_audiowriter.FFMPEG_AudioWriter.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.audio.io.ffmpeg\_audiowriter.FFMPEG\_AudioWriter
========================================================

.. currentmodule:: moviepy.audio.io.ffmpeg_audiowriter

.. autoclass:: FFMPEG_AudioWriter
   :members:
````

## File: docs/reference/reference/moviepy.audio.io.ffmpeg_audiowriter.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.io.ffmpeg\_audiowriter
====================================


.. automodule:: moviepy.audio.io.ffmpeg_audiowriter

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      FFMPEG_AudioWriter
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      ffmpeg_audiowrite
````

## File: docs/reference/reference/moviepy.audio.io.ffplay_audiopreviewer.ffplay_audiopreview.rst
````
moviepy.audio.io.ffplay\_audiopreviewer.ffplay\_audiopreview
============================================================

.. currentmodule:: moviepy.audio.io.ffplay_audiopreviewer

.. autofunction:: ffplay_audiopreview
````

## File: docs/reference/reference/moviepy.audio.io.ffplay_audiopreviewer.FFPLAY_AudioPreviewer.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.audio.io.ffplay\_audiopreviewer.FFPLAY\_AudioPreviewer
==============================================================

.. currentmodule:: moviepy.audio.io.ffplay_audiopreviewer

.. autoclass:: FFPLAY_AudioPreviewer
   :members:
````

## File: docs/reference/reference/moviepy.audio.io.ffplay_audiopreviewer.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.io.ffplay\_audiopreviewer
=======================================


.. automodule:: moviepy.audio.io.ffplay_audiopreviewer

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      FFPLAY_AudioPreviewer
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      ffplay_audiopreview
````

## File: docs/reference/reference/moviepy.audio.io.readers.FFMPEG_AudioReader.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.audio.io.readers.FFMPEG\_AudioReader
============================================

.. currentmodule:: moviepy.audio.io.readers

.. autoclass:: FFMPEG_AudioReader
   :members:
````

## File: docs/reference/reference/moviepy.audio.io.readers.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.io.readers
========================


.. automodule:: moviepy.audio.io.readers

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      FFMPEG_AudioReader
````

## File: docs/reference/reference/moviepy.audio.io.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.io
================


.. automodule:: moviepy.audio.io

   

   
   
   


   
   
   


   
   
   



.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: custom_autosummary/module.rst
   :recursive:


   moviepy.audio.io.AudioFileClip


   moviepy.audio.io.ffmpeg_audiowriter


   moviepy.audio.io.ffplay_audiopreviewer


   moviepy.audio.io.readers
````

## File: docs/reference/reference/moviepy.audio.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio
=============


.. automodule:: moviepy.audio

   

   
   
   


   
   
   


   
   
   



.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: custom_autosummary/module.rst
   :recursive:


   moviepy.audio.AudioClip


   moviepy.audio.fx


   moviepy.audio.io


   moviepy.audio.tools
````

## File: docs/reference/reference/moviepy.audio.tools.cuts.find_audio_period.rst
````
moviepy.audio.tools.cuts.find\_audio\_period
============================================

.. currentmodule:: moviepy.audio.tools.cuts

.. autofunction:: find_audio_period
````

## File: docs/reference/reference/moviepy.audio.tools.cuts.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.tools.cuts
========================


.. automodule:: moviepy.audio.tools.cuts

   

   
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      find_audio_period
````

## File: docs/reference/reference/moviepy.audio.tools.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.audio.tools
===================


.. automodule:: moviepy.audio.tools

   

   
   
   


   
   
   


   
   
   



.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: custom_autosummary/module.rst
   :recursive:


   moviepy.audio.tools.cuts
````

## File: docs/reference/reference/moviepy.Clip.Clip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.Clip.Clip
=================

.. currentmodule:: moviepy.Clip

.. autoclass:: Clip
   :members:
````

## File: docs/reference/reference/moviepy.Clip.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.Clip
============


.. automodule:: moviepy.Clip

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      Clip
````

## File: docs/reference/reference/moviepy.config.check.rst
````
moviepy.config.check
====================

.. currentmodule:: moviepy.config

.. autofunction:: check
````

## File: docs/reference/reference/moviepy.config.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.config
==============


.. automodule:: moviepy.config

   

   
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      check
      try_cmd
````

## File: docs/reference/reference/moviepy.config.try_cmd.rst
````
moviepy.config.try\_cmd
=======================

.. currentmodule:: moviepy.config

.. autofunction:: try_cmd
````

## File: docs/reference/reference/moviepy.decorators.add_mask_if_none.rst
````
moviepy.decorators.add\_mask\_if\_none
======================================

.. currentmodule:: moviepy.decorators

.. autofunction:: add_mask_if_none
````

## File: docs/reference/reference/moviepy.decorators.apply_to_audio.rst
````
moviepy.decorators.apply\_to\_audio
===================================

.. currentmodule:: moviepy.decorators

.. autofunction:: apply_to_audio
````

## File: docs/reference/reference/moviepy.decorators.apply_to_mask.rst
````
moviepy.decorators.apply\_to\_mask
==================================

.. currentmodule:: moviepy.decorators

.. autofunction:: apply_to_mask
````

## File: docs/reference/reference/moviepy.decorators.audio_video_effect.rst
````
moviepy.decorators.audio\_video\_effect
=======================================

.. currentmodule:: moviepy.decorators

.. autofunction:: audio_video_effect
````

## File: docs/reference/reference/moviepy.decorators.convert_masks_to_RGB.rst
````
moviepy.decorators.convert\_masks\_to\_RGB
==========================================

.. currentmodule:: moviepy.decorators

.. autofunction:: convert_masks_to_RGB
````

## File: docs/reference/reference/moviepy.decorators.convert_parameter_to_seconds.rst
````
moviepy.decorators.convert\_parameter\_to\_seconds
==================================================

.. currentmodule:: moviepy.decorators

.. autofunction:: convert_parameter_to_seconds
````

## File: docs/reference/reference/moviepy.decorators.convert_path_to_string.rst
````
moviepy.decorators.convert\_path\_to\_string
============================================

.. currentmodule:: moviepy.decorators

.. autofunction:: convert_path_to_string
````

## File: docs/reference/reference/moviepy.decorators.outplace.rst
````
moviepy.decorators.outplace
===========================

.. currentmodule:: moviepy.decorators

.. autofunction:: outplace
````

## File: docs/reference/reference/moviepy.decorators.preprocess_args.rst
````
moviepy.decorators.preprocess\_args
===================================

.. currentmodule:: moviepy.decorators

.. autofunction:: preprocess_args
````

## File: docs/reference/reference/moviepy.decorators.requires_duration.rst
````
moviepy.decorators.requires\_duration
=====================================

.. currentmodule:: moviepy.decorators

.. autofunction:: requires_duration
````

## File: docs/reference/reference/moviepy.decorators.requires_fps.rst
````
moviepy.decorators.requires\_fps
================================

.. currentmodule:: moviepy.decorators

.. autofunction:: requires_fps
````

## File: docs/reference/reference/moviepy.decorators.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.decorators
==================


.. automodule:: moviepy.decorators

   

   
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      add_mask_if_none
      apply_to_audio
      apply_to_mask
      audio_video_effect
      convert_masks_to_RGB
      convert_parameter_to_seconds
      convert_path_to_string
      outplace
      preprocess_args
      requires_duration
      requires_fps
      use_clip_fps_by_default
````

## File: docs/reference/reference/moviepy.decorators.use_clip_fps_by_default.rst
````
moviepy.decorators.use\_clip\_fps\_by\_default
==============================================

.. currentmodule:: moviepy.decorators

.. autofunction:: use_clip_fps_by_default
````

## File: docs/reference/reference/moviepy.Effect.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.Effect
==============

 
.. automodule:: moviepy.Effect
   :inherited-members:
````

## File: docs/reference/reference/moviepy.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy
=======


.. automodule:: moviepy

   

   
   
   


   
   
   


   
   
   



.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: custom_autosummary/module.rst
   :recursive:


   moviepy.Clip


   moviepy.Effect


   moviepy.audio


   moviepy.config


   moviepy.decorators


   moviepy.tools



   moviepy.video
````

## File: docs/reference/reference/moviepy.tools.close_all_clips.rst
````
moviepy.tools.close\_all\_clips
===============================

.. currentmodule:: moviepy.tools

.. autofunction:: close_all_clips
````

## File: docs/reference/reference/moviepy.tools.convert_to_seconds.rst
````
moviepy.tools.convert\_to\_seconds
==================================

.. currentmodule:: moviepy.tools

.. autofunction:: convert_to_seconds
````

## File: docs/reference/reference/moviepy.tools.cross_platform_popen_params.rst
````
moviepy.tools.cross\_platform\_popen\_params
============================================

.. currentmodule:: moviepy.tools

.. autofunction:: cross_platform_popen_params
````

## File: docs/reference/reference/moviepy.tools.deprecated_version_of.rst
````
moviepy.tools.deprecated\_version\_of
=====================================

.. currentmodule:: moviepy.tools

.. autofunction:: deprecated_version_of
````

## File: docs/reference/reference/moviepy.tools.find_extension.rst
````
moviepy.tools.find\_extension
=============================

.. currentmodule:: moviepy.tools

.. autofunction:: find_extension
````

## File: docs/reference/reference/moviepy.tools.no_display_available.rst
````
moviepy.tools.no\_display\_available
====================================

.. currentmodule:: moviepy.tools

.. autofunction:: no_display_available
````

## File: docs/reference/reference/moviepy.tools.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.tools
=============


.. automodule:: moviepy.tools

   

   
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      close_all_clips
      convert_to_seconds
      cross_platform_popen_params
      deprecated_version_of
      find_extension
      no_display_available
      subprocess_call
````

## File: docs/reference/reference/moviepy.tools.subprocess_call.rst
````
moviepy.tools.subprocess\_call
==============================

.. currentmodule:: moviepy.tools

.. autofunction:: subprocess_call
````

## File: docs/reference/reference/moviepy.video.compositing.CompositeVideoClip.clips_array.rst
````
moviepy.video.compositing.CompositeVideoClip.clips\_array
=========================================================

.. currentmodule:: moviepy.video.compositing.CompositeVideoClip

.. autofunction:: clips_array
````

## File: docs/reference/reference/moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip
===============================================================

.. currentmodule:: moviepy.video.compositing.CompositeVideoClip

.. autoclass:: CompositeVideoClip
   :members:
````

## File: docs/reference/reference/moviepy.video.compositing.CompositeVideoClip.concatenate_videoclips.rst
````
moviepy.video.compositing.CompositeVideoClip.concatenate\_videoclips
====================================================================

.. currentmodule:: moviepy.video.compositing.CompositeVideoClip

.. autofunction:: concatenate_videoclips
````

## File: docs/reference/reference/moviepy.video.compositing.CompositeVideoClip.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.compositing.CompositeVideoClip
============================================


.. automodule:: moviepy.video.compositing.CompositeVideoClip

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      CompositeVideoClip
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      clips_array
      concatenate_videoclips
````

## File: docs/reference/reference/moviepy.video.compositing.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.compositing
=========================


.. automodule:: moviepy.video.compositing

   

   
   
   


   
   
   


   
   
   



.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: custom_autosummary/module.rst
   :recursive:


   moviepy.video.compositing.CompositeVideoClip
````

## File: docs/reference/reference/moviepy.video.fx.AccelDecel.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.AccelDecel
===========================

 
.. automodule:: moviepy.video.fx.AccelDecel
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.BlackAndWhite.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.BlackAndWhite
==============================

 
.. automodule:: moviepy.video.fx.BlackAndWhite
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.Blink.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.Blink
======================

 
.. automodule:: moviepy.video.fx.Blink
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.Crop.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.Crop
=====================

 
.. automodule:: moviepy.video.fx.Crop
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.CrossFadeIn.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.CrossFadeIn
============================

 
.. automodule:: moviepy.video.fx.CrossFadeIn
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.CrossFadeOut.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.CrossFadeOut
=============================

 
.. automodule:: moviepy.video.fx.CrossFadeOut
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.EvenSize.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.EvenSize
=========================

 
.. automodule:: moviepy.video.fx.EvenSize
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.FadeIn.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.FadeIn
=======================

 
.. automodule:: moviepy.video.fx.FadeIn
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.FadeOut.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.FadeOut
========================

 
.. automodule:: moviepy.video.fx.FadeOut
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.Freeze.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.Freeze
=======================

 
.. automodule:: moviepy.video.fx.Freeze
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.FreezeRegion.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.FreezeRegion
=============================

 
.. automodule:: moviepy.video.fx.FreezeRegion
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.GammaCorrection.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.GammaCorrection
================================

 
.. automodule:: moviepy.video.fx.GammaCorrection
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.HeadBlur.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.HeadBlur
=========================

 
.. automodule:: moviepy.video.fx.HeadBlur
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.InvertColors.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.InvertColors
=============================

 
.. automodule:: moviepy.video.fx.InvertColors
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.Loop.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.Loop
=====================

 
.. automodule:: moviepy.video.fx.Loop
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.LumContrast.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.LumContrast
============================

 
.. automodule:: moviepy.video.fx.LumContrast
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.MakeLoopable.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.MakeLoopable
=============================

 
.. automodule:: moviepy.video.fx.MakeLoopable
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.Margin.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.Margin
=======================

 
.. automodule:: moviepy.video.fx.Margin
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.MaskColor.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.MaskColor
==========================

 
.. automodule:: moviepy.video.fx.MaskColor
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.MasksAnd.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.MasksAnd
=========================

 
.. automodule:: moviepy.video.fx.MasksAnd
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.MasksOr.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.MasksOr
========================

 
.. automodule:: moviepy.video.fx.MasksOr
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.MirrorX.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.MirrorX
========================

 
.. automodule:: moviepy.video.fx.MirrorX
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.MirrorY.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.MirrorY
========================

 
.. automodule:: moviepy.video.fx.MirrorY
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.MultiplyColor.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.MultiplyColor
==============================

 
.. automodule:: moviepy.video.fx.MultiplyColor
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.MultiplySpeed.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.MultiplySpeed
==============================

 
.. automodule:: moviepy.video.fx.MultiplySpeed
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.Painting.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.Painting
=========================

 
.. automodule:: moviepy.video.fx.Painting
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.Resize.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.Resize
=======================

 
.. automodule:: moviepy.video.fx.Resize
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.Rotate.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.Rotate
=======================

 
.. automodule:: moviepy.video.fx.Rotate
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx
================


.. automodule:: moviepy.video.fx

   

   
   
   


   
   
   


   
   
   



.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: custom_autosummary/module.rst
   :recursive:


   moviepy.video.fx.AccelDecel


   moviepy.video.fx.BlackAndWhite


   moviepy.video.fx.Blink


   moviepy.video.fx.Crop


   moviepy.video.fx.CrossFadeIn


   moviepy.video.fx.CrossFadeOut


   moviepy.video.fx.EvenSize


   moviepy.video.fx.FadeIn


   moviepy.video.fx.FadeOut


   moviepy.video.fx.Freeze


   moviepy.video.fx.FreezeRegion


   moviepy.video.fx.GammaCorrection


   moviepy.video.fx.HeadBlur


   moviepy.video.fx.InvertColors


   moviepy.video.fx.Loop


   moviepy.video.fx.LumContrast


   moviepy.video.fx.MakeLoopable


   moviepy.video.fx.Margin


   moviepy.video.fx.MaskColor


   moviepy.video.fx.MasksAnd


   moviepy.video.fx.MasksOr


   moviepy.video.fx.MirrorX


   moviepy.video.fx.MirrorY


   moviepy.video.fx.MultiplyColor


   moviepy.video.fx.MultiplySpeed


   moviepy.video.fx.Painting


   moviepy.video.fx.Resize


   moviepy.video.fx.Rotate


   moviepy.video.fx.Scroll


   moviepy.video.fx.SlideIn


   moviepy.video.fx.SlideOut


   moviepy.video.fx.SuperSample


   moviepy.video.fx.TimeMirror


   moviepy.video.fx.TimeSymmetrize
````

## File: docs/reference/reference/moviepy.video.fx.Scroll.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.Scroll
=======================

 
.. automodule:: moviepy.video.fx.Scroll
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.SlideIn.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.SlideIn
========================

 
.. automodule:: moviepy.video.fx.SlideIn
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.SlideOut.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.SlideOut
=========================

 
.. automodule:: moviepy.video.fx.SlideOut
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.SuperSample.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.SuperSample
============================

 
.. automodule:: moviepy.video.fx.SuperSample
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.TimeMirror.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.TimeMirror
===========================

 
.. automodule:: moviepy.video.fx.TimeMirror
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.fx.TimeSymmetrize.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.fx.TimeSymmetrize
===============================

 
.. automodule:: moviepy.video.fx.TimeSymmetrize
   :inherited-members:
````

## File: docs/reference/reference/moviepy.video.io.display_in_notebook.display_in_notebook.rst
````
moviepy.video.io.display\_in\_notebook.display\_in\_notebook
============================================================

.. currentmodule:: moviepy.video.io.display_in_notebook

.. autofunction:: display_in_notebook
````

## File: docs/reference/reference/moviepy.video.io.display_in_notebook.html_embed.rst
````
moviepy.video.io.display\_in\_notebook.html\_embed
==================================================

.. currentmodule:: moviepy.video.io.display_in_notebook

.. autofunction:: html_embed
````

## File: docs/reference/reference/moviepy.video.io.display_in_notebook.HTML2.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.io.display\_in\_notebook.HTML2
============================================

.. currentmodule:: moviepy.video.io.display_in_notebook

.. autoclass:: HTML2
   :members:
````

## File: docs/reference/reference/moviepy.video.io.display_in_notebook.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.io.display\_in\_notebook
======================================


.. automodule:: moviepy.video.io.display_in_notebook

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      HTML2
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      display_in_notebook
      html_embed
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_reader.ffmpeg_parse_infos.rst
````
moviepy.video.io.ffmpeg\_reader.ffmpeg\_parse\_infos
====================================================

.. currentmodule:: moviepy.video.io.ffmpeg_reader

.. autofunction:: ffmpeg_parse_infos
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_reader.ffmpeg_read_image.rst
````
moviepy.video.io.ffmpeg\_reader.ffmpeg\_read\_image
===================================================

.. currentmodule:: moviepy.video.io.ffmpeg_reader

.. autofunction:: ffmpeg_read_image
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_reader.FFMPEG_VideoReader.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.io.ffmpeg\_reader.FFMPEG\_VideoReader
===================================================

.. currentmodule:: moviepy.video.io.ffmpeg_reader

.. autoclass:: FFMPEG_VideoReader
   :members:
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_reader.FFmpegInfosParser.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.io.ffmpeg\_reader.FFmpegInfosParser
=================================================

.. currentmodule:: moviepy.video.io.ffmpeg_reader

.. autoclass:: FFmpegInfosParser
   :members:
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_reader.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.io.ffmpeg\_reader
===============================


.. automodule:: moviepy.video.io.ffmpeg_reader

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      FFMPEG_VideoReader
      FFmpegInfosParser
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      ffmpeg_parse_infos
      ffmpeg_read_image
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_tools.ffmpeg_extract_audio.rst
````
moviepy.video.io.ffmpeg\_tools.ffmpeg\_extract\_audio
=====================================================

.. currentmodule:: moviepy.video.io.ffmpeg_tools

.. autofunction:: ffmpeg_extract_audio
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_tools.ffmpeg_extract_subclip.rst
````
moviepy.video.io.ffmpeg\_tools.ffmpeg\_extract\_subclip
=======================================================

.. currentmodule:: moviepy.video.io.ffmpeg_tools

.. autofunction:: ffmpeg_extract_subclip
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_tools.ffmpeg_merge_video_audio.rst
````
moviepy.video.io.ffmpeg\_tools.ffmpeg\_merge\_video\_audio
==========================================================

.. currentmodule:: moviepy.video.io.ffmpeg_tools

.. autofunction:: ffmpeg_merge_video_audio
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_tools.ffmpeg_resize.rst
````
moviepy.video.io.ffmpeg\_tools.ffmpeg\_resize
=============================================

.. currentmodule:: moviepy.video.io.ffmpeg_tools

.. autofunction:: ffmpeg_resize
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_tools.ffmpeg_stabilize_video.rst
````
moviepy.video.io.ffmpeg\_tools.ffmpeg\_stabilize\_video
=======================================================

.. currentmodule:: moviepy.video.io.ffmpeg_tools

.. autofunction:: ffmpeg_stabilize_video
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_tools.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.io.ffmpeg\_tools
==============================


.. automodule:: moviepy.video.io.ffmpeg_tools

   

   
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      ffmpeg_extract_audio
      ffmpeg_extract_subclip
      ffmpeg_merge_video_audio
      ffmpeg_resize
      ffmpeg_stabilize_video
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_writer.FFMPEG_VideoWriter.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.io.ffmpeg\_writer.FFMPEG\_VideoWriter
===================================================

.. currentmodule:: moviepy.video.io.ffmpeg_writer

.. autoclass:: FFMPEG_VideoWriter
   :members:
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_writer.ffmpeg_write_image.rst
````
moviepy.video.io.ffmpeg\_writer.ffmpeg\_write\_image
====================================================

.. currentmodule:: moviepy.video.io.ffmpeg_writer

.. autofunction:: ffmpeg_write_image
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_writer.ffmpeg_write_video.rst
````
moviepy.video.io.ffmpeg\_writer.ffmpeg\_write\_video
====================================================

.. currentmodule:: moviepy.video.io.ffmpeg_writer

.. autofunction:: ffmpeg_write_video
````

## File: docs/reference/reference/moviepy.video.io.ffmpeg_writer.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.io.ffmpeg\_writer
===============================


.. automodule:: moviepy.video.io.ffmpeg_writer

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      FFMPEG_VideoWriter
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      ffmpeg_write_image
      ffmpeg_write_video
````

## File: docs/reference/reference/moviepy.video.io.ffplay_previewer.ffplay_preview_video.rst
````
moviepy.video.io.ffplay\_previewer.ffplay\_preview\_video
=========================================================

.. currentmodule:: moviepy.video.io.ffplay_previewer

.. autofunction:: ffplay_preview_video
````

## File: docs/reference/reference/moviepy.video.io.ffplay_previewer.FFPLAY_VideoPreviewer.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.io.ffplay\_previewer.FFPLAY\_VideoPreviewer
=========================================================

.. currentmodule:: moviepy.video.io.ffplay_previewer

.. autoclass:: FFPLAY_VideoPreviewer
   :members:
````

## File: docs/reference/reference/moviepy.video.io.ffplay_previewer.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.io.ffplay\_previewer
==================================


.. automodule:: moviepy.video.io.ffplay_previewer

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      FFPLAY_VideoPreviewer
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      ffplay_preview_video
````

## File: docs/reference/reference/moviepy.video.io.gif_writers.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.io.gif\_writers
=============================


.. automodule:: moviepy.video.io.gif_writers

   

   
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      write_gif_with_imageio
````

## File: docs/reference/reference/moviepy.video.io.gif_writers.write_gif_with_imageio.rst
````
moviepy.video.io.gif\_writers.write\_gif\_with\_imageio
=======================================================

.. currentmodule:: moviepy.video.io.gif_writers

.. autofunction:: write_gif_with_imageio
````

## File: docs/reference/reference/moviepy.video.io.ImageSequenceClip.ImageSequenceClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.io.ImageSequenceClip.ImageSequenceClip
====================================================

.. currentmodule:: moviepy.video.io.ImageSequenceClip

.. autoclass:: ImageSequenceClip
   :members:
````

## File: docs/reference/reference/moviepy.video.io.ImageSequenceClip.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.io.ImageSequenceClip
==================================


.. automodule:: moviepy.video.io.ImageSequenceClip

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      ImageSequenceClip
````

## File: docs/reference/reference/moviepy.video.io.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.io
================


.. automodule:: moviepy.video.io

   

   
   
   


   
   
   


   
   
   



.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: custom_autosummary/module.rst
   :recursive:


   moviepy.video.io.ImageSequenceClip


   moviepy.video.io.VideoFileClip


   moviepy.video.io.display_in_notebook


   moviepy.video.io.ffmpeg_reader


   moviepy.video.io.ffmpeg_tools


   moviepy.video.io.ffmpeg_writer


   moviepy.video.io.ffplay_previewer


   moviepy.video.io.gif_writers
````

## File: docs/reference/reference/moviepy.video.io.VideoFileClip.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.io.VideoFileClip
==============================


.. automodule:: moviepy.video.io.VideoFileClip

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      VideoFileClip
````

## File: docs/reference/reference/moviepy.video.io.VideoFileClip.VideoFileClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.io.VideoFileClip.VideoFileClip
============================================

.. currentmodule:: moviepy.video.io.VideoFileClip

.. autoclass:: VideoFileClip
   :members:
````

## File: docs/reference/reference/moviepy.video.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video
=============


.. automodule:: moviepy.video

   

   
   
   


   
   
   


   
   
   



.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: custom_autosummary/module.rst
   :recursive:


   moviepy.video.VideoClip


   moviepy.video.compositing


   moviepy.video.fx


   moviepy.video.io


   moviepy.video.tools
````

## File: docs/reference/reference/moviepy.video.tools.credits.CreditsClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.tools.credits.CreditsClip
=======================================

.. currentmodule:: moviepy.video.tools.credits

.. autoclass:: CreditsClip
   :members:
````

## File: docs/reference/reference/moviepy.video.tools.credits.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.tools.credits
===========================


.. automodule:: moviepy.video.tools.credits

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      CreditsClip
````

## File: docs/reference/reference/moviepy.video.tools.cuts.detect_scenes.rst
````
moviepy.video.tools.cuts.detect\_scenes
=======================================

.. currentmodule:: moviepy.video.tools.cuts

.. autofunction:: detect_scenes
````

## File: docs/reference/reference/moviepy.video.tools.cuts.find_video_period.rst
````
moviepy.video.tools.cuts.find\_video\_period
============================================

.. currentmodule:: moviepy.video.tools.cuts

.. autofunction:: find_video_period
````

## File: docs/reference/reference/moviepy.video.tools.cuts.FramesMatch.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.tools.cuts.FramesMatch
====================================

.. currentmodule:: moviepy.video.tools.cuts

.. autoclass:: FramesMatch
   :members:
````

## File: docs/reference/reference/moviepy.video.tools.cuts.FramesMatches.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.tools.cuts.FramesMatches
======================================

.. currentmodule:: moviepy.video.tools.cuts

.. autoclass:: FramesMatches
   :members:
````

## File: docs/reference/reference/moviepy.video.tools.cuts.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.tools.cuts
========================


.. automodule:: moviepy.video.tools.cuts

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      FramesMatch
      FramesMatches
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      detect_scenes
      find_video_period
````

## File: docs/reference/reference/moviepy.video.tools.drawing.blit.rst
````
moviepy.video.tools.drawing.blit
================================

.. currentmodule:: moviepy.video.tools.drawing

.. autofunction:: blit
````

## File: docs/reference/reference/moviepy.video.tools.drawing.circle.rst
````
moviepy.video.tools.drawing.circle
==================================

.. currentmodule:: moviepy.video.tools.drawing

.. autofunction:: circle
````

## File: docs/reference/reference/moviepy.video.tools.drawing.color_gradient.rst
````
moviepy.video.tools.drawing.color\_gradient
===========================================

.. currentmodule:: moviepy.video.tools.drawing

.. autofunction:: color_gradient
````

## File: docs/reference/reference/moviepy.video.tools.drawing.color_split.rst
````
moviepy.video.tools.drawing.color\_split
========================================

.. currentmodule:: moviepy.video.tools.drawing

.. autofunction:: color_split
````

## File: docs/reference/reference/moviepy.video.tools.drawing.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.tools.drawing
===========================


.. automodule:: moviepy.video.tools.drawing

   

   
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      blit
      circle
      color_gradient
      color_split
````

## File: docs/reference/reference/moviepy.video.tools.interpolators.Interpolator.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.tools.interpolators.Interpolator
==============================================

.. currentmodule:: moviepy.video.tools.interpolators

.. autoclass:: Interpolator
   :members:
````

## File: docs/reference/reference/moviepy.video.tools.interpolators.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.tools.interpolators
=================================


.. automodule:: moviepy.video.tools.interpolators

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      Interpolator
      Trajectory
````

## File: docs/reference/reference/moviepy.video.tools.interpolators.Trajectory.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.tools.interpolators.Trajectory
============================================

.. currentmodule:: moviepy.video.tools.interpolators

.. autoclass:: Trajectory
   :members:
````

## File: docs/reference/reference/moviepy.video.tools.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.tools
===================


.. automodule:: moviepy.video.tools

   

   
   
   


   
   
   


   
   
   



.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: custom_autosummary/module.rst
   :recursive:


   moviepy.video.tools.credits


   moviepy.video.tools.cuts


   moviepy.video.tools.drawing


   moviepy.video.tools.interpolators


   moviepy.video.tools.subtitles
````

## File: docs/reference/reference/moviepy.video.tools.subtitles.file_to_subtitles.rst
````
moviepy.video.tools.subtitles.file\_to\_subtitles
=================================================

.. currentmodule:: moviepy.video.tools.subtitles

.. autofunction:: file_to_subtitles
````

## File: docs/reference/reference/moviepy.video.tools.subtitles.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.tools.subtitles
=============================


.. automodule:: moviepy.video.tools.subtitles

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      SubtitlesClip
   
   


   
   
   .. rubric:: Functions

   .. autosummary::
      :toctree:
   
      file_to_subtitles
````

## File: docs/reference/reference/moviepy.video.tools.subtitles.SubtitlesClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.tools.subtitles.SubtitlesClip
===========================================

.. currentmodule:: moviepy.video.tools.subtitles

.. autoclass:: SubtitlesClip
   :members:
````

## File: docs/reference/reference/moviepy.video.VideoClip.BitmapClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.VideoClip.BitmapClip
==================================

.. currentmodule:: moviepy.video.VideoClip

.. autoclass:: BitmapClip
   :members:
````

## File: docs/reference/reference/moviepy.video.VideoClip.ColorClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.VideoClip.ColorClip
=================================

.. currentmodule:: moviepy.video.VideoClip

.. autoclass:: ColorClip
   :members:
````

## File: docs/reference/reference/moviepy.video.VideoClip.DataVideoClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.VideoClip.DataVideoClip
=====================================

.. currentmodule:: moviepy.video.VideoClip

.. autoclass:: DataVideoClip
   :members:
````

## File: docs/reference/reference/moviepy.video.VideoClip.ImageClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.VideoClip.ImageClip
=================================

.. currentmodule:: moviepy.video.VideoClip

.. autoclass:: ImageClip
   :members:
````

## File: docs/reference/reference/moviepy.video.VideoClip.rst
````
.. custom module to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202
   
moviepy.video.VideoClip
=======================


.. automodule:: moviepy.video.VideoClip

   

   
   
   .. rubric:: Classes

   .. autosummary::
      :toctree:
      :template: custom_autosummary/class.rst
   
      BitmapClip
      ColorClip
      DataVideoClip
      ImageClip
      TextClip
      UpdatedVideoClip
      VideoClip
````

## File: docs/reference/reference/moviepy.video.VideoClip.TextClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.VideoClip.TextClip
================================

.. currentmodule:: moviepy.video.VideoClip

.. autoclass:: TextClip
   :members:
````

## File: docs/reference/reference/moviepy.video.VideoClip.UpdatedVideoClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.VideoClip.UpdatedVideoClip
========================================

.. currentmodule:: moviepy.video.VideoClip

.. autoclass:: UpdatedVideoClip
   :members:
````

## File: docs/reference/reference/moviepy.video.VideoClip.VideoClip.rst
````
.. custom class to enable complete documentation of every function
   see https://stackoverflow.com/a/62613202

moviepy.video.VideoClip.VideoClip
=================================

.. currentmodule:: moviepy.video.VideoClip

.. autoclass:: VideoClip
   :members:
````

## File: docs/reference/index.rst
````
.. _reference_manual:


Api Reference
================

This is the definitive place to find all the details on MoviePy API documentation.

For a more beginner introduction, please see :ref:`getting_started`, for a more detailed explanations of the different concepts in MoviePy,
see :ref:`user_guide`.

.. autosummary::
   :toctree: reference
   :recursive:
   :template: custom_autosummary/module.rst

   moviepy
````

## File: docs/user_guide/compositing.rst
````
.. _compositing:

Compositing Multiple Clips
=========================================

Video composition, also known as non-linear editing, is the process of mixing and playing several clips together in a new clip. This video is a good example of what compositing you can do with MoviePy:

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; padding-top: 30px; margin-bottom:30px; height: 0; overflow: hidden; margin-left:15%;">
        <iframe type="text/html" src="https://youtube.com/embed/rIehsqqYFEM?rel=0" frameborder="0"
        style="position: absolute; top: 0; bottom: 10; width: 70%; height: 100%; "></iframe>
    </div>

.. note::
    Before starting, note that video clips generally carry an audio track and a mask, which are also clips. When you compose these clips together, the soundtrack and mask of the final clip are automatically generated by putting together the soundtracks and masks of the clips.
    So most of the time you don't need to worry about mixing the audio and masks.

Juxtaposing and Concatenating Clips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two simple ways of putting clips together are to concatenate them (to play them one after the other in a single long clip) or to juxtapose them (to put them side by side in a single larger clip).

Concatenating Multiple Clips
"""""""""""""""""""""""""""""""""

Concatenation can be done very easily with the function :py:func:`~moviepy.video.compositing.CompositeVideoClip.concatenate_videoclips`.

.. literalinclude:: /_static/code/user_guide/compositing/concatenate.py
    :language: python

The ``final_clip`` is a clip that plays the clips 1, 2, and 3 one after the other.

.. note::
    The clips do not need to be the same size. If they aren't, they will all appear centered in a clip large enough to contain the biggest of them, with optionally a color of your choosing to fill the background.

For more info, see :py:func:`~moviepy.video.compositing.CompositeVideoClip.concatenate_videoclips`.

Juxtaposing Multiple Clips
""""""""""""""""""""""""""""""

Putting multiple clips side by side is done with :py:func:`~moviepy.video.compositing.CompositeVideoClip.clip_array`:

.. literalinclude:: /_static/code/user_guide/compositing/juxtaposing.py
    :language: python

You obtain a clip which looks like this:

.. figure:: /_static/medias/user_guide/stacked.jpeg
   :align: center

For more info, see :py:func:`~moviepy.video.compositing.CompositeVideoClip.clip_array`.

More Complex Video Compositing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :py:class:`~moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip` class is the base of all video compositing.
For example, internally, both :py:func:`~moviepy.video.compositing.CompositeVideoClip.concatenate_videoclips` and :py:func:`~moviepy.video.compositing.CompositeVideoClip.clip_array` create a :py:class:`~moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip`.

It provides a very flexible way to compose clips by layering multiple clips on top of each other, in the order they have been passed to :py:class:`~moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip`. Here's an example:

.. literalinclude:: /_static/code/user_guide/compositing/CompositeVideoClip.py
    :language: python

Now ``final_clip`` plays all clips at the same time, with ``clip3`` over ``clip2`` over ``clip1``. It means that, if all clips have the same size, then only ``clip3``, which is on top, will be visible in the video...

Unless ``clip3`` and/or ``clip2`` have masks which hide parts of them.

.. note::
    Note that by default the composition has the size of its first clip (as it is generally a *background*). But sometimes you will want to make your clips *float* in a bigger composition.
    To do so, just pass the size of the final composition as ``size`` parameter of :py:class:`~moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip`.

For now we have stacked multiple clips on top of each other, but this is obviously not enough for doing real video compositing.
For that, we will need to change when some clips start and stop playing, as well as define the x:y position of these clips in the final video.

For more info, see :py:class:`~moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip`.

Changing Starting and Stopping Times of Clips
""""""""""""""""""""""""""""""""""""""""""""""""

In a CompositionClip, each clip starts to play at a time that is specified by its ``clip.start`` attribute, and will play until ``clip.end``.

So, considering that you would want to play ``clip1`` for the first 6 seconds, ``clip2`` 5 seconds after the start of the video, and finally ``clip3`` at the end of ``clip2``, you would do as follows:

.. literalinclude:: /_static/code/user_guide/compositing/with_start.py
    :language: python

.. note::
    When working with timing of your clips, you will frequently want to keep only parts of the original clip.
    To do so, you should take a look at :py:meth:`~moviepy.Clip.Clip.subclipped` and :py:meth:`~moviepy.Clip.Clip.with_section_cut_out`.

Positioning Clips
""""""""""""""""""

Frequently, you will want a smaller clip to appear on top of a larger one and decide where it will appear in the composition by setting their position.

You can do so by using the :py:meth:`~moviepy.video.VideoClip.VideoClip.with_position` method. The position is always defined from the top left corner, but you can define it in many ways:

.. literalinclude:: /_static/code/user_guide/compositing/with_position.py
    :language: python

When indicating the position, keep in mind that the ``y`` coordinate has its zero at the top of the picture:

.. figure:: /_static/medias/user_guide/videoWH.jpeg

Adding Transition Effects
""""""""""""""""""""""""""

The last part of composition is adding transition effects. For example, when a clip starts while another is still playing, it would be nice to make the new one fade-in instead of showing abruptly.

To do so, we can use the transitions offered by MoviePy in :py:mod:`~moviepy.video.compositing.transitions`, like :py:func:`~moviepy.video.compositing.transitions.crossfadein`:

.. literalinclude:: /_static/code/user_guide/compositing/crossfadein.py
    :language: python

MoviePy offers only a few transitions in :py:mod:`~moviepy.video.compositing.transitions`. But technically, transitions are mostly effects applied to the mask of a clip!
That means you can actually use any of the already existing effects and use them as transitions by applying them on the mask of your clip (see :py:mod:`moviepy.video.fx`).

For more info, see :py:mod:`~moviepy.video.compositing.transitions` and :py:mod:`~moviepy.video.fx`.

Compositing Audio Clips
-----------------------

When you mix video clips together, MoviePy will automatically compose their respective audio tracks to form the audio track of the final clip, so you don't need to worry about compositing these tracks yourself.

If you want to make a custom audio track from several audio sources, audio clips can be mixed together like video clips, with :py:class:`~moviepy.audio.AudioClip.CompositeAudioClip` and :py:func:`~moviepy.audio.AudioClip.concatenate_audioclips`:

.. literalinclude:: /_static/code/user_guide/compositing/CompositeAudioClip.py
    :language: python
````

## File: docs/user_guide/create_effects.rst
````
.. _create_effects:

Creating Your Own Effects
========================================================

In addition to the existing effects already offered by MoviePy, we can create our own effects to modify a clip however we want.

Why Create Your Own Effects?
------------------------------------

For simple enough tasks, we've seen that we can :ref:`modify <filters>`. Though it might be enough for simple tasks, filters are kind of limited:

- They can only access the frame and/or timepoint.
- We cannot pass arguments to them.
- They are hard to maintain and reuse.

To allow for more complex and reusable clip modifications, we can create our own custom effects, which we will later apply with :py:func:`~moviepy.Clip.Clip.with_effects`.

For example, imagine we want to add a progress bar to a clip. To do so, we will not only need the time and image of the current frame but also the total duration of the clip. We will also probably want to be able to pass parameters to define the appearance of the progress bar, such as color or height. This is a perfect task for an effect!

Creating an Effect
--------------------

In MoviePy, effects are objects of type :py:class:`moviepy.Effect.Effect`, which is the base abstract class for all effects (similar to how :py:class:`~moviepy.Clip.Clip` is the base for all :py:class:`~moviepy.video.VideoClip.VideoClip` and :py:class:`~moviepy.audio.AudioClip.AudioClip`).

So, to create an effect, we will need to inherit the :py:class:`~moviepy.Effect.Effect` class and do two things:

- Create an ``__init__`` method to be able to receive the parameters of our effect.
- Implement the inherited :py:meth:`~moviepy.Effect.Effect.apply` method, which must take as an argument the clip we want to modify and return the modified version.

In the end, your effect will probably use :py:func:`~moviepy.Clip.Clip.time_transform`, :py:func:`~moviepy.Clip.Clip.image_transform`, or :py:func:`~moviepy.Clip.Clip.transform` to really apply your modifications to the clip. The main difference is that because your filter will be a method or an anonymous function inside your effect class, you will be able to access all properties of your object from it!

So, let's see how we could create our progress bar effect:

.. literalinclude:: /_static/code/user_guide/effects/custom_effect.py
    :language: python

.. note::
    When creating an effect, you frequently have to write boilerplate code for assigning properties on object initialization. ``dataclasses`` is a nice way to limit that.

If you want to create your own effects, in addition to this documentation, we strongly encourage you to go and take a look at the existing ones (see :py:mod:`moviepy.video.fx` and :py:mod:`moviepy.audio.fx`) to see how they work and take inspiration.
````

## File: docs/user_guide/index.rst
````
.. _user_guide:

The MoviePy User Guide
------------------------------

The User Guide covers all of MoviePy's main concepts grouped by tasks (loading, editing, composing, rendering), with a presentation of the different concepts/elements relative to the tasks along with short code examples.

It is a good place for users wishing to understand more precisely one of these aspects and to discover the different MoviePy elements relative to it.

For users wanting to have a quick overview of how to use MoviePy, a better place to start is the :ref:`getting_started` section, and more specifically the :ref:`moviepy_10_minutes` tutorial.

For a full overview of MoviePy, see the :ref:`reference_manual`.

.. toctree::
   :maxdepth: 1
   
   loading
   modifying
   create_effects
   compositing
   rendering
````

## File: docs/user_guide/loading.rst
````
.. _loading:

Loading Resources as Clips
===================================

The first step for making a video with MoviePy is to load the resources you wish to include in the final video.

In this section, we present the different types of clips and how to load them.
For information on modifying a clip, see :ref:`modifying`. For how to put clips together, see :ref:`compositing`. And for how to see/save them, see :ref:`rendering` (we will usually save them in examples, but we won't explain here).

There are many different resources you can use with MoviePy, and you will load different resources with different subtypes of :py:class:`~moviepy.Clip.Clip`, and more precisely of :py:class:`~moviepy.audio.AudioClip.AudioClip` for any audio element, or :py:class:`~moviepy.video.VideoClip.VideoClip` for any visual element.

The following code summarizes the base clips that you can create with MoviePy:

.. literalinclude:: /_static/code/user_guide/loading/loading.py
    :language: python

To understand all these clips more thoroughly, read the full documentation for each in the :ref:`reference_manual`.

Releasing Resources by Closing a Clip
-------------------------------------

When you create certain types of clip instances—e.g., ``VideoFileClip`` or ``AudioFileClip``—MoviePy creates a subprocess and locks the file. To release these resources when you are finished, you should call the ``close()`` method.

This is more important for more complex applications and is particularly important when running on Windows. While Python's garbage collector should eventually clean up the resources for you, closing them makes them available earlier.

However, if you close a clip too early, methods on the clip (and any clips derived from it) become unsafe.

So, the rules of thumb are:

* Call ``close()`` on any clip that you **construct** once you have finished using it and have also finished using any clip that was derived from it.
* Even if you close a :py:class:`~moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip` instance, you still need to close the clips it was created from.
* Otherwise, if you have a clip that was created by deriving it from another clip (e.g., by calling ``with_mask()``), then generally you shouldn't close it. Closing the original clip will also close the copy.

Clips act as `context managers <https://docs.python.org/3/reference/datamodel.html#context-managers>`_. This means you can use them with a ``with`` statement, and they will automatically be closed at the end of the block, even if there is an exception.

.. literalinclude:: /_static/code/user_guide/loading/closing.py
    :language: python

Categories of Video Clips
--------------------------

Video clips are the building blocks of longer videos. Technically, they are clips with a ``clip.get_frame(t)`` method which outputs a ``HxWx3`` numpy array representing the frame of the clip at time ``t``.

There are two main types of video clips:

* Animated clips (made with :py:class:`~moviepy.video.VideoClip.VideoFileClip`, :py:class:`~moviepy.video.VideoClip.VideoClip`, and :py:class:`~moviepy.video.io.ImageSequenceClip.ImageSequenceClip`), which will always have duration.
* Unanimated clips (made with :py:class:`~moviepy.video.VideoClip.ImageClip`, :py:class:`~moviepy.video.VideoClip.TextClip`, and :py:class:`~moviepy.video.VideoClip.ColorClip`), which show the same picture for an a-priori infinite duration.

There are also special video clips called masks, which belong to the categories above but output greyscale frames indicating which parts of another clip are visible or not.

A video clip can carry around an audio clip (:py:class:`~moviepy.audio.AudioClip.AudioClip`) in :py:attr:`~moviepy.video.VideoClip.VideoClip.audio` which is its *soundtrack*, and a mask clip in :py:attr:`~moviepy.video.VideoClip.VideoClip.mask`.

Animated Clips
~~~~~~~~~~~~~~~

These are clips whose image will change over time, and which have a duration and a number of Frames Per Second.

VideoClip
"""""""""

:py:class:`~moviepy.video.VideoClip.VideoClip` is the base class for all other video clips in MoviePy. If all you want is to edit video files, you will never need it. This class is practical when you want to make animations from frames that are generated by another library. 

All you need is to define a function ``frame_function(t)`` which returns a `HxWx3` numpy array (of 8-bits integers) representing the frame at time ``t``.

Here is an example where we will create a pulsating red circle with the graphical library `Pillow <https://pypi.org/project/Pillow/>`_.

.. literalinclude:: /_static/code/user_guide/loading/VideoClip.py
    :language: python

Resulting in this:

.. image:: /_static/medias/user_guide/circle.gif
   :width: 128 px
   :align: center
   :alt: A pulsating red circle on black background.

.. note::
    Clips that are made with a ``frame_function`` do not have an explicit frame rate nor duration by default, so you must provide duration at clip creation and a frame rate (``fps``, frames per second) for :py:meth:`~moviepy.video.VideoClip.VideoClip.write_gif` and :py:meth:`~moviepy.video.VideoClip.VideoClip.write_videofile`, and more generally for any methods that require iterating through the frames.

For more, see :py:class:`~moviepy.video.VideoClip.VideoClip`.

VideoFileClip
"""""""""""""""

A :py:class:`~moviepy.video.io.VideoFileClip.VideoFileClip` is a clip read from a video file (most formats are supported) or a GIF file. This is probably one of the most used objects! You load the video as follows:

.. literalinclude:: /_static/code/user_guide/loading/VideoFileClip.py
    :language: python

.. note::
    These clips will have an ``fps`` (frame per second) and ``duration`` attributes, which will be transmitted if you do small modifications of the clip, and will be used by default in :py:meth:`~moviepy.video.VideoClip.VideoClip.write_gif`, :py:meth:`~moviepy.video.VideoClip.VideoClip.write_videofile`, etc.

For more, see :py:class:`~moviepy.video.io.VideoFileClip.VideoFileClip`.

ImageSequenceClip
""""""""""""""""""

This :py:class:`~moviepy.video.io.ImageSequenceClip.ImageSequenceClip` is a clip made from a series of images:

.. literalinclude:: /_static/code/user_guide/loading/ImageSequenceClip.py
    :language: python

When creating an image sequence, ``sequence`` can be either a list of image names (that will be *played* in the provided order), a folder name (played in alphanumerical order), or a list of frames (Numpy arrays), obtained for instance from other clips.

.. warning::
    All the images in the list/folder/frames must be of the same size, or an exception will be raised.

For more, see :py:class:`~moviepy.video.io.ImageSequenceClip.ImageSequenceClip`.

DataVideoClip
"""""""""""""""

:py:class:`~moviepy.video.io.VideoClip.DataVideoClip` is a video clip that takes a list of datasets, a callback function, and makes each frame by iterating over the dataset and invoking the callback function with the current data as the first argument.

You will probably never use this. But if you do, think of it like a :py:class:`~moviepy.video.VideoClip.VideoClip`, where you make frames not based on time, but based on each entry of a data list.

.. literalinclude:: /_static/code/user_guide/loading/DataVideoClip.py
    :language: python

For more, see :py:class:`~moviepy.video.io.VideoClip.DataVideoClip`.

UpdatedVideoClip
""""""""""""""""""

.. warning::
    This is really advanced usage; you will probably never need it. If you do, please go read the code.

:py:class:`~moviepy.video.io.VideoClip.UpdatedVideoClip` is a video whose frame_function requires some objects to be updated before we can compute it.

This is particularly practical in science where some algorithms need to make some steps before a new frame can be generated, or maybe when trying to make a video based on a live exterior context.

When you use this, you pass a world object to it. A world object is an object that respects these 3 rules:

#. It has a ``clip_t`` property, indicating the current world time.
#. It has an ``update()`` method, that will update the world state and is responsible for increasing ``clip_t`` when a new frame can be drawn.
#. It has a ``to_frame()`` method, that will render a frame based on the world's current state.

On :py:meth:`~moviepy.video.io.VideoClip.UpdatedVideoClip.get_frame` call, your :py:class:`~moviepy.video.io.VideoClip.UpdatedVideoClip` will try to update the world until ``world.clip_t`` is superior or equal to frame time, then it will call ``world.to_frame()``.

.. literalinclude:: /_static/code/user_guide/loading/UpdatedVideoClip.py
    :language: python

Unanimated Clips
~~~~~~~~~~~~~~~~

These are clips whose image will, at least before modifications, stay the same. By default, they have no duration nor FPS, meaning you will need to define them before doing operations needing such information (for example, rendering).

ImageClip
"""""""""

:py:class:`~moviepy.video.VideoClip.ImageClip` is the base class for all unanimated clips; it's a video clip that always displays the same image. Along with :py:class:`~moviepy.video.io.VideoFileClip.VideoFileClip`, it's one of the most used kinds of clips.

You can create one as follows:

.. literalinclude:: /_static/code/user_guide/loading/ImageClip.py
    :language: python

For more, see :py:class:`~moviepy.video.VideoClip.ImageClip`.

TextClip
"""""""""

A :py:class:`~moviepy.video.VideoClip.TextClip` is a clip that will turn a text string into an image clip.

:py:class:`~moviepy.video.VideoClip.TextClip` accepts many parameters, letting you configure the appearance of the text, such as font and font size, color, interlining, text alignment, etc.

The font you want to use must be an `OpenType font <https://fr.wikipedia.org/wiki/OpenType>`_, and you will set it by passing the path to the font file.

Here are a few examples of using :py:class:`~moviepy.video.VideoClip.TextClip`:

.. literalinclude:: /_static/code/user_guide/loading/TextClip.py
    :language: python

.. note::
    The parameter ``method`` lets you define if text should be written and overflow if too long (``label``) or be automatically broken over multiple lines (``caption``).

For a more detailed explanation of all the parameters, see :py:class:`~moviepy.video.VideoClip.TextClip`.

ColorClip
"""""""""

A :py:class:`~moviepy.video.VideoClip.ColorClip` is a clip that will return an image of only one color. It is sometimes useful when doing compositing (see :ref:`compositing`).

.. literalinclude:: /_static/code/user_guide/loading/ColorClip.py
    :language: python

For more, see :py:class:`~moviepy.video.VideoClip.ColorClip`.

.. _loading#masks:

Mask Clips
~~~~~~~~~~~~~~

Masks are a special kind of :py:class:`~moviepy.video.VideoClip.VideoClip` with the property ``is_mask`` set to ``True``. They can be attached to any other kind of :py:class:`~moviepy.video.VideoClip.VideoClip` through method :py:meth:`~moviepy.video.VideoClip.VideoClip.with_mask`.

When a clip has a mask attached to it, this mask will indicate which pixels will be visible when the clip is composed with other clips (see :ref:`compositing`). Masks are also used to define transparency when you export the clip as GIF file or as a PNG.

The fundamental difference between masks and standard clips is that standard clips output frames with 3 components (R-G-B) per pixel, comprised between 0 and 255, while a mask has just one component per pixel, between 0 and 1 (1 indicating a fully visible pixel and 0 a transparent pixel). Seen otherwise, a mask is always in greyscale.

When you create or load a clip that you will use as a mask, you need to declare it. You can then attach it to a clip with the same dimensions:

.. literalinclude:: /_static/code/user_guide/loading/masks.py
    :language: python

.. note::
    In the case of video and image files, if these are not already black and white, they will be converted automatically.

    Also, when you load an image with an *alpha layer*, like a PNG, MoviePy will use this layer as a mask unless you pass ``transparent=False``.

Any video clip can be turned into a mask with :py:meth:`~moviepy.video.VideoClip.VideoClip.to_mask`, and a mask can be turned to a standard RGB video clip with :py:meth:`~moviepy.video.VideoClip.VideoClip.to_RGB()`.

Masks are treated differently by many methods (because their frames are different) but at the core, they are :py:class:`~moviepy.video.VideoClip.VideoClip`, so you can do with them everything you can do with a video clip: modify, cut, apply effects, save, etc.

Using Audio Elements with Audio Clips
-------------------------------------

In addition to :py:class:`~moviepy.video.VideoClip.VideoClip` for visuals, you can use audio elements, like an audio file, using the :py:class:`~moviepy.audio.AudioClip.AudioClip` class.

Both are quite similar, except :py:class:`~moviepy.audio.AudioClip.AudioClip` method :py:meth:`~moviepy.audio.AudioClip.AudioClip.get_frame` returns a numpy array of size ``Nx1`` for mono, and size ``Nx2`` for stereo.

AudioClip
~~~~~~~~~~

:py:class:`~moviepy.audio.AudioClip.AudioClip` is the base class for all audio clips. If all you want is to edit audio files, you will never need it.

All you need is to define a function ``frame_function(t)`` which returns a ``Nx1`` or ``Nx2`` numpy array representing the sound at time ``t``.

.. literalinclude:: /_static/code/user_guide/loading/AudioClip.py
    :language: python

For more, see :py:class:`~moviepy.audio.AudioClip.AudioClip`.

AudioFileClip
"""""""""""""""""

:py:class:`~moviepy.audio.io.AudioFileClip.AudioFileClip` is used to load an audio file. This is probably the only kind of audio clip you will use.

You simply pass it the file you want to load:

.. literalinclude:: /_static/code/user_guide/loading/AudioFileClip.py
    :language: python

For more, see :py:class:`~moviepy.audio.io.AudioFileClip.AudioFileClip`.

AudioArrayClip
"""""""""""""""""

:py:class:`~moviepy.audio.AudioClip.AudioArrayClip` is used to turn an array representing a sound into an audio clip. You will probably never use it unless you need to use the result of some third-party library without using a temporary file.

You need to provide a numpy array representing the sound (of size ``Nx1`` for mono, ``Nx2`` for stereo), and the number of fps, indicating the speed at which the sound is supposed to be played.

.. literalinclude:: /_static/code/user_guide/loading/AudioArrayClip.py
    :language: python

For more, see :py:class:`~moviepy.audio.AudioClip.AudioArrayClip`.
````

## File: docs/user_guide/modifying.rst
````
.. _modifying:

Modifying clips and apply effects
===================================

Of course, once you will have loaded a :py:class:`~moviepy.Clip.Clip` the next step of action will be to modify it to be able to integrate it in your final video.

To modify a clip, there is three main courses of actions :
 * The built-in methods of :py:class:`~moviepy.video.VideoClip.VideoClip` or :py:class:`~moviepy.audio.AudioClip.AudioClip` modifying the properties of the object.
 * The already-implemented effects of MoviePy you can apply on clips, usually affecting the clip by applying filters on each frame of the clip at rendering time.
 * The transformation filters that you can apply using :py:func:`~moviepy.Clip.Clip.transform` and :py:func:`~moviepy.Clip.Clip.time_transform`.


How modifications are applied to a clip ?
-------------------------------------------------------

Clip copy during modification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first thing you must know is that when modifying a clip, MoviePy **will never modify that clip directly**. 
Instead it will return **a modified copy of the original** and let the original untouched. This is known as out-place instead of in-place behavior.

To illustrate:

.. literalinclude:: /_static/code/user_guide/effects/modify_copy_example.py
    :language: python

This is an important point to understand, because it is one of the most recurrent source of bug for newcomers.


Memory consumption of effect and modifications 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When applying an effect or modification, it does not immediately apply the effect to all the frames of the clip, but only to the first frame: all the other frames will only be modified when required (that is, when you will write the whole clip to a file or when you will preview it). 

It means that creating a new clip is neither time nor memory hungry, all the computation happen during the final rendering.


Time representations in MoviePy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Many methods that we will see accept duration or timepoint as arguments. For instance :py:meth:`clip.subclipped(t_start, t_end) <moviepy.Clip.Clip.subclipped(t_start, t_end)>` which cuts the clip between two timepoints.

MoviePy usually accept duration and timepoint as either: 

* a number of seconds as a ``float``.
* a ``tuple`` with ``(minutes, seconds)`` or ``(hours, minutes, seconds)``.
* a ``string`` such as ``'00:03:50.54'``.

Also, you can usually provide negative times, indicating a time from the end of the clip. For example, ``clip.subclipped(-20, -10)`` cuts the clip between 20s before the end and 10s before the end.


Modify a clip using the ``with_*`` methods
-------------------------------------------------------

The first way to modify a clip is by modifying internal properties of your object, thus modifying his behavior.

These methods usually start with the prefix ``with_`` or ``without_``, indicating that they will return a copy of the clip with the properties modified.

So, you may write something like:

.. literalinclude:: /_static/code/user_guide/effects/using_with_methods.py
    :language: python

In addition to the ``with_*`` methods, a handful of very common methods are also accessible under shorter names:

- :py:meth:`~moviepy.video.VideoClip.VideoClip.resized`
- :py:meth:`~moviepy.video.VideoClip.VideoClip.crop`
- :py:meth:`~moviepy.video.VideoClip.VideoClip.rotate`

For a list of all those methods, see :py:class:`~moviepy.Clip.Clip` and :py:class:`~moviepy.video.VideoClip.VideoClip`.


.. _modifying#effects:

Modify a clip using effects 
---------------------------------

The second way to modify a clip is by using effects that will modify the frames of the clip (which internally are no more than `numpy arrays <https://numpy.org>`_)  by applying some sort of functions on them.

MoviePy come with many effects implemented in :py:mod:`moviepy.video.fx` for visual effects and :py:mod:`moviepy.audio.fx` for audio effects. 
For practicality, these two modules are loaded in MoviePy as ``vfx`` and ``afx``, letting you import them as ``from moviepy import vfx, afx``.

To use these effects, you simply need to instantiate them as object and apply them on your :py:class:`~moviepy.Clip.Clip` using method :py:meth:`~moviepy.Clip.Clip.with_effects`, with a list of :py:class:`~moviepy.Effect.Effect` objects you want to apply. 

For convenience the effects are also dynamically added as method of :py:class:`~moviepy.video.VideoClip.VideoClip` and :py:class:`~moviepy.video.AudioClip.AudioClip`  classes at runtime, letting you call them as simple method of your clip.

So, you may write something like:

.. literalinclude:: /_static/code/user_guide/effects/using_effects.py
    :language: python

.. note::
    MoviePy effects are automatically applied to both the sound and the mask of the clip if it is relevant, so that you don't have to worry about modifying these.

For a list of those effects, see :py:mod:`moviepy.video.fx` and :py:mod:`moviepy.audio.fx`.

In addition to the effects already provided by MoviePy, you can obviously :ref:`create_effects` and use them the same way.

.. _modifying#filters:

Modify a clip appearance and timing using filters
----------------------------------------------------------

In addition to modifying a clip's properties and using effects, you can also modify the appearance or timing of a clip by using your own custom *filters* with :py:func:`~moviepy.Clip.Clip.time_transform`, :py:func:`~moviepy.Clip.Clip.image_transform`, and more generally with :py:func:`~moviepy.Clip.Clip.transform`.

All these methods work by taking as first parameter a callback function that will receive either a clip frame, a timepoint, or both, and return a modified version of these.

Modify only the timing of a Clip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can change the timeline of the clip with :py:meth:`time_transform(your_filter) <moviepy.Clip.Clip.time_transform>`.
Where ``your_filter`` is a callback function taking clip time as a parameter and returning a new time:

.. literalinclude:: /_static/code/user_guide/effects/time_transform.py
    :language: python

Now the clip ``modified_clip1`` plays three times faster than ``my_clip``, while ``modified_clip2`` will be oscillating between 00:00:00 to 00:00:02 of ``my_clip``. Note that in the last case you have created a clip of infinite duration (which is not a problem for the moment).

.. note::
    By default :py:func:`~moviepy.Clip.Clip.time_transform` will only modify the clip main frame, without modifying clip audio or mask for :py:class:`~moviepy.video.VideoClip.VideoClip`. 
    
    If you wish to also modify audio and/or mask you can provide the parameter ``apply_to`` with either ``'audio'``, ``'mask'``, or ``['audio', 'mask']``. 


Modifying only the appearance of a Clip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For :py:class:`~moviepy.video.VideoClip.VideoClip`, you can change the appearance of the clip with :py:meth:`image_transform(your_filter) <moviepy.video.VideoClip.VideoClip.image_transform>`.
Where ``your_filter`` is a callback function, taking clip frame (a numpy array) as a parameter and returning the transformed frame:

.. literalinclude:: /_static/code/user_guide/effects/image_transform.py
    :language: python

Now the clip ``modified_clip1`` will have his green and blue canals inverted.

.. note::
    You can define if transformation should be applied to audio and mask same as for :py:func:`~moviepy.Clip.Clip.time_transform`.

.. note::
    Sometimes need to treat clip frames and mask frames in a different way. To distinguish between the two, you can always look at their shape, clips are ``H*W*3``, and masks ``H*W``.


Modifying both the appearance and the timing of a Clip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally, you may want to process the clip by taking into account both the time and the frame picture, for example to apply visual effects variating with time. 
This is possible with the method :py:meth:`transform(your_filter) <moviepy.Clip.Clip.transform>`.
Where ``your_filter`` is a callback function taking two parameters, and returning a new frame picture. Where first argument is a ``get_frame`` method (i.e. a function ``get_frame(time)`` which given a time returns the clip’s frame at that time), and the second argument is the time.

.. literalinclude:: /_static/code/user_guide/effects/transform.py
    :language: python

This will scroll down the clip, with a constant height of 360 pixels.

.. note::
    You can define if transformation should be applied to audio and mask same as for :py:func:`~moviepy.Clip.Clip.time_transform`. 

.. note::
    When programming a new effect, whenever it is possible, prefer using ``time_transform`` and ``image_transform`` instead of ``transform`` when implementing new effects.
    The reason is that, though they both internally rely on ``transform`` when these effects are applied to ``ImageClip`` objects, MoviePy will recognize they only need to be applied once instead of on each frame, resulting in faster renderings.

To keep things simple, we have only addressed the case of :py:class:`~moviepy.video.VideoClip.VideoClip`, but know that the same principle applies to :py:class:`~moviepy.audio.AudioClip.AudioClip`, except that instead of a picture frame, you will have an audio frame, which is also a numpy array.
````

## File: docs/user_guide/rendering.rst
````
.. _rendering:

Previewing and Saving Video Clips
=================================

Once you are done working with your clips, the final step will be to export the result into a video/image file, or sometimes to simply preview it in order to verify that everything is working as expected.

Previewing a Clip
-----------------

When you are working with a clip, you will frequently need to have a quick look at what your clip looks like, either to verify that everything is working as intended or to check how things look.

To do so, you could render your entire clip into a file, but that's a rather long task, and you only need a quick look, so a better solution exists: previewing.

Preview a Clip as a Video
~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::
    You must have ``ffplay`` installed and accessible to MoviePy to be able to use :py:func:`~moviepy.video.io.preview.preview`.
    If you're not sure, take a look :ref:`install#binaries`

The first thing you can do is to preview your clip as a video by calling the method :py:func:`~moviepy.video.io.preview.preview` on your clip:

.. literalinclude:: /_static/code/user_guide/rendering/preview.py
    :language: python

You will probably frequently want to preview only a small portion of your clip, though ``preview`` does not offer such capabilities, you can easily emulate such behavior by using :py:meth:`~moviepy.Clip.Clip.subclip`.

.. note::
    It is quite frequent for a clip preview to be out of sync or to play slower than it should. This indicates that your computer is not powerful enough to render the clip in real-time.
    
    Don't hesitate to play with the options of preview: for instance, lower the fps of the sound (11000 Hz is still fine) and the video. Also, downsizing your video with :py:meth:`~moviepy.video.VideoClip.VideoClip.resize` can help.

For more information, see :py:func:`~moviepy.video.io.preview.preview`.

.. note::
    A quite similar function is also available for :py:func:`~moviepy.audio.AudioClip.AudioClip`, see :py:func:`~moviepy.audio.io.ffplay_audiopreviewer.ffplay_audiopreview`.

Preview Just One Frame of a Clip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In many situations, you don't really need to preview your entire clip; seeing just one frame is enough to see how it looks and to ensure everything is going as expected.

To do so, you can use the method :py:func:`~moviepy.video.io.preview.show` on your clip, passing the frame time as an argument:

.. literalinclude:: /_static/code/user_guide/rendering/show.py
    :language: python

Contrary to video previewing, :py:func:`~moviepy.video.io.preview.show` does not require ``ffplay`` but uses the ``pillow`` ``Image.show`` function.

For more information, see :py:func:`~moviepy.video.io.preview.show`.

Showing a Clip in Jupyter Notebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you work with a `Jupyter Notebook <https://jupyter.org/>`_, it can be very practical to display your clip within the notebook. To do so, you can use the method :py:func:`~moviepy.video.io.display_in_notebook.display_in_notebook` on your clip.

.. image:: /_static/medias/user_guide/demo_preview.jpeg
    :width: 500px
    :align: center

With :py:func:`~moviepy.video.io.display_in_notebook.display_in_notebook`, you can embed videos, images, and sounds, either from a file or directly from a clip:

.. literalinclude:: /_static/code/user_guide/rendering/display_in_notebook.py
    :language: python

.. warning::
    Note that :py:func:`~moviepy.video.io.display_in_notebook.display_in_notebook` will only work if it is on the last line of the notebook cell. 

    Also, note that :py:func:`~moviepy.video.io.display_in_notebook.display_in_notebook` actually embeds the clips physically in your notebook. The advantage is that you can move the notebook or put it online and the videos will work. 
    However, the drawback is that the file size of the notebook can become very large. Depending on your browser, re-computing and displaying the video multiple times can take up space in the cache and the RAM (this will only be a problem for intensive uses).
    Restarting your browser solves the problem.

For more information, see :py:func:`~moviepy.video.io.display_in_notebook.display_in_notebook`.

Saving Your Clip into a File
----------------------------

Once you are satisfied with how your clip looks, you can save it into a file, a step known in video editing as rendering. MoviePy offers various ways to save your clip.

Video Files (.mp4, .webm, .ogv, ...)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The obvious first choice will be to write your clip to a video file, which you can do with :py:meth:`~moviepy.video.VideoClip.VideoClip.write_videofile`:

.. literalinclude:: /_static/code/user_guide/rendering/write_videofile.py
    :language: python

MoviePy can automatically find the default codec names for the most common file extensions. If you want to use exotic formats or if you are not happy with the defaults, you can provide the codec with ``codec='mpeg4'`` for instance.

There are many options when you are writing a video (bitrate, parameters of the audio writing, file size optimization, number of processors to use, etc.), and we will not go into detail about each. For more information, see :py:meth:`~moviepy.video.VideoClip.VideoClip.write_videofile`.

.. note::
    Although you are encouraged to experiment with the settings of ``write_videofile``, know that lowering the optimization preset or increasing the number of threads will not necessarily improve the rendering time, as the bottleneck may be in MoviePy's computation of each frame and not in ffmpeg encoding.

    Also, know that it is possible to pass additional parameters to the ffmpeg command line invoked by MoviePy by using the ``ffmpeg_params`` argument.

Sometimes it is impossible for MoviePy to guess the ``duration`` attribute of the clip (keep in mind that some clips, like ImageClips displaying a picture, have *a priori* an infinite duration). In such cases, the ``duration`` must be set manually with :py:meth:`~moviepy.Clip.Clip.with_duration`:

.. literalinclude:: /_static/code/user_guide/rendering/write_videofile_duration.py
    :language: python

.. note::
    A quite similar function is also available for :py:func:`~moviepy.audio.AudioClip.AudioClip`, see :py:func:`~moviepy.audio.io.AudioClip.write_audiofile`.

Export a Single Frame of the Clip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As with previewing, sometimes you will need to export only one frame of a clip, for example to create the preview image of a video. You can do so with :py:meth:`~moviepy.video.VideoClip.VideoClip.save_frame`:

.. literalinclude:: /_static/code/user_guide/rendering/save_frame.py
    :language: python

For more information, see :py:func:`~moviepy.video.VideoClip.VideoClip.save_frame`.

Animated GIFs
~~~~~~~~~~~~~

In addition to writing video files, MoviePy also lets you write GIF files with :py:meth:`~moviepy.video.VideoClip.VideoClip.write_gif`:

.. literalinclude:: /_static/code/user_guide/rendering/write_gif.py
    :language: python

For more information, see :py:func:`~moviepy.video.VideoClip.VideoClip.write_gif`.

Export All the Clip as Images in a Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lastly, you might wish to export an entire clip as an image sequence (multiple images in one directory, one image per frame). You can do so with the function :py:meth:`~moviepy.video.VideoClip.VideoClip.write_images_sequence`:

.. literalinclude:: /_static/code/user_guide/rendering/write_images_sequence.py
    :language: python

For more information, see :py:func:`~moviepy.video.VideoClip.VideoClip.write_images_sequence`.
```
````

## File: docs/conf.py
````python
# -*- coding: utf-8 -*-

"""MoviePy documentation build configuration file."""

import os
import sys


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(".."))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx_design",
    "sphinx.ext.coverage",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
]

autosectionlabel_prefix_document = True

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "MoviePy"
copyright = "2025, Zulko - MIT"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "2.2.1"

# The full version, including alpha/beta/rc tags.
# release = '0.2.3.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ---------------------------------------------------

sys.path.append(os.path.abspath("_themes"))
# html_theme_path = ['_themes']
html_theme = "pydata_sphinx_theme"  # formerly 'kr'
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
v2_page = "https://zulko.github.io/moviepy/getting_started/updating_to_v2.html"
html_theme_options = {
    "use_edit_page_button": True,
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/Zulko/moviepy/",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if
            # "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        }
    ],
    "announcement": f"""<p>MoviePy v2.0 have introduced breaking changes, see
<a href="{v2_page}">Updating from v1.X to v2.X</a> for more info.</p>""",
}

html_context = {
    "github_user": "Zulko",
    "github_repo": "moviepy",
    "github_version": "master",
    "doc_path": "docs",
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/medias/logo_small.jpeg"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    "moviepy.css",
]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "MoviePydoc"


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ("index", "MoviePy.tex", "MoviePy Documentation", "Zulko", "manual"),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", "moviepy", "MoviePy Documentation", ["Zulko"], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "MoviePy",
        "MoviePy Documentation",
        "Zulko",
        "MoviePy",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = "MoviePy"
epub_author = "Zulko"
epub_publisher = "Zulko"
epub_copyright = "2017, Zulko"

# The language of the text. It defaults to the language option
# or en if the language is not set.
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
# epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
# epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
# epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
# epub_tocdepth = 3

# Allow duplicate toc entries.
# epub_tocdup = True

# Fix unsupported image types using the PIL.
# epub_fix_images = False

# Scale large images.
# epub_max_image_width = 0

# If 'no', URL addresses will not be shown.
# epub_show_urls = 'inline'

# If false, no index is generated.
# epub_use_index = True

# autodoc_member_order = 'bysource'
````

## File: docs/index.rst
````
:notoc:

***********************
MoviePy documentation
***********************

.. image:: /_static/medias/logo.png
    :width: 50%
    :align: center

**Date**: |today| **Version**: |version|

**Useful links**:
`Binary Installers <https://pypi.org/project/moviepy/>`__ |
`Source Repository <https://github.com/Zulko/moviepy>`__ |
`Issues & Ideas <https://github.com/Zulko/moviepy>`__ |
`Q&A Support <https://www.reddit.com/r/moviepy/>`__ |

MoviePy is the `Python <https://www.python.org/>`__ reference tool for video editing automation! 

It's an open source, MIT-licensed library offering user-friendly video editing 
and manipulation tools for the `Python <https://www.python.org/>`__ programming language.

.. grid:: 1 2 2 2
    :gutter: 4
    :padding: 2 2 0 0
    :class-container: sd-text-center

    .. grid-item-card:: Getting started
        :img-top: _static/medias/index_getting_started.svg
        :class-card: intro-card
        :shadow: md

        New to *MoviePy*? Check out the getting started guides. They contain instructions
        to install *MoviePy* as well as introduction concepts and tutorials.

        +++

        .. button-ref:: getting_started
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            To the starting guide

    .. grid-item-card::  User guide
        :img-top: _static/medias/index_user_guide.svg
        :class-card: intro-card
        :shadow: md

        The user guide provides in-depth information on the
        key concepts of *MoviePy* with useful background information and explanation.

        +++

        .. button-ref:: user_guide
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            To the user guide

    .. grid-item-card::  API reference
        :img-top: _static/medias/index_api.svg
        :class-card: intro-card
        :shadow: md

        The reference guide contains a detailed description of
        the *MoviePy* API. The reference describes how the methods work and which parameters can
        be used. It assumes that you have an understanding of the key concepts.

        +++

        .. button-ref:: reference_manual
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            To the reference guide

    .. grid-item-card::  Developer guide
        :img-top: _static/medias/index_contribute.svg
        :class-card: intro-card
        :shadow: md

        Saw a typo in the documentation? Want to improve
        existing functionalities? The contributing guidelines will guide
        you through the process of improving *MoviePy*.

        +++

        .. button-ref:: developer_guide
            :ref-type: ref
            :click-parent:
            :color: secondary
            :expand:

            To the development guide




Contribute!
--------------

MoviePy is an open source software originally written by Zulko_ and released under the MIT licence. It works on Windows, Mac, and Linux. 

.. raw:: html

    <a href="https://twitter.com/share" class="twitter-share-button"
    data-text="MoviePy - Video editing with Python" data-size="large" data-hashtags="MoviePy">Tweet
    </a>
    <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';
    if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';
    fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');
    </script>

    <iframe type="text/html" src="https://ghbtns.com/github-btn.html?user=Zulko&repo=moviepy&type=watch&count=true&size=large"
    allowtransparency="true" frameborder="0" scrolling="0" width="152px" height="30px"></iframe>


.. toctree::
    :maxdepth: 3
    :hidden:
    :titlesonly:


    getting_started/index
    user_guide/index
    reference/index
    developer_guide/index


.. _PyPI: https://pypi.python.org/pypi/moviepy
.. _Zulko: https://github.com/Zulko/
.. _Stackoverflow: https://stackoverflow.com/
.. _Github: https://github.com/Zulko/moviepy
.. _Reddit: https://www.reddit.com/r/moviepy/
````

## File: docs/make.bat
````
@ECHO OFF

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set BUILDDIR=build
set ALLSPHINXOPTS=-d %BUILDDIR%/doctrees %SPHINXOPTS% .
set I18NSPHINXOPTS=%SPHINXOPTS% .
if NOT "%PAPER%" == "" (
	set ALLSPHINXOPTS=-D latex_paper_size=%PAPER% %ALLSPHINXOPTS%
	set I18NSPHINXOPTS=-D latex_paper_size=%PAPER% %I18NSPHINXOPTS%
)

if "%1" == "" goto help

if "%1" == "help" (
	:help
	echo.Please use `make ^<target^>` where ^<target^> is one of
	echo.  html       to make standalone HTML files
	echo.  dirhtml    to make HTML files named index.html in directories
	echo.  singlehtml to make a single large HTML file
	echo.  pickle     to make pickle files
	echo.  json       to make JSON files
	echo.  htmlhelp   to make HTML files and a HTML help project
	echo.  qthelp     to make HTML files and a qthelp project
	echo.  devhelp    to make HTML files and a Devhelp project
	echo.  epub       to make an epub
	echo.  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter
	echo.  text       to make text files
	echo.  man        to make manual pages
	echo.  texinfo    to make Texinfo files
	echo.  gettext    to make PO message catalogs
	echo.  changes    to make an overview over all changed/added/deprecated items
	echo.  xml        to make Docutils-native XML files
	echo.  pseudoxml  to make pseudoxml-XML files for display purposes
	echo.  linkcheck  to check all external links for integrity
	echo.  doctest    to run all doctests embedded in the documentation if enabled
	goto end
)

if "%1" == "clean" (
	for /d %%i in (%BUILDDIR%\*) do rmdir /q /s %%i
	del /q /s %BUILDDIR%\*
	goto end
)


%SPHINXBUILD% 2> nul
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.http://sphinx-doc.org/
	exit /b 1
)

if "%1" == "html" (
	%SPHINXBUILD% -b html %ALLSPHINXOPTS% %BUILDDIR%/html
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%/html.
	goto end
)

if "%1" == "dirhtml" (
	%SPHINXBUILD% -b dirhtml %ALLSPHINXOPTS% %BUILDDIR%/dirhtml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%/dirhtml.
	goto end
)

if "%1" == "singlehtml" (
	%SPHINXBUILD% -b singlehtml %ALLSPHINXOPTS% %BUILDDIR%/singlehtml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%/singlehtml.
	goto end
)

if "%1" == "pickle" (
	%SPHINXBUILD% -b pickle %ALLSPHINXOPTS% %BUILDDIR%/pickle
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can process the pickle files.
	goto end
)

if "%1" == "json" (
	%SPHINXBUILD% -b json %ALLSPHINXOPTS% %BUILDDIR%/json
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can process the JSON files.
	goto end
)

if "%1" == "htmlhelp" (
	%SPHINXBUILD% -b htmlhelp %ALLSPHINXOPTS% %BUILDDIR%/htmlhelp
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can run HTML Help Workshop with the ^
.hhp project file in %BUILDDIR%/htmlhelp.
	goto end
)

if "%1" == "qthelp" (
	%SPHINXBUILD% -b qthelp %ALLSPHINXOPTS% %BUILDDIR%/qthelp
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can run "qcollectiongenerator" with the ^
.qhcp project file in %BUILDDIR%/qthelp, like this:
	echo.^> qcollectiongenerator %BUILDDIR%\qthelp\MoviePy.qhcp
	echo.To view the help file:
	echo.^> assistant -collectionFile %BUILDDIR%\qthelp\MoviePy.ghc
	goto end
)

if "%1" == "devhelp" (
	%SPHINXBUILD% -b devhelp %ALLSPHINXOPTS% %BUILDDIR%/devhelp
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished.
	goto end
)

if "%1" == "epub" (
	%SPHINXBUILD% -b epub %ALLSPHINXOPTS% %BUILDDIR%/epub
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The epub file is in %BUILDDIR%/epub.
	goto end
)

if "%1" == "latex" (
	%SPHINXBUILD% -b latex %ALLSPHINXOPTS% %BUILDDIR%/latex
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; the LaTeX files are in %BUILDDIR%/latex.
	goto end
)

if "%1" == "latexpdf" (
	%SPHINXBUILD% -b latex %ALLSPHINXOPTS% %BUILDDIR%/latex
	cd %BUILDDIR%/latex
	make all-pdf
	cd %BUILDDIR%/..
	echo.
	echo.Build finished; the PDF files are in %BUILDDIR%/latex.
	goto end
)

if "%1" == "latexpdfja" (
	%SPHINXBUILD% -b latex %ALLSPHINXOPTS% %BUILDDIR%/latex
	cd %BUILDDIR%/latex
	make all-pdf-ja
	cd %BUILDDIR%/..
	echo.
	echo.Build finished; the PDF files are in %BUILDDIR%/latex.
	goto end
)

if "%1" == "text" (
	%SPHINXBUILD% -b text %ALLSPHINXOPTS% %BUILDDIR%/text
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The text files are in %BUILDDIR%/text.
	goto end
)

if "%1" == "man" (
	%SPHINXBUILD% -b man %ALLSPHINXOPTS% %BUILDDIR%/man
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The manual pages are in %BUILDDIR%/man.
	goto end
)

if "%1" == "texinfo" (
	%SPHINXBUILD% -b texinfo %ALLSPHINXOPTS% %BUILDDIR%/texinfo
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The Texinfo files are in %BUILDDIR%/texinfo.
	goto end
)

if "%1" == "gettext" (
	%SPHINXBUILD% -b gettext %I18NSPHINXOPTS% %BUILDDIR%/locale
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The message catalogs are in %BUILDDIR%/locale.
	goto end
)

if "%1" == "changes" (
	%SPHINXBUILD% -b changes %ALLSPHINXOPTS% %BUILDDIR%/changes
	if errorlevel 1 exit /b 1
	echo.
	echo.The overview file is in %BUILDDIR%/changes.
	goto end
)

if "%1" == "linkcheck" (
	%SPHINXBUILD% -b linkcheck %ALLSPHINXOPTS% %BUILDDIR%/linkcheck
	if errorlevel 1 exit /b 1
	echo.
	echo.Link check complete; look for any errors in the above output ^
or in %BUILDDIR%/linkcheck/output.txt.
	goto end
)

if "%1" == "doctest" (
	%SPHINXBUILD% -b doctest %ALLSPHINXOPTS% %BUILDDIR%/doctest
	if errorlevel 1 exit /b 1
	echo.
	echo.Testing of doctests in the sources finished, look at the ^
results in %BUILDDIR%/doctest/output.txt.
	goto end
)

if "%1" == "xml" (
	%SPHINXBUILD% -b xml %ALLSPHINXOPTS% %BUILDDIR%/xml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The XML files are in %BUILDDIR%/xml.
	goto end
)

if "%1" == "pseudoxml" (
	%SPHINXBUILD% -b pseudoxml %ALLSPHINXOPTS% %BUILDDIR%/pseudoxml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The pseudo-XML files are in %BUILDDIR%/pseudoxml.
	goto end
)

:end
````

## File: docs/Makefile
````
# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = build
PDFBUILDDIR   = /tmp
PDF           = ../manual.pdf

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest gettext

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  latexpdfja to make LaTeX files and run them through platex/dvipdfmx"
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  texinfo    to make Texinfo files"
	@echo "  info       to make Texinfo files and run them through makeinfo"
	@echo "  gettext    to make PO message catalogs"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  xml        to make Docutils-native XML files"
	@echo "  pseudoxml  to make pseudoxml-XML files for display purposes"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"

clean:
	rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

singlehtml:
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/MoviePy.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/MoviePy.qhc"

devhelp:
	$(SPHINXBUILD) -b devhelp $(ALLSPHINXOPTS) $(BUILDDIR)/devhelp
	@echo
	@echo "Build finished."
	@echo "To view the help file:"
	@echo "# mkdir -p $$HOME/.local/share/devhelp/MoviePy"
	@echo "# ln -s $(BUILDDIR)/devhelp $$HOME/.local/share/devhelp/MoviePy"
	@echo "# devhelp"

epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

latexpdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(PDFBUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(PDFBUILDDIR)/latex all-pdf
	cp $(PDFBUILDDIR)/latex/*.pdf $(PDF)
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

latexpdfja:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through platex and dvipdfmx..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf-ja
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

text:
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

man:
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/man."

texinfo:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo
	@echo "Build finished. The Texinfo files are in $(BUILDDIR)/texinfo."
	@echo "Run \`make' in that directory to run these through makeinfo" \
	      "(use \`make info' here to do that automatically)."

info:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo "Running Texinfo files through makeinfo..."
	make -C $(BUILDDIR)/texinfo info
	@echo "makeinfo finished; the Info files are in $(BUILDDIR)/texinfo."

gettext:
	$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) $(BUILDDIR)/locale
	@echo
	@echo "Build finished. The message catalogs are in $(BUILDDIR)/locale."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

xml:
	$(SPHINXBUILD) -b xml $(ALLSPHINXOPTS) $(BUILDDIR)/xml
	@echo
	@echo "Build finished. The XML files are in $(BUILDDIR)/xml."

pseudoxml:
	$(SPHINXBUILD) -b pseudoxml $(ALLSPHINXOPTS) $(BUILDDIR)/pseudoxml
	@echo
	@echo "Build finished. The pseudo-XML files are in $(BUILDDIR)/pseudoxml."
````

## File: docs/makehtml.sh
````bash
#!/bin/sh
make clean html

# open generated HTML files
if [[ $(uname) == 'Darwin' ]]; then
    open 'build/html/index.html' -a Firefox
elif [[ $(uname) == 'Linux' ]]; then
    firefox build/html/index.html
fi
````

## File: examples/soundtrack.py
````python
"""A simple test script on how to put a soundtrack to a movie."""

from moviepy import *


# We load a movie and replace the sound with some music:

movie = VideoFileClip("../../videos/dam.mov").with_audio(
    AudioFileClip("../../sounds/startars.ogg")
)


# If the soundtrack is longer than the movie, then at the end of the clip
# it will freeze on the last frame and wait for the clip to finish.
# If you don't want that, uncomment the next line:

# ~ movie.audio = movie.audio.with_duration(movie.duration)

movie.write_videofile("../../test_soundtrack.avi", codec="mpeg4")
````

## File: media/doc_medias/example.txt
````
Lorem ipsum
````

## File: media/subtitles-unicode.srt
````
0
00:00:00,000 --> 00:00:05,000
ÁÉíöÙ
````

## File: media/subtitles.srt
````
0
00:00:00,000 --> 00:00:01,000
Red!

1
00:00:02,000 --> 00:00:03,500
More Red!

2
00:00:5,000 --> 00:00:6,000
Green!

3
00:00:7,000 --> 00:00:8,000
Blue

4
00:00:9,000 --> 00:00:10,000
More Blue!
````

## File: media/traj.txt
````
# t(ms)	x	y
0	547	104
1000	210	78
2000	280	85
3000	337	93
4000	354	78
5000	381	68
6000	382	67
7000	382	67
8000	372	64
9000	372	65
````

## File: moviepy/audio/fx/__init__.py
````python
"""All the audio effects that can be applied to AudioClip and VideoClip."""

# import every video fx function

from moviepy.audio.fx.AudioDelay import AudioDelay
from moviepy.audio.fx.AudioFadeIn import AudioFadeIn
from moviepy.audio.fx.AudioFadeOut import AudioFadeOut
from moviepy.audio.fx.AudioLoop import AudioLoop
from moviepy.audio.fx.AudioNormalize import AudioNormalize
from moviepy.audio.fx.MultiplyStereoVolume import MultiplyStereoVolume
from moviepy.audio.fx.MultiplyVolume import MultiplyVolume


__all__ = (
    "AudioDelay",
    "AudioFadeIn",
    "AudioFadeOut",
    "AudioLoop",
    "AudioNormalize",
    "MultiplyStereoVolume",
    "MultiplyVolume",
)
````

## File: moviepy/audio/fx/AudioDelay.py
````python
from dataclasses import dataclass

import numpy as np

from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.fx.MultiplyVolume import MultiplyVolume
from moviepy.Clip import Clip
from moviepy.decorators import audio_video_effect
from moviepy.Effect import Effect


@dataclass
class AudioDelay(Effect):
    """Repeats audio certain number of times at constant intervals multiplying
    their volume levels using a linear space in the range 1 to ``decay`` argument
    value.

    Parameters
    ----------

    offset : float, optional
      Gap between repetitions start times, in seconds.

    n_repeats : int, optional
      Number of repetitions (without including the clip itself).

    decay : float, optional
      Multiplication factor for the volume level of the last repetition. Each
      repetition will have a value in the linear function between 1 and this value,
      increasing or decreasing constantly. Keep in mind that the last repetition
      will be muted if this is 0, and if is greater than 1, the volume will increase
      for each repetition.

    Examples
    --------

    .. code:: python

        from moviepy import *
        videoclip = AudioFileClip('myaudio.wav').with_effects([
            afx.AudioDelay(offset=.2, n_repeats=10, decayment=.2)
        ])

        # stereo A note
        frame_function = lambda t: np.array(
            [np.sin(440 * 2 * np.pi * t), np.sin(880 * 2 * np.pi * t)]
        ).T
        clip = AudioClip(frame_function=frame_function, duration=0.1, fps=44100)
        clip = clip.with_effects([afx.AudioDelay(offset=.2, n_repeats=11, decay=0)])
    """

    offset: float = 0.2
    n_repeats: int = 8
    decay: float = 1

    @audio_video_effect
    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        decayments = np.linspace(1, max(0, self.decay), self.n_repeats + 1)
        return CompositeAudioClip(
            [
                clip.copy(),
                *[
                    clip.with_start((rep + 1) * self.offset).with_effects(
                        [MultiplyVolume(decayments[rep + 1])]
                    )
                    for rep in range(self.n_repeats)
                ],
            ]
        )
````

## File: moviepy/audio/fx/AudioFadeIn.py
````python
from dataclasses import dataclass

import numpy as np

from moviepy.Clip import Clip
from moviepy.decorators import audio_video_effect
from moviepy.Effect import Effect
from moviepy.tools import convert_to_seconds


@dataclass
class AudioFadeIn(Effect):
    """Return an audio (or video) clip that is first mute, then the
    sound arrives progressively over ``duration`` seconds.

    Parameters
    ----------

    duration : float
        How long does it take for the sound to return to its normal level.

    Examples
    --------

    .. code:: python

        clip = VideoFileClip("media/chaplin.mp4")
        clip.with_effects([afx.AudioFadeIn("00:00:06")])
    """

    duration: float

    def __post_init__(self):
        self.duration = convert_to_seconds(self.duration)

    def _mono_factor_getter(self):
        return lambda t, duration: np.minimum(t / duration, 1)

    def _stereo_factor_getter(self, nchannels):
        def getter(t, duration):
            factor = np.minimum(t / duration, 1)
            return np.array([factor for _ in range(nchannels)]).T

        return getter

    @audio_video_effect
    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if clip.duration is None:
            raise ValueError("Attribute 'duration' not set")

        get_factor = (
            self._mono_factor_getter()
            if clip.nchannels == 1
            else self._stereo_factor_getter(clip.nchannels)
        )

        return clip.transform(
            lambda get_frame, t: get_factor(t, self.duration) * get_frame(t),
        )
````

## File: moviepy/audio/fx/AudioFadeOut.py
````python
from dataclasses import dataclass

import numpy as np

from moviepy.Clip import Clip
from moviepy.decorators import audio_video_effect
from moviepy.Effect import Effect
from moviepy.tools import convert_to_seconds


@dataclass
class AudioFadeOut(Effect):
    """Return a sound clip where the sound fades out progressively
    over ``duration`` seconds at the end of the clip.

    Parameters
    ----------

    duration : float
      How long does it take for the sound to reach the zero level at the end
      of the clip.

    Examples
    --------

    .. code:: python

        clip = VideoFileClip("media/chaplin.mp4")
        clip.with_effects([afx.AudioFadeOut("00:00:06")])
    """

    duration: float

    def __post_init__(self):
        self.duration = convert_to_seconds(self.duration)

    def _mono_factor_getter(self, clip_duration):
        return lambda t, duration: np.minimum(1.0 * (clip_duration - t) / duration, 1)

    def _stereo_factor_getter(self, clip_duration, nchannels):
        def getter(t, duration):
            factor = np.minimum(1.0 * (clip_duration - t) / duration, 1)
            return np.array([factor for _ in range(nchannels)]).T

        return getter

    @audio_video_effect
    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if clip.duration is None:
            raise ValueError("Attribute 'duration' not set")

        get_factor = (
            self._mono_factor_getter(clip.duration)
            if clip.nchannels == 1
            else self._stereo_factor_getter(clip.duration, clip.nchannels)
        )

        return clip.transform(
            lambda get_frame, t: get_factor(t, self.duration) * get_frame(t),
            keep_duration=True,
        )
````

## File: moviepy/audio/fx/AudioLoop.py
````python
from dataclasses import dataclass

from moviepy.audio.AudioClip import concatenate_audioclips
from moviepy.Clip import Clip
from moviepy.decorators import audio_video_effect
from moviepy.Effect import Effect


@dataclass
class AudioLoop(Effect):
    """Loops over an audio clip.

    Returns an audio clip that plays the given clip either
    `n_loops` times, or during `duration` seconds.

    Examples
    --------

    .. code:: python

        from moviepy import *
        videoclip = VideoFileClip('myvideo.mp4')
        music = AudioFileClip('music.ogg')
        audio = music.with_effects([afx.AudioLoop(duration=videoclip.duration)])
        videoclip.with_audio(audio)

    """

    n_loops: int = None
    duration: float = None

    @audio_video_effect
    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if self.duration is not None:
            self.n_loops = int(self.duration / clip.duration) + 1
            return concatenate_audioclips(self.n_loops * [clip]).with_duration(
                self.duration
            )

        return concatenate_audioclips(self.n_loops * [clip])
````

## File: moviepy/audio/fx/AudioNormalize.py
````python
from dataclasses import dataclass

from moviepy.audio.fx.MultiplyVolume import MultiplyVolume
from moviepy.Clip import Clip
from moviepy.decorators import audio_video_effect
from moviepy.Effect import Effect


@dataclass
class AudioNormalize(Effect):
    """Return a clip whose volume is normalized to 0db.

    Return an audio (or video) clip whose audio volume is normalized
    so that the maximum volume is at 0db, the maximum achievable volume.

    Examples
    --------

    >>> from moviepy import *
    >>> videoclip = VideoFileClip('myvideo.mp4').with_effects([afx.AudioNormalize()])

    """

    @audio_video_effect
    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        max_volume = clip.max_volume()
        if max_volume == 0:
            return clip
        else:
            return clip.with_effects([MultiplyVolume(1 / max_volume)])
````

## File: moviepy/audio/fx/MultiplyStereoVolume.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.decorators import audio_video_effect
from moviepy.Effect import Effect


@dataclass
class MultiplyStereoVolume(Effect):
    """For a stereo audioclip, this function enables to change the volume
    of the left and right channel separately (with the factors `left`
    and `right`). Makes a stereo audio clip in which the volume of left
    and right is controllable.

    Examples
    --------

    .. code:: python

        from moviepy import AudioFileClip
        music = AudioFileClip('music.ogg')
        # mutes left channel
        audio_r = music.with_effects([afx.MultiplyStereoVolume(left=0, right=1)])
        # halves audio volume
        audio_h = music.with_effects([afx.MultiplyStereoVolume(left=0.5, right=0.5)])
    """

    left: float = 1
    right: float = 1

    @audio_video_effect
    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""

        def stereo_volume(get_frame, t):
            frame = get_frame(t)
            if len(frame) == 1:  # mono
                frame *= self.left if self.left is not None else self.right
            else:  # stereo, stereo surround...
                for i in range(len(frame[0])):  # odd channels are left
                    frame[:, i] *= self.left if i % 2 == 0 else self.right
            return frame

        return clip.transform(stereo_volume)
````

## File: moviepy/audio/fx/MultiplyVolume.py
````python
from dataclasses import dataclass

import numpy as np

from moviepy.Clip import Clip
from moviepy.decorators import audio_video_effect
from moviepy.Effect import Effect
from moviepy.tools import convert_to_seconds


@dataclass
class MultiplyVolume(Effect):
    """Returns a clip with audio volume multiplied by the
    value `factor`. Can be applied to both audio and video clips.

    Parameters
    ----------

    factor : float
      Volume multiplication factor.

    start_time : float, optional
      Time from the beginning of the clip until the volume transformation
      begins to take effect, in seconds. By default at the beginning.

    end_time : float, optional
      Time from the beginning of the clip until the volume transformation
      ends to take effect, in seconds. By default at the end.

    Examples
    --------

    .. code:: python

        from moviepy import AudioFileClip

        music = AudioFileClip("music.ogg")
        # doubles audio volume
        doubled_audio_clip = music.with_effects([afx.MultiplyVolume(2)])
        # halves audio volume
        half_audio_clip = music.with_effects([afx.MultiplyVolume(0.5)])
        # silences clip during one second at third
        effect = afx.MultiplyVolume(0, start_time=2, end_time=3)
        silenced_clip = clip.with_effects([effect])
    """

    factor: float
    start_time: float = None
    end_time: float = None

    def __post_init__(self):
        if self.start_time is not None:
            self.start_time = convert_to_seconds(self.start_time)

        if self.end_time is not None:
            self.end_time = convert_to_seconds(self.end_time)

    def _multiply_volume_in_range(self, factor, start_time, end_time, nchannels):
        def factors_filter(factor, t):
            return np.array([factor if start_time <= t_ <= end_time else 1 for t_ in t])

        def multiply_stereo_volume(get_frame, t):
            return np.multiply(
                get_frame(t),
                np.array([factors_filter(factor, t) for _ in range(nchannels)]).T,
            )

        def multiply_mono_volume(get_frame, t):
            return np.multiply(get_frame(t), factors_filter(factor, t))

        return multiply_mono_volume if nchannels == 1 else multiply_stereo_volume

    @audio_video_effect
    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if self.start_time is None and self.end_time is None:
            return clip.transform(
                lambda get_frame, t: self.factor * get_frame(t),
                keep_duration=True,
            )

        return clip.transform(
            self._multiply_volume_in_range(
                self.factor,
                clip.start if self.start_time is None else self.start_time,
                clip.end if self.end_time is None else self.end_time,
                clip.nchannels,
            ),
            keep_duration=True,
        )
````

## File: moviepy/audio/io/__init__.py
````python
"""Class and methods to read, write, preview audiofiles."""
````

## File: moviepy/audio/io/AudioFileClip.py
````python
"""Implements AudioFileClip, a class for audio clips creation using audio files."""

from moviepy.audio.AudioClip import AudioClip
from moviepy.audio.io.readers import FFMPEG_AudioReader
from moviepy.decorators import convert_path_to_string


class AudioFileClip(AudioClip):
    """
    An audio clip read from a sound file, or an array.
    The whole file is not loaded in memory. Instead, only a portion is
    read and stored in memory. this portion includes frames before
    and after the last frames read, so that it is fast to read the sound
    backward and forward.

    Parameters
    ----------

    filename
      Either a soundfile name (of any extension supported by ffmpeg)
      as a string or a path-like object,
      or an array representing a sound. If the soundfile is not a .wav,
      it will be converted to .wav first, using the ``fps`` and
      ``bitrate`` arguments.

    buffersize:
      Size to load in memory (in number of frames)


    Attributes
    ----------

    nbytes
      Number of bits per frame of the original audio file.

    fps
      Number of frames per second in the audio file

    buffersize
      See Parameters.

    audio_stream_index
      The index of the audio stream to read from the file.

    Lifetime
    --------

    Note that this creates subprocesses and locks files. If you construct one
    of these instances, you must call close() afterwards, or the subresources
    will not be cleaned up until the process ends.

    Examples
    --------

    .. code:: python

        snd = AudioFileClip("song.wav")
        snd.close()
    """

    @convert_path_to_string("filename")
    def __init__(
        self,
        filename,
        decode_file=False,
        buffersize=200000,
        nbytes=2,
        fps=44100,
        audio_stream_index=0,
    ):
        AudioClip.__init__(self)

        self.filename = filename
        self.reader = FFMPEG_AudioReader(
            filename,
            decode_file=decode_file,
            fps=fps,
            nbytes=nbytes,
            buffersize=buffersize,
            audio_stream_index=audio_stream_index,
        )
        self.fps = fps
        self.duration = self.reader.duration
        self.end = self.reader.duration
        self.buffersize = self.reader.buffersize
        self.filename = filename

        self.frame_function = lambda t: self.reader.get_frame(t)
        self.nchannels = self.reader.nchannels

    def close(self):
        """Close the internal reader."""
        if self.reader:
            self.reader.close()
            self.reader = None
````

## File: moviepy/audio/io/ffmpeg_audiowriter.py
````python
"""MoviePy audio writing with ffmpeg."""

import subprocess as sp

import proglog

from moviepy.config import FFMPEG_BINARY
from moviepy.decorators import requires_duration
from moviepy.tools import cross_platform_popen_params, ffmpeg_escape_filename


class FFMPEG_AudioWriter:
    """
    A class to write an AudioClip into an audio file.

    Parameters
    ----------

    filename
      Name of any video or audio file, like ``video.mp4`` or ``sound.wav`` etc.

    size
      Size (width,height) in pixels of the output video.

    fps_input
      Frames per second of the input audio (given by the AudioClip being
      written down).

    nbytes : int, optional
      Number of bytes per sample. Default is 2 (16-bit audio).

    nchannels : int, optional
      Number of audio channels. Default is 2 (stereo).

    codec : str, optional
        The codec to use for the output. Default is ``libfdk_aac``.

    bitrate:
      A string indicating the bitrate of the final video. Only
      relevant for codecs which accept a bitrate.

    input_video : str, optional
      Path to an input video file. If provided, the audio will be muxed with this video.
      If not provided, the output will be audio-only.

    logfile : file-like object or None, optional
      A file object where FFMPEG logs will be written. If None, logs are suppressed.

    ffmpeg_params : list of str, optional
      Additional FFMPEG command-line parameters to customize the output.
    """

    def __init__(
        self,
        filename,
        fps_input,
        nbytes=2,
        nchannels=2,
        codec="libfdk_aac",
        bitrate=None,
        input_video=None,
        logfile=None,
        ffmpeg_params=None,
    ):
        if logfile is None:
            logfile = sp.PIPE
        self.logfile = logfile
        self.filename = filename
        self.codec = codec
        self.ext = self.filename.split(".")[-1]

        # order is important
        cmd = [
            FFMPEG_BINARY,
            "-y",
            "-loglevel",
            "error" if logfile == sp.PIPE else "info",
            "-f",
            "s%dle" % (8 * nbytes),
            "-acodec",
            "pcm_s%dle" % (8 * nbytes),
            "-ar",
            "%d" % fps_input,
            "-ac",
            "%d" % nchannels,
            "-i",
            "-",
        ]
        if input_video is None:
            cmd.extend(["-vn"])
        else:
            cmd.extend(["-i", ffmpeg_escape_filename(input_video), "-vcodec", "copy"])

        cmd.extend(["-acodec", codec] + ["-ar", "%d" % fps_input])
        cmd.extend(["-strict", "-2"])  # needed to support codec 'aac'
        if bitrate is not None:
            cmd.extend(["-ab", bitrate])
        if ffmpeg_params is not None:
            cmd.extend(ffmpeg_params)
        cmd.extend([ffmpeg_escape_filename(filename)])

        popen_params = cross_platform_popen_params(
            {"stdout": sp.DEVNULL, "stderr": logfile, "stdin": sp.PIPE}
        )

        self.proc = sp.Popen(cmd, **popen_params)

    def write_frames(self, frames_array):
        """Send the audio frame (a chunck of ``AudioClip``) to ffmpeg for writting"""
        try:
            self.proc.stdin.write(frames_array.tobytes())
        except IOError as err:
            _, ffmpeg_error = self.proc.communicate()
            if ffmpeg_error is not None:
                ffmpeg_error = ffmpeg_error.decode()
            else:
                # The error was redirected to a logfile with `write_logfile=True`,
                # so read the error from that file instead
                self.logfile.seek(0)
                ffmpeg_error = self.logfile.read()

            error = (
                f"{err}\n\nMoviePy error: FFMPEG encountered the following error while "
                f"writing file {self.filename}:\n\n {ffmpeg_error}"
            )

            if "Unknown encoder" in ffmpeg_error:
                error += (
                    "\n\nThe audio export failed because FFMPEG didn't find the "
                    f"specified codec for audio encoding {self.codec}. "
                    "Please install this codec or change the codec when calling "
                    "write_videofile or write_audiofile.\nFor instance for mp3:\n"
                    "   >>> write_videofile('myvid.mp4', audio_codec='libmp3lame')"
                )

            elif "incorrect codec parameters ?" in ffmpeg_error:
                error += (
                    "\n\nThe audio export failed, possibly because the "
                    f"codec specified for the video {self.codec} is not compatible"
                    f" with the given extension {self.ext}. Please specify a "
                    "valid 'codec' argument in write_audiofile or 'audio_codoc'"
                    "argument in write_videofile. This would be "
                    "'libmp3lame' for mp3, 'libvorbis' for ogg..."
                )

            elif "bitrate not specified" in ffmpeg_error:
                error += (
                    "\n\nThe audio export failed, possibly because the "
                    "bitrate you specified was too high or too low for "
                    "the audio codec."
                )

            elif "Invalid encoder type" in ffmpeg_error:
                error += (
                    "\n\nThe audio export failed because the codec "
                    "or file extension you provided is not suitable for audio"
                )

            raise IOError(error)

    def close(self):
        """Closes the writer, terminating the subprocess if is still alive."""
        if hasattr(self, "proc") and self.proc:
            self.proc.stdin.close()
            self.proc.stdin = None
            if self.proc.stderr is not None:
                self.proc.stderr.close()
                self.proc.stderr = None
            # If this causes deadlocks, consider terminating instead.
            self.proc.wait()
            self.proc = None

    def __del__(self):
        # If the garbage collector comes, make sure the subprocess is terminated.
        self.close()

    # Support the Context Manager protocol, to ensure that resources are cleaned up.

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


@requires_duration
def ffmpeg_audiowrite(
    clip,
    filename,
    fps,
    nbytes,
    buffersize,
    codec="libvorbis",
    bitrate=None,
    write_logfile=False,
    ffmpeg_params=None,
    logger="bar",
):
    """
    A function that wraps the FFMPEG_AudioWriter to write an AudioClip
    to a file.
    """
    if write_logfile:
        logfile = open(filename + ".log", "w+")
    else:
        logfile = None
    logger = proglog.default_bar_logger(logger)
    logger(message="MoviePy - Writing audio in %s" % filename)
    writer = FFMPEG_AudioWriter(
        filename,
        fps,
        nbytes,
        clip.nchannels,
        codec=codec,
        bitrate=bitrate,
        logfile=logfile,
        ffmpeg_params=ffmpeg_params,
    )

    for chunk in clip.iter_chunks(
        chunksize=buffersize, quantize=True, nbytes=nbytes, fps=fps, logger=logger
    ):
        writer.write_frames(chunk)

    writer.close()

    if write_logfile:
        logfile.close()
    logger(message="MoviePy - Done.")
````

## File: moviepy/audio/io/ffplay_audiopreviewer.py
````python
"""MoviePy audio writing with ffmpeg."""

import subprocess as sp

from moviepy.config import FFPLAY_BINARY
from moviepy.decorators import requires_duration
from moviepy.tools import cross_platform_popen_params
from moviepy.video.io import ffmpeg_tools


class FFPLAY_AudioPreviewer:
    """
    A class to preview an AudioClip.

    Parameters
    ----------

    fps_input
      Frames per second of the input audio (given by the AudioClip being
      written down).

    nbytes:
      Number of bytes to encode the sound: 1 for 8bit sound, 2 for
      16bit, 4 for 32bit sound. Default is 2 bytes, it's fine.

    nchannels:
      Number of audio channels in the clip. Default to 2 channels.
    """

    def __init__(
        self,
        fps_input,
        nbytes=2,
        nchannels=2,
    ):
        # order is important
        cmd = [
            FFPLAY_BINARY,
            "-autoexit",  # If you don't precise, ffplay won't stop at end
            "-nodisp",  # If you don't precise a window is
            "-f",
            "s%dle" % (8 * nbytes),
            "-ar",
            "%d" % fps_input,
        ]

        # Adapt number of channels argument to ffplay version
        ffplay_version = ffmpeg_tools.ffplay_version()[1]
        if int(ffplay_version.split(".")[0]) >= 7:
            cmd += [
                "-ch_layout",
                "stereo" if nchannels == 2 else "mono",
            ]
        else:
            cmd += [
                "-ac",
                "%d" % nchannels,
            ]

        cmd += [
            "-i",
            "-",
        ]

        popen_params = cross_platform_popen_params(
            {"stdout": sp.DEVNULL, "stderr": sp.STDOUT, "stdin": sp.PIPE}
        )

        self.proc = sp.Popen(cmd, **popen_params)

    def write_frames(self, frames_array):
        """Send a raw audio frame (a chunck of audio) to ffplay to be played"""
        try:
            self.proc.stdin.write(frames_array.tobytes())
        except IOError as err:
            _, ffplay_error = self.proc.communicate()
            if ffplay_error is not None:
                ffplay_error = ffplay_error.decode()

            error = (
                f"{err}\n\nMoviePy error: FFPLAY encountered the following error while "
                f":\n\n {ffplay_error}"
            )

            raise IOError(error)

    def close(self):
        """Closes the writer, terminating the subprocess if is still alive."""
        if hasattr(self, "proc") and self.proc:
            self.proc.stdin.close()
            self.proc.stdin = None
            if self.proc.stderr is not None:
                self.proc.stderr.close()
                self.proc.stderr = None
            # If this causes deadlocks, consider terminating instead.
            self.proc.wait()
            self.proc = None

    def __del__(self):
        # If the garbage collector comes, make sure the subprocess is terminated.
        self.close()

    # Support the Context Manager protocol, to ensure that resources are cleaned up.

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


@requires_duration
def ffplay_audiopreview(
    clip, fps=None, buffersize=2000, nbytes=2, audio_flag=None, video_flag=None
):
    """
    A function that wraps the FFPLAY_AudioPreviewer to preview an AudioClip

    Parameters
    ----------

    fps
       Frame rate of the sound. 44100 gives top quality, but may cause
       problems if your computer is not fast enough and your clip is
       complicated. If the sound jumps during the preview, lower it
       (11025 is still fine, 5000 is tolerable).

    buffersize
      The sound is not generated all at once, but rather made by bunches
      of frames (chunks). ``buffersize`` is the size of such a chunk.
      Try varying it if you meet audio problems (but you shouldn't
      have to).

    nbytes:
      Number of bytes to encode the sound: 1 for 8bit sound, 2 for
      16bit, 4 for 32bit sound. 2 bytes is fine.

    audio_flag, video_flag:
      Instances of class threading events that are used to synchronize
      video and audio during ``VideoClip.preview()``.
    """
    if not fps:
        if not clip.fps:
            fps = 44100
        else:
            fps = clip.fps

    with FFPLAY_AudioPreviewer(fps, nbytes, clip.nchannels) as previewer:
        first_frame = True
        for chunk in clip.iter_chunks(
            chunksize=buffersize, quantize=True, nbytes=nbytes, fps=fps
        ):
            # On first frame, wait for video
            if first_frame:
                first_frame = False

                if audio_flag is not None:
                    audio_flag.set()  # Say to video that audio is ready

                if video_flag is not None:
                    video_flag.wait()  # Wait for video to be ready

            previewer.write_frames(chunk)
````

## File: moviepy/audio/io/readers.py
````python
"""MoviePy audio reading with ffmpeg."""

import subprocess as sp
import warnings

import numpy as np

from moviepy.config import FFMPEG_BINARY
from moviepy.tools import cross_platform_popen_params, ffmpeg_escape_filename
from moviepy.video.io.ffmpeg_reader import ffmpeg_parse_infos


class FFMPEG_AudioReader:
    """A class to read the audio in either video files or audio files
    using ffmpeg. ffmpeg will read any audio and transform them into
    raw data.

    Parameters
    ----------

    filename
      Name of any video or audio file, like ``video.mp4`` or
      ``sound.wav`` etc.

    buffersize
      The size of the buffer to use. Should be bigger than the buffer
      used by ``write_audiofile``

    print_infos
      Print the ffmpeg infos on the file being read (for debugging)

    fps
      Desired frames per second in the decoded signal that will be
      received from ffmpeg

    nbytes
      Desired number of bytes (1,2,4) in the signal that will be
      received from ffmpeg

    audio_stream_index
      The index of the audio stream to read from the file.
    """

    def __init__(
        self,
        filename,
        buffersize,
        decode_file=False,
        print_infos=False,
        fps=44100,
        nbytes=2,
        nchannels=2,
        audio_stream_index=0,
    ):
        # TODO bring FFMPEG_AudioReader more in line with FFMPEG_VideoReader
        # E.g. here self.pos is still 1-indexed.
        # (or have them inherit from a shared parent class)
        self.filename = filename
        self.nbytes = nbytes
        self.fps = fps
        self.format = "s%dle" % (8 * nbytes)
        self.codec = "pcm_s%dle" % (8 * nbytes)
        self.nchannels = nchannels
        infos = ffmpeg_parse_infos(
            filename, decode_file=decode_file, print_infos=print_infos
        )
        self.duration = infos["duration"]
        self.bitrate = infos["audio_bitrate"]
        self.infos = infos
        self.proc = None
        self.audio_stream_index = audio_stream_index

        self.n_frames = int(self.fps * self.duration)
        self.buffersize = min(self.n_frames + 1, buffersize)
        self.buffer = None
        self.buffer_startframe = 1
        self.initialize()
        self.buffer_around(1)

    def initialize(self, start_time=0):
        """Opens the file, creates the pipe."""
        self.close()  # if any

        if start_time != 0:
            offset = min(1, start_time)
            i_arg = [
                "-ss",
                "%.05f" % (start_time - offset),
                "-i",
                ffmpeg_escape_filename(self.filename),
                "-map",
                "0:a:%d" % self.audio_stream_index,
                "-vn",
                "-ss",
                "%.05f" % offset,
            ]
        else:
            i_arg = ["-i", ffmpeg_escape_filename(self.filename), "-vn"]

        cmd = (
            [FFMPEG_BINARY]
            + i_arg
            + [
                "-loglevel",
                "error",
                "-f",
                self.format,
                "-acodec",
                self.codec,
                "-ar",
                "%d" % self.fps,
                "-ac",
                "%d" % self.nchannels,
                "-",
            ]
        )

        popen_params = cross_platform_popen_params(
            {
                "bufsize": self.buffersize,
                "stdout": sp.PIPE,
                "stderr": sp.PIPE,
                "stdin": sp.DEVNULL,
            }
        )

        self.proc = sp.Popen(cmd, **popen_params)

        self.pos = np.round(self.fps * start_time)

    def skip_chunk(self, chunksize):
        """Skip a chunk of audio data by reading and discarding the specified number of
        frames from the audio stream. The audio stream is read from the `proc` stdout.
        After skipping the chunk, the `pos` attribute is updated accordingly.

        Parameters
        ----------
        chunksize (int):
          The number of audio frames to skip.
        """
        _ = self.proc.stdout.read(self.nchannels * chunksize * self.nbytes)
        self.proc.stdout.flush()
        self.pos = self.pos + chunksize

    def read_chunk(self, chunksize):
        """Read a chunk of audio data from the audio stream.

        This method reads a chunk of audio data from the audio stream. The
        specified number of frames, given by `chunksize`, is read from the
        `proc` stdout. The audio data is returned as a NumPy array, where
        each row corresponds to a frame and each column corresponds to a
        channel. If there is not enough audio left to read, the remaining
        portion is padded with zeros, ensuring that the returned array has
        the desired length. The `pos` attribute is updated accordingly.

        Parameters
        ----------
        chunksize (float):
          The desired number of audio frames to read.

        """
        # chunksize is not being autoconverted from float to int
        chunksize = int(round(chunksize))
        s = self.proc.stdout.read(self.nchannels * chunksize * self.nbytes)
        data_type = {1: "int8", 2: "int16", 4: "int32"}[self.nbytes]
        if hasattr(np, "frombuffer"):
            result = np.frombuffer(s, dtype=data_type)
        else:
            result = np.fromstring(s, dtype=data_type)
        result = (1.0 * result / 2 ** (8 * self.nbytes - 1)).reshape(
            (int(len(result) / self.nchannels), self.nchannels)
        )

        # Pad the read chunk with zeros when there isn't enough audio
        # left to read, so the buffer is always at full length.
        pad = np.zeros((chunksize - len(result), self.nchannels), dtype=result.dtype)
        result = np.concatenate([result, pad])
        # self.proc.stdout.flush()
        self.pos = self.pos + chunksize
        return result

    def seek(self, pos):
        """Read a frame at time t. Note for coders: getting an arbitrary
        frame in the video with ffmpeg can be painfully slow if some
        decoding has to be done. This function tries to avoid fectching
        arbitrary frames whenever possible, by moving between adjacent
        frames.
        """
        if (pos < self.pos) or (pos > (self.pos + 1000000)):
            t = 1.0 * pos / self.fps
            self.initialize(t)
        elif pos > self.pos:
            self.skip_chunk(pos - self.pos)
        # last case standing: pos = current pos
        self.pos = pos

    def get_frame(self, tt):
        """Retrieve the audio frame(s) corresponding to the given timestamp(s).

        Parameters
        ----------
        tt (float or numpy.ndarray):
          The timestamp(s) at which to retrieve the audio frame(s).
          If `tt` is a single float value, the frame corresponding to that
          timestamp is returned. If `tt` is a NumPy array of timestamps, an
          array of frames corresponding to each timestamp is returned.
        """
        if isinstance(tt, np.ndarray):
            # lazy implementation, but should not cause problems in
            # 99.99 %  of the cases

            # elements of t that are actually in the range of the
            # audio file.
            in_time = (tt >= 0) & (tt < self.duration)

            # Check that the requested time is in the valid range
            if not in_time.any():
                raise IOError(
                    "Error in file %s, " % (self.filename)
                    + "Accessing time t=%.02f-%.02f seconds, " % (tt[0], tt[-1])
                    + "with clip duration=%f seconds, " % self.duration
                )

            # The np.round in the next line is super-important.
            # Removing it results in artifacts in the noise.
            frames = np.round((self.fps * tt)).astype(int)[in_time]
            fr_min, fr_max = frames.min(), frames.max()

            # if min and max frames don't fit the buffer, it results in IndexError
            # we avoid that by recursively calling this function on smaller length
            # and concatenate the results:w
            max_frame_threshold = fr_min + self.buffersize // 2
            threshold_idx = np.searchsorted(frames, max_frame_threshold, side="right")
            if threshold_idx != len(frames):
                in_time_head = in_time[0:threshold_idx]
                in_time_tail = in_time[threshold_idx:]
                return np.concatenate(
                    [self.get_frame(in_time_head), self.get_frame(in_time_tail)]
                )

            if not (0 <= (fr_min - self.buffer_startframe) < len(self.buffer)):
                self.buffer_around(fr_min)
            elif not (0 <= (fr_max - self.buffer_startframe) < len(self.buffer)):
                self.buffer_around(fr_max)

            try:
                result = np.zeros((len(tt), self.nchannels))
                indices = frames - self.buffer_startframe
                result[in_time] = self.buffer[indices]
                return result

            except IndexError as error:
                warnings.warn(
                    "Error in file %s, " % (self.filename)
                    + "At time t=%.02f-%.02f seconds, " % (tt[0], tt[-1])
                    + "indices wanted: %d-%d, " % (indices.min(), indices.max())
                    + "but len(buffer)=%d\n" % (len(self.buffer))
                    + str(error),
                    UserWarning,
                )

                # repeat the last frame instead
                indices[indices >= len(self.buffer)] = len(self.buffer) - 1
                result[in_time] = self.buffer[indices]
                return result

        else:
            ind = int(self.fps * tt)
            if ind < 0 or ind > self.n_frames:  # out of time: return 0
                return np.zeros(self.nchannels)

            if not (0 <= (ind - self.buffer_startframe) < len(self.buffer)):
                # out of the buffer: recenter the buffer
                self.buffer_around(ind)

            # read the frame in the buffer
            return self.buffer[ind - self.buffer_startframe]

    def buffer_around(self, frame_number):
        """Fill the buffer with frames, centered on frame_number if possible."""
        # start-frame for the buffer
        new_bufferstart = max(0, frame_number - self.buffersize // 2)

        if self.buffer is not None:
            current_f_end = self.buffer_startframe + self.buffersize
            if new_bufferstart < current_f_end < new_bufferstart + self.buffersize:
                # We already have part of what must be read
                conserved = current_f_end - new_bufferstart
                chunksize = self.buffersize - conserved
                array = self.read_chunk(chunksize)
                self.buffer = np.vstack([self.buffer[-conserved:], array])
            else:
                self.seek(new_bufferstart)
                self.buffer = self.read_chunk(self.buffersize)
        else:
            self.seek(new_bufferstart)
            self.buffer = self.read_chunk(self.buffersize)

        self.buffer_startframe = new_bufferstart

    def close(self):
        """Closes the reader, terminating the subprocess if is still alive."""
        if self.proc:
            if self.proc.poll() is None:
                self.proc.terminate()
                self.proc.stdout.close()
                self.proc.stderr.close()
                self.proc.wait()
            self.proc = None

    def __del__(self):
        # If the garbage collector comes, make sure the subprocess is terminated.
        self.close()
````

## File: moviepy/audio/tools/__init__.py
````python
"""Tools to better processing and edition of audio."""
````

## File: moviepy/audio/tools/cuts.py
````python
"""Cutting utilities working with audio."""

import numpy as np


def find_audio_period(clip, min_time=0.1, max_time=2, time_resolution=0.01):
    """Finds the period, in seconds of an audioclip.

    Parameters
    ----------

    min_time : float, optional
      Minimum bound for the returned value.

    max_time : float, optional
      Maximum bound for the returned value.

    time_resolution : float, optional
      Numerical precision.
    """
    chunksize = int(time_resolution * clip.fps)
    chunk_duration = 1.0 * chunksize / clip.fps
    # v denotes the list of volumes
    v = np.array([(chunk**2).sum() for chunk in clip.iter_chunks(chunksize)])
    v = v - v.mean()
    corrs = np.correlate(v, v, mode="full")[-len(v) :]
    corrs[: int(min_time / chunk_duration)] = 0
    corrs[int(max_time / chunk_duration) :] = 0
    return chunk_duration * np.argmax(corrs)
````

## File: moviepy/audio/__init__.py
````python
"""Everything about audio manipulation."""
````

## File: moviepy/audio/AudioClip.py
````python
"""Implements AudioClip (base class for audio clips) and its main subclasses:

- Audio clips: AudioClip, AudioFileClip, AudioArrayClip
- Composition: CompositeAudioClip
"""

import numbers
import os

import numpy as np
import proglog

from moviepy.audio.io.ffmpeg_audiowriter import ffmpeg_audiowrite
from moviepy.audio.io.ffplay_audiopreviewer import ffplay_audiopreview
from moviepy.Clip import Clip
from moviepy.decorators import convert_path_to_string, requires_duration
from moviepy.tools import extensions_dict


class AudioClip(Clip):
    """Base class for audio clips.

    See ``AudioFileClip`` and ``CompositeAudioClip`` for usable classes.

    An AudioClip is a Clip with a ``frame_function``  attribute of
    the form `` t -> [ f_t ]`` for mono sound and
    ``t-> [ f1_t, f2_t ]`` for stereo sound (the arrays are Numpy arrays).
    The `f_t` are floats between -1 and 1. These bounds can be
    trespassed without problems (the program will put the
    sound back into the bounds at conversion time, without much impact).

    Parameters
    ----------

    frame_function
      A function `t-> frame at time t`. The frame does not mean much
      for a sound, it is just a float. What 'makes' the sound are
      the variations of that float in the time.

    duration
      Duration of the clip (in seconds). Some clips are infinite, in
      this case their duration will be ``None``.

    nchannels
      Number of channels (one or two for mono or stereo).

    Examples
    --------

    .. code:: python

        # Plays the note A in mono (a sine wave of frequency 440 Hz)
        import numpy as np
        frame_function = lambda t: np.sin(440 * 2 * np.pi * t)
        clip = AudioClip(frame_function, duration=5, fps=44100)
        clip.preview()

        # Plays the note A in stereo (two sine waves of frequencies 440 and 880 Hz)
        frame_function = lambda t: np.array([
            np.sin(440 * 2 * np.pi * t),
            np.sin(880 * 2 * np.pi * t)
        ]).T.copy(order="C")
        clip = AudioClip(frame_function, duration=3, fps=44100)
        clip.preview()

    """

    def __init__(self, frame_function=None, duration=None, fps=None):
        super().__init__()

        if fps is not None:
            self.fps = fps

        if frame_function is not None:
            self.frame_function = frame_function
            frame0 = self.get_frame(0)
            if hasattr(frame0, "__iter__"):
                self.nchannels = len(list(frame0))
            else:
                self.nchannels = 1
        if duration is not None:
            self.duration = duration
            self.end = duration

    @requires_duration
    def iter_chunks(
        self,
        chunksize=None,
        chunk_duration=None,
        fps=None,
        quantize=False,
        nbytes=2,
        logger=None,
    ):
        """Iterator that returns the whole sound array of the clip by chunks"""
        if fps is None:
            fps = self.fps
        logger = proglog.default_bar_logger(logger)
        if chunk_duration is not None:
            chunksize = int(chunk_duration * fps)

        total_size = int(fps * self.duration)

        nchunks = total_size // chunksize + 1

        positions = np.linspace(0, total_size, nchunks + 1, endpoint=True, dtype=int)

        for i in logger.iter_bar(chunk=list(range(nchunks))):
            size = positions[i + 1] - positions[i]
            assert size <= chunksize
            timings = (1.0 / fps) * np.arange(positions[i], positions[i + 1])
            yield self.to_soundarray(
                timings, nbytes=nbytes, quantize=quantize, fps=fps, buffersize=chunksize
            )

    @requires_duration
    def to_soundarray(
        self, tt=None, fps=None, quantize=False, nbytes=2, buffersize=50000
    ):
        """
        Transforms the sound into an array that can be played by pygame
        or written in a wav file. See ``AudioClip.preview``.

        Parameters
        ----------

        fps
          Frame rate of the sound for the conversion.
          44100 for top quality.

        nbytes
          Number of bytes to encode the sound: 1 for 8bit sound,
          2 for 16bit, 4 for 32bit sound.

        """
        if tt is None:
            if fps is None:
                fps = self.fps

            max_duration = 1 * buffersize / fps
            if self.duration > max_duration:
                stacker = np.vstack if self.nchannels == 2 else np.hstack
                return stacker(
                    tuple(
                        self.iter_chunks(
                            fps=fps, quantize=quantize, nbytes=2, chunksize=buffersize
                        )
                    )
                )
            else:
                tt = np.arange(0, self.duration, 1.0 / fps)
        """
        elif len(tt)> 1.5*buffersize:
            nchunks = int(len(tt)/buffersize+1)
            tt_chunks = np.array_split(tt, nchunks)
            return stacker([self.to_soundarray(tt=ttc, buffersize=buffersize, fps=fps,
                                        quantize=quantize, nbytes=nbytes)
                              for ttc in tt_chunks])
        """
        snd_array = self.get_frame(tt)

        if quantize:
            snd_array = np.maximum(-0.99, np.minimum(0.99, snd_array))
            inttype = {1: "int8", 2: "int16", 4: "int32"}[nbytes]
            snd_array = (2 ** (8 * nbytes - 1) * snd_array).astype(inttype)

        return snd_array

    def max_volume(self, stereo=False, chunksize=50000, logger=None):
        """Returns the maximum volume level of the clip."""
        # max volume separated by channels if ``stereo`` and not mono
        stereo = stereo and self.nchannels > 1

        # zero for each channel
        maxi = np.zeros(self.nchannels)
        for chunk in self.iter_chunks(chunksize=chunksize, logger=logger):
            maxi = np.maximum(maxi, abs(chunk).max(axis=0))

        # if mono returns float, otherwise array of volumes by channel
        return maxi if stereo else maxi[0]

    @requires_duration
    @convert_path_to_string("filename")
    def write_audiofile(
        self,
        filename,
        fps=None,
        nbytes=2,
        buffersize=2000,
        codec=None,
        bitrate=None,
        ffmpeg_params=None,
        write_logfile=False,
        logger="bar",
    ):
        """Writes an audio file from the AudioClip.


        Parameters
        ----------

        filename
          Name of the output file, as a string or a path-like object.

        fps
          Frames per second. If not set, it will try default to self.fps if
          already set, otherwise it will default to 44100.

        nbytes
          Sample width (set to 2 for 16-bit sound, 4 for 32-bit sound)

        buffersize
          The sound is not generated all at once, but rather made by bunches
          of frames (chunks). ``buffersize`` is the size of such a chunk.
          Try varying it if you meet audio problems (but you shouldn't
          have to). Default to 2000

        codec
          Which audio codec should be used. If None provided, the codec is
          determined based on the extension of the filename. Choose
          'pcm_s16le' for 16-bit wav and 'pcm_s32le' for 32-bit wav.

        bitrate
          Audio bitrate, given as a string like '50k', '500k', '3000k'.
          Will determine the size and quality of the output file.
          Note that it mainly an indicative goal, the bitrate won't
          necessarily be the this in the output file.

        ffmpeg_params
          Any additional parameters you would like to pass, as a list
          of terms, like ['-option1', 'value1', '-option2', 'value2']

        write_logfile
          If true, produces a detailed logfile named filename + '.log'
          when writing the file

        logger
          Either ``"bar"`` for progress bar or ``None`` or any Proglog logger.

        """
        if not fps:
            if hasattr(self, "fps"):
                fps = self.fps
            else:
                fps = 44100

        if codec is None:
            name, ext = os.path.splitext(os.path.basename(filename))
            try:
                codec = extensions_dict[ext[1:]]["codec"][0]
            except KeyError:
                raise ValueError(
                    "MoviePy couldn't find the codec associated "
                    "with the filename. Provide the 'codec' "
                    "parameter in write_audiofile."
                )

        return ffmpeg_audiowrite(
            self,
            filename,
            fps,
            nbytes,
            buffersize,
            codec=codec,
            bitrate=bitrate,
            write_logfile=write_logfile,
            ffmpeg_params=ffmpeg_params,
            logger=logger,
        )

    @requires_duration
    def audiopreview(
        self, fps=None, buffersize=2000, nbytes=2, audio_flag=None, video_flag=None
    ):
        """
        Preview an AudioClip using ffplay

        Parameters
        ----------

        fps
            Frame rate of the sound. 44100 gives top quality, but may cause
            problems if your computer is not fast enough and your clip is
            complicated. If the sound jumps during the preview, lower it
            (11025 is still fine, 5000 is tolerable).

        buffersize
            The sound is not generated all at once, but rather made by bunches
            of frames (chunks). ``buffersize`` is the size of such a chunk.
            Try varying it if you meet audio problems (but you shouldn't
            have to).

        nbytes:
            Number of bytes to encode the sound: 1 for 8bit sound, 2 for
            16bit, 4 for 32bit sound. 2 bytes is fine.

        audio_flag, video_flag:
            Instances of class threading events that are used to synchronize
            video and audio during ``VideoClip.preview()``.
        """
        ffplay_audiopreview(
            clip=self,
            fps=fps,
            buffersize=buffersize,
            nbytes=nbytes,
            audio_flag=audio_flag,
            video_flag=video_flag,
        )

    def __add__(self, other):
        if isinstance(other, AudioClip):
            return concatenate_audioclips([self, other])
        return super(AudioClip, self).__add__(other)


class AudioArrayClip(AudioClip):
    """

    An audio clip made from a sound array.

    Parameters
    ----------

    array
      A Numpy array representing the sound, of size Nx1 for mono,
      Nx2 for stereo.

    fps
      Frames per second : speed at which the sound is supposed to be
      played.

    """

    def __init__(self, array, fps):
        Clip.__init__(self)
        self.array = array
        self.fps = fps
        self.duration = 1.0 * len(array) / fps

        def frame_function(t):
            """Complicated, but must be able to handle the case where t
            is a list of the form sin(t).
            """
            if isinstance(t, np.ndarray):
                array_inds = np.round(self.fps * t).astype(int)
                in_array = (array_inds >= 0) & (array_inds < len(self.array))
                result = np.zeros((len(t), 2))
                result[in_array] = self.array[array_inds[in_array]]
                return result
            else:
                i = int(self.fps * t)
                if i < 0 or i >= len(self.array):
                    return 0 * self.array[0]
                else:
                    return self.array[i]

        self.frame_function = frame_function
        self.nchannels = len(list(self.get_frame(0)))


class CompositeAudioClip(AudioClip):
    """Clip made by composing several AudioClips.

    An audio clip made by putting together several audio clips.

    Parameters
    ----------

    clips
      List of audio clips, which may start playing at different times or
      together, depends on their ``start`` attributes. If all have their
      ``duration`` attribute set, the duration of the composite clip is
      computed automatically.
    """

    def __init__(self, clips):
        self.clips = clips
        self.nchannels = max(clip.nchannels for clip in self.clips)

        # self.duration is set at AudioClip
        duration = None
        for end in self.ends:
            if end is None:
                break
            duration = max(end, duration or 0)

        # self.fps is set at AudioClip
        fps = None
        for clip in self.clips:
            if hasattr(clip, "fps") and isinstance(clip.fps, numbers.Number):
                fps = max(clip.fps, fps or 0)

        super().__init__(duration=duration, fps=fps)

    @property
    def starts(self):
        """Returns starting times for all clips in the composition."""
        return (clip.start for clip in self.clips)

    @property
    def ends(self):
        """Returns ending times for all clips in the composition."""
        return (clip.end for clip in self.clips)

    def frame_function(self, t):
        """Renders a frame for the composition for the time ``t``."""
        played_parts = [clip.is_playing(t) for clip in self.clips]

        sounds = [
            clip.get_frame(t - clip.start) * np.array([part]).T
            for clip, part in zip(self.clips, played_parts)
            if (part is not False)
        ]

        if isinstance(t, np.ndarray):
            zero = np.zeros((len(t), self.nchannels))
        else:
            zero = np.zeros(self.nchannels)

        return zero + sum(sounds)


def concatenate_audioclips(clips):
    """Concatenates one AudioClip after another, in the order that are passed
    to ``clips`` parameter.

    Parameters
    ----------

    clips
      List of audio clips, which will be played one after other.
    """
    # start, end/start2, end2/start3... end
    starts_end = np.cumsum([0, *[clip.duration for clip in clips]])
    newclips = [clip.with_start(t) for clip, t in zip(clips, starts_end[:-1])]

    return CompositeAudioClip(newclips).with_duration(starts_end[-1])
````

## File: moviepy/video/compositing/__init__.py
````python
"""All for compositing video clips."""
````

## File: moviepy/video/compositing/CompositeVideoClip.py
````python
"""Main video composition interface of MoviePy."""

from functools import reduce

import numpy as np
from PIL import Image

from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.video.VideoClip import ColorClip, VideoClip


class CompositeVideoClip(VideoClip):
    """
    A VideoClip made of other videoclips displayed together. This is the
    base class for most compositions.

    Parameters
    ----------

    size
      The size (width, height) of the final clip.

    clips
      A list of videoclips.

      Clips with a higher ``layer`` attribute will be displayed
      on top of other clips in a lower layer.
      If two or more clips share the same ``layer``,
      then the one appearing latest in ``clips`` will be displayed
      on top (i.e. it has the higher layer).

      For each clip:

      - The attribute ``pos`` determines where the clip is placed.
          See ``VideoClip.set_pos``
      - The mask of the clip determines which parts are visible.

      Finally, if all the clips in the list have their ``duration``
      attribute set, then the duration of the composite video clip
      is computed automatically

    bg_color
      Color for the unmasked and unfilled regions. Set to None for these
      regions to be transparent (will be slower).
      Default is black (0, 0, 0).

    use_bgclip
      Set to True if the first clip in the list should be used as the
      'background' on which all other clips are blitted. That first clip must
      have the same size as the final clip. If it has no transparency, the final
      clip will have no mask.

    The clip with the highest FPS will be the FPS of the composite clip.

    """

    def __init__(
        self, clips, size=None, bg_color=(0, 0, 0), use_bgclip=False, is_mask=False
    ):
        if size is None:
            size = clips[0].size

        if use_bgclip and (clips[0].mask is None):
            transparent = False
        else:
            transparent = True if bg_color is None else False

        # If we must not use first clip as background and we dont have a color
        # we generate a black background if clip should not be transparent and
        # a transparent background if transparent
        if (not use_bgclip) and bg_color is None:
            if transparent:
                bg_color = 0.0 if is_mask else (0, 0, 0, 0)
            else:
                bg_color = 0.0 if is_mask else (0, 0, 0)

        fpss = [clip.fps for clip in clips if getattr(clip, "fps", None)]
        self.fps = max(fpss) if fpss else None

        VideoClip.__init__(self)

        self.size = size
        self.is_mask = is_mask
        self.clips = clips
        self.bg_color = bg_color

        # Use first clip as background if necessary, else use color
        # either set by user or previously generated
        if use_bgclip:
            self.bg = clips[0]
            self.clips = clips[1:]
            self.created_bg = False
        else:
            self.clips = clips
            self.bg = ColorClip(size, color=self.bg_color, is_mask=is_mask)
            self.created_bg = True

        # order self.clips by layer
        self.clips = sorted(self.clips, key=lambda clip: clip.layer_index)

        # compute duration
        ends = [clip.end for clip in self.clips]
        if None not in ends:
            duration = max(ends)
            self.duration = duration
            self.end = duration

        # compute audio
        audioclips = [v.audio for v in self.clips if v.audio is not None]
        if audioclips:
            self.audio = CompositeAudioClip(audioclips)

        # compute mask if necessary
        if transparent:
            maskclips = [
                (clip.mask if (clip.mask is not None) else clip.with_mask().mask)
                .with_position(clip.pos)
                .with_end(clip.end)
                .with_start(clip.start, change_end=False)
                .with_layer_index(clip.layer_index)
                for clip in self.clips
            ]

            if use_bgclip and self.bg.mask:
                maskclips = [self.bg.mask] + maskclips

            self.mask = CompositeVideoClip(
                maskclips, self.size, is_mask=True, bg_color=0.0
            )

    def frame_function(self, t):
        """The clips playing at time `t` are blitted over one another."""
        # For the mask we recalculate the final transparency we'll need
        # to apply on the result image
        if self.is_mask:
            mask = np.zeros((self.size[1], self.size[0]), dtype=float)
            for clip in self.playing_clips(t):
                mask = clip.compose_mask(mask, t)

            return mask

        # Try doing clip merging with pillow
        bg_t = t - self.bg.start
        bg_frame = self.bg.get_frame(bg_t).astype("uint8")
        bg_img = Image.fromarray(bg_frame)

        if self.bg.mask:
            bgm_t = t - self.bg.mask.start
            bg_mask = (self.bg.mask.get_frame(bgm_t) * 255).astype("uint8")
            bg_mask_img = Image.fromarray(bg_mask).convert("L")

            # Resize bg_mask_img to match bg_img, always use top left corner
            if bg_mask_img.size != bg_img.size:
                mask_width, mask_height = bg_mask_img.size
                img_width, img_height = bg_img.size

                if mask_width > img_width or mask_height > img_height:
                    bg_mask_img = bg_mask_img.crop((0, 0, img_width, img_height))
                else:
                    new_mask = Image.new("L", (img_width, img_height), 0)
                    new_mask.paste(bg_mask_img, (0, 0))
                    bg_mask_img = new_mask

            bg_img = bg_img.convert("RGBA")
            bg_img.putalpha(bg_mask_img)

        # For each clip apply on top of current img
        current_img = bg_img
        for clip in self.playing_clips(t):
            current_img = clip.compose_on(current_img, t)

        # Turn Pillow image into a numpy array
        # force contigous for perfs
        frame = np.ascontiguousarray(current_img)

        # If frame have transparency, remove it
        # our mask will take care of it during rendering
        if frame.shape[2] == 4:
            # Manual copy is more performent than np copy
            # and ensure C order for later rendering
            h, w = frame.shape[:2]
            rgb = np.empty((h, w, 3), dtype=frame.dtype, order="C")
            rgb[..., 0] = frame[..., 0]
            rgb[..., 1] = frame[..., 1]
            rgb[..., 2] = frame[..., 2]

            del frame
            return rgb

        return frame

    def playing_clips(self, t=0):
        """Returns a list of the clips in the composite clips that are
        actually playing at the given time `t`.
        """
        return [clip for clip in self.clips if clip.is_playing(t)]

    def close(self):
        """Closes the instance, releasing all the resources."""
        if self.created_bg and self.bg:
            # Only close the background clip if it was locally created.
            # Otherwise, it remains the job of whoever created it.
            self.bg.close()
            self.bg = None
        if hasattr(self, "audio") and self.audio:
            self.audio.close()
            self.audio = None


def clips_array(array, rows_widths=None, cols_heights=None, bg_color=None):
    """Given a matrix whose rows are clips, creates a CompositeVideoClip where
    all clips are placed side by side horizontally for each clip in each row
    and one row on top of the other for each row. So given next matrix of clips
    with same size:

    ```python
    clips_array([[clip1, clip2, clip3], [clip4, clip5, clip6]])
    ```

    the result will be a CompositeVideoClip with a layout displayed like:

    ```
    ┏━━━━━━━┳━━━━━━━┳━━━━━━━┓
    ┃       ┃       ┃       ┃
    ┃ clip1 ┃ clip2 ┃ clip3 ┃
    ┃       ┃       ┃       ┃
    ┣━━━━━━━╋━━━━━━━╋━━━━━━━┫
    ┃       ┃       ┃       ┃
    ┃ clip4 ┃ clip5 ┃ clip6 ┃
    ┃       ┃       ┃       ┃
    ┗━━━━━━━┻━━━━━━━┻━━━━━━━┛
    ```

    If some clips doesn't fulfill the space required by the rows or columns
    in which are placed, that space will be filled by the color defined in
    ``bg_color``.

    array
      Matrix of clips included in the returned composited video clip.

    rows_widths
      Widths of the different rows in pixels. If ``None``, is set automatically.

    cols_heights
      Heights of the different columns in pixels. If ``None``, is set automatically.

    bg_color
       Fill color for the masked and unfilled regions. Set to ``None`` for these
       regions to be transparent (processing will be slower).
    """
    array = np.array(array)
    sizes_array = np.array([[clip.size for clip in line] for line in array])

    # find row width and col_widths automatically if not provided
    if rows_widths is None:
        rows_widths = sizes_array[:, :, 1].max(axis=1)
    if cols_heights is None:
        cols_heights = sizes_array[:, :, 0].max(axis=0)

    # compute start positions of X for rows and Y for columns
    xs = np.cumsum([0] + list(cols_heights))
    ys = np.cumsum([0] + list(rows_widths))

    for j, (x, ch) in enumerate(zip(xs[:-1], cols_heights)):
        for i, (y, rw) in enumerate(zip(ys[:-1], rows_widths)):
            clip = array[i, j]
            w, h = clip.size
            # if clip not fulfill row width or column height
            if (w < ch) or (h < rw):
                clip = CompositeVideoClip(
                    [clip.with_position("center")], size=(ch, rw), bg_color=bg_color
                ).with_duration(clip.duration)

            array[i, j] = clip.with_position((x, y))

    return CompositeVideoClip(array.flatten(), size=(xs[-1], ys[-1]), bg_color=bg_color)


def concatenate_videoclips(
    clips, method="chain", transition=None, bg_color=None, is_mask=False, padding=0
):
    """Concatenates several video clips.

    Returns a video clip made by clip by concatenating several video clips.
    (Concatenated means that they will be played one after another).

    There are two methods:

    - method="chain": will produce a clip that simply outputs
      the frames of the successive clips, without any correction if they are
      not of the same size of anything. If none of the clips have masks the
      resulting clip has no mask, else the mask is a concatenation of masks
      (using completely opaque for clips that don't have masks, obviously).
      If you have clips of different size and you want to write directly the
      result of the concatenation to a file, use the method "compose" instead.

    - method="compose", if the clips do not have the same resolution, the final
      resolution will be such that no clip has to be resized.
      As a consequence the final clip has the height of the highest clip and the
      width of the widest clip of the list. All the clips with smaller dimensions
      will appear centered. The border will be transparent if mask=True, else it
      will be of the color specified by ``bg_color``.

    The clip with the highest FPS will be the FPS of the result clip.

    Parameters
    ----------
    clips
      A list of video clips which must all have their ``duration``
      attributes set.
    method
      "chain" or "compose": see above.
    transition
      A clip that will be played between each two clips of the list.

    bg_color
      Only for method='compose'. Color of the background.
      Set to None for a transparent clip

    padding
      Only for method='compose'. Duration during two consecutive clips.
      Note that for negative padding, a clip will partly play at the same
      time as the clip it follows (negative padding is cool for clips who fade
      in on one another). A non-null padding automatically sets the method to
      `compose`.

    """
    if transition is not None:
        clip_transition_pairs = [[v, transition] for v in clips[:-1]]
        clips = reduce(lambda x, y: x + y, clip_transition_pairs) + [clips[-1]]
        transition = None

    timings = np.cumsum([0] + [clip.duration for clip in clips])

    sizes = [clip.size for clip in clips]

    w = max(size[0] for size in sizes)
    h = max(size[1] for size in sizes)

    timings = np.maximum(0, timings + padding * np.arange(len(timings)))
    timings[-1] -= padding  # Last element is the duration of the whole

    if method == "chain":

        def frame_function(t):
            i = max([i for i, e in enumerate(timings) if e <= t])
            return clips[i].get_frame(t - timings[i])

        def get_mask(clip):
            mask = clip.mask or ColorClip(clip.size, color=1, is_mask=True)
            if mask.duration is None:
                mask.duration = clip.duration
            return mask

        result = VideoClip(is_mask=is_mask, frame_function=frame_function)
        if any([clip.mask is not None for clip in clips]):
            masks = [get_mask(clip) for clip in clips]
            result.mask = concatenate_videoclips(masks, method="chain", is_mask=True)
            result.clips = clips
    elif method == "compose":
        result = CompositeVideoClip(
            [
                clip.with_start(t).with_position("center")
                for (clip, t) in zip(clips, timings)
            ],
            size=(w, h),
            bg_color=bg_color,
            is_mask=is_mask,
        )
    else:
        raise Exception(
            "MoviePy Error: The 'method' argument of "
            "concatenate_videoclips must be 'chain' or 'compose'"
        )

    result.timings = timings

    result.start_times = timings[:-1]
    result.start, result.duration, result.end = 0, timings[-1], timings[-1]

    audio_t = [
        (clip.audio, t) for clip, t in zip(clips, timings) if clip.audio is not None
    ]
    if audio_t:
        result.audio = CompositeAudioClip(
            [a.with_start(t) for a, t in audio_t]
        ).with_duration(result.duration)

    fpss = [clip.fps for clip in clips if getattr(clip, "fps", None) is not None]
    result.fps = max(fpss) if fpss else None
    return result
````

## File: moviepy/video/fx/__init__.py
````python
"""All the visual effects that can be applied to VideoClip."""

# import every video fx function

from moviepy.video.fx.AccelDecel import AccelDecel
from moviepy.video.fx.BlackAndWhite import BlackAndWhite
from moviepy.video.fx.Blink import Blink
from moviepy.video.fx.Crop import Crop
from moviepy.video.fx.CrossFadeIn import CrossFadeIn
from moviepy.video.fx.CrossFadeOut import CrossFadeOut
from moviepy.video.fx.EvenSize import EvenSize
from moviepy.video.fx.FadeIn import FadeIn
from moviepy.video.fx.FadeOut import FadeOut
from moviepy.video.fx.Freeze import Freeze
from moviepy.video.fx.FreezeRegion import FreezeRegion
from moviepy.video.fx.GammaCorrection import GammaCorrection
from moviepy.video.fx.HeadBlur import HeadBlur
from moviepy.video.fx.InvertColors import InvertColors
from moviepy.video.fx.Loop import Loop
from moviepy.video.fx.LumContrast import LumContrast
from moviepy.video.fx.MakeLoopable import MakeLoopable
from moviepy.video.fx.Margin import Margin
from moviepy.video.fx.MaskColor import MaskColor
from moviepy.video.fx.MasksAnd import MasksAnd
from moviepy.video.fx.MasksOr import MasksOr
from moviepy.video.fx.MirrorX import MirrorX
from moviepy.video.fx.MirrorY import MirrorY
from moviepy.video.fx.MultiplyColor import MultiplyColor
from moviepy.video.fx.MultiplySpeed import MultiplySpeed
from moviepy.video.fx.Painting import Painting
from moviepy.video.fx.Resize import Resize
from moviepy.video.fx.Rotate import Rotate
from moviepy.video.fx.Scroll import Scroll
from moviepy.video.fx.SlideIn import SlideIn
from moviepy.video.fx.SlideOut import SlideOut
from moviepy.video.fx.SuperSample import SuperSample
from moviepy.video.fx.TimeMirror import TimeMirror
from moviepy.video.fx.TimeSymmetrize import TimeSymmetrize


__all__ = (
    "AccelDecel",
    "BlackAndWhite",
    "Blink",
    "Crop",
    "CrossFadeIn",
    "CrossFadeOut",
    "EvenSize",
    "FadeIn",
    "FadeOut",
    "Freeze",
    "FreezeRegion",
    "GammaCorrection",
    "HeadBlur",
    "InvertColors",
    "Loop",
    "LumContrast",
    "MakeLoopable",
    "Margin",
    "MasksAnd",
    "MaskColor",
    "MasksOr",
    "MirrorX",
    "MirrorY",
    "MultiplyColor",
    "MultiplySpeed",
    "Painting",
    "Resize",
    "Rotate",
    "Scroll",
    "SlideIn",
    "SlideOut",
    "SuperSample",
    "TimeMirror",
    "TimeSymmetrize",
)
````

## File: moviepy/video/fx/AccelDecel.py
````python
from dataclasses import dataclass

from moviepy.Effect import Effect


@dataclass
class AccelDecel(Effect):
    """Accelerates and decelerates a clip, useful for GIF making.

    Parameters
    ----------

    new_duration : float
      Duration for the new transformed clip. If None, will be that of the
      current clip.

    abruptness : float
      Slope shape in the acceleration-deceleration function. It will depend
      on the value of the parameter:

      * ``-1 < abruptness < 0``: speed up, down, up.
      * ``abruptness == 0``: no effect.
      * ``abruptness > 0``: speed down, up, down.

    soonness : float
      For positive abruptness, determines how soon the transformation occurs.
      Should be a positive number.

    Raises
    ------

    ValueError
      When ``sooness`` argument is lower than 0.

    Examples
    --------

    The following graphs show functions generated by different combinations
    of arguments, where the value of the slopes represents the speed of the
    videos generated, being the linear function (in red) a combination that
    does not produce any transformation.

    .. image:: /_static/medias/accel_decel-fx-params.png
      :alt: acced_decel FX parameters combinations
    """

    new_duration: float = None
    abruptness: float = 1.0
    soonness: float = 1.0

    def _f_accel_decel(
        self, t, old_duration, new_duration, abruptness=1.0, soonness=1.0
    ):
        a = 1.0 + abruptness

        def _f(t):
            def f1(t):
                return (0.5) ** (1 - a) * (t**a)

            def f2(t):
                return 1 - f1(1 - t)

            return (t < 0.5) * f1(t) + (t >= 0.5) * f2(t)

        return old_duration * _f((t / new_duration) ** soonness)

    def apply(self, clip):
        """Apply the effect to the clip."""
        if self.new_duration is None:
            self.new_duration = clip.duration

        if self.soonness < 0:
            raise ValueError("'sooness' should be a positive number")

        return clip.time_transform(
            lambda t: self._f_accel_decel(
                t=t,
                old_duration=clip.duration,
                new_duration=self.new_duration,
                abruptness=self.abruptness,
                soonness=self.soonness,
            )
        ).with_duration(self.new_duration)
````

## File: moviepy/video/fx/BlackAndWhite.py
````python
from dataclasses import dataclass

import numpy as np

from moviepy.Effect import Effect


@dataclass
class BlackAndWhite(Effect):
    """Desaturates the picture, makes it black and white.
    Parameter RGB allows to set weights for the different color
    channels.
    If RBG is 'CRT_phosphor' a special set of values is used.
    preserve_luminosity maintains the sum of RGB to 1.
    """

    RGB: str = None
    preserve_luminosity: bool = True

    def apply(self, clip):
        """Apply the effect to the clip."""
        if self.RGB is None:
            self.RGB = [1, 1, 1]

        if self.RGB == "CRT_phosphor":
            self.RGB = [0.2125, 0.7154, 0.0721]

        R, G, B = (
            1.0
            * np.array(self.RGB)
            / (sum(self.RGB) if self.preserve_luminosity else 1)
        )

        def filter(im):
            im = R * im[:, :, 0] + G * im[:, :, 1] + B * im[:, :, 2]
            return np.dstack(3 * [im]).astype("uint8")

        return clip.image_transform(filter)
````

## File: moviepy/video/fx/Blink.py
````python
from dataclasses import dataclass

from moviepy.Effect import Effect


@dataclass
class Blink(Effect):
    """
    Makes the clip blink. At each blink it will be displayed ``duration_on``
    seconds and disappear ``duration_off`` seconds. Will only work in
    composite clips.
    """

    duration_on: float
    duration_off: float

    def apply(self, clip):
        """Apply the effect to the clip."""
        if clip.mask is None:
            clip = clip.with_mask()

        duration = self.duration_on + self.duration_off
        clip.mask = clip.mask.transform(
            lambda get_frame, t: get_frame(t) * ((t % duration) < self.duration_on)
        )

        return clip
````

## File: moviepy/video/fx/Crop.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class Crop(Effect):
    """Effect to crop a clip to get a new clip in which just a rectangular
    subregion of the original clip is conserved. `x1,y1` indicates the top left
    corner and `x2,y2` is the lower right corner of the cropped region. All
    coordinates are in pixels. Float numbers are accepted.

    To crop an arbitrary rectangle:

    >>> Crop(x1=50, y1=60, x2=460, y2=275)

    Only remove the part above y=30:

    >>> Crop(y1=30)

    Crop a rectangle that starts 10 pixels left and is 200px wide

    >>> Crop(x1=10, width=200)

    Crop a rectangle centered in x,y=(300,400), width=50, height=150 :

    >>> Crop(x_center=300, y_center=400, width=50, height=150)

    Any combination of the above should work, like for this rectangle
    centered in x=300, with explicit y-boundaries:

    >>> Crop(x_center=300, width=400, y1=100, y2=600)

    """

    x1: int = None
    y1: int = None
    x2: int = None
    y2: int = None
    width: int = None
    height: int = None
    x_center: int = None
    y_center: int = None

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if self.width and self.x1 is not None:
            self.x2 = self.x1 + self.width
        elif self.width and self.x2 is not None:
            self.x1 = self.x2 - self.width

        if self.height and self.y1 is not None:
            self.y2 = self.y1 + self.height
        elif self.height and self.y2 is not None:
            self.y1 = self.y2 - self.height

        if self.x_center:
            self.x1, self.x2 = (
                self.x_center - self.width / 2,
                self.x_center + self.width / 2,
            )

        if self.y_center:
            self.y1, self.y2 = (
                self.y_center - self.height / 2,
                self.y_center + self.height / 2,
            )

        self.x1 = self.x1 or 0
        self.y1 = self.y1 or 0
        self.x2 = self.x2 or clip.size[0]
        self.y2 = self.y2 or clip.size[1]

        return clip.image_transform(
            lambda frame: frame[
                int(self.y1) : int(self.y2), int(self.x1) : int(self.x2)
            ],
            apply_to=["mask"],
        )
````

## File: moviepy/video/fx/CrossFadeIn.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect
from moviepy.video.fx.FadeIn import FadeIn


@dataclass
class CrossFadeIn(Effect):
    """Makes the clip appear progressively, over ``duration`` seconds.
    Only works when the clip is included in a CompositeVideoClip.
    """

    duration: float

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if clip.duration is None:
            raise ValueError("Attribute 'duration' not set")

        if clip.mask is None:
            clip = clip.with_mask()

        clip.mask.duration = clip.duration
        clip.mask = clip.mask.with_effects([FadeIn(self.duration)])

        return clip
````

## File: moviepy/video/fx/CrossFadeOut.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect
from moviepy.video.fx.FadeOut import FadeOut


@dataclass
class CrossFadeOut(Effect):
    """Makes the clip disappear progressively, over ``duration`` seconds.
    Only works when the clip is included in a CompositeVideoClip.
    """

    duration: float

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if clip.duration is None:
            raise ValueError("Attribute 'duration' not set")

        if clip.mask is None:
            clip = clip.with_mask()

        clip.mask.duration = clip.duration
        clip.mask = clip.mask.with_effects([FadeOut(self.duration)])

        return clip
````

## File: moviepy/video/fx/EvenSize.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class EvenSize(Effect):
    """Crops the clip to make dimensions even."""

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        w, h = clip.size
        w_even = w % 2 == 0
        h_even = h % 2 == 0
        if w_even and h_even:
            return clip

        if not w_even and not h_even:

            def image_filter(a):
                return a[:-1, :-1, :]

        elif h_even:

            def image_filter(a):
                return a[:, :-1, :]

        else:

            def image_filter(a):
                return a[:-1, :, :]

        return clip.image_transform(image_filter, apply_to=["mask"])
````

## File: moviepy/video/fx/FadeIn.py
````python
from dataclasses import dataclass

import numpy as np

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class FadeIn(Effect):
    """Makes the clip progressively appear from some color (black by default),
    over ``duration`` seconds at the beginning of the clip. Can be used for
    masks too, where the initial color must be a number between 0 and 1.

    For cross-fading (progressive appearance or disappearance of a clip
    over another clip, see ``CrossFadeIn``
    """

    duration: float
    initial_color: list = None

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if self.initial_color is None:
            self.initial_color = 0 if clip.is_mask else [0, 0, 0]

        self.initial_color = np.array(self.initial_color)

        def filter(get_frame, t):
            if t >= self.duration:
                return get_frame(t)
            else:
                fading = 1.0 * t / self.duration
                return fading * get_frame(t) + (1 - fading) * self.initial_color

        return clip.transform(filter)
````

## File: moviepy/video/fx/FadeOut.py
````python
from dataclasses import dataclass

import numpy as np

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class FadeOut(Effect):
    """Makes the clip progressively fade to some color (black by default),
    over ``duration`` seconds at the end of the clip. Can be used for masks too,
    where the final color must be a number between 0 and 1.

    For cross-fading (progressive appearance or disappearance of a clip over another
    clip), see ``CrossFadeOut``
    """

    duration: float
    final_color: list = None

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if clip.duration is None:
            raise ValueError("Attribute 'duration' not set")

        if self.final_color is None:
            self.final_color = 0 if clip.is_mask else [0, 0, 0]

        self.final_color = np.array(self.final_color)

        def filter(get_frame, t):
            if (clip.duration - t) >= self.duration:
                return get_frame(t)
            else:
                fading = 1.0 * (clip.duration - t) / self.duration
                return fading * get_frame(t) + (1 - fading) * self.final_color

        return clip.transform(filter)
````

## File: moviepy/video/fx/Freeze.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect
from moviepy.video.compositing.CompositeVideoClip import concatenate_videoclips


@dataclass
class Freeze(Effect):
    """Momentarily freeze the clip at time t.

    Set `t='end'` to freeze the clip at the end (actually it will freeze on the
    frame at time clip.duration - padding_end seconds - 1 / clip_fps).
    With ``duration`` you can specify the duration of the freeze.
    With ``total_duration`` you can specify the total duration of
    the clip and the freeze (i.e. the duration of the freeze is
    automatically computed). One of them must be provided.

    With ``update_start_end`` you can define if the effect must preserve
    and/or update start and end properties of the original clip
    """

    t: float = 0
    freeze_duration: float = None
    total_duration: float = None
    padding_end: float = 0
    update_start_end: bool = True

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if clip.duration is None:
            raise ValueError("Attribute 'duration' not set")

        if self.t == "end":
            self.t = clip.duration - self.padding_end - 1 / clip.fps

        if self.freeze_duration is None:
            if self.total_duration is None:
                raise ValueError(
                    "You must provide either 'freeze_duration' or 'total_duration'"
                )
            self.freeze_duration = self.total_duration - clip.duration

        before = [clip[: self.t]] if (self.t != 0) else []
        freeze = [clip.to_ImageClip(self.t).with_duration(self.freeze_duration)]
        after = [clip[self.t :]] if (self.t != clip.duration) else []

        new_clip = concatenate_videoclips(before + freeze + after)
        if self.update_start_end:
            if clip.start is not None:
                new_clip = new_clip.with_start(clip.start)
            if clip.end is not None:
                new_clip = new_clip.with_end(clip.end + self.freeze_duration)

        return new_clip
````

## File: moviepy/video/fx/FreezeRegion.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.Crop import Crop


@dataclass
class FreezeRegion(Effect):
    """Freezes one region of the clip while the rest remains animated.

    You can choose one of three methods by providing either `region`,
    `outside_region`, or `mask`.

    Parameters
    ----------

    t
      Time at which to freeze the freezed region.

    region
      A tuple (x1, y1, x2, y2) defining the region of the screen (in pixels)
      which will be freezed. You can provide outside_region or mask instead.

    outside_region
      A tuple (x1, y1, x2, y2) defining the region of the screen (in pixels)
      which will be the only non-freezed region.

    mask
      If not None, will overlay a freezed version of the clip on the current clip,
      with the provided mask. In other words, the "visible" pixels in the mask
      indicate the freezed region in the final picture.

    """

    t: float = 0
    region: tuple = None
    outside_region: tuple = None
    mask: Clip = None

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if self.region is not None:
            x1, y1, _x2, _y2 = self.region
            freeze = (
                clip.with_effects([Crop(*self.region)])
                .to_ImageClip(t=self.t)
                .with_duration(clip.duration)
                .with_position((x1, y1))
            )
            return CompositeVideoClip([clip, freeze])

        elif self.outside_region is not None:
            x1, y1, x2, y2 = self.outside_region
            animated_region = clip.with_effects(
                [Crop(*self.outside_region)]
            ).with_position((x1, y1))
            freeze = clip.to_ImageClip(t=self.t).with_duration(clip.duration)
            return CompositeVideoClip([freeze, animated_region])

        elif self.mask is not None:
            freeze = (
                clip.to_ImageClip(t=self.t)
                .with_duration(clip.duration)
                .with_mask(self.mask)
            )
            return CompositeVideoClip([clip, freeze])
````

## File: moviepy/video/fx/GammaCorrection.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class GammaCorrection(Effect):
    """Gamma-correction of a video clip."""

    gamma: float

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""

        def filter(im):
            corrected = 255 * (1.0 * im / 255) ** self.gamma
            return corrected.astype("uint8")

        return clip.image_transform(filter)
````

## File: moviepy/video/fx/HeadBlur.py
````python
from dataclasses import dataclass

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class HeadBlur(Effect):
    """Returns a filter that will blur a moving part (a head ?) of the frames.

    The position of the blur at time t is defined by (fx(t), fy(t)), the radius
    of the blurring by ``radius`` and the intensity of the blurring by ``intensity``.
    """

    fx: callable
    fy: callable
    radius: float
    intensity: float = None

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if self.intensity is None:
            self.intensity = int(2 * self.radius / 3)

        def filter(gf, t):
            im = gf(t).copy()
            h, w, d = im.shape
            x, y = int(self.fx(t)), int(self.fy(t))
            x1, x2 = max(0, x - self.radius), min(x + self.radius, w)
            y1, y2 = max(0, y - self.radius), min(y + self.radius, h)

            image = Image.fromarray(im)
            mask = Image.new("RGB", image.size)
            draw = ImageDraw.Draw(mask)
            draw.ellipse([x1, y1, x2, y2], fill=(255, 255, 255))

            blurred = image.filter(ImageFilter.GaussianBlur(radius=self.intensity))

            res = np.where(np.array(mask) > 0, np.array(blurred), np.array(image))
            return res

        return clip.transform(filter)
````

## File: moviepy/video/fx/InvertColors.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class InvertColors(Effect):
    """Returns the color-inversed clip.

    The values of all pixels are replaced with (255-v) or (1-v) for masks
    Black becomes white, green becomes purple, etc.
    """

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        maxi = 1.0 if clip.is_mask else 255
        return clip.image_transform(lambda f: maxi - f)
````

## File: moviepy/video/fx/Loop.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class Loop(Effect):
    """
    Returns a clip that plays the current clip in an infinite loop.
    Ideal for clips coming from GIFs.

    Parameters
    ----------

    n
      Number of times the clip should be played. If `None` the
      the clip will loop indefinitely (i.e. with no set duration).

    duration
      Total duration of the clip. Can be specified instead of n.
    """

    n: int = None
    duration: float = None

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if clip.duration is None:
            raise ValueError("Attribute 'duration' not set")

        previous_duration = clip.duration
        clip = clip.time_transform(
            lambda t: t % previous_duration, apply_to=["mask", "audio"]
        )

        if self.n:
            self.duration = self.n * previous_duration

        if self.duration:
            clip = clip.with_duration(self.duration)

        return clip
````

## File: moviepy/video/fx/LumContrast.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class LumContrast(Effect):
    """Luminosity-contrast correction of a clip."""

    lum: float = 0
    contrast: float = 0
    contrast_threshold: float = 127

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""

        def image_filter(im):
            im = 1.0 * im  # float conversion
            corrected = (
                im + self.lum + self.contrast * (im - float(self.contrast_threshold))
            )
            corrected[corrected < 0] = 0
            corrected[corrected > 255] = 255
            return corrected.astype("uint8")

        return clip.image_transform(image_filter)
````

## File: moviepy/video/fx/MakeLoopable.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.CrossFadeIn import CrossFadeIn


@dataclass
class MakeLoopable(Effect):
    """Makes the clip fade in progressively at its own end, this way it can be
    looped indefinitely.

    Parameters
    ----------

    overlap_duration : float
      Duration of the fade-in (in seconds).
    """

    overlap_duration: float

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        clip2 = clip.with_effects([CrossFadeIn(self.overlap_duration)]).with_start(
            clip.duration - self.overlap_duration
        )
        return CompositeVideoClip([clip, clip2]).subclipped(
            self.overlap_duration, clip.duration
        )
````

## File: moviepy/video/fx/Margin.py
````python
from dataclasses import dataclass

import numpy as np

from moviepy.Clip import Clip
from moviepy.Effect import Effect
from moviepy.video.VideoClip import ImageClip


@dataclass
class Margin(Effect):
    """Draws an external margin all around the frame.

    Parameters
    ----------

    margin_size : int, optional
      If not ``None``, then the new clip has a margin size of
      size ``margin_size`` in pixels on the left, right, top, and bottom.

    left : int, optional
      If ``margin_size=None``, margin size for the new clip in left direction.

    right : int, optional
      If ``margin_size=None``, margin size for the new clip in right direction.

    top : int, optional
      If ``margin_size=None``, margin size for the new clip in top direction.

    bottom : int, optional
      If ``margin_size=None``, margin size for the new clip in bottom direction.

    color : tuple, optional
      Color of the margin.

    opacity : float, optional
      Opacity of the margin. Setting this value to 0 yields transparent margins.
    """

    margin_size: int = None
    left: int = 0
    right: int = 0
    top: int = 0
    bottom: int = 0
    color: tuple = (0, 0, 0)
    opacity: float = 1.0

    def add_margin(self, clip: Clip):
        """Add margins to the clip."""
        if (self.opacity != 1.0) and (clip.mask is None) and not (clip.is_mask):
            clip = clip.with_mask()

        if self.margin_size is not None:
            self.left = self.right = self.top = self.bottom = self.margin_size

        def make_bg(w, h):
            new_w, new_h = w + self.left + self.right, h + self.top + self.bottom
            if clip.is_mask:
                shape = (new_h, new_w)
                bg = np.tile(self.opacity, (new_h, new_w)).astype(float).reshape(shape)
            else:
                shape = (new_h, new_w, 3)
                bg = np.tile(self.color, (new_h, new_w)).reshape(shape)
            return bg

        if isinstance(clip, ImageClip):
            im = make_bg(clip.w, clip.h)
            im[self.top : self.top + clip.h, self.left : self.left + clip.w] = clip.img
            return clip.image_transform(lambda pic: im)

        else:

            def filter(get_frame, t):
                pic = get_frame(t)
                h, w = pic.shape[:2]
                im = make_bg(w, h)
                im[self.top : self.top + h, self.left : self.left + w] = pic
                return im

            return clip.transform(filter)

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        # We apply once on clip and once on mask if we have one
        clip = self.add_margin(clip=clip)

        if clip.mask:
            clip.mask = self.add_margin(clip=clip.mask)

        return clip
````

## File: moviepy/video/fx/MaskColor.py
````python
from dataclasses import dataclass

import numpy as np

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class MaskColor(Effect):
    """Returns a new clip with a mask for transparency where the original
    clip is of the given color.

    You can also have a "progressive" mask by specifying a non-null distance
    threshold ``threshold``. In this case, if the distance between a pixel and
    the given color is d, the transparency will be

    d**stiffness / (threshold**stiffness + d**stiffness)

    which is 1 when d>>threshold and 0 for d<<threshold, the stiffness of the
    effect being parametrized by ``stiffness``
    """

    color: tuple = (0, 0, 0)
    threshold: float = 0
    stiffness: float = 1

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        color = np.array(self.color)

        def hill(x):
            if self.threshold:
                return x**self.stiffness / (
                    self.threshold**self.stiffness + x**self.stiffness
                )
            else:
                return 1.0 * (x != 0)

        def flim(im):
            return hill(np.sqrt(((im - color) ** 2).sum(axis=2)))

        mask = clip.image_transform(flim)
        mask.is_mask = True
        return clip.with_mask(mask)
````

## File: moviepy/video/fx/MasksAnd.py
````python
from dataclasses import dataclass
from typing import Union

import numpy as np

from moviepy.Clip import Clip
from moviepy.Effect import Effect
from moviepy.video.VideoClip import ImageClip


@dataclass
class MasksAnd(Effect):
    """Returns the logical 'and' (minimum pixel color values) between two masks.

    The result has the duration of the clip to which has been applied, if it has any.

    Parameters
    ----------

    other_clip ImageClip or np.ndarray
      Clip used to mask the original clip.

    Examples
    --------

    .. code:: python

        clip = ColorClip(color=(255, 0, 0), size=(1, 1))      # red
        mask = ColorClip(color=(0, 255, 0), size=(1, 1))      # green
        masked_clip = clip.with_effects([vfx.MasksAnd(mask)]) # black
        masked_clip.get_frame(0)
        [[[0 0 0]]]
    """

    other_clip: Union[Clip, np.ndarray]

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        # to ensure that 'and' of two ImageClips will be an ImageClip
        if isinstance(self.other_clip, ImageClip):
            self.other_clip = self.other_clip.img

        if isinstance(self.other_clip, np.ndarray):
            return clip.image_transform(
                lambda frame: np.minimum(frame, self.other_clip)
            )
        else:
            return clip.transform(
                lambda get_frame, t: np.minimum(
                    get_frame(t), self.other_clip.get_frame(t)
                )
            )
````

## File: moviepy/video/fx/MasksOr.py
````python
from dataclasses import dataclass
from typing import Union

import numpy as np

from moviepy.Clip import Clip
from moviepy.Effect import Effect
from moviepy.video.VideoClip import ImageClip


@dataclass
class MasksOr(Effect):
    """Returns the logical 'or' (maximum pixel color values) between two masks.

    The result has the duration of the clip to which has been applied, if it has any.

    Parameters
    ----------

    other_clip ImageClip or np.ndarray
      Clip used to mask the original clip.

    Examples
    --------

    .. code:: python

        clip = ColorClip(color=(255, 0, 0), size=(1, 1))     # red
        mask = ColorClip(color=(0, 255, 0), size=(1, 1))     # green
        masked_clip = clip.with_effects([vfx.MasksOr(mask)]) # yellow
        masked_clip.get_frame(0)
        [[[255 255   0]]]
    """

    other_clip: Union[Clip, np.ndarray]

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        # to ensure that 'or' of two ImageClips will be an ImageClip
        if isinstance(self.other_clip, ImageClip):
            self.other_clip = self.other_clip.img

        if isinstance(self.other_clip, np.ndarray):
            return clip.image_transform(
                lambda frame: np.maximum(frame, self.other_clip)
            )
        else:
            return clip.transform(
                lambda get_frame, t: np.maximum(
                    get_frame(t), self.other_clip.get_frame(t)
                )
            )
````

## File: moviepy/video/fx/MirrorX.py
````python
from dataclasses import dataclass
from typing import List, Union

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class MirrorX(Effect):
    """Flips the clip horizontally (and its mask too, by default)."""

    apply_to: Union[List, str] = "mask"

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        return clip.image_transform(lambda img: img[:, ::-1], apply_to=self.apply_to)
````

## File: moviepy/video/fx/MirrorY.py
````python
from dataclasses import dataclass
from typing import List, Union

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class MirrorY(Effect):
    """Flips the clip vertically (and its mask too, by default)."""

    apply_to: Union[List, str] = "mask"

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        return clip.image_transform(lambda img: img[::-1], apply_to=self.apply_to)
````

## File: moviepy/video/fx/MultiplyColor.py
````python
from dataclasses import dataclass

import numpy as np

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class MultiplyColor(Effect):
    """
    Multiplies the clip's colors by the given factor, can be used
    to decrease or increase the clip's brightness (is that the
    right word ?)
    """

    factor: float

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        return clip.image_transform(
            lambda frame: np.minimum(255, (self.factor * frame)).astype("uint8")
        )
````

## File: moviepy/video/fx/MultiplySpeed.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class MultiplySpeed(Effect):
    """Returns a clip playing the current clip but at a speed multiplied by ``factor``.

    Instead of factor one can indicate the desired ``final_duration`` of the clip, and
    the factor will be automatically computed. The same effect is applied to the clip's
    audio and mask if any.
    """

    factor: float = None
    final_duration: float = None

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if self.final_duration:
            self.factor = 1.0 * clip.duration / self.final_duration

        new_clip = clip.time_transform(
            lambda t: self.factor * t, apply_to=["mask", "audio"]
        )

        if clip.duration is not None:
            new_clip = new_clip.with_duration(1.0 * clip.duration / self.factor)

        return new_clip
````

## File: moviepy/video/fx/Painting.py
````python
from dataclasses import dataclass

import numpy as np
from PIL import Image, ImageFilter

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class Painting(Effect):
    """Transforms any photo into some kind of painting.

    Transforms any photo into some kind of painting. Saturation
    tells at which point the colors of the result should be
    flashy. ``black`` gives the amount of black lines wanted.

    np_image : a numpy image
    """

    saturation: float = 1.4
    black: float = 0.006

    def to_painting(self, np_image, saturation=1.4, black=0.006):
        """Transforms any photo into some kind of painting.

        Transforms any photo into some kind of painting. Saturation
        tells at which point the colors of the result should be
        flashy. ``black`` gives the amount of black lines wanted.

        np_image : a numpy image
        """
        image = Image.fromarray(np_image)
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)

        # Convert the image to grayscale
        grayscale_image = image.convert("L")

        # Find the image edges
        edges_image = grayscale_image.filter(ImageFilter.FIND_EDGES)

        # Convert the edges image to a numpy array
        edges = np.array(edges_image)

        # Create the darkening effect
        darkening = black * (255 * np.dstack(3 * [edges]))

        # Apply the painting effect
        painting = saturation * np.array(image) - darkening

        # Clip the pixel values to the valid range of 0-255
        painting = np.maximum(0, np.minimum(255, painting))

        # Convert the pixel values to unsigned 8-bit integers
        painting = painting.astype("uint8")

        return painting

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        return clip.image_transform(
            lambda im: self.to_painting(im, self.saturation, self.black)
        )
````

## File: moviepy/video/fx/Resize.py
````python
import numbers
from dataclasses import dataclass
from typing import Union

import numpy as np
from PIL import Image

from moviepy.Effect import Effect


@dataclass
class Resize(Effect):
    """Effect returning a video clip that is a resized version of the clip.

    Parameters
    ----------

    new_size : tuple or float or function, optional
        Can be either
        - ``(width, height)`` in pixels or a float representing
        - A scaling factor, like ``0.5``.
        - A function of time returning one of these.

    height : int, optional
        Height of the new clip in pixels. The width is then computed so
        that the width/height ratio is conserved.

    width : int, optional
        Width of the new clip in pixels. The height is then computed so
        that the width/height ratio is conserved.

    Examples
    --------

    .. code:: python

        clip.with_effects([vfx.Resize((460,720))]) # New resolution: (460,720)
        clip.with_effects([vfx.Resize(0.6)]) # width and height multiplied by 0.6
        clip.with_effects([vfx.Resize(width=800)]) # height computed automatically.
        clip.with_effects([vfx.Resize(lambda t : 1+0.02*t)]) # slow clip swelling
    """

    new_size: Union[tuple, float, callable] = None
    height: int = None
    width: int = None
    apply_to_mask: bool = True

    def resizer(self, pic, new_size):
        """Resize the image using PIL."""
        new_size = list(map(int, new_size))
        pil_img = Image.fromarray(pic)
        resized_pil = pil_img.resize(new_size, Image.Resampling.LANCZOS)
        return np.array(resized_pil)

    def apply(self, clip):
        """Apply the effect to the clip."""
        w, h = clip.size

        if self.new_size is not None:

            def translate_new_size(new_size_):
                """Returns a [w, h] pair from `new_size_`. If `new_size_` is a
                scalar, then work out the correct pair using the clip's size.
                Otherwise just return `new_size_`
                """
                if isinstance(new_size_, numbers.Number):
                    return [new_size_ * w, new_size_ * h]
                else:
                    return new_size_

            if hasattr(self.new_size, "__call__"):
                # The resizing is a function of time

                def get_new_size(t):
                    return translate_new_size(self.new_size(t))

                if clip.is_mask:

                    def filter(get_frame, t):
                        return (
                            self.resizer(
                                (255 * get_frame(t)).astype("uint8"), get_new_size(t)
                            )
                            / 255.0
                        )

                else:

                    def filter(get_frame, t):
                        return self.resizer(
                            get_frame(t).astype("uint8"), get_new_size(t)
                        )

                newclip = clip.transform(
                    filter,
                    keep_duration=True,
                    apply_to=(["mask"] if self.apply_to_mask else []),
                )
                if self.apply_to_mask and clip.mask is not None:
                    newclip.mask = clip.mask.with_effects(
                        [Resize(self.new_size, apply_to_mask=False)]
                    )

                return newclip

            else:
                self.new_size = translate_new_size(self.new_size)

        elif self.height is not None:
            if hasattr(self.height, "__call__"):

                def func(t):
                    return 1.0 * int(self.height(t)) / h

                return clip.with_effects([Resize(func)])

            else:
                self.new_size = [w * self.height / h, self.height]

        elif self.width is not None:
            if hasattr(self.width, "__call__"):

                def func(t):
                    return 1.0 * self.width(t) / w

                return clip.with_effects([Resize(func)])

            else:
                self.new_size = [self.width, h * self.width / w]
        else:
            raise ValueError(
                "You must provide either 'new_size' or 'height' or 'width'"
            )

        # From here, the resizing is constant (not a function of time), size=newsize

        if clip.is_mask:

            def image_filter(pic):
                return (
                    1.0
                    * self.resizer((255 * pic).astype("uint8"), self.new_size)
                    / 255.0
                )

        else:

            def image_filter(pic):
                return self.resizer(pic.astype("uint8"), self.new_size)

        new_clip = clip.image_transform(image_filter)

        if self.apply_to_mask and clip.mask is not None:
            new_clip.mask = clip.mask.with_effects(
                [Resize(self.new_size, apply_to_mask=False)]
            )

        return new_clip
````

## File: moviepy/video/fx/Rotate.py
````python
import math
from dataclasses import dataclass

import numpy as np
from PIL import Image

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class Rotate(Effect):
    """
    Rotates the specified clip by ``angle`` degrees (or radians) anticlockwise
    If the angle is not a multiple of 90 (degrees) or ``center``, ``translate``,
    and ``bg_color`` are not ``None``, there will be black borders.
    You can make them transparent with:

    >>> new_clip = clip.with_mask().rotate(72)

    Parameters
    ----------

    clip : VideoClip
    A video clip.

    angle : float
    Either a value or a function angle(t) representing the angle of rotation.

    unit : str, optional
    Unit of parameter `angle` (either "deg" for degrees or "rad" for radians).

    resample : str, optional
    An optional resampling filter. One of "nearest", "bilinear", or "bicubic".

    expand : bool, optional
    If true, expands the output image to make it large enough to hold the
    entire rotated image. If false or omitted, make the output image the same
    size as the input image.

    translate : tuple, optional
    An optional post-rotate translation (a 2-tuple).

    center : tuple, optional
    Optional center of rotation (a 2-tuple). Origin is the upper left corner.

    bg_color : tuple, optional
    An optional color for area outside the rotated image. Only has effect if
    ``expand`` is true.
    """

    angle: float
    unit: str = "deg"
    resample: str = "bicubic"
    expand: bool = True
    center: tuple = None
    translate: tuple = None
    bg_color: tuple = None

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        try:
            resample = {
                "bilinear": Image.BILINEAR,
                "nearest": Image.NEAREST,
                "bicubic": Image.BICUBIC,
            }[self.resample]
        except KeyError:
            raise ValueError(
                "'resample' argument must be either 'bilinear', 'nearest' or 'bicubic'"
            )

        if hasattr(self.angle, "__call__"):
            get_angle = self.angle
        else:
            get_angle = lambda t: self.angle

        def filter(get_frame, t):
            angle = get_angle(t)
            im = get_frame(t)

            if self.unit == "rad":
                angle = math.degrees(angle)

            angle %= 360
            if not self.center and not self.translate and not self.bg_color:
                if (angle == 0) and self.expand:
                    return im
                if (angle == 90) and self.expand:
                    transpose = [1, 0] if len(im.shape) == 2 else [1, 0, 2]
                    return np.transpose(im, axes=transpose)[::-1]
                elif (angle == 270) and self.expand:
                    transpose = [1, 0] if len(im.shape) == 2 else [1, 0, 2]
                    return np.transpose(im, axes=transpose)[:, ::-1]
                elif (angle == 180) and self.expand:
                    return im[::-1, ::-1]

            pillow_kwargs = {}

            if self.bg_color is not None:
                pillow_kwargs["fillcolor"] = self.bg_color

            if self.center is not None:
                pillow_kwargs["center"] = self.center

            if self.translate is not None:
                pillow_kwargs["translate"] = self.translate

            # PIL expects uint8 type data. However a mask image has values in the
            # range [0, 1] and is of float type.  To handle this we scale it up by
            # a factor 'a' for use with PIL and then back again by 'a' afterwards.
            if im.dtype == "float64":
                # this is a mask image
                a = 255.0
            else:
                a = 1

            # call PIL.rotate
            return (
                np.array(
                    Image.fromarray(np.array(a * im).astype(np.uint8)).rotate(
                        angle, expand=self.expand, resample=resample, **pillow_kwargs
                    )
                )
                / a
            )

        return clip.transform(filter, apply_to=["mask"])
````

## File: moviepy/video/fx/Scroll.py
````python
from moviepy.Effect import Effect


class Scroll(Effect):
    """Effect that scrolls horizontally or vertically a clip, e.g. to make end credits

    Parameters
    ----------
    w, h
      The width and height of the final clip. Default to clip.w and clip.h

    x_speed, y_speed
      The speed of the scroll in the x and y directions.

    x_start, y_start
      The starting position of the scroll in the x and y directions.


    apply_to
      Whether to apply the effect to the mask too.
    """

    def __init__(
        self,
        w=None,
        h=None,
        x_speed=0,
        y_speed=0,
        x_start=0,
        y_start=0,
        apply_to="mask",
    ):
        self.w = w
        self.h = h
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.x_start = x_start
        self.y_start = y_start
        self.apply_to = apply_to

    def apply(self, clip):
        """Apply the effect to the clip."""
        if self.h is None:
            self.h = clip.h

        if self.w is None:
            self.w = clip.w

        x_max = self.w - 1
        y_max = self.h - 1

        def filter(get_frame, t):
            x = int(max(0, min(x_max, self.x_start + round(self.x_speed * t))))
            y = int(max(0, min(y_max, self.y_start + round(self.y_speed * t))))
            return get_frame(t)[y : y + self.h, x : x + self.w]

        return clip.transform(filter, apply_to=self.apply_to)
````

## File: moviepy/video/fx/SlideIn.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class SlideIn(Effect):
    """Makes the clip arrive from one side of the screen.

    Only works when the clip is included in a CompositeVideoClip,
    and if the clip has the same size as the whole composition.

    Parameters
    ----------

    clip : moviepy.Clip.Clip
      A video clip.

    duration : float
      Time taken for the clip to be fully visible

    side : str
      Side of the screen where the clip comes from. One of
      'top', 'bottom', 'left' or 'right'.

    Examples
    --------

    .. code:: python

        from moviepy import *

        clips = [... make a list of clips]
        slided_clips = [
            CompositeVideoClip([clip.with_effects([vfx.SlideIn(1, "left")])])
            for clip in clips
        ]
        final_clip = concatenate_videoclips(slided_clips, padding=-1)

        clip = ColorClip(
            color=(255, 0, 0), duration=1, size=(300, 300)
        ).with_fps(60)
        final_clip = CompositeVideoClip([clip.with_effects([vfx.SlideIn(1, "right")])])
    """

    duration: float
    side: str

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        w, h = clip.size
        pos_dict = {
            "left": lambda t: (min(0, w * (t / self.duration - 1)), "center"),
            "right": lambda t: (max(0, w * (1 - t / self.duration)), "center"),
            "top": lambda t: ("center", min(0, h * (t / self.duration - 1))),
            "bottom": lambda t: ("center", max(0, h * (1 - t / self.duration))),
        }

        return clip.with_position(pos_dict[self.side])
````

## File: moviepy/video/fx/SlideOut.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class SlideOut(Effect):
    """Makes the clip goes away by one side of the screen.

    Only works when the clip is included in a CompositeVideoClip,
    and if the clip has the same size as the whole composition.

    Parameters
    ----------

    clip : moviepy.Clip.Clip
      A video clip.

    duration : float
      Time taken for the clip to be fully visible

    side : str
      Side of the screen where the clip goes. One of
      'top', 'bottom', 'left' or 'right'.

    Examples
    --------

    .. code:: python

        from moviepy import *

        clips = [... make a list of clips]
        slided_clips = [
            CompositeVideoClip([clip.with_effects([vfx.SlideOut(1, "left")])])
            for clip in clips
        ]
        final_clip = concatenate_videoclips(slided_clips, padding=-1)

        clip = ColorClip(
            color=(255, 0, 0), duration=1, size=(300, 300)
        ).with_fps(60)
        final_clip = CompositeVideoClip([clip.with_effects([vfx.SlideOut(1, "right")])])
    """

    duration: float
    side: str

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if clip.duration is None:
            raise ValueError("Attribute 'duration' not set")

        w, h = clip.size
        ts = clip.duration - self.duration  # start time of the effect.
        pos_dict = {
            "left": lambda t: (min(0, w * (-(t - ts) / self.duration)), "center"),
            "right": lambda t: (max(0, w * ((t - ts) / self.duration)), "center"),
            "top": lambda t: ("center", min(0, h * (-(t - ts) / self.duration))),
            "bottom": lambda t: ("center", max(0, h * ((t - ts) / self.duration))),
        }

        return clip.with_position(pos_dict[self.side])
````

## File: moviepy/video/fx/SuperSample.py
````python
from dataclasses import dataclass

import numpy as np

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class SuperSample(Effect):
    """Replaces each frame at time t by the mean of `n_frames` equally spaced frames
    taken in the interval [t-d, t+d]. This results in motion blur.
    """

    d: float
    n_frames: int

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""

        def filter(get_frame, t):
            timings = np.linspace(t - self.d, t + self.d, self.n_frames)
            frame_average = np.mean(
                1.0 * np.array([get_frame(t_) for t_ in timings], dtype="uint16"),
                axis=0,
            )
            return frame_average.astype("uint8")

        return clip.transform(filter)
````

## File: moviepy/video/fx/TimeMirror.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class TimeMirror(Effect):
    """
    Returns a clip that plays the current clip backwards.
    The clip must have its ``duration`` attribute set.
    The same effect is applied to the clip's audio and mask if any.
    """

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if clip.duration is None:
            raise ValueError("Attribute 'duration' not set")

        return clip[::-1]
````

## File: moviepy/video/fx/TimeSymmetrize.py
````python
from dataclasses import dataclass

from moviepy.Clip import Clip
from moviepy.Effect import Effect


@dataclass
class TimeSymmetrize(Effect):
    """
    Returns a clip that plays the current clip once forwards and
    then once backwards. This is very practival to make video that
    loop well, e.g. to create animated GIFs.
    This effect is automatically applied to the clip's mask and audio
    if they exist.
    """

    def apply(self, clip: Clip) -> Clip:
        """Apply the effect to the clip."""
        if clip.duration is None:
            raise ValueError("Attribute 'duration' not set")

        return clip + clip[::-1]
````

## File: moviepy/video/io/__init__.py
````python
"""Classes and methods for reading, writing and previewing video files."""
````

## File: moviepy/video/io/display_in_notebook.py
````python
"""Implements ``display_in_notebook``, a function to embed images/videos/audio in the
Jupyter Notebook.
"""

# Notes:
# All media are physically embedded in the Jupyter Notebook
# (instead of simple links to the original files)
# That is because most browsers use a cache system and they won't
# properly refresh the media when the original files are changed.

import inspect
import os
from base64 import b64encode

from moviepy.audio.AudioClip import AudioClip
from moviepy.tools import extensions_dict
from moviepy.video.io.ffmpeg_reader import ffmpeg_parse_infos
from moviepy.video.VideoClip import ImageClip, VideoClip


try:  # pragma: no cover
    from IPython.display import HTML

    ipython_available = True

    class HTML2(HTML):  # noqa D101
        def __add__(self, other):
            return HTML2(self.data + other.data)

except ImportError:

    def HTML2(content):  # noqa D103
        return content

    ipython_available = False


sorry = "Sorry, seems like your browser doesn't support HTML5 audio/video"
templates = {
    "audio": (
        "<audio controls>"
        "<source %(options)s  src='data:audio/%(ext)s;base64,%(data)s'>"
        + sorry
        + "</audio>"
    ),
    "image": "<img %(options)s src='data:image/%(ext)s;base64,%(data)s'>",
    "video": (
        "<video %(options)s"
        "src='data:video/%(ext)s;base64,%(data)s' controls>" + sorry + "</video>"
    ),
}


def html_embed(
    clip, filetype=None, maxduration=60, rd_kwargs=None, center=True, **html_kwargs
):
    """Returns HTML5 code embedding the clip.

    Parameters
    ----------

    clip : moviepy.Clip.Clip
      Either a file name, or a clip to preview.
      Either an image, a sound or a video. Clips will actually be
      written to a file and embedded as if a filename was provided.

    filetype : str, optional
      One of 'video','image','audio'. If None is given, it is determined
      based on the extension of ``filename``, but this can bug.

    maxduration : float, optional
      An error will be raised if the clip's duration is more than the indicated
      value (in seconds), to avoid spoiling the browser's cache and the RAM.

    rd_kwargs : dict, optional
      Keyword arguments for the rendering, like ``dict(fps=15, bitrate="50k")``.
      Allow you to give some options to the render process. You can, for
      example, disable the logger bar passing ``dict(logger=None)``.

    center : bool, optional
      If true (default), the content will be wrapped in a
      ``<div align=middle>`` HTML container, so the content will be displayed
      at the center.

    html_kwargs
      Allow you to give some options, like ``width=260``, ``autoplay=True``,
      ``loop=1`` etc.

    Examples
    --------
    .. code:: python

        from moviepy import *
        # later ...
        html_embed(clip, width=360)
        html_embed(clip.audio)

        clip.write_gif("test.gif")
        html_embed('test.gif')

        clip.save_frame("first_frame.jpeg")
        html_embed("first_frame.jpeg")
    """
    if rd_kwargs is None:  # pragma: no cover
        rd_kwargs = {}

    if "Clip" in str(clip.__class__):
        TEMP_PREFIX = "__temp__"
        if isinstance(clip, ImageClip):
            filename = TEMP_PREFIX + ".png"
            kwargs = {"filename": filename, "with_mask": True}
            argnames = inspect.getfullargspec(clip.save_frame).args
            kwargs.update(
                {key: value for key, value in rd_kwargs.items() if key in argnames}
            )
            clip.save_frame(**kwargs)
        elif isinstance(clip, VideoClip):
            filename = TEMP_PREFIX + ".mp4"
            kwargs = {"filename": filename, "preset": "ultrafast"}
            kwargs.update(rd_kwargs)
            clip.write_videofile(**kwargs)
        elif isinstance(clip, AudioClip):
            filename = TEMP_PREFIX + ".mp3"
            kwargs = {"filename": filename}
            kwargs.update(rd_kwargs)
            clip.write_audiofile(**kwargs)
        else:
            raise ValueError("Unknown class for the clip. Cannot embed and preview.")

        return html_embed(
            filename,
            maxduration=maxduration,
            rd_kwargs=rd_kwargs,
            center=center,
            **html_kwargs,
        )

    filename = clip
    options = " ".join(["%s='%s'" % (str(k), str(v)) for k, v in html_kwargs.items()])
    name, ext = os.path.splitext(filename)
    ext = ext[1:]

    if filetype is None:
        ext = filename.split(".")[-1].lower()
        if ext == "gif":
            filetype = "image"
        elif ext in extensions_dict:
            filetype = extensions_dict[ext]["type"]
        else:
            raise ValueError(
                "No file type is known for the provided file. Please provide "
                "argument `filetype` (one of 'image', 'video', 'sound') to the "
                "display_in_notebook function."
            )

    if filetype == "video":
        # The next lines set the HTML5-cvompatible extension and check that the
        # extension is HTML5-valid
        exts_htmltype = {"mp4": "mp4", "webm": "webm", "ogv": "ogg"}
        allowed_exts = " ".join(exts_htmltype.keys())
        try:
            ext = exts_htmltype[ext]
        except Exception:
            raise ValueError(
                "This video extension cannot be displayed in the "
                "Jupyter Notebook. Allowed extensions: " + allowed_exts
            )

    if filetype in ["audio", "video"]:
        duration = ffmpeg_parse_infos(filename, decode_file=True)["duration"]
        if duration > maxduration:
            raise ValueError(
                (
                    "The duration of video %s (%.1f) exceeds the 'maxduration'"
                    " attribute. You can increase 'maxduration', by passing"
                    " 'maxduration' parameter to display_in_notebook function."
                    " But note that embedding large videos may take all the memory"
                    " away!"
                )
                % (filename, duration)
            )

    with open(filename, "rb") as file:
        data = b64encode(file.read()).decode("utf-8")

    template = templates[filetype]

    result = template % {"data": data, "options": options, "ext": ext}
    if center:
        result = r"<div align=middle>%s</div>" % result

    return result


def display_in_notebook(
    clip,
    filetype=None,
    maxduration=60,
    t=None,
    fps=None,
    rd_kwargs=None,
    center=True,
    **html_kwargs,
):
    """Displays clip content in an Jupyter Notebook.

    Remarks: If your browser doesn't support HTML5, this should warn you.
    If nothing is displayed, maybe your file or filename is wrong.
    Important: The media will be physically embedded in the notebook.

    Parameters
    ----------

    clip : moviepy.Clip.Clip
      Either the name of a file, or a clip to preview. The clip will actually
      be written to a file and embedded as if a filename was provided.

    filetype : str, optional
      One of ``"video"``, ``"image"`` or ``"audio"``. If None is given, it is
      determined based on the extension of ``filename``, but this can bug.

    maxduration : float, optional
      An error will be raised if the clip's duration is more than the indicated
      value (in seconds), to avoid spoiling the browser's cache and the RAM.

    t : float, optional
      If not None, only the frame at time t will be displayed in the notebook,
      instead of a video of the clip.

    fps : int, optional
      Enables to specify an fps, as required for clips whose fps is unknown.

    rd_kwargs : dict, optional
      Keyword arguments for the rendering, like ``dict(fps=15, bitrate="50k")``.
      Allow you to give some options to the render process. You can, for
      example, disable the logger bar passing ``dict(logger=None)``.

    center : bool, optional
      If true (default), the content will be wrapped in a
      ``<div align=middle>`` HTML container, so the content will be displayed
      at the center.

    kwargs
      Allow you to give some options, like ``width=260``, etc. When editing
      looping gifs, a good choice is ``loop=1, autoplay=1``.

    Examples
    --------

    .. code:: python

        from moviepy import *
        # later ...
        clip.display_in_notebook(width=360)
        clip.audio.display_in_notebook()

        clip.write_gif("test.gif")
        display_in_notebook('test.gif')

        clip.save_frame("first_frame.jpeg")
        display_in_notebook("first_frame.jpeg")
    """
    if not ipython_available:
        raise ImportError("Only works inside an Jupyter Notebook")

    if rd_kwargs is None:
        rd_kwargs = {}

    if fps is not None:
        rd_kwargs["fps"] = fps

    if t is not None:
        clip = clip.to_ImageClip(t)

    return HTML2(
        html_embed(
            clip,
            filetype=filetype,
            maxduration=maxduration,
            center=center,
            rd_kwargs=rd_kwargs,
            **html_kwargs,
        )
    )
````

## File: moviepy/video/io/errors.py
````python
"""contains the errors that can be raised by the video IO functions."""


class VideoCorruptedError(RuntimeError):
    """Error raised when a video file is corrupted."""
````

## File: moviepy/video/io/ffmpeg_reader.py
````python
"""Implements all the functions to read a video or a picture using ffmpeg."""

import os
import re
import subprocess as sp
import warnings
from typing import List

import numpy as np

from moviepy.config import FFMPEG_BINARY  # ffmpeg, ffmpeg.exe, etc...
from moviepy.tools import (
    convert_to_seconds,
    cross_platform_popen_params,
    ffmpeg_escape_filename,
)
from moviepy.video.io.errors import VideoCorruptedError


class FFMPEG_VideoReader:
    """Class for video byte-level reading with ffmpeg."""

    def __init__(
        self,
        filename,
        decode_file=True,
        print_infos=False,
        bufsize=None,
        pixel_format="rgb24",
        check_duration=True,
        target_resolution=None,
        resize_algo="bicubic",
        fps_source="fps",
    ):
        self.filename = filename
        self.proc = None
        infos = ffmpeg_parse_infos(
            filename,
            check_duration=check_duration,
            fps_source=fps_source,
            decode_file=decode_file,
            print_infos=print_infos,
        )
        # If framerate is unavailable, assume 1.0 FPS to avoid divide-by-zero errors.
        self.fps = infos.get("video_fps", 1.0)
        # If frame size is unavailable, set 1x1 divide-by-zero errors.
        self.size = infos.get("video_size", (1, 1))

        # ffmpeg automatically rotates videos if rotation information is
        # available, so exchange width and height
        self.rotation = abs(infos.get("video_rotation", 0))
        if self.rotation in [90, 270]:
            self.size = [self.size[1], self.size[0]]

        if target_resolution:
            if None in target_resolution:
                ratio = 1
                for idx, target in enumerate(target_resolution):
                    if target:
                        ratio = target / self.size[idx]
                self.size = (int(self.size[0] * ratio), int(self.size[1] * ratio))
            else:
                self.size = target_resolution
        self.resize_algo = resize_algo

        self.duration = infos.get("video_duration", 0.0)
        self.ffmpeg_duration = infos.get("duration", 0.0)
        self.n_frames = infos.get("video_n_frames", 0)
        self.bitrate = infos.get("video_bitrate", 0)

        self.infos = infos

        self.pixel_format = pixel_format
        self.depth = 4 if pixel_format[-1] == "a" else 3
        # 'a' represents 'alpha' which means that each pixel has 4 values instead of 3.
        # See https://github.com/Zulko/moviepy/issues/1070#issuecomment-644457274

        if bufsize is None:
            w, h = self.size
            bufsize = self.depth * w * h + 100

        self.bufsize = bufsize
        self.initialize()

    def initialize(self, start_time=0):
        """
        Opens the file, creates the pipe.

        Sets self.pos to the appropriate value (1 if start_time == 0 because
        it pre-reads the first frame).
        """
        self.close(delete_lastread=False)  # if any

        # self.pos represents the (0-indexed) index of the frame that is next in line
        # to be read by self.read_frame().
        # Eg when self.pos is 1, the 2nd frame will be read next.
        self.pos = self.get_frame_number(start_time)

        # Getting around a difference between ffmpeg and moviepy seeking:
        # "moviepy seek" means "get the frame displayed at time t"
        #   Hence given a 29.97 FPS video, seeking to .01s means "get frame 0".
        # "ffmpeg seek" means "skip all frames until you reach time t".
        #   This time, seeking to .01s means "get frame 1". Surprise!
        #
        # (In 30fps, timestamps like 2.0s, 3.5s will give the same frame output
        # under both rules, for the timestamp can be represented exactly in
        # decimal.)
        #
        # So we'll subtract an epsilon from the timestamp given to ffmpeg.
        if self.pos != 0:
            start_time = self.pos * (1 / self.fps) - 0.00001
        else:
            start_time = 0.0

        if start_time != 0:
            offset = min(1, start_time)
            i_arg = [
                "-ss",
                "%.06f" % (start_time - offset),
                "-i",
                ffmpeg_escape_filename(self.filename),
                "-ss",
                "%.06f" % offset,
            ]
        else:
            i_arg = ["-i", ffmpeg_escape_filename(self.filename)]

        # For webm video (vp8 and vp9) with transparent layer, force libvpx/libvpx-vp9
        # as ffmpeg native webm decoder dont decode alpha layer
        # (see
        # https://www.reddit.com/r/ffmpeg/comments/fgpyfb/help_with_webm_with_alpha_channel/
        # )
        if self.depth == 4:
            codec_name = self.infos.get("video_codec_name")
            if codec_name == "vp9":
                i_arg = ["-c:v", "libvpx-vp9"] + i_arg
            elif codec_name == "vp8":
                i_arg = ["-c:v", "libvpx"] + i_arg

        cmd = (
            [FFMPEG_BINARY]
            + i_arg
            + [
                "-loglevel",
                "error",
                "-f",
                "image2pipe",
                "-vf",
                "scale=%d:%d" % tuple(self.size),
                "-sws_flags",
                self.resize_algo,
                "-pix_fmt",
                self.pixel_format,
                "-vcodec",
                "rawvideo",
                "-",
            ]
        )

        popen_params = cross_platform_popen_params(
            {
                "bufsize": self.bufsize,
                "stdout": sp.PIPE,
                "stderr": sp.PIPE,
                "stdin": sp.DEVNULL,
            }
        )
        self.proc = sp.Popen(cmd, **popen_params)
        self.last_read = self.read_frame()

    def skip_frames(self, n=1):
        """Reads and throws away n frames"""
        w, h = self.size
        for i in range(n):
            self.proc.stdout.read(self.depth * w * h)

            # self.proc.stdout.flush()
        self.pos += n

    def read_frame(self):
        """
        Reads the next frame from the file.
        Note that upon (re)initialization, the first frame will already have been read
        and stored in ``self.last_read``.
        """
        w, h = self.size
        nbytes = self.depth * w * h

        s = self.proc.stdout.read(nbytes)

        if len(s) != nbytes:
            warnings.warn(
                (
                    "In file %s, %d bytes wanted but %d bytes read at frame index"
                    " %d (out of a total %d frames), at time %.02f/%.02f sec."
                    " Using the last valid frame instead."
                )
                % (
                    self.filename,
                    nbytes,
                    len(s),
                    self.pos,
                    self.n_frames,
                    1.0 * self.pos / self.fps,
                    self.duration,
                ),
                UserWarning,
            )
            if not hasattr(self, "last_read"):
                raise IOError(
                    (
                        "MoviePy error: failed to read the first frame of "
                        f"video file {self.filename}. That might mean that the file is "
                        "corrupted. That may also mean that you are using "
                        "a deprecated version of FFMPEG. On Ubuntu/Debian "
                        "for instance the version in the repos is deprecated. "
                        "Please update to a recent version from the website."
                    )
                )

            result = self.last_read

        else:
            if hasattr(np, "frombuffer"):
                result = np.frombuffer(s, dtype="uint8")
            else:
                result = np.fromstring(s, dtype="uint8")
            result.shape = (h, w, len(s) // (w * h))  # reshape((h, w, len(s)//(w*h)))
            self.last_read = result

        # We have to do this down here because `self.pos` is used in the warning above
        self.pos += 1

        return result

    def get_frame(self, t):
        """Read a file video frame at time t.

        Note for coders: getting an arbitrary frame in the video with
        ffmpeg can be painfully slow if some decoding has to be done.
        This function tries to avoid fetching arbitrary frames
        whenever possible, by moving between adjacent frames.
        """
        # + 1 so that it represents the frame position that it will be
        # after the frame is read. This makes the later comparisons easier.
        pos = self.get_frame_number(t) + 1

        # Initialize proc if it is not open
        if not self.proc:
            print("Proc not detected")
            self.initialize(t)
            return self.last_read

        if pos == self.pos:
            return self.last_read
        elif (pos < self.pos) or (pos > self.pos + 100):
            # We can't just skip forward to `pos` or it would take too long
            self.initialize(t)
            return self.last_read
        else:
            # If pos == self.pos + 1, this line has no effect
            self.skip_frames(pos - self.pos - 1)
            result = self.read_frame()
            return result

    @property
    def lastread(self):
        """Alias of `self.last_read` for backwards compatibility with MoviePy 1.x."""
        return self.last_read

    def get_frame_number(self, t):
        """Helper method to return the frame number at time ``t``"""
        # I used this horrible '+0.00001' hack because sometimes due to numerical
        # imprecisions a 3.0 can become a 2.99999999... which makes the int()
        # go to the previous integer. This makes the fetching more robust when you
        # are getting the nth frame by writing get_frame(n/fps).
        return int(self.fps * t + 0.00001)

    def close(self, delete_lastread=True):
        """Closes the reader terminating the process, if is still open."""
        if self.proc:
            if self.proc.poll() is None:
                self.proc.terminate()
                self.proc.stdout.close()
                self.proc.stderr.close()
                self.proc.wait()
            self.proc = None
        if delete_lastread and hasattr(self, "last_read"):
            del self.last_read

    def __del__(self):
        self.close()


def ffmpeg_read_image(filename, with_mask=True, pixel_format=None):
    """Read an image file (PNG, BMP, JPEG...).

    Wraps FFMPEG_Videoreader to read just one image.
    Returns an ImageClip.

    This function is not meant to be used directly in MoviePy.
    Use ImageClip instead to make clips out of image files.

    Parameters
    ----------

    filename
      Name of the image file. Can be of any format supported by ffmpeg.

    with_mask
      If the image has a transparency layer, ``with_mask=true`` will save
      this layer as the mask of the returned ImageClip

    pixel_format
      Optional: Pixel format for the image to read. If is not specified
      'rgb24' will be used as the default format unless ``with_mask`` is set
      as ``True``, then 'rgba' will be used.

    """
    if not pixel_format:
        pixel_format = "rgba" if with_mask else "rgb24"
    reader = FFMPEG_VideoReader(
        filename, pixel_format=pixel_format, check_duration=False
    )
    im = reader.last_read
    del reader
    return im


class FFmpegInfosParser:
    """An (hopefully) robuste ffmpeg `-i` command option file information parser.
    Is designed to parse the output by extracting the different blocks of informations,
    based on the indentation, in order to create an easy to handle block tree

    Parameters
    ----------

    filename
      Name of the file parsed, only used to raise accurate error messages.

    infos
      Information returned by FFmpeg.

    fps_source
      Indicates what source data will be preferably used to retrieve fps data.

    check_duration
      Enable or disable the parsing of the duration of the file. Useful to
      skip the duration check, for example, for images.

    decode_file
      Indicates if the whole file has been decoded. The duration parsing strategy
      will differ depending on this argument.
    """

    class ParseDimensionError(VideoCorruptedError):
        """Error raised when we cannot find dimensions in a video stream"""

        pass

    class ParseDurationError(VideoCorruptedError):
        """Error raised when we cannot find duration in a video stream"""

        pass

    class InfoBlock:
        """Represents a block of output from ffmpeg, which can be an input file,
        stream, chapter or metadata.
        """

        def __init__(self, block_line, indent_level=0):
            self.type = "unknown"
            self.childs: List[FFmpegInfosParser.InfoBlock] = []
            self.parent = None
            self.indent_level = indent_level
            self.head_line = block_line
            self.raw_data = []
            self.data = {}

        def add_child(self, child):
            """Adds a child to the current block."""
            child.parent = self
            self.childs.append(child)

    def __init__(
        self,
        infos,
        filename,
        fps_source="fps",
        check_duration=True,
        decode_file=False,
    ):
        self.infos = infos
        self.filename = filename
        self.check_duration = check_duration
        self.fps_source = fps_source
        self.duration_tag_separator = "time=" if decode_file else "Duration: "
        self.blocks = None
        self.video_stream = None
        self.audio_stream = None
        self.data_stream = None

        self.result = {
            "video_found": False,
            "audio_found": False,
            "metadata": {},
            "blocks": None,
            "inputs": {},
        }

    def _extract_block(self, index, start_indent, block: InfoBlock = None):
        lines = self.infos.splitlines()
        block.content = []
        multiline = None
        is_last_line = False
        while index < len(lines) - 1:
            index += 1
            is_last_line = index == (len(lines) - 1)
            line = lines[index]
            indent_level = (len(line) - len(line.lstrip())) / 2
            line = line.strip()

            if not is_last_line:
                next_line = lines[index + 1].strip()
            else:
                next_line = False

            # End of block
            if indent_level <= start_indent:
                index -= 1
                break

            # New block
            if line.lstrip().startswith(
                ("Metadata", "Stream", "Side data", "Chapter", "Chapters")
            ):
                (child_block, index) = self._extract_block(
                    index, indent_level, self.InfoBlock(line.lstrip(), indent_level)
                )
                self._parse_headline_data(child_block)
                block.add_child(child_block)
                continue

            # Support for multiline entries
            if line.startswith(":") or (next_line and next_line.startswith(":")):
                if not multiline:
                    multiline = line
                    continue
                elif next_line.startswith(":"):
                    multiline += "\n" + line[1:].strip()
                    continue

            if multiline:
                line = multiline + "\n" + line[1:].strip()
                multiline = None

            # Standard line, add to block raw data and parsed data
            block.raw_data.append(line)
            field, value = self._parse_line(line)
            block.data[field] = value

        return (block, index)

    def _parse_headline_data(self, block: InfoBlock):
        line = block.head_line.lstrip()
        if line.startswith("Input "):
            block.type = "input"
        elif line.startswith("Metadata:"):
            block.type = "metadata"
        elif line.startswith("Stream "):
            block.type = "stream"
            self._parse_stream(block)
        elif line.startswith("Side data:"):
            block.type = "side_data"
        elif line.startswith("Chapters"):
            block.type = "chapters"
        elif line.startswith("Chapter"):
            block.type = "chapter"
            self._parse_chapter(block)

    def _parse_line(self, line):
        """Parse a standard line to return (field, value) with typecasting
        when needed (rotate, displaymatrix)
        """
        specials = (
            "Ambient Viewing Environment,",
            "Content Light Level Metadata,",
            "Mastering Display Metadata,",
        )
        line = line.strip()
        if line.startswith(specials):
            infos = line.split(",", 1)
        else:
            infos = line.split(":", 1)

        field = infos[0].strip()
        value = infos[1].strip()

        if field == "rotate":
            value = float(value)

        elif field == "displaymatrix":
            match = re.search(r"[-+]?\d+(\.\d+)?", value)
            if match:
                # We must multiply by -1 because displaymatrix return info
                # about how to rotate to show video, not about video rotation
                value = float(match.group()) * -1

        return (field, value)

    def _parse_duration(self, line):
        """Parse the duration from the block data."""
        try:
            match_duration = re.search(
                r"([0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9])",
                line,
            )
            if match_duration is None:
                raise VideoCorruptedError(f"Could not parse duration from {line!r}")
            return convert_to_seconds(match_duration.group(1))
        except VideoCorruptedError:
            raise
        except Exception:
            raise IOError(
                (
                    "MoviePy error: failed to read the duration of file '%s'.\n"
                    "Here are the file infos returned by ffmpeg:\n\n%s"
                )
                % (self.filename, self.infos)
            )

    def _parse_stream(self, block: InfoBlock):
        # get input number, stream number, language and type
        main_info_match = re.search(
            r"^Stream\s#(\d+):(\d+)(?:\[\w+\])?\(?(\w+)?\)?:\s(\w+):",
            block.head_line.lstrip(),
        )
        (
            input_number,
            stream_number,
            language,
            stream_type,
        ) = main_info_match.groups()
        block.data["input_number"] = int(input_number)
        block.data["stream_number"] = int(stream_number)
        block.data["stream_type_lower"] = stream_type.lower()

        if language == "und":
            language = None

        block.data["language"] = language
        block.data["default"] = block.head_line.rstrip().endswith("(default)")

        if block.data["stream_type_lower"] == "audio":
            self._parse_stream_audio(block)
        elif block.data["stream_type_lower"] == "video":
            self._parse_stream_video(block)
        elif block.data["stream_type_lower"] == "data":
            self._parse_stream_data(block)

    def _parse_stream_audio(self, block: InfoBlock):
        """Parses data from "Stream ... Audio" line."""
        try:
            block.data["fps"] = int(re.search(r" (\d+) Hz", block.head_line).group(1))
        except (AttributeError, ValueError):
            # AttributeError: 'NoneType' object has no attribute 'group'
            # ValueError: invalid literal for int() with base 10: '<string>'
            block.data["fps"] = "unknown"

        match_audio_bitrate = re.search(r"(\d+) k(i?)b/s", block.head_line)
        block.data["bitrate"] = (
            int(match_audio_bitrate.group(1)) if match_audio_bitrate else None
        )

        # Store default stream, or first stream if we dont find any default
        if block.data["default"] or not self.audio_stream:
            self.audio_stream = block

    def _parse_stream_data(self, block: InfoBlock):
        """Parses data from "Stream ... Data" line."""
        # Store default stream, or first stream if we dont find any default
        if block.data["default"] or not self.data_stream:
            self.data_stream = block

    def _parse_stream_video(self, block: InfoBlock):
        """Parses data from "Stream ... Video" line."""
        try:
            match_video_size = re.search(r" (\d+)x(\d+)[,\s]", block.head_line)
            if match_video_size:
                # size, of the form 460x320 (w x h)
                block.data["size"] = [int(num) for num in match_video_size.groups()]
        except Exception:
            raise FFmpegInfosParser.ParseDimensionError()

        match_bitrate = re.search(r"(\d+) k(i?)b/s", block.head_line)
        block.data["bitrate"] = int(match_bitrate.group(1)) if match_bitrate else None

        # Get the frame rate. Sometimes it's 'tbr', sometimes 'fps', sometimes
        # tbc, and sometimes tbc/2...
        # Current policy: Trust fps first, then tbr unless fps_source is
        # specified as 'tbr' in which case try tbr then fps

        # If result is near from x*1000/1001 where x is 23,24,25,50,
        # replace by x*1000/1001 (very common case for the fps).

        if self.fps_source == "fps":
            try:
                fps = self._parse_fps(block.head_line)
            except (AttributeError, ValueError):
                fps = self._parse_tbr(block.head_line)
        elif self.fps_source == "tbr":
            try:
                fps = self._parse_tbr(block.head_line)
            except (AttributeError, ValueError):
                fps = self._parse_fps(block.head_line)
        else:
            raise ValueError(
                ("fps source '%s' not supported parsing the video '%s'")
                % (self.fps_source, self.filename)
            )

        # It is known that a fps of 24 is often written as 24000/1001
        # but then ffmpeg nicely rounds it to 23.98, which we hate.
        coef = 1000.0 / 1001.0
        for x in [23, 24, 25, 30, 50]:
            if (fps != x) and abs(fps - x * coef) < 0.01:
                fps = x * coef
        block.data["fps"] = fps

        # Try to extract video codec and profile
        main_info_match = re.search(
            r"Video:\s(\w+)?\s?(\([^)]+\))?",
            block.head_line.lstrip(),
        )

        if main_info_match is not None:
            (codec_name, profile) = main_info_match.groups()
            block.data["codec_name"] = codec_name
            block.data["profile"] = profile

        # Store default stream, or first stream if we dont find any default
        if block.data["default"] or not self.video_stream:
            self.video_stream = block

    def _parse_fps(self, line):
        """Parses number of FPS from a line of the ``ffmpeg -i`` command output."""
        return float(re.search(r" (\d+.?\d*) fps", line).group(1))

    def _parse_tbr(self, line):
        """Parses number of TBS from a line of the ``ffmpeg -i`` command output."""
        s_tbr = re.search(r" (\d+.?\d*k?) tbr", line).group(1)

        # Sometimes comes as e.g. 12k. We need to replace that with 12000.
        if s_tbr[-1] == "k":
            tbr = float(s_tbr[:-1]) * 1000
        else:
            tbr = float(s_tbr)
        return tbr

    def _parse_chapter(self, block: InfoBlock):
        # extract chapter data
        chapter_data_match = re.search(
            r"^Chapter #(\d+):(\d+): start (\d+\.?\d+?), end (\d+\.?\d+?)",
            block.head_line.strip(),
        )
        input_number, chapter_number, start, end = chapter_data_match.groups()

        # start building the chapter
        block.data = {
            "input_number": int(input_number),
            "chapter_number": int(chapter_number),
            "start": float(start),
            "end": float(end),
        }

    def _parse_blocks(self, root: InfoBlock):
        for key, data in root.data.items():
            if key == "Duration":
                self.result["duration"] = self._parse_duration(data)

                bitrate_match = re.search(r"bitrate: (\d+) k(i?)b/s", data)
                self.result["bitrate"] = (
                    int(bitrate_match.group(1)) if bitrate_match else None
                )

                start_match = re.search(r"start: (\d+\.?\d+)", data)
                self.result["start"] = (
                    float(start_match.group(1)) if start_match else None
                )
            else:
                if "metadata" not in self.result:
                    self.result["metadata"] = {}

                self.result["metadata"][key] = data

        # For input direct metadata blocks, add meta to results
        for child in root.childs:
            if child.type in ("metadata", "side_data"):
                for key, data in child.data.items():
                    if "metadata" not in self.result:
                        self.result["metadata"] = {}

                    self.result["metadata"][key] = data

        if self.video_stream:
            self.result["video_found"] = True
            self.result["video_size"] = self.video_stream.data.get("size", None)
            self.result["video_bitrate"] = self.video_stream.data.get("bitrate", None)
            self.result["video_fps"] = self.video_stream.data["fps"]
            self.result["video_codec_name"] = self.video_stream.data.get(
                "codec_name", None
            )
            self.result["video_profile"] = self.video_stream.data.get("profile", None)
            for child in self.video_stream.childs:
                if child.type in ("metadata", "side_data"):
                    for key, data in child.data.items():
                        if key in ("rotate", "displaymatrix"):
                            self.result["video_rotation"] = data

        if self.audio_stream:
            self.result["audio_found"] = True
            self.result["audio_fps"] = self.audio_stream.data["fps"]
            self.result["audio_bitrate"] = self.audio_stream.data["bitrate"]

        if self.result["video_found"] and self.check_duration:
            if "duration" not in self.result:
                raise self.ParseDurationError()

            self.result["video_duration"] = self.result["duration"]
            self.result["video_n_frames"] = int(
                self.result["duration"] * self.result.get("video_fps", 0)
            )
        else:
            self.result["video_n_frames"] = 0
            self.result["video_duration"] = 0.0

        self._populate_inputs(root=root)

    def _populate_inputs(self, root: InfoBlock):
        """Forge inputs for compatibility with old versions, not used anywhere though"""
        for child in root.childs:
            if child.type == "stream":
                if "streams" not in self.result["inputs"]:
                    self.result["inputs"]["streams"] = []

                stream = child.data

                for stream_child in child.childs:
                    if stream_child.type == "metadata":
                        stream["metadata"] = stream_child.data
                    elif stream_child.type == "side_data":
                        stream["side_data"] = stream_child.data

                self.result["inputs"]["streams"].append(stream)

            elif child.type == "chapters":
                for chapter in child.childs:
                    if "chapters" not in self.result["inputs"]:
                        self.result["inputs"]["chapters"] = []

                    chap = chapter.data

                    for chapter_child in chapter.childs:
                        if chapter_child.type == "metadata":
                            chap["metadata"] = chapter_child.data
                        elif chapter_child.type == "side_data":
                            chap["side_data"] = chapter_child.data

                    self.result["inputs"]["chapters"].append(chap)

            elif child.type == "metadata":
                self.result["metadata"] = child.data

        if self.audio_stream:
            self.result["default_audio_input_number"] = self.audio_stream.data[
                "input_number"
            ]
            self.result["default_audio_stream_number"] = self.audio_stream.data[
                "stream_number"
            ]

        if self.video_stream:
            self.result["default_video_input_number"] = self.video_stream.data[
                "input_number"
            ]
            self.result["default_video_stream_number"] = self.video_stream.data[
                "stream_number"
            ]

        if self.data_stream:
            self.result["default_data_input_number"] = self.data_stream.data[
                "input_number"
            ]
            self.result["default_data_stream_number"] = self.data_stream.data[
                "stream_number"
            ]

    def parse(self):
        """Parses the information returned by FFmpeg in stderr executing their binary
        for a file with ``-i`` option and returns a dictionary with all data needed
        by MoviePy.
        """
        try:
            first_input = 0
            for line in self.infos.splitlines():
                if line.startswith("Input"):
                    break
                first_input += 1

            root_block = self.InfoBlock(self.infos.splitlines()[first_input], 0)
            self._extract_block(first_input, 0, root_block)
            self._parse_blocks(root_block)
            self.blocks = root_block
            self.result["blocks"] = root_block
            return self.result
        except self.ParseDimensionError:
            raise IOError(
                (
                    "MoviePy error: failed to read video dimensions in"
                    " file '%s'.\nHere are the file infos returned by"
                    "ffmpeg:\n\n%s"
                )
                % (self.filename, self.infos)
            )
        except self.ParseDurationError:
            raise IOError(
                (
                    "MoviePy error: failed to read video duration in"
                    " file '%s'.\nHere are the file infos returned by"
                    "ffmpeg:\n\n%s"
                )
                % (self.filename, self.infos)
            )


def ffmpeg_parse_infos(
    filename,
    check_duration=True,
    fps_source="fps",
    decode_file=False,
    print_infos=False,
):
    """Get the information of a file using ffmpeg.

    Returns a dictionary with next fields:

    - ``"audio_bitrate"``
    - ``"audio_found"``
    - ``"audio_fps"``
    - ``"bitrate"``
    - ``"duration"``
    - ``"inputs"``
    - ``"metadata"``
    - ``"start"``
    - ``"video_bitrate"``
    - ``"video_codec_name"``
    - ``"video_duration"``
    - ``"video_fps"``
    - ``"video_found"``
    - ``"video_n_frames"``
    - ``"video_profile"``
    - ``"video_rotation"``
    - ``"video_size"``

    Note that "video_duration" is slightly smaller than "duration" to avoid
    fetching the incomplete frames at the end, which raises an error.

    Parameters
    ----------

    filename
      Name of the file parsed, only used to raise accurate error messages.

    infos
      Information returned by FFmpeg.

    fps_source
      Indicates what source data will be preferably used to retrieve fps data.

    check_duration
      Enable or disable the parsing of the duration of the file. Useful to
      skip the duration check, for example, for images.

    decode_file
      Indicates if the whole file must be read to retrieve their duration.
      This is needed for some files in order to get the correct duration (see
      https://github.com/Zulko/moviepy/pull/1222).
    """
    # Open the file in a pipe, read output
    cmd = [FFMPEG_BINARY, "-hide_banner", "-i", ffmpeg_escape_filename(filename)]
    if decode_file:
        cmd.extend(["-f", "null", "-"])

    popen_params = cross_platform_popen_params(
        {
            "bufsize": 10**5,
            "stdout": sp.PIPE,
            "stderr": sp.PIPE,
            "stdin": sp.DEVNULL,
        }
    )

    proc = sp.Popen(cmd, **popen_params)
    (output, error) = proc.communicate()
    infos = error.decode("utf8", errors="ignore")

    proc.terminate()
    del proc

    if print_infos:
        # print the whole info text returned by FFMPEG
        print(infos)

    try:
        return FFmpegInfosParser(
            infos,
            filename,
            fps_source=fps_source,
            check_duration=check_duration,
            decode_file=decode_file,
        ).parse()
    except VideoCorruptedError:
        raise
    except Exception as exc:
        if os.path.isdir(filename):
            raise IsADirectoryError(f"'{filename}' is a directory")
        elif not os.path.exists(filename):
            raise FileNotFoundError(f"'{filename}' not found")
        raise IOError(f"Error passing `ffmpeg -i` command output: \n\n{infos}") from exc
````

## File: moviepy/video/io/ffmpeg_tools.py
````python
"""Miscellaneous bindings to ffmpeg."""

import os
import re
import subprocess
from pathlib import Path

from moviepy.config import FFMPEG_BINARY, FFPLAY_BINARY
from moviepy.decorators import convert_parameter_to_seconds, convert_path_to_string
from moviepy.tools import ffmpeg_escape_filename, subprocess_call


@convert_path_to_string(("inputfile", "outputfile"))
@convert_parameter_to_seconds(("start_time", "end_time"))
def ffmpeg_extract_subclip(
    inputfile, start_time, end_time, outputfile=None, logger="bar"
):
    """Makes a new video file playing video file between two times.

    Parameters
    ----------

    inputfile : str
      Path to the file from which the subclip will be extracted.

    start_time : float
      Moment of the input clip that marks the start of the produced subclip.

    end_time : float
      Moment of the input clip that marks the end of the produced subclip.

    outputfile : str, optional
      Path to the output file. Defaults to
      ``<inputfile_name>SUB<start_time>_<end_time><ext>``.
    """
    if not outputfile:
        name, ext = os.path.splitext(inputfile)
        t1, t2 = [int(1000 * t) for t in [start_time, end_time]]
        outputfile = "%sSUB%d_%d%s" % (name, t1, t2, ext)

    cmd = [
        FFMPEG_BINARY,
        "-y",
        "-ss",
        "%0.2f" % start_time,
        "-i",
        ffmpeg_escape_filename(inputfile),
        "-t",
        "%0.2f" % (end_time - start_time),
        "-map",
        "0",
        "-vcodec",
        "copy",
        "-acodec",
        "copy",
        "-copyts",
        ffmpeg_escape_filename(outputfile),
    ]
    subprocess_call(cmd, logger=logger)


@convert_path_to_string(("videofile", "audiofile", "outputfile"))
def ffmpeg_merge_video_audio(
    videofile,
    audiofile,
    outputfile,
    video_codec="copy",
    audio_codec="copy",
    logger="bar",
):
    """Merges video file and audio file into one movie file.

    Parameters
    ----------

    videofile : str
      Path to the video file used in the merge.

    audiofile : str
      Path to the audio file used in the merge.

    outputfile : str
      Path to the output file.

    video_codec : str, optional
      Video codec used by FFmpeg in the merge.

    audio_codec : str, optional
      Audio codec used by FFmpeg in the merge.
    """
    cmd = [
        FFMPEG_BINARY,
        "-y",
        "-i",
        ffmpeg_escape_filename(audiofile),
        "-i",
        ffmpeg_escape_filename(videofile),
        "-vcodec",
        video_codec,
        "-acodec",
        audio_codec,
        ffmpeg_escape_filename(outputfile),
    ]

    subprocess_call(cmd, logger=logger)


@convert_path_to_string(("inputfile", "outputfile"))
def ffmpeg_extract_audio(inputfile, outputfile, bitrate=3000, fps=44100, logger="bar"):
    """Extract the sound from a video file and save it in ``outputfile``.

    Parameters
    ----------

    inputfile : str
      The path to the file from which the audio will be extracted.

    outputfile : str
      The path to the file to which the audio will be stored.

    bitrate : int, optional
      Bitrate for the new audio file.

    fps : int, optional
      Frame rate for the new audio file.
    """
    cmd = [
        FFMPEG_BINARY,
        "-y",
        "-i",
        ffmpeg_escape_filename(inputfile),
        "-ab",
        "%dk" % bitrate,
        "-ar",
        "%d" % fps,
        ffmpeg_escape_filename(outputfile),
    ]
    subprocess_call(cmd, logger=logger)


@convert_path_to_string(("inputfile", "outputfile"))
def ffmpeg_resize(inputfile, outputfile, size, logger="bar"):
    """Resizes a file to new size and write the result in another.

    Parameters
    ----------

    inputfile : str
      Path to the file to be resized.

    outputfile : str
      Path to the output file.

    size : list or tuple
      New size in format ``[width, height]`` for the output file.
    """
    cmd = [
        FFMPEG_BINARY,
        "-i",
        ffmpeg_escape_filename(inputfile),
        "-vf",
        "scale=%d:%d" % (size[0], size[1]),
        ffmpeg_escape_filename(outputfile),
    ]

    subprocess_call(cmd, logger=logger)


@convert_path_to_string(("inputfile", "outputfile", "output_dir"))
def ffmpeg_stabilize_video(
    inputfile, outputfile=None, output_dir="", overwrite_file=True, logger="bar"
):
    """
    Stabilizes ``filename`` and write the result to ``output``.

    Parameters
    ----------

    inputfile : str
      The name of the shaky video.

    outputfile : str, optional
      The name of new stabilized video. Defaults to appending '_stabilized' to
      the input file name.

    output_dir : str, optional
      The directory to place the output video in. Defaults to the current
      working directory.

    overwrite_file : bool, optional
      If ``outputfile`` already exists in ``output_dir``, then overwrite
      ``outputfile`` Defaults to True.
    """
    if not outputfile:
        without_dir = os.path.basename(inputfile)
        name, ext = os.path.splitext(without_dir)
        outputfile = f"{name}_stabilized{ext}"

    outputfile = os.path.join(output_dir, outputfile)
    cmd = [
        FFMPEG_BINARY,
        "-i",
        ffmpeg_escape_filename(inputfile),
        "-vf",
        "deshake",
        ffmpeg_escape_filename(outputfile),
    ]

    if overwrite_file:
        cmd.append("-y")

    subprocess_call(cmd, logger=logger)


@convert_path_to_string(("input_file", "output_file"))
def ffmpeg_copy(input_file, output_file):
    """
    Re-mix a video file using ffmpeg.
    This may fix issues with corrupted video file.

    Parameters
    ----------
    input_file : str or Path file that will be re-encoded
    output_file: str or Path path to save the re-encoded file

    Returns
    -------
    None
    """
    # Convert input and output files to Path objects
    input_path = Path(input_file).resolve()
    output_path = Path(output_file).resolve()

    # Check if the input file exists
    if not input_path.exists():
        raise FileNotFoundError(f"Input file '{input_file}' not found.")

    try:
        # Construct the ffmpeg command
        command = [
            FFMPEG_BINARY,
            "-y",
            "-i",
            str(input_path),
            "-c",
            "copy",  # Copy streams without re-encoding
            str(output_path),
        ]

        # Run the command
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        raise IOError(f"Error: ffmpeg command failed with error {e}") from e


def ffmpeg_version():
    """
    Retrieve the FFmpeg version.

    This function retrieves both the full and numeric version of FFmpeg
    by executing the `ffmpeg -version` command. The full version includes
    additional details like build information, while the numeric version
    contains only the version numbers (e.g., '7.0.2').

    Return
    ------
    tuple
        A tuple containing:
        - `full_version` (str): The complete version string (e.g., '7.0.2-static').
        - `numeric_version` (str): The numeric version string (e.g., '7.0.2').

    Example
    -------
    >>> ffmpeg_version()
    ('7.0.2-static', '7.0.2')

    Raises
    ------
    subprocess.CalledProcessError
        If the FFmpeg command fails to execute properly.
    """
    cmd = [
        FFMPEG_BINARY,
        "-version",
        "-v",
        "quiet",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, check=True)

    # Extract the version number from the first line of output
    full_version = result.stdout.splitlines()[0].split()[2]
    numeric_version = re.match(r"^[0-9.]+", full_version).group(0)
    return (full_version, numeric_version)


def ffplay_version():
    """
    Retrieve the FFplay version.

    This function retrieves both the full and numeric version of FFplay
    by executing the `ffplay -version` command. The full version includes
    additional details like build information, while the numeric version
    contains only the version numbers (e.g., '6.0.1').

    Return
    ------
    tuple
        A tuple containing:
        - `full_version` (str): The complete version string (e.g., '6.0.1-static').
        - `numeric_version` (str): The numeric version string (e.g., '6.0.1').

    Example
    -------
    >>> ffplay_version()
    ('6.0.1-static', '6.0.1')

    Raises
    ------
    subprocess.CalledProcessError
        If the FFplay command fails to execute properly.
    """
    cmd = [
        FFPLAY_BINARY,
        "-version",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    # Extract the version number from the first line of output
    full_version = result.stdout.splitlines()[0].split()[2]
    numeric_version = re.match(r"^[0-9.]+", full_version).group(0)
    return (full_version, numeric_version)
````

## File: moviepy/video/io/ffmpeg_writer.py
````python
"""
On the long term this will implement several methods to make videos
out of VideoClips
"""

import subprocess as sp

import numpy as np
from proglog import proglog

from moviepy.config import FFMPEG_BINARY
from moviepy.tools import cross_platform_popen_params, ffmpeg_escape_filename


class FFMPEG_VideoWriter:
    """A class for FFMPEG-based video writing.

    Parameters
    ----------

    filename : str
      Any filename like ``"video.mp4"`` etc. but if you want to avoid
      complications it is recommended to use the generic extension ``".avi"``
      for all your videos.

    size : tuple or list
      Size of the output video in pixels (width, height).

    fps : int
      Frames per second in the output video file.

    codec : str, optional
      FFMPEG codec. It seems that in terms of quality the hierarchy is
      'rawvideo' = 'png' > 'mpeg4' > 'libx264'
      'png' manages the same lossless quality as 'rawvideo' but yields
      smaller files. Type ``ffmpeg -codecs`` in a terminal to get a list
      of accepted codecs.

      Note for default 'libx264': by default the pixel format yuv420p
      is used. If the video dimensions are not both even (e.g. 720x405)
      another pixel format is used, and this can cause problem in some
      video readers.

    audiofile : str, optional
      The name of an audio file that will be incorporated to the video.

    audio_codec : str, optional
      FFMPEG audio codec. If None, ``"copy"`` codec is used.

    preset : str, optional
      Sets the time that FFMPEG will take to compress the video. The slower,
      the better the compression rate. Possibilities are: ``"ultrafast"``,
      ``"superfast"``, ``"veryfast"``, ``"faster"``, ``"fast"``,  ``"medium"``
      (default), ``"slow"``, ``"slower"``, ``"veryslow"``, ``"placebo"``.

    bitrate : str, optional
      Only relevant for codecs which accept a bitrate. "5000k" offers
      nice results in general.

    with_mask : bool, optional
      Set to ``True`` if there is a mask in the video to be encoded.

    pixel_format : str, optional
      Optional: Pixel format for the output video file. If is not specified
      ``"rgb24"`` will be used as the default format unless ``with_mask`` is
      set as ``True``, then ``"rgba"`` will be used.

    logfile : int, optional
      File descriptor for logging output. If not defined, ``subprocess.PIPE``
      will be used. Defined using another value, the log level of the ffmpeg
      command will be "info", otherwise "error".

    threads : int, optional
      Number of threads used to write the output with ffmpeg.

    ffmpeg_params : list, optional
      Additional parameters passed to ffmpeg command.

    print_cmd : bool, optional
      If set to ``True``, the ffmpeg command used to write the video will be
      printed to the console. This can be useful for debugging purposes.
      Default is ``False``.
    """

    def __init__(
        self,
        filename,
        size,
        fps,
        codec="libx264",
        audiofile=None,
        audio_codec=None,
        preset="medium",
        bitrate=None,
        with_mask=False,
        logfile=None,
        threads=None,
        ffmpeg_params=None,
        pixel_format=None,
        print_cmd=False,
    ):
        if logfile is None:
            logfile = sp.PIPE
        self.logfile = logfile
        self.filename = filename
        self.codec = codec
        self.audio_codec = audio_codec
        self.ext = self.filename.split(".")[-1]

        input_pixel_format = "rgba" if with_mask else "rgb24"

        # order is important
        cmd = [
            FFMPEG_BINARY,
            "-y",
            "-loglevel",
            "error" if logfile == sp.PIPE else "info",
            "-f",
            "rawvideo",
            "-vcodec",
            "rawvideo",
            "-s",
            "%dx%d" % (size[0], size[1]),
            "-pix_fmt",
            input_pixel_format,
            "-r",
            "%.02f" % fps,
            "-an",
            "-i",
            "-",
        ]
        if audiofile is not None:
            if audio_codec is None:
                audio_codec = "copy"
            cmd.extend(["-i", audiofile, "-acodec", audio_codec])

        if codec == "h264_nvenc":
            cmd.extend(["-c:v", codec])
        else:
            cmd.extend(["-vcodec", codec])

        cmd.extend(["-preset", preset])

        if ffmpeg_params is not None:
            cmd.extend(ffmpeg_params)

        if bitrate is not None:
            cmd.extend(["-b", bitrate])

        if threads is not None:
            cmd.extend(["-threads", str(threads)])

        # Disable auto alt ref for transparent webm and set pix format to yuva420p
        if codec == "libvpx" and with_mask:
            cmd.extend(["-pix_fmt", "yuva420p"])
            cmd.extend(["-auto-alt-ref", "0"])
        elif (
            (codec == "libx264" or codec == "h264_nvenc")
            and (size[0] % 2 == 0)
            and (size[1] % 2 == 0)
        ):
            cmd.extend(["-pix_fmt", "yuva420p"])
        else:
            # For all other codecs, we use the pixel format specified by the user
            # or the default one.
            if pixel_format is None:
                pixel_format = "rgba" if with_mask else "rgb24"
            cmd.extend(["-pix_fmt", pixel_format])

        cmd.extend([ffmpeg_escape_filename(filename)])

        if print_cmd:
            print("FFMPEG command:", " ".join(cmd))

        popen_params = cross_platform_popen_params(
            {"stdout": sp.DEVNULL, "stderr": logfile, "stdin": sp.PIPE}
        )

        self.proc = sp.Popen(cmd, **popen_params)

    def write_frame(self, img_array):
        """Writes one frame in the file."""
        try:
            # ffmpeg expects the data to be in C order, so we ensure that
            # the input array is contiguous in memory.
            if not img_array.flags["C_CONTIGUOUS"]:
                img_array = img_array.copy(order="C")

            self.proc.stdin.write(img_array)
        except IOError as err:
            _, ffmpeg_error = self.proc.communicate()
            if ffmpeg_error is not None:
                ffmpeg_error = ffmpeg_error.decode()
            else:
                # The error was redirected to a logfile with `write_logfile=True`,
                # so read the error from that file instead
                self.logfile.seek(0)
                ffmpeg_error = self.logfile.read()

            error = (
                f"{err}\n\nMoviePy error: FFMPEG encountered the following error while "
                f"writing file {self.filename}: \n\n {ffmpeg_error}"
            )

            if "Unknown encoder" in ffmpeg_error or "Unknown decoder" in ffmpeg_error:
                error += (
                    "\n\nThe video export failed because FFMPEG didn't find the "
                    "specified codec for video or audio. "
                    "Please install this codec or change the codec when calling "
                    "write_videofile.\nFor instance:\n"
                    "  >>> clip.write_videofile('myvid.webm', audio='myaudio.mp3', "
                    "codec='libvpx', audio_codec='aac')"
                )

            elif "incorrect codec parameters ?" in ffmpeg_error:
                error += (
                    "\n\nThe video export failed, possibly because the codec "
                    f"specified for the video {self.codec} is not compatible with "
                    f"the given extension {self.ext}.\n"
                    "Please specify a valid 'codec' argument in write_videofile.\n"
                    "This would be 'libx264' or 'mpeg4' for mp4, "
                    "'libtheora' for ogv, 'libvpx for webm.\n"
                    "Another possible reason is that the audio codec was not "
                    "compatible with the video codec. For instance, the video "
                    "extensions 'ogv' and 'webm' only allow 'libvorbis' (default) as a"
                    "video codec."
                )

            elif "bitrate not specified" in ffmpeg_error:
                error += (
                    "\n\nThe video export failed, possibly because the bitrate "
                    "specified was too high or too low for the video codec."
                )

            elif "Invalid encoder type" in ffmpeg_error:
                error += (
                    "\n\nThe video export failed because the codec "
                    "or file extension you provided is not suitable for video"
                )

            raise IOError(error)

    def close(self):
        """Closes the writer, terminating the subprocess if is still alive."""
        if self.proc:
            self.proc.stdin.close()
            if self.proc.stderr is not None:
                self.proc.stderr.close()
            self.proc.wait()

            self.proc = None

    # Support the Context Manager protocol, to ensure that resources are cleaned up.

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


def ffmpeg_write_video(
    clip,
    filename,
    fps,
    codec="libx264",
    bitrate=None,
    preset="medium",
    write_logfile=False,
    audiofile=None,
    audio_codec=None,
    threads=None,
    ffmpeg_params=None,
    logger="bar",
    pixel_format=None,
):
    """Write the clip to a videofile. See VideoClip.write_videofile for details
    on the parameters.
    """
    logger = proglog.default_bar_logger(logger)

    if write_logfile:
        logfile = open(filename + ".log", "w+")
    else:
        logfile = None

    logger(message="MoviePy - Writing video %s\n" % filename)

    has_mask = clip.mask is not None

    with FFMPEG_VideoWriter(
        filename,
        clip.size,
        fps,
        codec=codec,
        preset=preset,
        bitrate=bitrate,
        with_mask=has_mask,
        logfile=logfile,
        audiofile=audiofile,
        audio_codec=audio_codec,
        threads=threads,
        ffmpeg_params=ffmpeg_params,
        pixel_format=pixel_format,
    ) as writer:
        for t, frame in clip.iter_frames(
            logger=logger, with_times=True, fps=fps, dtype="uint8"
        ):
            if clip.mask is not None:
                mask = 255 * clip.mask.get_frame(t)
                if mask.dtype != "uint8":
                    mask = mask.astype("uint8")
                frame = np.dstack([frame, mask])

            writer.write_frame(frame)

    if write_logfile:
        logfile.close()
    logger(message="MoviePy - Done !")


def ffmpeg_write_image(filename, image, logfile=False, pixel_format=None):
    """Writes an image (HxWx3 or HxWx4 numpy array) to a file, using ffmpeg.

    Parameters
    ----------

    filename : str
        Path to the output file.

    image : np.ndarray
        Numpy array with the image data.

    logfile : bool, optional
        Writes the ffmpeg output inside a logging file (``True``) or not
        (``False``).

    pixel_format : str, optional
        Pixel format for ffmpeg. If not defined, it will be discovered checking
        if the image data contains an alpha channel (``"rgba"``) or not
        (``"rgb24"``).
    """
    if image.dtype != "uint8":
        image = image.astype("uint8")

    if not pixel_format:
        pixel_format = "rgba" if (image.shape[2] == 4) else "rgb24"

    cmd = [
        FFMPEG_BINARY,
        "-y",
        "-s",
        "%dx%d" % (image.shape[:2][::-1]),
        "-f",
        "rawvideo",
        "-pix_fmt",
        pixel_format,
        "-i",
        "-",
        ffmpeg_escape_filename(filename),
    ]

    if logfile:
        log_file = open(filename + ".log", "w+")
    else:
        log_file = sp.PIPE

    popen_params = cross_platform_popen_params(
        {"stdout": sp.DEVNULL, "stderr": log_file, "stdin": sp.PIPE}
    )

    proc = sp.Popen(cmd, **popen_params)
    out, err = proc.communicate(image.tobytes())

    if proc.returncode:
        error = (
            f"{err}\n\nMoviePy error: FFMPEG encountered the following error while "
            f"writing file {filename} with command {cmd}: \n\n {err.decode()}"
        )

        raise IOError(error)

    del proc
````

## File: moviepy/video/io/ffplay_previewer.py
````python
"""
On the long term this will implement several methods to make videos
out of VideoClips
"""

import subprocess as sp

from moviepy.config import FFPLAY_BINARY
from moviepy.tools import cross_platform_popen_params


class FFPLAY_VideoPreviewer:
    """A class for FFPLAY-based video preview.

    Parameters
    ----------

    size : tuple or list
      Size of the output video in pixels (width, height).

    fps : int
      Frames per second in the output video file.

    pixel_format : str
      Pixel format for the output video file, ``rgb24`` for normal video, ``rgba``
      if video with mask.
    """

    def __init__(
        self,
        size,
        fps,
        pixel_format,
    ):
        # order is important
        cmd = [
            FFPLAY_BINARY,
            "-autoexit",  # If you don't precise, ffplay won't stop at end
            "-f",
            "rawvideo",
            "-pixel_format",
            pixel_format,
            "-video_size",
            "%dx%d" % (size[0], size[1]),
            "-framerate",
            "%.02f" % fps,
            "-",
        ]

        popen_params = cross_platform_popen_params(
            {"stdout": sp.DEVNULL, "stderr": sp.STDOUT, "stdin": sp.PIPE}
        )

        self.proc = sp.Popen(cmd, **popen_params)

    def show_frame(self, img_array):
        """Writes one frame in the file."""
        try:
            self.proc.stdin.write(img_array.tobytes())
        except IOError as err:
            _, ffplay_error = self.proc.communicate()
            if ffplay_error is not None:
                ffplay_error = ffplay_error.decode()

            error = (
                f"{err}\n\nMoviePy error: FFPLAY encountered the following error while "
                f"previewing clip :\n\n {ffplay_error}"
            )

            raise IOError(error)

    def close(self):
        """Closes the writer, terminating the subprocess if is still alive."""
        if self.proc:
            self.proc.stdin.close()
            if self.proc.stderr is not None:
                self.proc.stderr.close()
            self.proc.wait()

            self.proc = None

    # Support the Context Manager protocol, to ensure that resources are cleaned up.

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


def ffplay_preview_video(
    clip, fps, pixel_format="rgb24", audio_flag=None, video_flag=None
):
    """Preview the clip using ffplay. See VideoClip.preview for details
    on the parameters.

    Parameters
    ----------

    clip : VideoClip
      The clip to preview

    fps : int
      Number of frames per seconds in the displayed video.

    pixel_format : str, optional
      Warning: This is not used anywhere in the code and should probably
      be removed.
      It is believed pixel format rgb24 does not work properly for now because
      it requires applying a mask on CompositeVideoClip and that is believed to
      not be working.

      Pixel format for the output video file, ``rgb24`` for normal video, ``rgba``
      if video with mask

    audio_flag : Thread.Event, optional
      A thread event that video will wait for. If not provided we ignore audio

    video_flag : Thread.Event, optional
      A thread event that video will set after first frame has been shown. If not
      provided, we simply ignore
    """
    with FFPLAY_VideoPreviewer(clip.size, fps, pixel_format) as previewer:
        first_frame = True
        for t, frame in clip.iter_frames(with_times=True, fps=fps, dtype="uint8"):
            previewer.show_frame(frame)

            # After first frame is shown, if we have audio/video flag, set video ready
            # and wait for audio
            if first_frame:
                first_frame = False

                if video_flag:
                    video_flag.set()  # say to the audio: video is ready

                if audio_flag:
                    audio_flag.wait()  # wait for the audio to be ready
````

## File: moviepy/video/io/gif_writers.py
````python
"""MoviePy video GIFs writing."""

import imageio.v3 as iio
import proglog

from moviepy.decorators import requires_duration, use_clip_fps_by_default


@requires_duration
@use_clip_fps_by_default
def write_gif_with_imageio(clip, filename, fps=None, loop=0, logger="bar"):
    """Writes the gif with the Python library ImageIO (calls FreeImage)."""
    logger = proglog.default_bar_logger(logger)

    with iio.imopen(filename, "w", plugin="pillow") as writer:
        logger(message="MoviePy - Building file %s with imageio." % filename)
        for frame in clip.iter_frames(fps=fps, logger=logger, dtype="uint8"):
            writer.write(
                frame, duration=1000 / fps, loop=loop
            )  # Duration is in ms not s
````

## File: moviepy/video/io/ImageSequenceClip.py
````python
"""Implements ImageSequenceClip, a class to create a video clip from a set
of image files.
"""

import os

import numpy as np
from imageio.v2 import imread

from moviepy.video.VideoClip import VideoClip


class ImageSequenceClip(VideoClip):
    """A VideoClip made from a series of images.

    Parameters
    ----------

    sequence
      Can be one of these:

      - The name of a folder (containing only pictures). The pictures
        will be considered in alphanumerical order.
      - A list of names of image files. In this case you can choose to
        load the pictures in memory pictures
      - A list of Numpy arrays representing images.

    fps
      Number of picture frames to read per second. Instead, you can provide
      the duration of each image with durations (see below)

    durations
      List of the duration of each picture.

    with_mask
      Should the alpha layer of PNG images be considered as a mask ?

    is_mask
      Will this sequence of pictures be used as an animated mask.

    load_images
      Specify that all images should be loaded into the RAM. This is only
      interesting if you have a small number of images that will be used
      more than once.
    """

    def __init__(
        self,
        sequence,
        fps=None,
        durations=None,
        with_mask=True,
        is_mask=False,
        load_images=False,
    ):
        # CODE WRITTEN AS IT CAME, MAY BE IMPROVED IN THE FUTURE

        if (fps is None) and (durations is None):
            raise ValueError("Please provide either 'fps' or 'durations'.")
        VideoClip.__init__(self, is_mask=is_mask)

        # Parse the data

        self.fromfiles = True

        if isinstance(sequence, list):
            if isinstance(sequence[0], str):
                if load_images:
                    sequence = [imread(file) for file in sequence]
                    self.fromfiles = False
            else:
                # sequence is already a list of numpy arrays
                self.fromfiles = False
        else:
            # sequence is a folder name, make it a list of files:
            sequence = sorted(
                [os.path.join(sequence, file) for file in os.listdir(sequence)]
            )

        # check that all the images are of the same size
        if isinstance(sequence[0], str):
            size = imread(sequence[0]).shape
        else:
            size = sequence[0].shape

        for image in sequence:
            image1 = image
            if isinstance(image, str):
                image1 = imread(image)
            if size != image1.shape:
                raise Exception(
                    "MoviePy: ImageSequenceClip requires all images to be the same size"
                )

        self.fps = fps
        if fps is not None:
            durations = [1.0 / fps for image in sequence]
            self.images_starts = [
                1.0 * i / fps - np.finfo(np.float32).eps for i in range(len(sequence))
            ]
        else:
            self.images_starts = [0] + list(np.cumsum(durations))
        self.durations = durations
        self.duration = sum(durations)
        self.end = self.duration
        self.sequence = sequence

        if fps is None:
            self.fps = len(sequence) / self.duration

        if self.fromfiles:
            self.last_index = None
            self.last_image = None

            if with_mask and (imread(self.sequence[0]).shape[2] == 4):
                self.mask = ImageSequenceClip(
                    sequence=sequence,
                    fps=fps,
                    durations=durations,
                    with_mask=False,
                    is_mask=True,
                    load_images=load_images,
                )

        else:
            if with_mask and (self.sequence[0].shape[2] == 4):
                self.mask = ImageSequenceClip(
                    sequence=sequence,
                    fps=fps,
                    durations=durations,
                    with_mask=False,
                    is_mask=True,
                    load_images=load_images,
                )

        self.size = self.frame_function(0).shape[:2][::-1]

    def _find_image_index(self, t):
        return max([i for i in range(len(self.sequence)) if self.images_starts[i] <= t])

    def frame_function(self, t):
        """Retrieves the frame corresponding to the given time `t`.

        Depending on whether the frames are loaded from files or provided as
        an in-memory sequence, this function either reads the frame from disk
        or accesses it directly from the sequence.

        Parameters
        ----------

        t (float): The time (in seconds) for which the corresponding frame
            is to be retrieved.

        Returns
        -------

        numpy.ndarray: The image frame at the specified time. If `is_mask`
            is True, the alpha channel of the image is returned
            as a float array normalized to the range [0, 1].
            Otherwise, the RGB channels of the image are returned.

        """
        index = self._find_image_index(t)

        if self.fromfiles:
            self.last_index = index

            if self.is_mask:
                self.last_image = (
                    imread(self.sequence[index])[:, :, 3].astype(float) / 255.0
                )
            else:
                self.last_image = imread(self.sequence[index])[:, :, :3]

            return self.last_image
        else:
            if self.is_mask:
                return self.sequence[index][:, :, 3].astype(float) / 255.0
            else:
                return self.sequence[index][:, :, :3]
````

## File: moviepy/video/io/VideoFileClip.py
````python
"""Implements VideoFileClip, a class for video clips creation using video files."""

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.decorators import convert_path_to_string
from moviepy.video.io.ffmpeg_reader import FFMPEG_VideoReader
from moviepy.video.VideoClip import VideoClip


class VideoFileClip(VideoClip):
    """A video clip originating from a movie file. For instance:

    .. code:: python

        clip = VideoFileClip("myHolidays.mp4")
        clip.close()
        with VideoFileClip("myMaskVideo.avi") as clip2:
            pass  # Implicit close called by context manager.


    Parameters
    ----------

    filename:
      The name of the video file, as a string or a path-like object.
      It can have any extension supported by ffmpeg:
      .ogv, .mp4, .mpeg, .avi, .mov etc.

    has_mask:
      Set this to 'True' if there is a mask included in the videofile.
      Video files rarely contain masks, but some video codecs enable
      that. For instance if you have a MoviePy VideoClip with a mask you
      can save it to a videofile with a mask. (see also
      ``VideoClip.write_videofile`` for more details).

    audio:
      Set to `False` if the clip doesn't have any audio or if you do not
      wish to read the audio.

    target_resolution:
      Set to (desired_width, desired_height) to have ffmpeg resize the frames
      before returning them. This is much faster than streaming in high-res
      and then resizing. If either dimension is None, the frames are resized
      by keeping the existing aspect ratio.

    resize_algorithm:
      The algorithm used for resizing. Default: "bicubic", other popular
      options include "bilinear" and "fast_bilinear". For more information, see
      https://ffmpeg.org/ffmpeg-scaler.html

    fps_source:
      The fps value to collect from the metadata. Set by default to 'fps', but
      can be set to 'tbr', which may be helpful if you are finding that it is reading
      the incorrect fps from the file.

    pixel_format
      Optional: Pixel format for the video to read. If is not specified
      'rgb24' will be used as the default format unless ``has_mask`` is set
      as ``True``, then 'rgba' will be used.

    is_mask
      `True` if the clip is going to be used as a mask.

    audio_stream_index
      The index of the audio stream to read from the file.


    Attributes
    ----------

    filename:
      Name of the original video file.

    fps:
      Frames per second in the original file.


    Read docs for Clip() and VideoClip() for other, more generic, attributes.

    Lifetime
    --------

    Note that this creates subprocesses and locks files. If you construct one
    of these instances, you must call close() afterwards, or the subresources
    will not be cleaned up until the process ends.

    If copies are made, and close() is called on one, it may cause methods on
    the other copies to fail.
    """

    @convert_path_to_string("filename")
    def __init__(
        self,
        filename,
        decode_file=False,
        has_mask=False,
        audio=True,
        audio_buffersize=200000,
        target_resolution=None,
        resize_algorithm="bicubic",
        audio_fps=44100,
        audio_nbytes=2,
        fps_source="fps",
        pixel_format=None,
        is_mask=False,
        audio_stream_index=0,
    ):
        VideoClip.__init__(self, is_mask=is_mask)

        # Make a reader
        if not pixel_format:
            pixel_format = "rgba" if has_mask else "rgb24"

        self.reader = FFMPEG_VideoReader(
            filename,
            decode_file=decode_file,
            pixel_format=pixel_format,
            target_resolution=target_resolution,
            resize_algo=resize_algorithm,
            fps_source=fps_source,
        )

        # Make some of the reader's attributes accessible from the clip
        self.duration = self.reader.duration
        self.end = self.reader.duration

        self.fps = self.reader.fps
        self.size = self.reader.size
        self.rotation = self.reader.rotation

        self.filename = filename

        if has_mask:
            self.frame_function = lambda t: self.reader.get_frame(t)[:, :, :3]

            def mask_frame_function(t):
                return self.reader.get_frame(t)[:, :, 3] / 255.0

            self.mask = VideoClip(
                is_mask=True, frame_function=mask_frame_function
            ).with_duration(self.duration)
            self.mask.fps = self.fps

        else:
            self.frame_function = lambda t: self.reader.get_frame(t)

        # Make a reader for the audio, if any.
        if audio and self.reader.infos["audio_found"]:
            self.audio = AudioFileClip(
                filename,
                buffersize=audio_buffersize,
                fps=audio_fps,
                nbytes=audio_nbytes,
                audio_stream_index=audio_stream_index,
            )

    def __deepcopy__(self, memo):
        """Implements ``copy.deepcopy(clip)`` behaviour as ``copy.copy(clip)``.

        VideoFileClip class instances can't be deeply copied because the locked Thread
        of ``proc`` isn't pickleable. Without this override, calls to
        ``copy.deepcopy(clip)`` would raise a ``TypeError``:

        ```
        TypeError: cannot pickle '_thread.lock' object
        ```
        """
        return self.__copy__()

    def close(self):
        """Close the internal reader."""
        if self.reader:
            self.reader.close()
            self.reader = None

        try:
            if self.audio:
                self.audio.close()
                self.audio = None
        except AttributeError:  # pragma: no cover
            pass
````

## File: moviepy/video/tools/credits.py
````python
"""Contains different functions to make end and opening credits, even though it is
difficult to fill everyone needs in this matter.
"""

from moviepy.decorators import convert_path_to_string
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.Resize import Resize
from moviepy.video.VideoClip import ImageClip, TextClip


class CreditsClip(TextClip):
    """Credits clip.

    Parameters
    ----------

    creditfile
      A string or path like object pointing to a text file
      whose content must be as follows:

      ..code:: python

          # This is a comment
          # The next line says : leave 4 blank lines
          .blank 4

          ..Executive Story Editor
          MARCEL DURAND

          ..Associate Producers
          MARTIN MARCEL
          DIDIER MARTIN

          ..Music Supervisor
          JEAN DIDIER

    width
      Total width of the credits text in pixels

    gap
      Horizontal gap in pixels between the jobs and the names

    color
      Color of the text. See ``TextClip.list('color')``
      for a list of acceptable names.

    font
      Name of the font to use. See ``TextClip.list('font')`` for
      the list of fonts you can use on your computer.

    font_size
      Size of font to use

    stroke_color
      Color of the stroke (=contour line) of the text. If ``None``,
      there will be no stroke.

    stroke_width
      Width of the stroke, in pixels. Can be a float, like 1.5.

    bg_color
      Color of the background. If ``None``, the background will be transparent.

    Returns
    -------

    image
      An ImageClip instance that looks like this and can be scrolled
      to make some credits: ::

          Executive Story Editor    MARCEL DURAND
             Associate Producers    MARTIN MARCEL
                                    DIDIER MARTIN
                Music Supervisor    JEAN DIDIER

    """

    @convert_path_to_string("creditfile")
    def __init__(
        self,
        creditfile,
        width,
        color="white",
        stroke_color="black",
        stroke_width=2,
        font="Impact-Normal",
        font_size=60,
        bg_color=None,
        gap=0,
    ):
        # Parse the .txt file
        texts = []
        one_line = True

        with open(creditfile) as file:
            for line in file:
                if line.startswith(("\n", "#")):
                    # exclude blank lines or comments
                    continue
                elif line.startswith(".blank"):
                    # ..blank n
                    for i in range(int(line.split(" ")[1])):
                        texts.append(["\n", "\n"])
                elif line.startswith(".."):
                    texts.append([line[2:], ""])
                    one_line = True
                elif one_line:
                    texts.append(["", line])
                    one_line = False
                else:
                    texts.append(["\n", line])

        left, right = ("".join(line) for line in zip(*texts))

        # Make two columns for the credits
        left, right = [
            TextClip(
                text=txt,
                color=color,
                stroke_color=stroke_color,
                stroke_width=stroke_width,
                font=font,
                font_size=font_size,
                text_align=align,
            )
            for txt, align in [(left, "left"), (right, "right")]
        ]

        both_columns = CompositeVideoClip(
            [left, right.with_position((left.w + gap, 0))],
            size=(left.w + right.w + gap, right.h),
            bg_color=bg_color,
        )

        # Scale to the required size
        scaled = both_columns.with_effects([Resize(width=width)])

        # Transform the CompositeVideoClip into an ImageClip

        # Calls ImageClip.__init__()
        super(TextClip, self).__init__(scaled.get_frame(0))
        self.mask = ImageClip(scaled.mask.get_frame(0), is_mask=True)
````

## File: moviepy/video/tools/cuts.py
````python
"""Contains everything that can help automate the cuts in MoviePy."""

from collections import defaultdict

import numpy as np

from moviepy.decorators import convert_parameter_to_seconds, use_clip_fps_by_default


@use_clip_fps_by_default
@convert_parameter_to_seconds(["start_time"])
def find_video_period(clip, fps=None, start_time=0.3):
    """Find the period of a video based on frames correlation.

    Parameters
    ----------

    clip : moviepy.Clip.Clip
      Clip for which the video period will be computed.

    fps : int, optional
      Number of frames per second used computing the period. Higher values will
      produce more accurate periods, but the execution time will be longer.

    start_time : float, optional
      First timeframe used to calculate the period of the clip.

    Examples
    --------

    .. code:: python

        from moviepy import *
        from moviepy.video.tools.cuts import find_video_period

        clip = VideoFileClip("media/chaplin.mp4").subclipped(0, 1).loop(2)
        round(videotools.find_video_period(clip, fps=80), 6)
        1
    """

    def frame(t):
        return clip.get_frame(t).flatten()

    timings = np.arange(start_time, clip.duration, 1 / fps)[1:]
    ref = frame(0)
    corrs = [np.corrcoef(ref, frame(t))[0, 1] for t in timings]
    return timings[np.argmax(corrs)]


class FramesMatch:
    """Frames match inside a set of frames.

    Parameters
    ----------

    start_time : float
      Starting time.

    end_time : float
      End time.

    min_distance : float
      Lower bound on the distance between the first and last frames

    max_distance : float
      Upper bound on the distance between the first and last frames
    """

    def __init__(self, start_time, end_time, min_distance, max_distance):
        self.start_time = start_time
        self.end_time = end_time
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.time_span = end_time - start_time

    def __str__(self):  # pragma: no cover
        return "(%.04f, %.04f, %.04f, %.04f)" % (
            self.start_time,
            self.end_time,
            self.min_distance,
            self.max_distance,
        )

    def __repr__(self):  # pragma: no cover
        return self.__str__()

    def __iter__(self):  # pragma: no cover
        return iter(
            (self.start_time, self.end_time, self.min_distance, self.max_distance)
        )

    def __eq__(self, other):
        return (
            other.start_time == self.start_time
            and other.end_time == self.end_time
            and other.min_distance == self.min_distance
            and other.max_distance == self.max_distance
        )


class FramesMatches(list):
    """Frames matches inside a set of frames.

    You can instantiate it passing a list of FramesMatch objects or
    using the class methods ``load`` and ``from_clip``.

    Parameters
    ----------

    lst : list
      Iterable of FramesMatch objects.
    """

    def __init__(self, lst):
        list.__init__(self, sorted(lst, key=lambda e: e.max_distance))

    def best(self, n=1, percent=None):
        """Returns a new instance of FramesMatches object or a FramesMatch
        from the current class instance given different conditions.

        By default returns the first FramesMatch that the current instance
        stores.

        Parameters
        ----------

        n : int, optional
          Number of matches to retrieve from the current FramesMatches object.
          Only has effect when ``percent=None``.

        percent : float, optional
          Percent of the current match to retrieve.

        Returns
        -------

        FramesMatch or FramesMatches : If the number of matches to retrieve is
          greater than 1 returns a FramesMatches object, otherwise a
          FramesMatch.

        """
        if percent is not None:
            n = len(self) * percent / 100
        return self[0] if n == 1 else FramesMatches(self[: int(n)])

    def filter(self, condition):
        """Return a FramesMatches object obtained by filtering out the
        FramesMatch which do not satistify a condition.

        Parameters
        ----------

        condition : func
          Function which takes a FrameMatch object as parameter and returns a
          bool.

        Examples
        --------
        .. code:: python

            # Only keep the matches corresponding to (> 1 second) sequences.
            new_matches = matches.filter(lambda match: match.time_span > 1)
        """
        return FramesMatches(filter(condition, self))

    def save(self, filename):
        """Save a FramesMatches object to a file.

        Parameters
        ----------

        filename : str
          Path to the file in which will be dumped the FramesMatches object data.
        """
        np.savetxt(
            filename,
            np.array([np.array(list(e)) for e in self]),
            fmt="%.03f",
            delimiter="\t",
        )

    @staticmethod
    def load(filename):
        """Load a FramesMatches object from a file.

        Parameters
        ----------

        filename : str
          Path to the file to use loading a FramesMatches object.

        Examples
        --------
        >>> matching_frames = FramesMatches.load("somefile")
        """
        arr = np.loadtxt(filename)
        mfs = [FramesMatch(*e) for e in arr]
        return FramesMatches(mfs)

    @staticmethod
    def from_clip(clip, distance_threshold, max_duration, fps=None, logger="bar"):
        """Finds all the frames that look alike in a clip, for instance to make
        a looping GIF.

        Parameters
        ----------

        clip : moviepy.video.VideoClip.VideoClip
          A MoviePy video clip.

        distance_threshold : float
          Distance above which a match is rejected.

        max_duration : float
          Maximal duration (in seconds) between two matching frames.

        fps : int, optional
          Frames per second (default will be ``clip.fps``).

        logger : str, optional
          Either ``"bar"`` for progress bar or ``None`` or any Proglog logger.

        Returns
        -------

        FramesMatches
            All pairs of frames with ``end_time - start_time < max_duration``
            and whose distance is under ``distance_threshold``.

        Examples
        --------

        We find all matching frames in a given video and turn the best match
        with a duration of 1.5 seconds or more into a GIF:

        .. code:: python

            from moviepy import VideoFileClip
            from moviepy.video.tools.cuts import FramesMatches

            clip = VideoFileClip("foo.mp4").resize(width=200)
            matches = FramesMatches.from_clip(
                clip, distance_threshold=10, max_duration=3,  # will take time
            )
            best = matches.filter(lambda m: m.time_span > 1.5).best()
            clip.subclipped(best.start_time, best.end_time).write_gif("foo.gif")
        """
        N_pixels = clip.w * clip.h * 3

        def dot_product(F1, F2):
            return (F1 * F2).sum() / N_pixels

        frame_dict = {}  # will store the frames and their mutual distances

        def distance(t1, t2):
            uv = dot_product(frame_dict[t1]["frame"], frame_dict[t2]["frame"])
            u, v = frame_dict[t1]["|F|sq"], frame_dict[t2]["|F|sq"]
            return np.sqrt(u + v - 2 * uv)

        matching_frames = []  # the final result.

        for t, frame in clip.iter_frames(with_times=True, logger=logger):
            flat_frame = 1.0 * frame.flatten()
            F_norm_sq = dot_product(flat_frame, flat_frame)
            F_norm = np.sqrt(F_norm_sq)

            for t2 in list(frame_dict.keys()):
                # forget old frames, add 't' to the others frames
                # check for early rejections based on differing norms
                if (t - t2) > max_duration:
                    frame_dict.pop(t2)
                else:
                    frame_dict[t2][t] = {
                        "min": abs(frame_dict[t2]["|F|"] - F_norm),
                        "max": frame_dict[t2]["|F|"] + F_norm,
                    }
                    frame_dict[t2][t]["rejected"] = (
                        frame_dict[t2][t]["min"] > distance_threshold
                    )

            t_F = sorted(frame_dict.keys())

            frame_dict[t] = {"frame": flat_frame, "|F|sq": F_norm_sq, "|F|": F_norm}

            for i, t2 in enumerate(t_F):
                # Compare F(t) to all the previous frames

                if frame_dict[t2][t]["rejected"]:
                    continue

                dist = distance(t, t2)
                frame_dict[t2][t]["min"] = frame_dict[t2][t]["max"] = dist
                frame_dict[t2][t]["rejected"] = dist >= distance_threshold

                for t3 in t_F[i + 1 :]:
                    # For all the next times t3, use d(F(t), F(end_time)) to
                    # update the bounds on d(F(t), F(t3)). See if you can
                    # conclude on whether F(t) and F(t3) match.
                    t3t, t2t3 = frame_dict[t3][t], frame_dict[t2][t3]
                    t3t["max"] = min(t3t["max"], dist + t2t3["max"])
                    t3t["min"] = max(t3t["min"], dist - t2t3["max"], t2t3["min"] - dist)

                    if t3t["min"] > distance_threshold:
                        t3t["rejected"] = True

            # Store all the good matches (end_time,t)
            matching_frames += [
                (t1, t, frame_dict[t1][t]["min"], frame_dict[t1][t]["max"])
                for t1 in frame_dict
                if (t1 != t) and not frame_dict[t1][t]["rejected"]
            ]

        return FramesMatches([FramesMatch(*e) for e in matching_frames])

    def select_scenes(
        self, match_threshold, min_time_span, nomatch_threshold=None, time_distance=0
    ):
        """Select the scenes at which a video clip can be reproduced as the
        smoothest possible way, mainly oriented for the creation of GIF images.

        Parameters
        ----------

        match_threshold : float
          Maximum distance possible between frames. The smaller, the
          better-looping the GIFs are.

        min_time_span : float
          Minimum duration for a scene. Only matches with a duration longer
          than the value passed to this parameters will be extracted.

        nomatch_threshold : float, optional
          Minimum distance possible between frames. If is ``None``, then it is
          chosen equal to ``match_threshold``.

        time_distance : float, optional
          Minimum time offset possible between matches.

        Returns
        -------

        FramesMatches : New instance of the class with the selected scenes.

        Examples
        --------

        .. code:: python

            from pprint import pprint
            from moviepy import *
            from moviepy.video.tools.cuts import FramesMatches

            ch_clip = VideoFileClip("media/chaplin.mp4").subclipped(1, 4)
            mirror_and_clip = [ch_clip.with_effects([vfx.TimeMirror()]), ch_clip]
            clip = concatenate_videoclips(mirror_and_clip)

            result = FramesMatches.from_clip(clip, 10, 3).select_scenes(
                1, 2, nomatch_threshold=0,
            )
            print(result)
            # [(1.0000, 4.0000, 0.0000, 0.0000),
            #  (1.1600, 3.8400, 0.0000, 0.0000),
            #  (1.2800, 3.7200, 0.0000, 0.0000),
            #  (1.4000, 3.6000, 0.0000, 0.0000)]
        """
        if nomatch_threshold is None:
            nomatch_threshold = match_threshold

        dict_starts = defaultdict(lambda: [])
        for start, end, min_distance, max_distance in self:
            dict_starts[start].append([end, min_distance, max_distance])

        starts_ends = sorted(dict_starts.items(), key=lambda k: k[0])

        result = []
        min_start = 0
        for start, ends_distances in starts_ends:
            if start < min_start:
                continue

            ends = [end for (end, min_distance, max_distance) in ends_distances]
            great_matches = [
                (end, min_distance, max_distance)
                for (end, min_distance, max_distance) in ends_distances
                if max_distance < match_threshold
            ]

            great_long_matches = [
                (end, min_distance, max_distance)
                for (end, min_distance, max_distance) in great_matches
                if (end - start) > min_time_span
            ]

            if not great_long_matches:
                continue  # No GIF can be made starting at this time

            poor_matches = {
                end
                for (end, min_distance, max_distance) in ends_distances
                if min_distance > nomatch_threshold
            }
            short_matches = {end for end in ends if (end - start) <= 0.6}

            if not poor_matches.intersection(short_matches):
                continue

            end = max(end for (end, min_distance, max_distance) in great_long_matches)
            end, min_distance, max_distance = next(
                e for e in great_long_matches if e[0] == end
            )

            result.append(FramesMatch(start, end, min_distance, max_distance))
            min_start = start + time_distance

        return FramesMatches(result)

    def write_gifs(self, clip, gifs_dir, **kwargs):
        """Extract the matching frames represented by the instance from a clip
        and write them as GIFs in a directory, one GIF for each matching frame.

        Parameters
        ----------

        clip : video.VideoClip.VideoClip
          A video clip whose frames scenes you want to obtain as GIF images.

        gif_dir : str
          Directory in which the GIF images will be written.

        kwargs
          Passed as ``clip.write_gif`` optional arguments.

        Examples
        --------

        .. code:: python

            import os
            from pprint import pprint
            from moviepy import *
            from moviepy.video.tools.cuts import FramesMatches

            ch_clip = VideoFileClip("media/chaplin.mp4").subclipped(1, 4)
            clip = concatenate_videoclips([ch_clip.time_mirror(), ch_clip])

            result = FramesMatches.from_clip(clip, 10, 3).select_scenes(
                1, 2, nomatch_threshold=0,
            )

            os.mkdir("foo")
            result.write_gifs(clip, "foo")
            # MoviePy - Building file foo/00000100_00000400.gif with imageio.
            # MoviePy - Building file foo/00000115_00000384.gif with imageio.
            # MoviePy - Building file foo/00000128_00000372.gif with imageio.
            # MoviePy - Building file foo/00000140_00000360.gif with imageio.
        """
        for start, end, _, _ in self:
            name = "%s/%08d_%08d.gif" % (gifs_dir, 100 * start, 100 * end)
            clip.subclipped(start, end).write_gif(name, **kwargs)


@use_clip_fps_by_default
def detect_scenes(
    clip=None, luminosities=None, luminosity_threshold=10, logger="bar", fps=None
):
    """Detects scenes of a clip based on luminosity changes.

    Note that for large clip this may take some time.

    Returns
    -------

    tuple : cuts, luminosities
      cuts is a series of cuts [(0,t1), (t1,t2),...(...,tf)]
      luminosities are the luminosities computed for each
      frame of the clip.

    Parameters
    ----------

    clip : video.VideoClip.VideoClip, optional
      A video clip. Can be None if a list of luminosities is
      provided instead. If provided, the luminosity of each
      frame of the clip will be computed. If the clip has no
      'fps' attribute, you must provide it.

    luminosities : list, optional
      A list of luminosities, e.g. returned by detect_scenes
      in a previous run.

    luminosity_threshold : float, optional
      Determines a threshold above which the 'luminosity jumps'
      will be considered as scene changes. A scene change is defined
      as a change between 2 consecutive frames that is larger than
      (avg * thr) where avg is the average of the absolute changes
      between consecutive frames.

    logger : str, optional
      Either ``"bar"`` for progress bar or ``None`` or any Proglog logger.

    fps : int, optional
      Frames per second value. Must be provided if you provide
      no clip or a clip without fps attribute.
    """
    if luminosities is None:
        luminosities = [
            f.sum() for f in clip.iter_frames(fps=fps, dtype="uint32", logger=logger)
        ]

    luminosities = np.array(luminosities, dtype=float)
    if clip is not None:
        end = clip.duration
    else:
        end = len(luminosities) * (1.0 / fps)
    luminosity_diffs = abs(np.diff(luminosities))
    avg = luminosity_diffs.mean()
    luminosity_jumps = (
        1 + np.array(np.nonzero(luminosity_diffs > luminosity_threshold * avg))[0]
    )
    timings = [0] + list((1.0 / fps) * luminosity_jumps) + [end]
    cuts = [(t1, t2) for t1, t2 in zip(timings, timings[1:])]
    return cuts, luminosities
````

## File: moviepy/video/tools/drawing.py
````python
"""Deals with making images (np arrays). It provides drawing
methods that are difficult to do with the existing Python libraries.
"""

import numpy as np


def color_gradient(
    size,
    p1,
    p2=None,
    vector=None,
    radius=None,
    color_1=0.0,
    color_2=1.0,
    shape="linear",
    offset=0,
):
    """Draw a linear, bilinear, or radial gradient.

    The result is a picture of size ``size``, whose color varies
    gradually from color `color_1` in position ``p1`` to color ``color_2``
    in position ``p2``.

    If it is a RGB picture the result must be transformed into
    a 'uint8' array to be displayed normally:

    Parameters
    ----------

    size : tuple or list
        Size (width, height) in pixels of the final image array.

    p1 : tuple or list
       Position for the first coordinate of the gradient in pixels (x, y).
       The color 'before' ``p1`` is ``color_1`` and it gradually changes in
       the direction of ``p2`` until it is ``color_2`` when it reaches ``p2``.

    p2 : tuple or list, optional
       Position for the second coordinate of the gradient in pixels (x, y).
        Coordinates (x, y)  of the limit point for ``color_1``
        and ``color_2``.

    vector : tuple or list, optional
        A vector (x, y) in pixels that can be provided instead of ``p2``.
        ``p2`` is then defined as (p1 + vector).

    color_1 : tuple or list, optional
        Starting color for the gradient. As default, black. Either floats
        between 0 and 1 (for gradients used in masks) or [R, G, B] arrays
        (for colored gradients).

    color_2 : tuple or list, optional
        Color for the second point in the gradient. As default, white. Either
        floats between 0 and 1 (for gradients used in masks) or [R, G, B]
        arrays (for colored gradients).

    shape : str, optional
        Shape of the gradient. Can be either ``"linear"``, ``"bilinear"`` or
        ``"circular"``. In a linear gradient the color varies in one direction,
        from point ``p1`` to point ``p2``. In a bilinear gradient it also
        varies symmetrically from ``p1`` in the other direction. In a circular
        gradient it goes from ``color_1`` to ``color_2`` in all directions.

    radius : float, optional
        If ``shape="radial"``, the radius of the gradient is defined with the
        parameter ``radius``, in pixels.

    offset : float, optional
        Real number between 0 and 1 indicating the fraction of the vector
        at which the gradient actually starts. For instance if ``offset``
        is 0.9 in a gradient going from p1 to p2, then the gradient will
        only occur near p2 (before that everything is of color ``color_1``)
        If the offset is 0.9 in a radial gradient, the gradient will
        occur in the region located between 90% and 100% of the radius,
        this creates a blurry disc of radius ``d(p1, p2)``.

    Returns
    -------

    image
        An Numpy array of dimensions (width, height, n_colors) of type float
        representing the image of the gradient.

    Examples
    --------

    .. code:: python

        color_gradient((10, 1), (0, 0), p2=(10, 0))  # from white to black
        #[[1.  0.9 0.8 0.7 0.6 0.5 0.4 0.3 0.2 0.1]]
        # from red to green
        color_gradient(
            (10, 1), (0, 0),
            p2=(10, 0),
            color_1=(255, 0, 0),
            color_2=(0, 255, 0)
        )
        # [[[  0.  255.    0. ]
        #   [ 25.5 229.5   0. ]
        #   [ 51.  204.    0. ]
        #   [ 76.5 178.5   0. ]
        #   [102.  153.    0. ]
        #   [127.5 127.5   0. ]
        #   [153.  102.    0. ]
        #   [178.5  76.5   0. ]
        #   [204.   51.    0. ]
        #   [229.5  25.5   0. ]]]
    """
    # np-arrayize and change x,y coordinates to y,x
    w, h = size

    color_1 = np.array(color_1).astype(float)
    color_2 = np.array(color_2).astype(float)

    if shape == "bilinear":
        if vector is None:
            if p2 is None:
                raise ValueError("You must provide either 'p2' or 'vector'")
            vector = np.array(p2) - np.array(p1)

        m1, m2 = [
            color_gradient(
                size,
                p1,
                vector=v,
                color_1=1.0,
                color_2=0.0,
                shape="linear",
                offset=offset,
            )
            for v in [vector, [-v for v in vector]]
        ]

        arr = np.maximum(m1, m2)
        if color_1.size > 1:
            arr = np.dstack(3 * [arr])
        return arr * color_1 + (1 - arr) * color_2

    p1 = np.array(p1[::-1]).astype(float)

    M = np.dstack(np.meshgrid(range(w), range(h))[::-1]).astype(float)

    if shape == "linear":
        if vector is None:
            if p2 is not None:
                vector = np.array(p2[::-1]) - p1
            else:
                raise ValueError("You must provide either 'p2' or 'vector'")
        else:
            vector = np.array(vector[::-1])

        norm = np.linalg.norm(vector)
        n_vec = vector / norm**2  # norm 1/norm(vector)

        p1 = p1 + offset * vector
        arr = (M - p1).dot(n_vec) / (1 - offset)
        arr = np.minimum(1, np.maximum(0, arr))
        if color_1.size > 1:
            arr = np.dstack(3 * [arr])
        return arr * color_1 + (1 - arr) * color_2

    elif shape == "radial":
        if (radius or 0) == 0:
            arr = np.ones((h, w))
        else:
            arr = (np.sqrt(((M - p1) ** 2).sum(axis=2))) - offset * radius
            arr = arr / ((1 - offset) * radius)
            arr = np.minimum(1.0, np.maximum(0, arr))

        if color_1.size > 1:
            arr = np.dstack(3 * [arr])
        return (1 - arr) * color_1 + arr * color_2
    raise ValueError("Invalid shape, should be either 'radial', 'linear' or 'bilinear'")


def color_split(
    size,
    x=None,
    y=None,
    p1=None,
    p2=None,
    vector=None,
    color_1=0,
    color_2=1.0,
    gradient_width=0,
):
    """Make an image split in 2 colored regions.

    Returns an array of size ``size`` divided in two regions called 1 and
    2 in what follows, and which will have colors color_1 and color_2
    respectively.

    Parameters
    ----------

    x : int, optional
        If provided, the image is split horizontally in x, the left
        region being region 1.

    y : int, optional
        If provided, the image is split vertically in y, the top region
        being region 1.

    p1, p2: tuple or list, optional
        Positions (x1, y1), (x2, y2) in pixels, where the numbers can be
        floats. Region 1 is defined as the whole region on the left when
        going from ``p1`` to ``p2``.

    p1, vector: tuple or list, optional
        ``p1`` is (x1,y1) and vector (v1,v2), where the numbers can be
        floats. Region 1 is then the region on the left when starting
        in position ``p1`` and going in the direction given by ``vector``.

    gradient_width : float, optional
        If not zero, the split is not sharp, but gradual over a region of
        width ``gradient_width`` (in pixels). This is preferable in many
        situations (for instance for antialiasing).

    Examples
    --------

    .. code:: python

        size = [200, 200]

        # an image with all pixels with x<50 =0, the others =1
        color_split(size, x=50, color_1=0, color_2=1)

        # an image with all pixels with y<50 red, the others green
        color_split(size, x=50, color_1=[255, 0, 0], color_2=[0, 255, 0])

        # An image split along an arbitrary line (see below)
        color_split(size, p1=[20, 50], p2=[25, 70], color_1=0, color_2=1)
    """
    if gradient_width or ((x is None) and (y is None)):
        if p2 is not None:
            vector = np.array(p2) - np.array(p1)
        elif x is not None:
            vector = np.array([0, -1.0])
            p1 = np.array([x, 0])
        elif y is not None:
            vector = np.array([1.0, 0.0])
            p1 = np.array([0, y])

        x, y = vector
        vector = np.array([y, -x]).astype("float")
        norm = np.linalg.norm(vector)
        vector = max(0.1, gradient_width) * vector / norm
        return color_gradient(
            size, p1, vector=vector, color_1=color_1, color_2=color_2, shape="linear"
        )
    else:
        w, h = size
        shape = (h, w) if np.isscalar(color_1) else (h, w, len(color_1))
        arr = np.zeros(shape)
        if x:
            arr[:, :x] = color_1
            arr[:, x:] = color_2
        elif y:
            arr[:y] = color_1
            arr[y:] = color_2
        return arr


def circle(screensize, center, radius, color=1.0, bg_color=0, blur=1):
    """Draw an image with a circle.

    Draws a circle of color ``color``, on a background of color ``bg_color``,
    on a screen of size ``screensize`` at the position ``center=(x, y)``,
    with a radius ``radius`` but slightly blurred on the border by ``blur``
    pixels.

    Parameters
    ----------

    screensize : tuple or list
        Size of the canvas.

    center : tuple or list
        Center of the circle.

    radius : float
        Radius of the circle, in pixels.

    bg_color : tuple or float, optional
        Color for the background of the canvas. As default, black.

    blur : float, optional
        Blur for the border of the circle.

    Examples
    --------

    .. code:: python

        from moviepy.video.tools.drawing import circle

        circle(
            (5, 5),  # size
            (2, 2),  # center
            2,      # radius
        )
        # array([[0.        , 0.        , 0.        , 0.        , 0.        ],
        #        [0.        , 0.58578644, 1.        , 0.58578644, 0.        ],
        #        [0.        , 1.        , 1.        , 1.        , 0.        ],
        #        [0.        , 0.58578644, 1.        , 0.58578644, 0.        ],
        #        [0.        , 0.        , 0.        , 0.        , 0.        ]])
    """
    offset = 1.0 * (radius - blur) / radius if radius else 0
    return color_gradient(
        screensize,
        p1=center,
        radius=radius,
        color_1=color,
        color_2=bg_color,
        shape="radial",
        offset=offset,
    )
````

## File: moviepy/video/tools/interpolators.py
````python
"""Classes for easy interpolation of trajectories and curves."""

import numpy as np


class Interpolator:
    """Poorman's linear interpolator.

    Parameters
    ----------

    tt : list, optional
      List of time frames for the interpolator.

    ss : list, optional
      List of values for the interpolator.

    ttss : list, optional
      Lists of time frames and their correspondients values for the
      interpolator. This argument can be used instead of ``tt`` and ``ss``
      to instantiate the interpolator using an unique argument.

    left : float, optional
      Value to return when ``t < tt[0]``.

    right : float, optional
      Value to return when ``t > tt[-1]``.


    Examples
    --------

    .. code:: python

        # instantiate using `tt` and `ss`
        interpolator = Interpolator(tt=[0, 1, 2], ss=[3, 4, 5])

        # instantiate using `ttss`
        interpolator = Interpolator(ttss=[[0, 3], [1, 4], [2, 5]])  # [t, value]
    """

    def __init__(self, tt=None, ss=None, ttss=None, left=None, right=None):
        if ttss is not None:
            tt, ss = zip(*ttss)

        self.tt = 1.0 * np.array(tt)
        self.ss = 1.0 * np.array(ss)
        self.left = left
        self.right = right
        self.tmin, self.tmax = min(tt), max(tt)

    def __call__(self, t):
        """Interpolates ``t``.

        Parameters
        ----------

        t : float
          Time frame for which the correspondent value will be returned.
        """
        return np.interp(t, self.tt, self.ss, self.left, self.right)


class Trajectory:
    """Trajectory compound by time frames and (x, y) pixels.

    It's designed as an interpolator, so you can get the position at a given
    time ``t``. You can instantiate it from a file using the methods
    ``from_file`` and ``load_list``.


    Parameters
    ----------

    tt : list or numpy.ndarray
      Time frames.

    xx : list or numpy.ndarray
      X positions in the trajectory.

    yy : list or numpy.ndarray
      Y positions in the trajectory.


    Examples
    --------

    >>> trajectory = Trajectory([0, .166, .333], [554, 474, 384], [100, 90, 91])
    """

    def __init__(self, tt, xx, yy):
        self.tt = 1.0 * np.array(tt)
        self.xx = np.array(xx)
        self.yy = np.array(yy)
        self.update_interpolators()

    def __call__(self, t):
        """Interpolates the trajectory at the given time ``t``.

        Parameters
        ----------

        t : float
          Time for which to the corresponding position will be returned.
        """
        return np.array([self.xi(t), self.yi(t)])

    def addx(self, x):
        """Adds a value to the ``xx`` position of the trajectory.

        Parameters
        ----------

        x : int
          Value added to ``xx`` in the trajectory.


        Returns
        -------

        Trajectory : new instance with the new X position included.
        """
        return Trajectory(self.tt, self.xx + x, self.yy)

    def addy(self, y):
        """Adds a value to the ``yy`` position of the trajectory.

        Parameters
        ----------

        y : int
          Value added to ``yy`` in the trajectory.


        Returns
        -------

        Trajectory : new instance with the new Y position included.
        """
        return Trajectory(self.tt, self.xx, self.yy + y)

    def update_interpolators(self):
        """Updates the internal X and Y position interpolators for the instance."""
        self.xi = Interpolator(self.tt, self.xx)
        self.yi = Interpolator(self.tt, self.yy)

    def txy(self, tms=False):
        """Returns all times with the X and Y values of each position.

        Parameters
        ----------

        tms : bool, optional
          If is ``True``, the time will be returned in milliseconds.
        """
        return zip((1000 if tms else 1) * self.tt, self.xx, self.yy)

    def to_file(self, filename):
        """Saves the trajectory data in a text file.

        Parameters
        ----------

        filename : str
          Path to the location of the new trajectory text file.
        """
        np.savetxt(
            filename,
            np.array(list(self.txy(tms=True))),
            fmt="%d",
            delimiter="\t",
        )

    @staticmethod
    def from_file(filename):
        """Instantiates an object of Trajectory using a data text file.

        Parameters
        ----------

        filename : str
          Path to the location of trajectory text file to load.


        Returns
        -------

        Trajectory : new instance loaded from text file.
        """
        arr = np.loadtxt(filename, delimiter="\t")
        tt, xx, yy = arr.T
        return Trajectory(1.0 * tt / 1000, xx, yy)

    @staticmethod
    def save_list(trajs, filename):
        """Saves a set of trajectories into a text file.

        Parameters
        ----------

        trajs : list
          List of trajectories to be saved.

        filename : str
          Path of the text file that will store the trajectories data.
        """
        N = len(trajs)
        arr = np.hstack([np.array(list(t.txy(tms=True))) for t in trajs])
        np.savetxt(
            filename,
            arr,
            fmt="%d",
            delimiter="\t",
            header="\t".join(N * ["t(ms)", "x", "y"]),
        )

    @staticmethod
    def load_list(filename):
        """Loads a list of trajectories from a data text file.

        Parameters
        ----------

        filename : str
          Path of the text file that stores the data of a set of trajectories.


        Returns
        -------

        list : List of trajectories loaded from the file.
        """
        arr = np.loadtxt(filename, delimiter="\t").T
        Nlines = arr.shape[0]
        return [
            Trajectory(tt=1.0 * a[0] / 1000, xx=a[1], yy=a[2])
            for a in np.split(arr, Nlines / 3)
        ]
````

## File: moviepy/video/tools/subtitles.py
````python
"""Experimental module for subtitles support."""

import re

import numpy as np

from moviepy.decorators import convert_path_to_string
from moviepy.tools import convert_to_seconds
from moviepy.video.VideoClip import TextClip, VideoClip


class SubtitlesClip(VideoClip):
    """A Clip that serves as "subtitle track" in videos.

    One particularity of this class is that the images of the
    subtitle texts are not generated beforehand, but only if
    needed.

    Parameters
    ----------

    subtitles
        Either the name of a file as a string or path-like object, or a list

    font
        Path to a font file to be used. Optional if make_textclip is provided.

    make_textclip
        A custom function to use for text clip generation. If None, a TextClip
        will be generated.

        The function must take a text as argument and return a VideoClip
        to be used as caption

    encoding
        Optional, specifies srt file encoding.
        Any standard Python encoding is allowed (listed at
        https://docs.python.org/3.8/library/codecs.html#standard-encodings)

    Examples
    --------

    .. code:: python

        from moviepy.video.tools.subtitles import SubtitlesClip
        from moviepy.video.io.VideoFileClip import VideoFileClip
        generator = lambda text: TextClip(text, font='./path/to/font.ttf',
                                        font_size=24, color='white')
        sub = SubtitlesClip("subtitles.srt", make_textclip=generator, encoding='utf-8')
        myvideo = VideoFileClip("myvideo.avi")
        final = CompositeVideoClip([clip, subtitles])
        final.write_videofile("final.mp4", fps=myvideo.fps)

    """

    def __init__(self, subtitles, font=None, make_textclip=None, encoding=None):
        VideoClip.__init__(self, has_constant_size=False)

        if not isinstance(subtitles, list):
            # `subtitles` is a string or path-like object
            subtitles = file_to_subtitles(subtitles, encoding=encoding)

        # subtitles = [(map(convert_to_seconds, times), text)
        #              for times, text in subtitles]
        self.subtitles = subtitles
        self.textclips = dict()

        self.font = font

        if make_textclip is None:
            if self.font is None:
                raise ValueError("Argument font is required if make_textclip is None.")

            def make_textclip(txt):
                return TextClip(
                    font=self.font,
                    text=txt,
                    font_size=24,
                    color="#ffffff",
                    stroke_color="#000000",
                    stroke_width=1,
                )

        self.make_textclip = make_textclip
        self.start = 0
        self.duration = max([tb for ((ta, tb), txt) in self.subtitles])
        self.end = self.duration

        def add_textclip_if_none(t):
            """Will generate a textclip if it hasn't been generated asked
            to generate it yet. If there is no subtitle to show at t, return
            false.
            """
            sub = [
                ((text_start, text_end), text)
                for ((text_start, text_end), text) in self.textclips.keys()
                if (text_start <= t < text_end)
            ]
            if not sub:
                sub = [
                    ((text_start, text_end), text)
                    for ((text_start, text_end), text) in self.subtitles
                    if (text_start <= t < text_end)
                ]
                if not sub:
                    return False
            sub = sub[0]
            if sub not in self.textclips.keys():
                self.textclips[sub] = self.make_textclip(sub[1])

            return sub

        def frame_function(t):
            sub = add_textclip_if_none(t)
            return self.textclips[sub].get_frame(t) if sub else np.array([[[0, 0, 0]]])

        def make_mask_frame(t):
            sub = add_textclip_if_none(t)
            return self.textclips[sub].mask.get_frame(t) if sub else np.array([[0]])

        self.frame_function = frame_function
        hasmask = bool(self.make_textclip("T").mask)
        self.mask = VideoClip(make_mask_frame, is_mask=True) if hasmask else None

    def in_subclip(self, start_time=None, end_time=None):
        """Returns a sequence of [(t1,t2), text] covering all the given subclip
        from start_time to end_time. The first and last times will be cropped so as
        to be exactly start_time and end_time if possible.
        """

        def is_in_subclip(t1, t2):
            try:
                return (start_time <= t1 < end_time) or (start_time < t2 <= end_time)
            except Exception:
                return False

        def try_cropping(t1, t2):
            try:
                return max(t1, start_time), min(t2, end_time)
            except Exception:
                return t1, t2

        return [
            (try_cropping(t1, t2), txt)
            for ((t1, t2), txt) in self.subtitles
            if is_in_subclip(t1, t2)
        ]

    def __iter__(self):
        return iter(self.subtitles)

    def __getitem__(self, k):
        return self.subtitles[k]

    def __str__(self):
        def to_srt(sub_element):
            (start_time, end_time), text = sub_element
            formatted_start_time = convert_to_seconds(start_time)
            formatted_end_time = convert_to_seconds(end_time)
            return "%s - %s\n%s" % (formatted_start_time, formatted_end_time, text)

        return "\n\n".join(to_srt(sub) for sub in self.subtitles)

    def match_expr(self, expr):
        """Matches a regular expression against the subtitles of the clip."""
        return SubtitlesClip(
            [sub for sub in self.subtitles if re.findall(expr, sub[1]) != []]
        )

    def write_srt(self, filename):
        """Writes an ``.srt`` file with the content of the clip."""
        with open(filename, "w+") as file:
            file.write(str(self))


@convert_path_to_string("filename")
def file_to_subtitles(filename, encoding=None):
    """Converts a srt file into subtitles.

    The returned list is of the form ``[((start_time,end_time),'some text'),...]``
    and can be fed to SubtitlesClip.

    Only works for '.srt' format for the moment.
    """
    times_texts = []
    current_times = None
    current_text = ""
    with open(filename, "r", encoding=encoding) as file:
        for line in file:
            times = re.findall("([0-9]*:[0-9]*:[0-9]*,[0-9]*)", line)
            if times:
                current_times = [convert_to_seconds(t) for t in times]
            elif line.strip() == "":
                times_texts.append((current_times, current_text.strip("\n")))
                current_times, current_text = None, ""
            elif current_times:
                current_text += line
    return times_texts
````

## File: moviepy/video/__init__.py
````python
"""Everything about video manipulation."""
````

## File: moviepy/video/VideoClip.py
````python
"""Implements VideoClip (base class for video clips) and its main subclasses:

- Animated clips:     VideoFileClip, ImageSequenceClip, BitmapClip
- Static image clips: ImageClip, ColorClip, TextClip,
"""

import copy as _copy
import os
import threading
from numbers import Real
from typing import TYPE_CHECKING, Callable, List, Union

import numpy as np
import proglog
from imageio.v2 import imread as imread_v2
from imageio.v3 import imwrite
from PIL import Image, ImageDraw, ImageFont

from moviepy.video.io.ffplay_previewer import ffplay_preview_video


if TYPE_CHECKING:
    from moviepy.Effect import Effect

from moviepy.Clip import Clip
from moviepy.decorators import (
    add_mask_if_none,
    apply_to_mask,
    convert_masks_to_RGB,
    convert_parameter_to_seconds,
    convert_path_to_string,
    outplace,
    requires_duration,
    requires_fps,
    use_clip_fps_by_default,
)
from moviepy.tools import compute_position, extensions_dict, find_extension
from moviepy.video.fx.Crop import Crop
from moviepy.video.fx.Resize import Resize
from moviepy.video.fx.Rotate import Rotate
from moviepy.video.io.ffmpeg_writer import ffmpeg_write_video
from moviepy.video.io.gif_writers import write_gif_with_imageio


class VideoClip(Clip):
    """Base class for video clips.

    See ``VideoFileClip``, ``ImageClip`` etc. for more user-friendly classes.


    Parameters
    ----------

    is_mask
      `True` if the clip is going to be used as a mask.

    duration
      Duration of the clip in seconds. If None we got a clip of infinite
      duration

    has_constant_size
      Define if clip size is constant or if it may vary with time. Default
      to True



    Attributes
    ----------

    size
      The size of the clip, (width,height), in pixels.

    w, h
      The width and height of the clip, in pixels.

    is_mask
      Boolean set to `True` if the clip is a mask.

    frame_function
      A function ``t-> frame at time t`` where ``frame`` is a
      w*h*3 RGB array.

    mask (default None)
      VideoClip mask attached to this clip. If mask is ``None``,
                The video clip is fully opaque.

    audio (default None)
      An AudioClip instance containing the audio of the video clip.

    pos
      A function ``t->(x,y)`` where ``x,y`` is the position
      of the clip when it is composed with other clips.
      See ``VideoClip.set_pos`` for more details

    relative_pos
      See variable ``pos``.

    layer
      Indicates which clip is rendered on top when two clips overlap in
      a CompositeVideoClip. The highest number is rendered on top.
      Default is 0.

    """

    def __init__(
        self, frame_function=None, is_mask=False, duration=None, has_constant_size=True
    ):
        super().__init__()
        self.mask = None
        self.audio = None
        self.pos = lambda t: (0, 0)
        self.relative_pos = False
        self.layer_index = 0
        if frame_function:
            self.frame_function = frame_function
            self.size = self.get_frame(0).shape[:2][::-1]
        self.is_mask = is_mask
        self.has_constant_size = has_constant_size
        if duration is not None:
            self.duration = duration
            self.end = duration

    @property
    def w(self):
        """Returns the width of the video."""
        return self.size[0]

    @property
    def h(self):
        """Returns the height of the video."""
        return self.size[1]

    @property
    def aspect_ratio(self):
        """Returns the aspect ratio of the video."""
        return self.w / float(self.h)

    @property
    @requires_duration
    @requires_fps
    def n_frames(self):
        """Returns the number of frames of the video."""
        return int(self.duration * self.fps)

    def __copy__(self):
        """Mixed copy of the clip.

        Returns a shallow copy of the clip whose mask and audio will
        be shallow copies of the clip's mask and audio if they exist.

        This method is intensively used to produce new clips every time
        there is an outplace transformation of the clip (clip.resize,
        clip.subclipped, etc.)

        Acts like a deepcopy except for the fact that readers and other
        possible unpickleables objects are not copied.
        """
        cls = self.__class__
        new_clip = cls.__new__(cls)
        for attr in self.__dict__:
            value = getattr(self, attr)
            if attr in ("mask", "audio"):
                value = _copy.copy(value)
            setattr(new_clip, attr, value)
        return new_clip

    copy = __copy__

    # ===============================================================
    # EXPORT OPERATIONS

    @convert_parameter_to_seconds(["t"])
    @convert_masks_to_RGB
    def save_frame(self, filename, t=0, with_mask=True):
        """Save a clip's frame to an image file.

        Saves the frame of clip corresponding to time ``t`` in ``filename``.
        ``t`` can be expressed in seconds (15.35), in (min, sec),
        in (hour, min, sec), or as a string: '01:03:05.35'.

        Parameters
        ----------

        filename : str
          Name of the file in which the frame will be stored.

        t : float or tuple or str, optional
          Moment of the frame to be saved. As default, the first frame will be
          saved.

        with_mask : bool, optional
          If is ``True`` the mask is saved in the alpha layer of the picture
          (only works with PNGs).
        """
        im = self.get_frame(t)
        if with_mask and self.mask is not None:
            mask = 255 * self.mask.get_frame(t)
            im = np.dstack([im, mask]).astype("uint8")
        else:
            im = im.astype("uint8")

        imwrite(filename, im)

    @requires_duration
    @use_clip_fps_by_default
    @convert_masks_to_RGB
    @convert_path_to_string(["filename", "temp_audiofile", "temp_audiofile_path"])
    def write_videofile(
        self,
        filename,
        fps=None,
        codec=None,
        bitrate=None,
        audio=True,
        audio_fps=44100,
        preset="medium",
        audio_nbytes=4,
        audio_codec=None,
        audio_bitrate=None,
        audio_bufsize=2000,
        temp_audiofile=None,
        temp_audiofile_path="",
        remove_temp=True,
        write_logfile=False,
        threads=None,
        ffmpeg_params=None,
        logger="bar",
        pixel_format=None,
    ):
        """Write the clip to a videofile.

        Parameters
        ----------

        filename
          Name of the video file to write in, as a string or a path-like object.
          The extension must correspond to the "codec" used (see below),
          or simply be '.avi' (which will work with any codec).

        fps
          Number of frames per second in the resulting video file. If None is
          provided, and the clip has an fps attribute, this fps will be used.

        codec
          Codec to use for image encoding. Can be any codec supported
          by ffmpeg. If the filename is has extension '.mp4', '.ogv', '.webm',
          the codec will be set accordingly, but you can still set it if you
          don't like the default. For other extensions, the output filename
          must be set accordingly.

          Some examples of codecs are:

          - ``'libx264'`` (default codec for file extension ``.mp4``)
            makes well-compressed videos (quality tunable using 'bitrate').
          - ``'mpeg4'`` (other codec for extension ``.mp4``) can be an alternative
            to ``'libx264'``, and produces higher quality videos by default.
          - ``'rawvideo'`` (use file extension ``.avi``) will produce
            a video of perfect quality, of possibly very huge size.
          - ``png`` (use file extension ``.avi``) will produce a video
            of perfect quality, of smaller size than with ``rawvideo``.
          - ``'libvorbis'`` (use file extension ``.ogv``) is a nice video
            format, which is completely free/ open source. However not
            everyone has the codecs installed by default on their machine.
          - ``'libvpx'`` (use file extension ``.webm``) is tiny a video
            format well indicated for web videos (with HTML5). Open source.

        audio
          Either ``True``, ``False``, or a file name.
          If ``True`` and the clip has an audio clip attached, this
          audio clip will be incorporated as a soundtrack in the movie.
          If ``audio`` is the name of an audio file, this audio file
          will be incorporated as a soundtrack in the movie.

        audio_fps
          frame rate to use when generating the sound.

        temp_audiofile
          the name of the temporary audiofile, as a string or path-like object,
          to be created and then used to write the complete video, if any.

        temp_audiofile_path
          the location that the temporary audiofile is placed, as a
          string or path-like object. Defaults to the current working directory.

        audio_codec
          Which audio codec should be used. Examples are 'libmp3lame'
          for '.mp3', 'libvorbis' for 'ogg', 'libfdk_aac':'m4a',
          'pcm_s16le' for 16-bit wav and 'pcm_s32le' for 32-bit wav.
          Default is 'libmp3lame', unless the video extension is 'ogv'
          or 'webm', at which case the default is 'libvorbis'.

        audio_bitrate
          Audio bitrate, given as a string like '50k', '500k', '3000k'.
          Will determine the size/quality of audio in the output file.
          Note that it mainly an indicative goal, the bitrate won't
          necessarily be the this in the final file.

        preset
          Sets the time that FFMPEG will spend optimizing the compression.
          Choices are: ultrafast, superfast, veryfast, faster, fast, medium,
          slow, slower, veryslow, placebo. Note that this does not impact
          the quality of the video, only the size of the video file. So
          choose ultrafast when you are in a hurry and file size does not
          matter.

        threads
          Number of threads to use for ffmpeg. Can speed up the writing of
          the video on multicore computers.

        ffmpeg_params
          Any additional ffmpeg parameters you would like to pass, as a list
          of terms, like ['-option1', 'value1', '-option2', 'value2'].

        write_logfile
          If true, will write log files for the audio and the video.
          These will be files ending with '.log' with the name of the
          output file in them.

        logger
          Either ``"bar"`` for progress bar or ``None`` or any Proglog logger.

        pixel_format
          Pixel format for the output video file.

        Examples
        --------

        .. code:: python

            from moviepy import VideoFileClip
            clip = VideoFileClip("myvideo.mp4").subclipped(100,120)
            clip.write_videofile("my_new_video.mp4")
            clip.close()

        """
        name, ext = os.path.splitext(os.path.basename(filename))
        ext = ext[1:].lower()
        logger = proglog.default_bar_logger(logger)

        if codec is None:
            try:
                codec = extensions_dict[ext]["codec"][0]
            except KeyError:
                raise ValueError(
                    "MoviePy couldn't find the codec associated "
                    "with the filename. Provide the 'codec' "
                    "parameter in write_videofile."
                )

        if audio_codec is None:
            if ext in ["ogv", "webm"]:
                audio_codec = "libvorbis"
            else:
                audio_codec = "libmp3lame"
        elif audio_codec == "raw16":
            audio_codec = "pcm_s16le"
        elif audio_codec == "raw32":
            audio_codec = "pcm_s32le"

        audiofile = audio if isinstance(audio, str) else None
        make_audio = (
            (audiofile is None) and (audio is True) and (self.audio is not None)
        )

        if make_audio and temp_audiofile:
            # The audio will be the clip's audio
            audiofile = temp_audiofile
        elif make_audio:
            audio_ext = find_extension(audio_codec)
            audiofile = os.path.join(
                temp_audiofile_path,
                name + Clip._TEMP_FILES_PREFIX + "wvf_snd.%s" % audio_ext,
            )

        # enough cpu for multiprocessing ? USELESS RIGHT NOW, WILL COME AGAIN
        # enough_cpu = (multiprocessing.cpu_count() > 1)
        logger(message="MoviePy - Building video %s." % filename)
        if make_audio:
            self.audio.write_audiofile(
                audiofile,
                audio_fps,
                audio_nbytes,
                audio_bufsize,
                audio_codec,
                bitrate=audio_bitrate,
                write_logfile=write_logfile,
                logger=logger,
            )
            # The audio is already encoded,
            # so there is no need to encode it during video export
            audio_codec = "copy"

        ffmpeg_write_video(
            self,
            filename,
            fps,
            codec,
            bitrate=bitrate,
            preset=preset,
            write_logfile=write_logfile,
            audiofile=audiofile,
            audio_codec=audio_codec,
            threads=threads,
            ffmpeg_params=ffmpeg_params,
            logger=logger,
            pixel_format=pixel_format,
        )

        if remove_temp and make_audio:
            if os.path.exists(audiofile):
                os.remove(audiofile)
        logger(message="MoviePy - video ready %s" % filename)

    @requires_duration
    @use_clip_fps_by_default
    @convert_masks_to_RGB
    def write_images_sequence(
        self, name_format, fps=None, with_mask=True, logger="bar"
    ):
        """Writes the videoclip to a sequence of image files.

        Parameters
        ----------

        name_format
          A filename specifying the numerotation format and extension
          of the pictures. For instance "frame%03d.png" for filenames
          indexed with 3 digits and PNG format. Also possible:
          "some_folder/frame%04d.jpeg", etc.

        fps
          Number of frames per second to consider when writing the
          clip. If not specified, the clip's ``fps`` attribute will
          be used if it has one.

        with_mask
          will save the clip's mask (if any) as an alpha canal (PNGs only).

        logger
          Either ``"bar"`` for progress bar or ``None`` or any Proglog logger.


        Returns
        -------

        names_list
          A list of all the files generated.

        Notes
        -----

        The resulting image sequence can be read using e.g. the class
        ``ImageSequenceClip``.

        """
        logger = proglog.default_bar_logger(logger)
        # Fails on GitHub macos CI
        # logger(message="MoviePy - Writing frames %s." % name_format)

        timings = np.arange(0, self.duration, 1.0 / fps)

        filenames = []
        for i, t in logger.iter_bar(t=list(enumerate(timings))):
            name = name_format % i
            filenames.append(name)
            self.save_frame(name, t, with_mask=with_mask)
        # logger(message="MoviePy - Done writing frames %s." % name_format)

        return filenames

    @requires_duration
    @convert_masks_to_RGB
    @convert_path_to_string("filename")
    def write_gif(
        self,
        filename,
        fps=None,
        loop=0,
        logger="bar",
    ):
        """Write the VideoClip to a GIF file.

        Converts a VideoClip into an animated GIF using imageio

        Parameters
        ----------

        filename
          Name of the resulting gif file, as a string or a path-like object.

        fps
          Number of frames per second (see note below). If it
          isn't provided, then the function will look for the clip's
          ``fps`` attribute (VideoFileClip, for instance, have one).

        loop : int, optional
          Repeat the clip using ``loop`` iterations in the resulting GIF.

        progress_bar
          If True, displays a progress bar


        Notes
        -----

        The gif will be playing the clip in real time (you can
        only change the frame rate). If you want the gif to be played
        slower than the clip you will use

        .. code:: python

            # slow down clip 50% and make it a gif
            myClip.multiply_speed(0.5).to_gif('myClip.gif')

        """
        # A little sketchy at the moment, maybe move all that in write_gif,
        #  refactor a little... we will see.

        write_gif_with_imageio(
            self,
            filename,
            fps=fps,
            loop=loop,
            logger=logger,
        )

    # ===============================================================
    # PREVIEW OPERATIONS

    @convert_masks_to_RGB
    @convert_parameter_to_seconds(["t"])
    def show(self, t=0, with_mask=True):
        """Splashes the frame of clip corresponding to time ``t``.

        Parameters
        ----------

        t : float or tuple or str, optional
        Time in seconds of the frame to display.

        with_mask : bool, optional
        ``False`` if the clip has a mask but you want to see the clip without
        the mask.

        Examples
        --------

        .. code:: python

            from moviepy import *

            clip = VideoFileClip("media/chaplin.mp4")
            clip.show(t=4)
        """
        clip = self.copy()

        # Warning : Comment to fix a bug on preview for compositevideoclip
        # it broke compositevideoclip and it does nothing on normal clip with alpha

        # if with_mask and (self.mask is not None):
        #   # Hate it, but cannot figure a better way with python awful circular
        #   # dependency
        #   from mpy.video.compositing.CompositeVideoClip import CompositeVideoClip
        #   clip = CompositeVideoClip([self.with_position((0, 0))])

        frame = clip.get_frame(t)
        pil_img = Image.fromarray(frame.astype("uint8"))

        pil_img.show()

    @requires_duration
    @convert_masks_to_RGB
    def preview(
        self, fps=15, audio=True, audio_fps=22050, audio_buffersize=3000, audio_nbytes=2
    ):
        """Displays the clip in a window, at the given frames per second.

        It will avoid that the clip be played faster than normal, but it
        cannot avoid the clip to be played slower than normal if the computations
        are complex. In this case, try reducing the ``fps``.

        Parameters
        ----------

        fps : int, optional
        Number of frames per seconds in the displayed video. Default to ``15``.

        audio : bool, optional
        ``True`` (default) if you want the clip's audio be played during
        the preview.

        audio_fps : int, optional
        The frames per second to use when generating the audio sound.

        audio_buffersize : int, optional
        The sized of the buffer used generating the audio sound.

        audio_nbytes : int, optional
        The number of bytes used generating the audio sound.

        Examples
        --------

        .. code:: python

            from moviepy import *
            clip = VideoFileClip("media/chaplin.mp4")
            clip.preview(fps=10, audio=False)
        """
        audio = audio and (self.audio is not None)
        audio_flag = None
        video_flag = None

        if audio:
            # the sound will be played in parallel. We are not
            # parralellizing it on different CPUs because it seems that
            # ffplay use several cpus.

            # two synchro-flags to tell whether audio and video are ready
            video_flag = threading.Event()
            audio_flag = threading.Event()
            # launch the thread
            audiothread = threading.Thread(
                target=self.audio.audiopreview,
                args=(
                    audio_fps,
                    audio_buffersize,
                    audio_nbytes,
                    audio_flag,
                    video_flag,
                ),
            )
            audiothread.start()

        # passthrough to ffmpeg, passing flag for ffmpeg to set
        ffplay_preview_video(
            clip=self, fps=fps, audio_flag=audio_flag, video_flag=video_flag
        )

    # -----------------------------------------------------------------
    # F I L T E R I N G

    def with_effects_on_subclip(
        self, effects: List["Effect"], start_time=0, end_time=None, **kwargs
    ):
        """Apply a transformation to a part of the clip.

        Returns a new clip in which the function ``fun`` (clip->clip)
        has been applied to the subclip between times `start_time` and `end_time`
        (in seconds).

        Examples
        --------

        .. code:: python

            # The scene between times t=3s and t=6s in ``clip`` will be
            # be played twice slower in ``new_clip``
            new_clip = clip.with_sub_effect(MultiplySpeed(0.5), 3, 6)

        """
        left = None if (start_time == 0) else self.subclipped(0, start_time)
        center = self.subclipped(start_time, end_time).with_effects(effects, **kwargs)
        right = None if (end_time is None) else self.subclipped(start_time=end_time)

        clips = [clip for clip in [left, center, right] if clip is not None]

        # beurk, have to find other solution
        from moviepy.video.compositing.CompositeVideoClip import concatenate_videoclips

        return concatenate_videoclips(clips).with_start(self.start)

    # IMAGE FILTERS

    def image_transform(self, image_func, apply_to=None):
        """Modifies the images of a clip by replacing the frame `get_frame(t)` by
        another frame,  `image_func(get_frame(t))`.
        """
        apply_to = apply_to or []
        return self.transform(lambda get_frame, t: image_func(get_frame(t)), apply_to)

    # --------------------------------------------------------------
    # C O M P O S I T I N G

    def fill_array(self, pre_array, shape=(0, 0)):
        """Fills an array to match the specified shape.

        If the `pre_array` is smaller than the desired shape, the missing rows
        or columns are added with ones to the bottom or right, respectively,
        until the shape matches. If the `pre_array` is larger than the desired
        shape, the excess rows or columns are cropped from the bottom or right,
        respectively, until the shape matches.

        The resulting array with the filled shape is returned.

        Parameters
        ----------
        pre_array (numpy.ndarray)
          The original array to be filled.

        shape (tuple)
          The desired shape of the resulting array.
        """
        pre_shape = pre_array.shape
        dx = shape[0] - pre_shape[0]
        dy = shape[1] - pre_shape[1]
        post_array = pre_array
        if dx < 0:
            post_array = pre_array[: shape[0]]
        elif dx > 0:
            x_1 = [[[1, 1, 1]] * pre_shape[1]] * dx
            post_array = np.vstack((pre_array, x_1))
        if dy < 0:
            post_array = post_array[:, : shape[1]]
        elif dy > 0:
            x_1 = [[[1, 1, 1]] * dy] * post_array.shape[0]
            post_array = np.hstack((post_array, x_1))
        return post_array

    def compose_on(self, background: Image.Image, t) -> Image.Image:
        """Returns the result of the clip's frame at time `t` on top
        on the given `picture`, the position of the clip being given
        by the clip's ``pos`` attribute. Meant for compositing.

        If the clip/backgrounds have transparency the transparency will
        be accounted for.

        The return is a Pillow Image

        Parameters
        ----------
        backrgound (Image)
          The background image to apply current clip on top of
          if the background image is transparent it must be given as a RGBA image

        t
          The time of clip to apply on top of clip

        Return
        """
        ct = t - self.start  # clip time

        # GET IMAGE AND MASK IF ANY
        clip_frame = self.get_frame(ct).astype("uint8")
        clip_img = Image.fromarray(clip_frame)

        if self.mask is not None:
            clip_mask = (self.mask.get_frame(ct) * 255).astype("uint8")
            clip_mask_img = Image.fromarray(clip_mask).convert("L")

            # Resize clip_mask_img to match clip_img, always use top left corner
            if clip_mask_img.size != clip_img.size:
                mask_width, mask_height = clip_mask_img.size
                img_width, img_height = clip_img.size

                if mask_width > img_width or mask_height > img_height:
                    # Crop mask if it is larger
                    clip_mask_img = clip_mask_img.crop((0, 0, img_width, img_height))
                else:
                    # Fill mask with 0 if it is smaller
                    new_mask = Image.new("L", (img_width, img_height), 0)
                    new_mask.paste(clip_mask_img, (0, 0))
                    clip_mask_img = new_mask

            clip_img = clip_img.convert("RGBA")
            clip_img.putalpha(clip_mask_img)

        # SET POSITION
        pos = self.pos(ct)
        pos = compute_position(clip_img.size, background.size, pos, self.relative_pos)

        # If neither background nor clip have alpha layer (check if mode end
        # with A), we can juste use pillow paste
        if clip_img.mode[-1] != "A" and background.mode[-1] != "A":
            background.paste(clip_img, pos)
            return background

        # If background has no alpha layer, we can just paste img on top of it
        # this is far more efficient than alpha compositing
        if background.mode[-1] != "A":
            background.paste(clip_img, pos, mask=clip_img)
            return background

        # For images with transparency we must use pillow alpha composite
        # instead of a simple paste, because pillow paste dont work nicely
        # with alpha compositing
        # Only do this in last resort, as it is slower than a simple paste
        # and we dont want to use it if we dont have to
        if background.mode[-1] != "A":
            background = background.convert("RGBA")

        if clip_img.mode[-1] != "A":
            clip_img = clip_img.convert("RGBA")

        # We need both image to do the same size for alpha compositing in pillow
        # so we must start by making a fully transparent canvas of background's
        # size and paste our clip img into it in position pos, only then can we
        # composite this canvas on top of background
        # Its actually faster to make the canvas in numpy and then convert it to PIL
        # than to make it in PIL directly
        canvas_np = np.zeros((background.height, background.width, 4), dtype=np.uint8)
        canvas = Image.fromarray(canvas_np)
        canvas.paste(clip_img, pos)
        result = Image.alpha_composite(background, canvas)
        return result

    def compose_mask(self, background_mask: np.ndarray, t: float) -> np.ndarray:
        """Returns the result of the clip's mask at time `t` composited
        on the given `background_mask`, the position of the clip being given
        by the clip's ``pos`` attribute. Meant for compositing.

        (warning: only use this function to blit two masks together, never images)

        Parameters
        ----------
        background_mask:
          The underlying mask onto which the clip mask will be composed.

        t:
          The time position in the clip at which to extract the mask.
        """
        ct = t - self.start  # clip time
        clip_mask = self.get_frame(ct).astype("float")

        # numpy shape is H*W not W*H
        bg_h, bg_w = background_mask.shape
        clip_h, clip_w = clip_mask.shape

        # SET POSITION
        pos = self.pos(ct)
        pos = compute_position((clip_w, clip_h), (bg_w, bg_h), pos, self.relative_pos)

        # ALPHA COMPOSITING
        # Determine the base_mask region to merge size
        x_start = int(max(pos[0], 0))  # Dont go under 0 left
        x_end = int(min(pos[0] + clip_w, bg_w))  # Dont go over base_mask width
        y_start = int(max(pos[1], 0))  # Dont go under 0 top
        y_end = int(min(pos[1] + clip_h, bg_h))  # Dont go over base_mask height

        # Determine the clip_mask region to overlapp
        # Dont go under 0 for horizontal, if we have negative margin of X px start at X
        # And dont go over clip width
        clip_x_start = int(max(0, -pos[0]))
        clip_x_end = int(clip_x_start + min((x_end - x_start), (clip_w - clip_x_start)))
        # same for vertical
        clip_y_start = int(max(0, -pos[1]))
        clip_y_end = int(clip_y_start + min((y_end - y_start), (clip_h - clip_y_start)))

        # Blend the overlapping regions
        # The calculus is base_opacity + clip_opacity * (1 - base_opacity)
        # this ensure that masks are drawn in the right order and
        # the contribution of each mask is proportional to their transparency
        #
        # Note :
        # Thinking in transparency is hard, as we tend to think
        # that 50% opaque + 40% opaque = 90% opacity, when it really its 70%
        # It's a lot easier to think in terms of "passing light"
        # Consider I emit 100 photons, and my first layer is 50% opaque, meaning it
        # will "stop" 50% of the photons, I'll have 50 photons left
        # now my second layer is blocking 40% of thoses 50 photons left
        # blocking 50 * 0.4 = 20 photons, and leaving me with only 30 photons
        # So, by adding two layer of 50% and 40% opacity my finaly opacity is only
        # of (100-30)*100 = 70% opacity !
        background_mask[y_start:y_end, x_start:x_end] = background_mask[
            y_start:y_end, x_start:x_end
        ] + clip_mask[clip_y_start:clip_y_end, clip_x_start:clip_x_end] * (
            1 - background_mask[y_start:y_end, x_start:x_end]
        )

        return background_mask

    def with_background_color(self, size=None, color=(0, 0, 0), pos=None, opacity=None):
        """Place the clip on a colored background.

        Returns a clip made of the current clip overlaid on a color
        clip of a possibly bigger size. Can serve to flatten transparent
        clips.

        Parameters
        ----------

        size
          Size (width, height) in pixels of the final clip.
          By default it will be the size of the current clip.

        color
          Background color of the final clip ([R,G,B]).

        pos
          Position of the clip in the final clip. 'center' is the default

        opacity
          Parameter in 0..1 indicating the opacity of the colored
          background.
        """
        from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

        if size is None:
            size = self.size
        if pos is None:
            pos = "center"

        if opacity is not None:
            colorclip = ColorClip(
                size, color=color, duration=self.duration
            ).with_opacity(opacity)
            result = CompositeVideoClip([colorclip, self.with_position(pos)])
        else:
            result = CompositeVideoClip(
                [self.with_position(pos)], size=size, bg_color=color
            )

        if (
            isinstance(self, ImageClip)
            and (not hasattr(pos, "__call__"))
            and ((self.mask is None) or isinstance(self.mask, ImageClip))
        ):
            new_result = result.to_ImageClip()
            if result.mask is not None:
                new_result.mask = result.mask.to_ImageClip()
            return new_result.with_duration(result.duration)

        return result

    @outplace
    def with_updated_frame_function(
        self, frame_function: Callable[[float], np.ndarray]
    ):
        """Change the clip's ``get_frame``.

        Returns a copy of the VideoClip instance, with the frame_function
        attribute set to `mf`.
        """
        self.frame_function = frame_function
        self.size = self.get_frame(0).shape[:2][::-1]

    @outplace
    def with_audio(self, audioclip):
        """Attach an AudioClip to the VideoClip.

        Returns a copy of the VideoClip instance, with the `audio`
        attribute set to ``audio``, which must be an AudioClip instance.
        """
        self.audio = audioclip

    @outplace
    def with_mask(self, mask: Union["VideoClip", str] = "auto"):
        """
        Set the clip's mask.

        Returns a copy of the VideoClip with the mask attribute set to
        ``mask``, which must be a greyscale (values in 0-1) VideoClip.

        Parameters
        ----------
        mask : Union["VideoClip", str], optional
            The mask to apply to the clip.
            If set to "auto", a default mask will be generated:
            - If the clip has a constant size, a solid mask with a value of 1.0
            will be created.
            - Otherwise, a dynamic solid mask will be created based on the frame size.
        """
        if mask == "auto":
            if self.has_constant_size:
                mask = ColorClip(self.size, 1.0, is_mask=True)
            else:

                def frame_function(t):
                    return np.ones(self.get_frame(t).shape[:2], dtype=float)

                mask = VideoClip(is_mask=True, frame_function=frame_function)
        self.mask = mask

    @outplace
    def without_mask(self):
        """Remove the clip's mask."""
        self.mask = None

    @add_mask_if_none
    @outplace
    def with_opacity(self, opacity):
        """Set the opacity/transparency level of the clip.

        Returns a semi-transparent copy of the clip where the mask is
        multiplied by ``op`` (any float, normally between 0 and 1).
        """
        self.mask = self.mask.image_transform(lambda pic: opacity * pic)

    @apply_to_mask
    @outplace
    def with_position(self, pos, relative=False):
        """Set the clip's position in compositions.

        Sets the position that the clip will have when included
        in compositions. The argument ``pos`` can be either a couple
        ``(x,y)`` or a function ``t-> (x,y)``. `x` and `y` mark the
        location of the top left corner of the clip, and can be
        of several types.

        Examples
        --------

        .. code:: python

            clip.with_position((45,150)) # x=45, y=150

            # clip horizontally centered, at the top of the picture
            clip.with_position(("center","top"))

            # clip is at 40% of the width, 70% of the height:
            clip.with_position((0.4,0.7), relative=True)

            # clip's position is horizontally centered, and moving up !
            clip.with_position(lambda t: ('center', 50+t))

        """
        self.relative_pos = relative
        if hasattr(pos, "__call__"):
            self.pos = pos
        else:
            self.pos = lambda t: pos

    @apply_to_mask
    @outplace
    def with_layer_index(self, index):
        """Set the clip's layer in compositions. Clips with a greater ``layer``
        attribute will be displayed on top of others.

        Note: Only has effect when the clip is used in a CompositeVideoClip.
        """
        self.layer_index = index

    def resized(self, new_size=None, height=None, width=None, apply_to_mask=True):
        """Returns a video clip that is a resized version of the clip.
        For info on the parameters, please see ``vfx.Resize``
        """
        return self.with_effects(
            [
                Resize(
                    new_size=new_size,
                    height=height,
                    width=width,
                    apply_to_mask=apply_to_mask,
                )
            ]
        )

    def rotated(
        self,
        angle: float,
        unit: str = "deg",
        resample: str = "bicubic",
        expand: bool = False,
        center: tuple = None,
        translate: tuple = None,
        bg_color: tuple = None,
    ):
        """Rotates the specified clip by ``angle`` degrees (or radians) anticlockwise
        If the angle is not a multiple of 90 (degrees) or ``center``, ``translate``,
        and ``bg_color`` are not ``None``.
        For info on the parameters, please see ``vfx.Rotate``
        """
        return self.with_effects(
            [
                Rotate(
                    angle=angle,
                    unit=unit,
                    resample=resample,
                    expand=expand,
                    center=center,
                    translate=translate,
                    bg_color=bg_color,
                )
            ]
        )

    def cropped(
        self,
        x1: int = None,
        y1: int = None,
        x2: int = None,
        y2: int = None,
        width: int = None,
        height: int = None,
        x_center: int = None,
        y_center: int = None,
    ):
        """Returns a new clip in which just a rectangular subregion of the
        original clip is conserved. x1,y1 indicates the top left corner and
        x2,y2 is the lower right corner of the cropped region.
        All coordinates are in pixels. Float numbers are accepted.
        For info on the parameters, please see ``vfx.Crop``
        """
        return self.with_effects(
            [
                Crop(
                    x1=x1,
                    y1=y1,
                    x2=x2,
                    y2=y2,
                    width=width,
                    height=height,
                    x_center=x_center,
                    y_center=y_center,
                )
            ]
        )

    # --------------------------------------------------------------
    # CONVERSIONS TO OTHER TYPES

    @convert_parameter_to_seconds(["t"])
    def to_ImageClip(self, t=0, with_mask=True, duration=None):
        """
        Returns an ImageClip made out of the clip's frame at time ``t``,
        which can be expressed in seconds (15.35), in (min, sec),
        in (hour, min, sec), or as a string: '01:03:05.35'.
        """
        new_clip = ImageClip(self.get_frame(t), is_mask=self.is_mask, duration=duration)
        if with_mask and self.mask is not None:
            new_clip.mask = self.mask.to_ImageClip(t)
        return new_clip

    def to_mask(self, canal=0):
        """Return a mask a video clip made from the clip."""
        if self.is_mask:
            return self
        else:
            new_clip = self.image_transform(lambda pic: 1.0 * pic[:, :, canal] / 255)
            new_clip.is_mask = True
            return new_clip

    def to_RGB(self):
        """Return a non-mask video clip made from the mask video clip."""
        if self.is_mask:
            new_clip = self.image_transform(
                lambda pic: np.dstack(3 * [255 * pic]).astype("uint8")
            )
            new_clip.is_mask = False
            return new_clip
        else:
            return self

    # ----------------------------------------------------------------
    # Audio

    @outplace
    def without_audio(self):
        """Remove the clip's audio.

        Return a copy of the clip with audio set to None.
        """
        self.audio = None

    def __add__(self, other):
        if isinstance(other, VideoClip):
            from moviepy.video.compositing.CompositeVideoClip import (
                concatenate_videoclips,
            )

            method = "chain" if self.size == other.size else "compose"
            return concatenate_videoclips([self, other], method=method)
        return super(VideoClip, self).__add__(other)

    def __or__(self, other):
        """
        Implement the or (self | other) to produce a video with self and other
        placed side by side horizontally.
        """
        if isinstance(other, VideoClip):
            from moviepy.video.compositing.CompositeVideoClip import clips_array

            return clips_array([[self, other]])
        return super(VideoClip, self).__or__(other)

    def __truediv__(self, other):
        """
        Implement division (self / other) to produce a video with self
        placed on top of other.
        """
        if isinstance(other, VideoClip):
            from moviepy.video.compositing.CompositeVideoClip import clips_array

            return clips_array([[self], [other]])
        return super(VideoClip, self).__or__(other)

    def __matmul__(self, n):
        """
        Implement matrice multiplication (self @ other) to rotate a video
        by other degrees
        """
        if not isinstance(n, Real):
            return NotImplemented

        from moviepy.video.fx.Rotate import Rotate

        return self.with_effects([Rotate(n)])

    def __and__(self, mask):
        """
        Implement the and (self & other) to produce a video with other
        used as a mask for self.
        """
        return self.with_mask(mask)


class DataVideoClip(VideoClip):
    """
    Class of video clips whose successive frames are functions
    of successive datasets

    Parameters
    ----------
    data
      A list of datasets, each dataset being used for one frame of the clip

    data_to_frame
      A function d -> video frame, where d is one element of the list `data`

    fps
      Number of frames per second in the animation
    """

    def __init__(self, data, data_to_frame, fps, is_mask=False, has_constant_size=True):
        self.data = data
        self.data_to_frame = data_to_frame
        self.fps = fps

        def frame_function(t):
            return self.data_to_frame(self.data[int(self.fps * t)])

        VideoClip.__init__(
            self,
            frame_function,
            is_mask=is_mask,
            duration=1.0 * len(data) / fps,
            has_constant_size=has_constant_size,
        )


class UpdatedVideoClip(VideoClip):
    """
    Class of clips whose frame_function requires some objects to
    be updated. Particularly practical in science where some
    algorithm needs to make some steps before a new frame can
    be generated.

    UpdatedVideoClips have the following frame_function:

    .. code:: python

        def frame_function(t):
            while self.world.clip_t < t:
                world.update() # updates, and increases world.clip_t
            return world.to_frame()

    Parameters
    ----------

    world
      An object with the following attributes:
      - world.clip_t: the clip's time corresponding to the world's state.
      - world.update() : update the world's state, (including increasing
      world.clip_t of one time step).
      - world.to_frame() : renders a frame depending on the world's state.

    is_mask
      True if the clip is a WxH mask with values in 0-1

    duration
      Duration of the clip, in seconds

    """

    def __init__(self, world, is_mask=False, duration=None):
        self.world = world

        def frame_function(t):
            while self.world.clip_t < t:
                world.update()
            return world.to_frame()

        VideoClip.__init__(
            self, frame_function=frame_function, is_mask=is_mask, duration=duration
        )


"""---------------------------------------------------------------------

    ImageClip (base class for all 'static clips') and its subclasses
    ColorClip and TextClip.
    I would have liked to put these in a separate file but Python is bad
    at cyclic imports.

---------------------------------------------------------------------"""


class ImageClip(VideoClip):
    """Class for non-moving VideoClips.

    A video clip originating from a picture. This clip will simply
    display the given picture at all times.

    Examples
    --------

    >>> clip = ImageClip("myHouse.jpeg")
    >>> clip = ImageClip( someArray ) # a Numpy array represent

    Parameters
    ----------

    img
      Any picture file (png, tiff, jpeg, etc.) as a string or a path-like object,
      or any array representing an RGB image (for instance a frame from a VideoClip).

    is_mask
      Set this parameter to `True` if the clip is a mask.

    transparent
      Set this parameter to `True` (default) if you want the alpha layer
      of the picture (if it exists) to be used as a mask.

    duration
      Duration of the clip in seconds. If not provided, the clip will
      have infinite duration (i.e. it will be displayed until the end of the
      composition in which it is included).

    Attributes
    ----------

    img
      Array representing the image of the clip.

    """

    def __init__(self, img, is_mask=False, transparent=True, duration=None):
        VideoClip.__init__(self, is_mask=is_mask, duration=duration)

        if not isinstance(img, np.ndarray):
            # img is a string or path-like object, so read it in from disk
            img = imread_v2(img)  # We use v2 imread cause v3 fail with gif

        if len(img.shape) == 3:  # img is (now) a RGB(a) numpy array
            if img.shape[2] == 4:
                if is_mask:
                    img = 1.0 * img[:, :, 0] / 255
                elif transparent:
                    self.mask = ImageClip(1.0 * img[:, :, 3] / 255, is_mask=True)
                    img = img[:, :, :3]
            elif is_mask:
                img = 1.0 * img[:, :, 0] / 255

        # if the image was just a 2D mask, it should arrive here
        # unchanged
        self.frame_function = lambda t: img
        self.size = img.shape[:2][::-1]
        self.img = img

    def transform(self, func, apply_to=None, keep_duration=True):
        """General transformation filter.

        Equivalent to VideoClip.transform. The result is no more an
        ImageClip, it has the class VideoClip (since it may be animated)
        """
        if apply_to is None:
            apply_to = []
        # When we use transform on an image clip it may become animated.
        # Therefore the result is not an ImageClip, just a VideoClip.
        new_clip = VideoClip.transform(
            self, func, apply_to=apply_to, keep_duration=keep_duration
        )
        new_clip.__class__ = VideoClip
        return new_clip

    @outplace
    def image_transform(self, image_func, apply_to=None):
        """Image-transformation filter.

        Does the same as VideoClip.image_transform, but for ImageClip the
        transformed clip is computed once and for all at the beginning,
        and not for each 'frame'.
        """
        if apply_to is None:
            apply_to = []
        arr = image_func(self.get_frame(0))
        self.size = arr.shape[:2][::-1]
        self.frame_function = lambda t: arr
        self.img = arr

        for attr in apply_to:
            a = getattr(self, attr, None)
            if a is not None:
                new_a = a.image_transform(image_func)
                setattr(self, attr, new_a)

    @outplace
    def time_transform(self, time_func, apply_to=None, keep_duration=False):
        """Time-transformation filter.

        Applies a transformation to the clip's timeline
        (see Clip.time_transform).

        This method does nothing for ImageClips (but it may affect their
        masks or their audios). The result is still an ImageClip.
        """
        if apply_to is None:
            apply_to = ["mask", "audio"]
        for attr in apply_to:
            a = getattr(self, attr, None)
            if a is not None:
                new_a = a.time_transform(time_func)
                setattr(self, attr, new_a)


class ColorClip(ImageClip):
    """An ImageClip showing just one color.

    Parameters
    ----------

    size
      Size tuple (width, height) in pixels of the clip.

    color
      If argument ``is_mask`` is False, ``color`` indicates
      the color in RGB of the clip (default is black). If `is_mask``
      is True, ``color`` must be  a float between 0 and 1 (default is 1)

    is_mask
      Set to true if the clip will be used as a mask.

    """

    def __init__(self, size, color=None, is_mask=False, duration=None):
        w, h = size

        if is_mask:
            shape = (h, w)
            if color is None:
                color = 0
            elif not np.isscalar(color):
                raise Exception("Color has to be a scalar when mask is true")
        else:
            if color is None:
                color = (0, 0, 0)
            elif not hasattr(color, "__getitem__"):
                raise Exception("Color has to contain RGB of the clip")
            elif isinstance(color, str):
                raise Exception(
                    "Color cannot be string. Color has to contain RGB of the clip"
                )
            shape = (h, w, len(color))

        super().__init__(
            np.tile(color, w * h).reshape(shape), is_mask=is_mask, duration=duration
        )


class TextClip(ImageClip):
    """Class for autogenerated text clips.

    Creates an ImageClip originating from a script-generated text image.

    Parameters
    ----------

    font
      Path to the font to use. Must be an OpenType font. If set to None
      (default) will use Pillow default font

    text
      A string of the text to write. Can be replaced by argument
      ``filename``.

    filename
      The name of a file in which there is the text to write,
      as a string or a path-like object.
      Can be provided instead of argument ``text``

    font_size
      Font size in point. Can be auto-set if method='caption',
      or if method='label' and size is set.

    size
      Size of the picture in pixels. Can be auto-set if
      method='label' and font_size is set, but mandatory if method='caption'.
      the height can be None for caption if font_size is defined,
      it will then be auto-determined.

    margin
      Margin to be added arround the text as a tuple of two (symmetrical) or
      four (asymmetrical). Either ``(horizontal, vertical)`` or
      ``(left, top, right, bottom)``. By default no margin (None, None).
      This is especially usefull for auto-compute size to give the text some
      extra room.

    color
      Color of the text. Default to "black". Can be
      a RGB (or RGBA if transparent = ``True``) ``tuple``, a color name, or an
      hexadecimal notation.

    bg_color
      Color of the background. Default to None for no background. Can be
      a RGB (or RGBA if transparent = ``True``) ``tuple``, a color name, or an
      hexadecimal notation.

    stroke_color
      Color of the stroke (=contour line) of the text. If ``None``,
      there will be no stroke.

    stroke_width
      Width of the stroke, in pixels. Must be an int.

    method
      Either :
        - 'label' (default), the picture will be autosized so as to fit the text
          either by auto-computing font size if width is provided or auto-computing
          width and eight if font size is defined

        - 'caption' the text will be drawn in a picture with fixed size provided
          with the ``size`` argument. The text will be wrapped automagically,
          either by auto-computing font size if width and height are provided or adding
          line break when necesarry if font size is defined

    text_align
      center | left | right. Text align similar to css. Default to ``left``.

    horizontal_align
      center | left | right. Define horizontal align of text bloc in image.
      Default to ``center``.

    vertical_align
      center | top | bottom. Define vertical align of text bloc in image.
      Default to ``center``.

    interline
      Interline spacing. Default to ``4``.

    transparent
      ``True`` (default) if you want to take into account the
      transparency in the image.

    duration
        Duration of the clip

    .. note::

      ** About final TextClip size **

      The final TextClip size will be of the absolute maximum height possible
      for the font and the number of line. It specifically mean that the final
      height might be a bit bigger than the real text height, i.e, absolute
      bottom pixel of text - absolute top pixel of text.
      This is because in a font, some letter go above standard top line (e.g
      letters with accents), and bellow standard baseline (e.g letters such as
      p, y, g).

      This notion is known under the name "ascent" and "descent" meaning the
      highest and lowest pixel above and below the baseline.

      If your first line doesn't have an "accent character" and your last line
      doesn't have a "descent character", you'll have some "fat" around.
    """

    @convert_path_to_string("filename")
    def __init__(
        self,
        font=None,
        text=None,
        filename=None,
        font_size=None,
        size=(None, None),
        margin=(None, None),
        color="black",
        bg_color=None,
        stroke_color=None,
        stroke_width=0,
        method="label",
        text_align="left",
        horizontal_align="center",
        vertical_align="center",
        interline=4,
        transparent=True,
        duration=None,
    ):
        if font is not None:
            try:
                _ = ImageFont.truetype(font)
            except TypeError as e:
                if "takes no arguments" in str(e):
                    pil_font = ImageFont.load_default()
                else:
                    raise
                raise ValueError(
                    "Invalid font {}, pillow failed to use it with error {}".format(
                        font, e
                    )
                )

        if filename:
            with open(filename, "r") as file:
                text = file.read().rstrip()  # Remove newline at end

        if text is None:
            raise ValueError("No text nor filename provided")

        if method not in ["caption", "label"]:
            raise ValueError("Method must be either `caption` or `label`.")

        # Compute the margin and apply it
        if len(margin) == 2:
            left_margin = right_margin = int(margin[0] or 0)
            top_margin = bottom_margin = int(margin[1] or 0)
        elif len(margin) == 4:
            left_margin = int(margin[0] or 0)
            top_margin = int(margin[1] or 0)
            right_margin = int(margin[2] or 0)
            bottom_margin = int(margin[3] or 0)
        else:
            raise ValueError("Margin must be a tuple of either 2 or 4 elements.")

        # Compute all img and text sizes if some are missing
        img_width, img_height = size

        if method == "caption":
            if img_width is None:
                raise ValueError("Size is mandatory when method is caption")

            if img_height is None and font_size is None:
                raise ValueError(
                    "Height is mandatory when method is caption and font size is None"
                )

            if font_size is None:
                font_size = self.__find_optimum_font_size(
                    text=text,
                    font=font,
                    stroke_width=stroke_width,
                    align=text_align,
                    spacing=interline,
                    width=img_width,
                    height=img_height,
                    allow_break=True,
                )

            # Add line breaks whenever needed
            text = "\n".join(
                self.__break_text(
                    width=img_width,
                    text=text,
                    font=font,
                    font_size=font_size,
                    stroke_width=stroke_width,
                    align=text_align,
                    spacing=interline,
                )
            )

            if img_height is None:
                img_height = self.__find_text_size(
                    text=text,
                    font=font,
                    font_size=font_size,
                    stroke_width=stroke_width,
                    align=text_align,
                    spacing=interline,
                    max_width=img_width,
                    allow_break=True,
                )[1]

        elif method == "label":
            if font_size is None and img_width is None:
                raise ValueError(
                    "Font size is mandatory when method is label and size is None"
                )

            if font_size is None:
                font_size = self.__find_optimum_font_size(
                    text=text,
                    font=font,
                    stroke_width=stroke_width,
                    align=text_align,
                    spacing=interline,
                    width=img_width,
                    height=img_height,
                )

            if img_width is None:
                img_width = self.__find_text_size(
                    text=text,
                    font=font,
                    font_size=font_size,
                    stroke_width=stroke_width,
                    align=text_align,
                    spacing=interline,
                )[0]

            if img_height is None:
                img_height = self.__find_text_size(
                    text=text,
                    font=font,
                    font_size=font_size,
                    stroke_width=stroke_width,
                    align=text_align,
                    spacing=interline,
                    max_width=img_width,
                )[1]

        img_width += left_margin + right_margin
        img_height += top_margin + bottom_margin

        # Trace the image
        img_mode = "RGBA" if transparent else "RGB"

        if bg_color is None and transparent:
            bg_color = (0, 0, 0, 0)

        img = Image.new(img_mode, (img_width, img_height), color=bg_color)
        if font:
            pil_font = ImageFont.truetype(font, font_size)
        else:
            try:
                # Only Pillow >= 10.1.0, can set font size
                pil_font = ImageFont.load_default(font_size)
            except TypeError:
                pil_font = ImageFont.load_default()

        draw = ImageDraw.Draw(img)

        # Dont need allow break here, because we already breaked in caption
        text_width, text_height = self.__find_text_size(
            text=text,
            font=font,
            font_size=font_size,
            stroke_width=stroke_width,
            align=text_align,
            spacing=interline,
            max_width=img_width,
        )

        x = 0
        if horizontal_align == "right":
            x = img_width - text_width - left_margin - right_margin
        elif horizontal_align == "center":
            x = (img_width - left_margin - right_margin - text_width) / 2

        y = 0
        if vertical_align == "bottom":
            y = img_height - text_height - top_margin - bottom_margin
        elif vertical_align == "center":
            y = (img_height - top_margin - bottom_margin - text_height) / 2

        # We use baseline as our anchor because it is predictable and reliable
        # That mean we always have to use left baseline instead. Else we would
        # always have a useless margin (the diff between ascender and top) on any
        # text. That mean our Y is actually not from 0 for top, but need to be
        # increment by ascent, since we have to reference from baseline.
        (ascent, _) = pil_font.getmetrics()
        y += ascent

        # Add margins and stroke size to start point
        y += top_margin
        x += left_margin
        y += stroke_width
        x += stroke_width

        draw.multiline_text(
            xy=(x, y),
            text=text,
            fill=color,
            font=pil_font,
            spacing=interline,
            align=text_align,
            stroke_width=stroke_width,
            stroke_fill=stroke_color,
            anchor="ls",
        )

        # We just need the image as a numpy array
        img_numpy = np.array(img)

        ImageClip.__init__(
            self, img=img_numpy, transparent=transparent, duration=duration
        )
        self.text = text
        self.color = color
        self.stroke_color = stroke_color

    def __break_text(
        self, width, text, font, font_size, stroke_width, align, spacing
    ) -> List[str]:
        """Break text to never overflow a width"""
        img = Image.new("RGB", (1, 1))
        if font:
            font_pil = ImageFont.truetype(font, font_size)
        else:
            try:
                # Only Pillow >= 10.1.0, can set font size
                font_pil = ImageFont.load_default(font_size)
            except TypeError:
                font_pil = ImageFont.load_default()

        draw = ImageDraw.Draw(img)

        lines = []
        current_line = ""

        # We try to break on spaces as much as possible
        # if a text dont contain spaces (ex chinese), we will break when possible
        last_space = 0
        for index, char in enumerate(text):
            if char == " ":
                last_space = index

            temp_line = current_line + char
            temp_left, temp_top, temp_right, temp_bottom = draw.multiline_textbbox(
                (0, 0),
                temp_line,
                font=font_pil,
                spacing=spacing,
                align=align,
                stroke_width=stroke_width,
            )
            temp_width = temp_right - temp_left

            if temp_width >= width:
                # If we had a space previously, add everything up to the space
                # and reset last_space and current_line else add everything up
                # to previous char
                if last_space:
                    lines.append(temp_line[0:last_space])
                    current_line = temp_line[last_space + 1 : index + 1]
                    last_space = 0
                else:
                    lines.append(current_line[0:index])
                    current_line = char
                    last_space = 0
            else:
                current_line = temp_line

        if current_line:
            lines.append(current_line)

        return lines

    def __find_text_size(
        self,
        text,
        font,
        font_size,
        stroke_width,
        align,
        spacing,
        max_width=None,
        allow_break=False,
    ) -> tuple[int, int]:
        """Find *real* dimensions a text will occupy, return a tuple (width, height)

        .. note::
            Text height calculation is quite complex due to how `Pillow` works.
            When calculating line height, `Pillow` actually uses the letter ``A``
            as a reference height, adding the spacing and the stroke width.
            However, ``A`` is a simple letter and does not account for ascent and
            descent, such as in ``Ô``.

            This means each line will be considered as having a "standard"
            height instead of the real maximum font size (``ascent + descent``).

            When drawing each line, `Pillow` will offset the new line by
            ``standard height * number of previous lines``.
            This mostly works, but if the spacing is not big enough,
            lines will overlap if a letter with an ascent (e.g., ``d``) is above
            a letter with a descent (e.g., ``p``).

            For our case, we use the baseline as the text anchor. This means that,
            no matter what, we need to draw the absolute top of our first line at
            ``0 + ascent + stroke_width`` to ensure the first pixel of any possible
            letter is aligned with the top border of the image (ignoring any
            additional margins, if needed).

            Therefore, our first line height will not start at ``0`` but at
            ``ascent + stroke_width``, and we need to account for that. Each
            subsequent line will then be drawn at
            ``index * standard height`` from this point. The position of the last
            line can be calculated as:
            ``(total_lines - 1) * standard height``.

            Finally, as we use the baseline as the text anchor, we also need to
            consider that the real size of the last line is not "standard" but
            rather ``standard + descent + stroke_width``.

            To summarize, the real height of the text is:
              ``initial padding + (lines - 1) * height + end padding``
            or:
              ``(ascent + stroke_width) + (lines - 1) * height + (descent + stroke_width)``
            or:
              ``real_font_size + (stroke_width * 2) + (lines - 1) * height``
        """
        img = Image.new("RGB", (1, 1))
        if font:
            font_pil = ImageFont.truetype(font, font_size)
        else:
            font_pil = ImageFont.load_default(font_size)
        ascent, descent = font_pil.getmetrics()
        real_font_size = ascent + descent
        draw = ImageDraw.Draw(img)

        # Compute individual line height with spaces using pillow internal method

        if max_width is not None and allow_break:
            lines = self.__break_text(
                width=max_width,
                text=text,
                font=font,
                font_size=font_size,
                stroke_width=stroke_width,
                align=align,
                spacing=spacing,
            )

            text = "\n".join(lines)

        # Use multiline textbbox to get width
        left, top, right, bottom = draw.multiline_textbbox(
            (0, 0),
            text,
            font=font_pil,
            spacing=spacing,
            align=align,
            stroke_width=stroke_width,
            anchor="ls",
        )

        # For height calculate manually as textbbox is not realiable
        line_height = self.__multiline_spacing(draw, font_pil, spacing, stroke_width)
        line_breaks = text.count("\n")
        lines_height = line_breaks * line_height
        paddings = real_font_size + stroke_width * 2
        height = int(lines_height + paddings)

        return (int(right - left), height)

    def __multiline_spacing(
        self,
        draw: ImageDraw.ImageDraw,
        font: Union[
            ImageFont.ImageFont, ImageFont.FreeTypeFont, ImageFont.TransposedFont
        ],
        spacing: float,
        stroke_width: float,
    ) -> float:
        """Calculate the spacing between lines for multiline text.

        This method is used to calculate the height of each line in a multiline
        text block, taking into account the font metrics, spacing, and stroke width.

        This is a dropped-in replacement for the deprecated
        `ImageDraw._multiline_spacing` method in Pillow.
        """
        return (
            draw.textbbox((0, 0), "A", font, stroke_width=stroke_width)[3]
            + stroke_width
            + spacing
        )

    def __find_optimum_font_size(
        self,
        text,
        font,
        stroke_width,
        align,
        spacing,
        width,
        height=None,
        allow_break=False,
    ):
        """Find the best font size to fit as optimally as possible
        in a box of some width and optionally height
        """
        max_font_size = width
        min_font_size = 1

        # Try find best size using bisection
        while min_font_size < max_font_size:
            avg_font_size = int((max_font_size + min_font_size) // 2)
            text_width, text_height = self.__find_text_size(
                text,
                font,
                avg_font_size,
                stroke_width,
                align,
                spacing,
                max_width=width,
                allow_break=allow_break,
            )

            if text_width <= width and (height is None or text_height <= height):
                min_font_size = avg_font_size + 1
            else:
                max_font_size = avg_font_size - 1

        # Check if the last font size tested fits within the given width and height
        text_width, text_height = self.__find_text_size(
            text,
            font,
            min_font_size,
            stroke_width,
            align,
            spacing,
            max_width=width,
            allow_break=allow_break,
        )
        if text_width <= width and (height is None or text_height <= height):
            return min_font_size
        else:
            return min_font_size - 1


class BitmapClip(VideoClip):
    """Clip made of color bitmaps. Mainly designed for testing purposes."""

    DEFAULT_COLOR_DICT = {
        "R": (255, 0, 0),
        "G": (0, 255, 0),
        "B": (0, 0, 255),
        "O": (0, 0, 0),
        "W": (255, 255, 255),
        "A": (89, 225, 62),
        "C": (113, 157, 108),
        "D": (215, 182, 143),
        "E": (57, 26, 252),
        "F": (225, 135, 33),
    }

    @convert_parameter_to_seconds(["duration"])
    def __init__(
        self, bitmap_frames, *, fps=None, duration=None, color_dict=None, is_mask=False
    ):
        """Creates a VideoClip object from a bitmap representation. Primarily used
        in the test suite.

        Parameters
        ----------

        bitmap_frames
          A list of frames. Each frame is a list of strings. Each string
          represents a row of colors. Each color represents an (r, g, b) tuple.
          Example input (2 frames, 5x3 pixel size)::

              [["RRRRR",
                "RRBRR",
                "RRBRR"],
               ["RGGGR",
                "RGGGR",
                "RGGGR"]]

        fps
          The number of frames per second to display the clip at. `duration` will
          calculated from the total number of frames. If both `fps` and `duration`
          are set, `duration` will be ignored.

        duration
          The total duration of the clip. `fps` will be calculated from the total
          number of frames. If both `fps` and `duration` are set, `duration` will
          be ignored.

        color_dict
          A dictionary that can be used to set specific (r, g, b) values that
          correspond to the letters used in ``bitmap_frames``.
          eg ``{"A": (50, 150, 150)}``.

          Defaults to::

              {
                "R": (255, 0, 0),
                "G": (0, 255, 0),
                "B": (0, 0, 255),
                "O": (0, 0, 0),  # "O" represents black
                "W": (255, 255, 255),
                # "A", "C", "D", "E", "F" represent arbitrary colors
                "A": (89, 225, 62),
                "C": (113, 157, 108),
                "D": (215, 182, 143),
                "E": (57, 26, 252),
              }

        is_mask
          Set to ``True`` if the clip is going to be used as a mask.
        """
        assert fps is not None or duration is not None

        self.color_dict = color_dict if color_dict else self.DEFAULT_COLOR_DICT

        frame_list = []
        for input_frame in bitmap_frames:
            output_frame = []
            for row in input_frame:
                output_frame.append([self.color_dict[color] for color in row])
            frame_list.append(np.array(output_frame))

        frame_array = np.array(frame_list)
        self.total_frames = len(frame_array)

        if fps is None:
            fps = self.total_frames / duration
        else:
            duration = self.total_frames / fps

        VideoClip.__init__(
            self,
            frame_function=lambda t: frame_array[int(t * fps)],
            is_mask=is_mask,
            duration=duration,
        )
        self.fps = fps

    def to_bitmap(self, color_dict=None):
        """Returns a valid bitmap list that represents each frame of the clip.
        If `color_dict` is not specified, then it will use the same `color_dict`
        that was used to create the clip.
        """
        color_dict = color_dict or self.color_dict

        bitmap = []
        for frame in self.iter_frames():
            bitmap.append([])
            for line in frame:
                bitmap[-1].append("")
                for pixel in line:
                    letter = list(color_dict.keys())[
                        list(color_dict.values()).index(tuple(pixel))
                    ]
                    bitmap[-1][-1] += letter

        return bitmap
````

## File: moviepy/__init__.py
````python
"""Imports everything that you need from the MoviePy submodules so that every thing
can be directly imported with ``from moviepy import *``.
"""

from moviepy.audio import fx as afx
from moviepy.audio.AudioClip import (
    AudioArrayClip,
    AudioClip,
    CompositeAudioClip,
    concatenate_audioclips,
)
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.Effect import Effect
from moviepy.tools import convert_to_seconds
from moviepy.version import __version__
from moviepy.video import fx as vfx, tools as videotools
from moviepy.video.compositing.CompositeVideoClip import (
    CompositeVideoClip,
    clips_array,
    concatenate_videoclips,
)
from moviepy.video.io import ffmpeg_tools
from moviepy.video.io.display_in_notebook import display_in_notebook
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import (
    BitmapClip,
    ColorClip,
    DataVideoClip,
    ImageClip,
    TextClip,
    UpdatedVideoClip,
    VideoClip,
)


# Add display in notebook to video and audioclip
VideoClip.display_in_notebook = display_in_notebook
AudioClip.display_in_notebook = display_in_notebook


# Importing with `from moviepy import *` will only import these names
__all__ = [
    "__version__",
    "VideoClip",
    "DataVideoClip",
    "UpdatedVideoClip",
    "ImageClip",
    "ColorClip",
    "TextClip",
    "BitmapClip",
    "VideoFileClip",
    "CompositeVideoClip",
    "clips_array",
    "ImageSequenceClip",
    "concatenate_videoclips",
    "AudioClip",
    "AudioArrayClip",
    "CompositeAudioClip",
    "concatenate_audioclips",
    "AudioFileClip",
    "Effect",
    "vfx",
    "afx",
    "videotools",
    "ffmpeg_tools",
    "convert_to_seconds",
]
````

## File: moviepy/Clip.py
````python
"""Implements the central object of MoviePy, the Clip, and all the methods that
are common to the two subclasses of Clip, VideoClip and AudioClip.
"""

import copy as _copy
from functools import reduce
from numbers import Real
from operator import add
from typing import TYPE_CHECKING, List

import numpy as np
import proglog


if TYPE_CHECKING:
    from moviepy.Effect import Effect

from moviepy.decorators import (
    apply_to_audio,
    apply_to_mask,
    convert_parameter_to_seconds,
    outplace,
    requires_duration,
    use_clip_fps_by_default,
)


class Clip:
    """Base class of all clips (VideoClips and AudioClips).

    Attributes
    ----------

    start : float
      When the clip is included in a composition, time of the
      composition at which the clip starts playing (in seconds).

    end : float
      When the clip is included in a composition, time of the
      composition at which the clip stops playing (in seconds).

    duration : float
      Duration of the clip (in seconds). Some clips are infinite, in
      this case their duration will be ``None``.
    """

    # prefix for all temporary video and audio files.
    # You can overwrite it with
    # >>> Clip._TEMP_FILES_PREFIX = "temp_"

    _TEMP_FILES_PREFIX = "TEMP_MPY_"

    def __init__(self):
        self.start = 0
        self.end = None
        self.duration = None

        self.memoize = False
        self.memoized_t = None
        self.memoized_frame = None

    def copy(self):
        """Allows the usage of ``.copy()`` in clips as chained methods invocation."""
        return _copy.copy(self)

    @convert_parameter_to_seconds(["t"])
    def get_frame(self, t):
        """Gets a numpy array representing the RGB picture of the clip,
        or (mono or stereo) value for a sound clip, at time ``t``.

        Parameters
        ----------

        t : float or tuple or str
          Moment of the clip whose frame will be returned.
        """
        # Coming soon: smart error handling for debugging at this point
        if self.memoize:
            if t == self.memoized_t:
                return self.memoized_frame
            else:
                frame = self.frame_function(t)
                self.memoized_t = t
                self.memoized_frame = frame
                return frame
        else:
            return self.frame_function(t)

    def transform(self, func, apply_to=None, keep_duration=True):
        """General processing of a clip.

        Returns a new Clip whose frames are a transformation
        (through function ``func``) of the frames of the current clip.

        Parameters
        ----------

        func : function
          A function with signature (gf,t -> frame) where ``gf`` will
          represent the current clip's ``get_frame`` method,
          i.e. ``gf`` is a function (t->image). Parameter `t` is a time
          in seconds, `frame` is a picture (=Numpy array) which will be
          returned by the transformed clip (see examples below).

        apply_to : {"mask", "audio", ["mask", "audio"]}, optional
          Can be either ``'mask'``, or ``'audio'``, or
          ``['mask','audio']``.
          Specifies if the filter should also be applied to the
          audio or the mask of the clip, if any.

        keep_duration : bool, optional
          Set to True if the transformation does not change the
          ``duration`` of the clip.

        Examples
        --------

        In the following ``new_clip`` a 100 pixels-high clip whose video
        content scrolls from the top to the bottom of the frames of
        ``clip`` at 50 pixels per second.

        >>> filter = lambda get_frame,t : get_frame(t)[int(t):int(t)+50, :]
        >>> new_clip = clip.transform(filter, apply_to='mask')

        """
        if apply_to is None:
            apply_to = []

        # mf = copy(self.frame_function)
        new_clip = self.with_updated_frame_function(lambda t: func(self.get_frame, t))

        if not keep_duration:
            new_clip.duration = None
            new_clip.end = None

        if isinstance(apply_to, str):
            apply_to = [apply_to]

        for attribute in apply_to:
            attribute_value = getattr(new_clip, attribute, None)
            if attribute_value is not None:
                new_attribute_value = attribute_value.transform(
                    func, keep_duration=keep_duration
                )
                setattr(new_clip, attribute, new_attribute_value)

        return new_clip

    def time_transform(self, time_func, apply_to=None, keep_duration=False):
        """
        Returns a Clip instance playing the content of the current clip
        but with a modified timeline, time ``t`` being replaced by the return
        of `time_func(t)`.

        Parameters
        ----------

        time_func : function
          A function ``t -> new_t``.

        apply_to : {"mask", "audio", ["mask", "audio"]}, optional
          Can be either 'mask', or 'audio', or ['mask','audio'].
          Specifies if the filter ``transform`` should also be applied to the
          audio or the mask of the clip, if any.

        keep_duration : bool, optional
          ``False`` (default) if the transformation modifies the
          ``duration`` of the clip.

        Examples
        --------

        .. code:: python

            # plays the clip (and its mask and sound) twice faster
            new_clip = clip.time_transform(lambda t: 2*t, apply_to=['mask', 'audio'])

            # plays the clip starting at t=3, and backwards:
            new_clip = clip.time_transform(lambda t: 3-t)

        """
        if apply_to is None:
            apply_to = []

        return self.transform(
            lambda get_frame, t: get_frame(time_func(t)),
            apply_to,
            keep_duration=keep_duration,
        )

    def with_effects(self, effects: List["Effect"]):
        """Return a copy of the current clip with the effects applied

        >>> new_clip = clip.with_effects([vfx.Resize(0.2, method="bilinear")])

        You can also pass multiple effect as a list

        >>> clip.with_effects([afx.VolumeX(0.5), vfx.Resize(0.3), vfx.Mirrorx()])
        """
        new_clip = self.copy()
        for effect in effects:
            # We always copy effect before using it, see Effect.copy
            # to see why we need to
            effect_copy = effect.copy()
            new_clip = effect_copy.apply(new_clip)

        return new_clip

    @apply_to_mask
    @apply_to_audio
    @convert_parameter_to_seconds(["t"])
    @outplace
    def with_start(self, t, change_end=True):
        """Returns a copy of the clip, with the ``start`` attribute set
        to ``t``, which can be expressed in seconds (15.35), in (min, sec),
        in (hour, min, sec), or as a string: '01:03:05.35'.

        These changes are also applied to the ``audio`` and ``mask``
        clips of the current clip, if they exist.

        note::
          The start and end attribute of a clip define when a clip will start
          playing when used in a composite video clip, not the start time of
          the clip itself.

          i.e: with_start(10) mean the clip will still start at his first frame,
          but if used in a composite video clip it will only start to show at
          10 seconds.

        Parameters
        ----------

        t : float or tuple or str
          New ``start`` attribute value for the clip.

        change_end : bool optional
          Indicates if the ``end`` attribute value must be changed accordingly,
          if possible. If ``change_end=True`` and the clip has a ``duration``
          attribute, the ``end`` attribute of the clip will be updated to
          ``start + duration``. If ``change_end=False`` and the clip has a
          ``end`` attribute, the ``duration`` attribute of the clip will be
          updated to ``end - start``.
        """
        self.start = t
        if (self.duration is not None) and change_end:
            self.end = t + self.duration
        elif self.end is not None:
            self.duration = self.end - self.start

    @apply_to_mask
    @apply_to_audio
    @convert_parameter_to_seconds(["t"])
    @outplace
    def with_end(self, t):
        """Returns a copy of the clip, with the ``end`` attribute set to ``t``,
        which can be expressed in seconds (15.35), in (min, sec), in
        (hour, min, sec), or as a string: '01:03:05.35'. Also sets the duration
        of the mask and audio, if any, of the returned clip.

        note::
          The start and end attribute of a clip define when a clip will start
          playing when used in a composite video clip, not the start time of
          the clip itself.

          i.e: with_start(10) mean the clip will still start at his first frame,
          but if used in a composite video clip it will only start to show at
          10 seconds.

        Parameters
        ----------

        t : float or tuple or str
          New ``end`` attribute value for the clip.
        """
        self.end = t
        if self.end is None:
            return
        if self.start is None:
            if self.duration is not None:
                self.start = max(0, t - self.duration)
        else:
            self.duration = self.end - self.start

    @apply_to_mask
    @apply_to_audio
    @convert_parameter_to_seconds(["duration"])
    @outplace
    def with_duration(self, duration, change_end=True):
        """Returns a copy of the clip, with the  ``duration`` attribute set to
        ``t``, which can be expressed in seconds (15.35), in (min, sec), in
        (hour, min, sec), or as a string: '01:03:05.35'. Also sets the duration
        of the mask and audio, if any, of the returned clip.

        If ``change_end is False``, the start attribute of the clip will be
        modified in function of the duration and the preset end of the clip.

        Parameters
        ----------

        duration : float
          New duration attribute value for the clip.

        change_end : bool, optional
          If ``True``, the ``end`` attribute value of the clip will be adjusted
          accordingly to the new duration using ``clip.start + duration``.
        """
        self.duration = duration

        if change_end:
            self.end = None if (duration is None) else (self.start + duration)
        else:
            if self.duration is None:
                raise ValueError("Cannot change clip start when new duration is None")
            self.start = self.end - duration

    @outplace
    def with_updated_frame_function(self, frame_function):
        """Sets a ``frame_function`` attribute for the clip. Useful for setting
        arbitrary/complicated videoclips.

        Parameters
        ----------

        frame_function : function
          New frame creator function for the clip.
          A frame_function is a function taking a time ``t`` as input and
          returning a frame (a numpy array) as a result.
        """
        self.frame_function = frame_function

    def with_fps(self, fps, change_duration=False):
        """Returns a copy of the clip with a new default fps for functions like
        write_videofile, iterframe, etc.

        Parameters
        ----------

        fps : int
          New ``fps`` attribute value for the clip.

        change_duration : bool, optional
          If ``change_duration=True``, then the video speed will change to
          match the new fps (conserving all frames 1:1). For example, if the
          fps is halved in this mode, the duration will be doubled.
        """
        if change_duration:
            from moviepy.video.fx.MultiplySpeed import MultiplySpeed

            newclip = self.with_effects([MultiplySpeed(fps / self.fps)])
        else:
            newclip = self.copy()

        newclip.fps = fps
        return newclip

    @outplace
    def with_is_mask(self, is_mask):
        """Says whether the clip is a mask or not.

        Parameters
        ----------

        is_mask : bool
          New ``is_mask`` attribute value for the clip.
        """
        self.is_mask = is_mask

    @outplace
    def with_memoize(self, memoize):
        """Sets whether the clip should keep the last frame read in memory.

        Parameters
        ----------

        memoize : bool
          Indicates if the clip should keep the last frame read in memory.
        """
        self.memoize = memoize

    @convert_parameter_to_seconds(["start_time", "end_time"])
    @apply_to_mask
    @apply_to_audio
    def subclipped(self, start_time=0, end_time=None):
        """Returns a clip playing the content of the current clip between times
        ``start_time`` and ``end_time``, which can be expressed in seconds
        (15.35), in (min, sec), in (hour, min, sec), or as a string:
        '01:03:05.35'.

        The ``mask`` and ``audio`` of the resulting subclip will be subclips of
        ``mask`` and ``audio`` the original clip, if they exist.

        It's equivalent to slice the clip as a sequence, like
        ``clip[t_start:t_end]``.

        Parameters
        ----------

        start_time : float or tuple or str, optional
          Moment that will be chosen as the beginning of the produced clip. If
          is negative, it is reset to ``clip.duration + start_time``.

        end_time : float or tuple or str, optional
          Moment that will be chosen as the end of the produced clip. If not
          provided, it is assumed to be the duration of the clip (potentially
          infinite). If is negative, it is reset to ``clip.duration + end_time``.
          For instance:

          >>> # cut the last two seconds of the clip:
          >>> new_clip = clip.subclipped(0, -2)

          If ``end_time`` is provided or if the clip has a duration attribute,
          the duration of the returned clip is set automatically.
        """
        if start_time < 0:
            # Make this more Python-like, a negative value means to move
            # backward from the end of the clip
            start_time = self.duration + start_time  # Remember start_time is negative

        if (self.duration is not None) and (start_time >= self.duration):
            raise ValueError(
                "start_time (%.02f) " % start_time
                + "should be smaller than the clip's "
                + "duration (%.02f)." % self.duration
            )

        new_clip = self.time_transform(lambda t: t + start_time, apply_to=[])

        if (end_time is None) and (self.duration is not None):
            end_time = self.duration

        elif (end_time is not None) and (end_time < 0):
            if self.duration is None:
                raise ValueError(
                    (
                        "Subclip with negative times (here %s)"
                        " can only be extracted from clips with a ``duration``"
                    )
                    % (str((start_time, end_time)))
                )

            else:
                end_time = self.duration + end_time

        if end_time is not None:
            # Allow a slight tolerance to account for rounding errors
            if (self.duration is not None) and (end_time - self.duration > 0.00000001):
                raise ValueError(
                    "end_time (%.02f) " % end_time
                    + "should be smaller or equal to the clip's "
                    + "duration (%.02f)." % self.duration
                )

            new_clip.duration = end_time - start_time
            new_clip.end = new_clip.start + new_clip.duration

        return new_clip

    @convert_parameter_to_seconds(["start_time", "end_time"])
    def with_section_cut_out(self, start_time, end_time):
        """
        Returns a clip playing the content of the current clip but
        skips the extract between ``start_time`` and ``end_time``, which can be
        expressed in seconds (15.35), in (min, sec), in (hour, min, sec),
        or as a string: '01:03:05.35'.

        If the original clip has a ``duration`` attribute set,
        the duration of the returned clip  is automatically computed as
        `` duration - (end_time - start_time)``.

        The resulting clip's ``audio`` and ``mask`` will also be cutout
        if they exist.

        Parameters
        ----------

        start_time : float or tuple or str
          Moment from which frames will be ignored in the resulting output.

        end_time : float or tuple or str
          Moment until which frames will be ignored in the resulting output.
        """
        new_clip = self.time_transform(
            lambda t: t + (t >= start_time) * (end_time - start_time),
            apply_to=["audio", "mask"],
        )

        if self.duration is not None:
            return new_clip.with_duration(self.duration - (end_time - start_time))
        else:  # pragma: no cover
            return new_clip

    def with_speed_scaled(self, factor: float = None, final_duration: float = None):
        """Returns a clip playing the current clip but at a speed multiplied
        by ``factor``. For info on the parameters, please see ``vfx.MultiplySpeed``.
        """
        from moviepy.video.fx.MultiplySpeed import MultiplySpeed

        return self.with_effects(
            [MultiplySpeed(factor=factor, final_duration=final_duration)]
        )

    def with_volume_scaled(self, factor: float, start_time=None, end_time=None):
        """Returns a new clip with audio volume multiplied by the value `factor`.
        For info on the parameters, please see ``afx.MultiplyVolume``
        """
        from moviepy.audio.fx.MultiplyVolume import MultiplyVolume

        return self.with_effects(
            [MultiplyVolume(factor=factor, start_time=start_time, end_time=end_time)]
        )

    @requires_duration
    @use_clip_fps_by_default
    def iter_frames(self, fps=None, with_times=False, logger=None, dtype=None):
        """Iterates over all the frames of the clip.

        Returns each frame of the clip as a HxWxN Numpy array,
        where N=1 for mask clips and N=3 for RGB clips.

        This function is not really meant for video editing. It provides an
        easy way to do frame-by-frame treatment of a video, for fields like
        science, computer vision...

        Parameters
        ----------

        fps : int, optional
          Frames per second for clip iteration. Is optional if the clip already
          has a ``fps`` attribute.

        with_times : bool, optional
          Ff ``True`` yield tuples of ``(t, frame)`` where ``t`` is the current
          time for the frame, otherwise only a ``frame`` object.

        logger : str, optional
          Either ``"bar"`` for progress bar or ``None`` or any Proglog logger.

        dtype : type, optional
          Type to cast Numpy array frames. Use ``dtype="uint8"`` when using the
          pictures to write video, images..

        Examples
        --------


        .. code:: python

            # prints the maximum of red that is contained
            # on the first line of each frame of the clip.
            from moviepy import VideoFileClip
            myclip = VideoFileClip('myvideo.mp4')
            print([frame[0,:,0].max()
                  for frame in myclip.iter_frames()])
        """
        logger = proglog.default_bar_logger(logger)
        for frame_index in logger.iter_bar(
            frame_index=np.arange(0, int(self.duration * fps))
        ):
            # int is used to ensure that floating point errors are rounded
            # down to the nearest integer
            t = frame_index / fps

            frame = self.get_frame(t)
            if (dtype is not None) and (frame.dtype != dtype):
                frame = frame.astype(dtype)
            if with_times:
                yield t, frame
            else:
                yield frame

    @convert_parameter_to_seconds(["t"])
    def is_playing(self, t):
        """If ``t`` is a time, returns true if t is between the start and the end
        of the clip. ``t`` can be expressed in seconds (15.35), in (min, sec), in
        (hour, min, sec), or as a string: '01:03:05.35'. If ``t`` is a numpy
        array, returns False if none of the ``t`` is in the clip, else returns a
        vector [b_1, b_2, b_3...] where b_i is true if tti is in the clip.
        """
        if isinstance(t, np.ndarray):
            # is the whole list of t outside the clip ?
            tmin, tmax = t.min(), t.max()

            if (self.end is not None) and (tmin >= self.end):
                return False

            if tmax < self.start:
                return False

            # If we arrive here, a part of t falls in the clip
            result = 1 * (t >= self.start)
            if self.end is not None:
                result *= t <= self.end
            return result

        else:
            return (t >= self.start) and ((self.end is None) or (t < self.end))

    def close(self):
        """Release any resources that are in use."""
        #    Implementation note for subclasses:
        #
        #    * Memory-based resources can be left to the garbage-collector.
        #    * However, any open files should be closed, and subprocesses
        #      should be terminated.
        #    * Be wary that shallow copies are frequently used.
        #      Closing a Clip may affect its copies.
        #    * Therefore, should NOT be called by __del__().
        pass

    def __eq__(self, other):
        if not isinstance(other, Clip):
            return NotImplemented

        # Make sure that the total number of frames is the same
        self_length = self.duration * self.fps
        other_length = other.duration * other.fps
        if self_length != other_length:
            return False

        # Make sure that each frame is the same
        for frame1, frame2 in zip(self.iter_frames(), other.iter_frames()):
            if not np.array_equal(frame1, frame2):
                return False

        return True

    def __enter__(self):
        """
        Support the Context Manager protocol,
        to ensure that resources are cleaned up.
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __getitem__(self, key):
        """
        Support extended slice and index operations over
        a clip object.

        Simple slicing is implemented via `subclip`.
        So, ``clip[t_start:t_end]`` is equivalent to
        ``clip.subclipped(t_start, t_end)``. If ``t_start`` is not
        given, default to ``0``, if ``t_end`` is not given,
        default to ``self.duration``.

        The slice object optionally support a third argument as
        a ``speed`` coefficient (that could be negative),
        ``clip[t_start:t_end:speed]``.

        For example ``clip[::-1]`` returns a reversed (a time_mirror fx)
        the video and ``clip[:5:2]`` returns the segment from 0 to 5s
        accelerated to 2x (ie. resulted duration would be 2.5s)

        In addition, a tuple of slices is supported, resulting in the concatenation
        of each segment. For example ``clip[(:1, 2:)]`` return a clip
        with the segment from 1 to 2s removed.

        If ``key`` is not a slice or tuple, we assume it's a time
        value (expressed in any format supported by `cvsec`)
        and return the frame at that time, passing the key
        to ``get_frame``.
        """
        apply_to = ["mask", "audio"]
        if isinstance(key, slice):
            # support for [start:end:speed] slicing. If speed is negative
            # a time mirror is applied.
            clip = self.subclipped(key.start or 0, key.stop or self.duration)

            if key.step:
                # change speed of the subclip
                factor = abs(key.step)
                if factor != 1:
                    # change speed
                    clip = clip.time_transform(
                        lambda t: factor * t, apply_to=apply_to, keep_duration=True
                    )
                    clip = clip.with_duration(1.0 * clip.duration / factor)
                if key.step < 0:
                    # time mirror
                    clip = clip.time_transform(
                        lambda t: clip.duration - t - 1 / self.fps,
                        keep_duration=True,
                        apply_to=apply_to,
                    )
            return clip
        elif isinstance(key, tuple):
            # get a concatenation of subclips
            return reduce(add, (self[k] for k in key))
        else:
            return self.get_frame(key)

    def __del__(self):
        # WARNING: as stated in close() above, if we call close, it closes clips
        # even if shallow copies are still in used, leading to some bugs, see:
        # https://github.com/Zulko/moviepy/issues/1994
        # so don't call self.close() here, rather do it manually in the code.
        pass

    def __add__(self, other):
        # concatenate. implemented in specialized classes
        return NotImplemented

    def __mul__(self, n):
        # loop n times where N is a real
        if not isinstance(n, Real):
            return NotImplemented

        from moviepy.video.fx.Loop import Loop

        return self.with_effects([Loop(n)])
````

## File: moviepy/config.py
````python
"""Third party programs configuration for MoviePy."""

import os
import subprocess as sp
from pathlib import Path

from moviepy.tools import cross_platform_popen_params


try:
    from dotenv import find_dotenv, load_dotenv

    DOTENV = find_dotenv()
    load_dotenv(DOTENV)
except ImportError:
    DOTENV = None

FFMPEG_BINARY = os.getenv("FFMPEG_BINARY", "ffmpeg-imageio")
FFPLAY_BINARY = os.getenv("FFPLAY_BINARY", "auto-detect")

IS_POSIX_OS = os.name == "posix"


def try_cmd(cmd):
    """Verify if the OS support command invocation as expected by moviepy"""
    try:
        popen_params = cross_platform_popen_params(
            {"stdout": sp.PIPE, "stderr": sp.PIPE, "stdin": sp.DEVNULL}
        )
        proc = sp.Popen(cmd, **popen_params)
        proc.communicate()
    except Exception as err:
        return False, err
    else:
        return True, None


if FFMPEG_BINARY == "ffmpeg-imageio":
    from imageio.plugins.ffmpeg import get_exe

    FFMPEG_BINARY = get_exe()

elif FFMPEG_BINARY == "auto-detect":
    if try_cmd(["ffmpeg"])[0]:
        FFMPEG_BINARY = "ffmpeg"
    elif not IS_POSIX_OS and try_cmd(["ffmpeg.exe"])[0]:
        FFMPEG_BINARY = "ffmpeg.exe"
    else:  # pragma: no cover
        FFMPEG_BINARY = "unset"
else:
    success, err = try_cmd([FFMPEG_BINARY])
    if not success:
        raise IOError(
            f"{err} - The path specified for the ffmpeg binary might be wrong"
        )


if FFPLAY_BINARY == "auto-detect":
    if try_cmd(["ffplay"])[0]:
        FFPLAY_BINARY = "ffplay"
    elif not IS_POSIX_OS and try_cmd(["ffplay.exe"])[0]:
        FFPLAY_BINARY = "ffplay.exe"
    else:  # pragma: no cover
        FFPLAY_BINARY = "unset"
else:
    success, err = try_cmd([FFPLAY_BINARY])
    if not success:
        raise IOError(
            f"{err} - The path specified for the ffmpeg binary might be wrong"
        )


def check():
    """Check if moviepy has found the binaries for FFmpeg."""
    if try_cmd([FFMPEG_BINARY])[0]:
        print(f"MoviePy: ffmpeg successfully found in '{FFMPEG_BINARY}'.")
    else:  # pragma: no cover
        print(f"MoviePy: can't find or access ffmpeg in '{FFMPEG_BINARY}'.")

    if try_cmd([FFPLAY_BINARY])[0]:
        print(f"MoviePy: ffplay successfully found in '{FFPLAY_BINARY}'.")
    else:  # pragma: no cover
        print(f"MoviePy: can't find or access ffplay in '{FFPLAY_BINARY}'.")

    if DOTENV:
        print(f"\n.env file content at {DOTENV}:\n")
        print(Path(DOTENV).read_text())


if __name__ == "__main__":  # pragma: no cover
    check()
````

## File: moviepy/decorators.py
````python
"""Decorators used by moviepy."""

import inspect
import os

import decorator

from moviepy.tools import convert_to_seconds


@decorator.decorator
def outplace(func, clip, *args, **kwargs):
    """Applies ``func(clip.copy(), *args, **kwargs)`` and returns ``clip.copy()``."""
    new_clip = clip.copy()
    func(new_clip, *args, **kwargs)
    return new_clip


@decorator.decorator
def convert_masks_to_RGB(func, clip, *args, **kwargs):
    """If the clip is a mask, convert it to RGB before running the function."""
    if clip.is_mask:
        clip = clip.to_RGB()
    return func(clip, *args, **kwargs)


@decorator.decorator
def apply_to_mask(func, clip, *args, **kwargs):
    """Applies the same function ``func`` to the mask of the clip created with
    ``func``.
    """
    new_clip = func(clip, *args, **kwargs)
    if getattr(new_clip, "mask", None):
        new_clip.mask = func(new_clip.mask, *args, **kwargs)
    return new_clip


@decorator.decorator
def apply_to_audio(func, clip, *args, **kwargs):
    """Applies the function ``func`` to the audio of the clip created with ``func``."""
    new_clip = func(clip, *args, **kwargs)
    if getattr(new_clip, "audio", None):
        new_clip.audio = func(new_clip.audio, *args, **kwargs)
    return new_clip


@decorator.decorator
def requires_duration(func, clip, *args, **kwargs):
    """Raises an error if the clip has no duration."""
    if clip.duration is None:
        raise ValueError("Attribute 'duration' not set")
    else:
        return func(clip, *args, **kwargs)


@decorator.decorator
def requires_fps(func, clip, *args, **kwargs):
    """Raises an error if the clip has no fps."""
    if not hasattr(clip, "fps") or clip.fps is None:
        raise ValueError("Attribute 'fps' not set")
    else:
        return func(clip, *args, **kwargs)


@decorator.decorator
def audio_video_effect(func, effect, clip, *args, **kwargs):
    """Use an audio function on a video/audio clip.

    This decorator tells that the function func (audioclip -> audioclip)
    can be also used on a video clip, at which case it returns a
    videoclip with unmodified video and modified audio.
    """
    if hasattr(clip, "audio"):
        if clip.audio is not None:
            clip.audio = func(effect, clip.audio, *args, **kwargs)
        return clip
    else:
        return func(effect, clip, *args, **kwargs)


def preprocess_args(preprocess_func, varnames):
    """Applies preprocess_func to variables in varnames before launching
    the function.
    """

    def decor(func):
        argnames = inspect.getfullargspec(func).args

        def wrapper(func, *args, **kwargs):
            new_args = [
                (
                    preprocess_func(arg)
                    if (name in varnames) and (arg is not None)
                    else arg
                )
                for (arg, name) in zip(args, argnames)
            ]
            new_kwargs = {
                kwarg: preprocess_func(value) if kwarg in varnames else value
                for (kwarg, value) in kwargs.items()
            }
            return func(*new_args, **new_kwargs)

        return decorator.decorate(func, wrapper)

    return decor


def convert_parameter_to_seconds(varnames):
    """Converts the specified variables to seconds."""
    return preprocess_args(convert_to_seconds, varnames)


def convert_path_to_string(varnames):
    """Converts the specified variables to a path string."""
    return preprocess_args(os.fspath, varnames)


@decorator.decorator
def add_mask_if_none(func, clip, *args, **kwargs):
    """Add a mask to the clip if there is none."""
    if clip.mask is None:
        clip = clip.with_mask()
    return func(clip, *args, **kwargs)


def use_clip_fps_by_default(func):
    """Will use ``clip.fps`` if no ``fps=...`` is provided in **kwargs**."""
    argnames = inspect.getfullargspec(func).args[1:]

    def find_fps(clip, fps):
        if fps is not None:
            return fps
        elif getattr(clip, "fps", None):
            return clip.fps
        raise AttributeError(
            "No 'fps' (frames per second) attribute specified"
            " for function %s and the clip has no 'fps' attribute. Either"
            " provide e.g. fps=24 in the arguments of the function, or define"
            " the clip's fps with `clip.fps=24`" % func.__name__
        )

    def wrapper(func, clip, *args, **kwargs):
        new_args = [
            find_fps(clip, arg) if name == "fps" else arg
            for (arg, name) in zip(args, argnames)
        ]
        new_kwargs = {
            kwarg: find_fps(clip, kwarg) if kwarg == "fps" else value
            for (kwarg, value) in kwargs.items()
        }

        return func(clip, *new_args, **new_kwargs)

    return decorator.decorate(func, wrapper)
````

## File: moviepy/Effect.py
````python
"""Defines the base class for all effects in MoviePy."""

import copy as _copy
from abc import ABCMeta, abstractmethod

from moviepy.Clip import Clip


class Effect(metaclass=ABCMeta):
    """Base abstract class for all effects in MoviePy.
    Any new effect have to extend this base class.
    """

    def copy(self):
        """Return a shallow copy of an Effect.

        You must *always* copy an ``Effect`` before applying,
        because some of them will modify their own attributes when applied.
        For example, setting a previously unset property by using target clip property.

        If we was to use the original effect, calling the same effect multiple times
        could lead to different properties, and different results for equivalent clips.

        By using copy, we ensure we can use the same effect object multiple times while
        maintaining the same behavior/result.

        In a way, copy makes the effect himself being kind of idempotent.
        """
        return _copy.copy(self)

    @abstractmethod
    def apply(self, clip: Clip) -> Clip:
        """Apply the current effect on a clip

        Parameters
        ----------
        clip
            The target clip to apply the effect on.
            (Internally, MoviePy will always pass a copy of the original clip)

        """
        pass
````

## File: moviepy/tools.py
````python
"""Misc. useful functions that can be used at many places in the program."""

import os
import platform
import subprocess as sp
import warnings

import proglog


OS_NAME = os.name


def cross_platform_popen_params(popen_params):
    """Wrap with this function a dictionary of ``subprocess.Popen`` kwargs and
    will be ready to work without unexpected behaviours in any platform.
    Currently, the implementation will add to them:

    - ``creationflags=0x08000000``: no extra unwanted window opens on Windows
      when the child process is created. Only added on Windows.
    """
    if OS_NAME == "nt":
        popen_params["creationflags"] = 0x08000000
    return popen_params


def subprocess_call(cmd, logger="bar"):
    """Executes the given subprocess command.

    Set logger to None or a custom Proglog logger to avoid printings.
    """
    logger = proglog.default_bar_logger(logger)
    logger(message="MoviePy - Running:\n>>> " + " ".join(cmd))

    popen_params = cross_platform_popen_params(
        {"stdout": sp.DEVNULL, "stderr": sp.PIPE, "stdin": sp.DEVNULL}
    )

    proc = sp.Popen(cmd, **popen_params)

    out, err = proc.communicate()  # proc.wait()
    proc.stderr.close()

    if proc.returncode:
        logger(message="MoviePy - Command returned an error")
        raise IOError(err.decode("utf8"))
    else:
        logger(message="MoviePy - Command successful")

    del proc


def ffmpeg_escape_filename(filename):
    """Escape a filename that we want to pass to the ffmpeg command line

    That will ensure the filename doesn't start with a '-' (which would raise an error)
    """
    if filename.startswith("-"):
        filename = "./" + filename

    return filename


def convert_to_seconds(time):
    """Will convert any time into seconds.

    If the type of `time` is not valid,
    it's returned as is.

    Here are the accepted formats:

    .. code:: python

        convert_to_seconds(15.4)   # seconds
        15.4
        convert_to_seconds((1, 21.5))   # (min,sec)
        81.5
        convert_to_seconds((1, 1, 2))   # (hr, min, sec)
        3662
        convert_to_seconds('01:01:33.045')
        3693.045
        convert_to_seconds('01:01:33,5')    # coma works too
        3693.5
        convert_to_seconds('1:33,5')    # only minutes and secs
        99.5
        convert_to_seconds('33.5')      # only secs
        33.5
    """
    factors = (1, 60, 3600)

    if isinstance(time, str):
        time = [float(part.replace(",", ".")) for part in time.split(":")]

    if not isinstance(time, (tuple, list)):
        return time

    return sum(mult * part for mult, part in zip(factors, reversed(time)))


def deprecated_version_of(func, old_name):
    """Indicates that a function is deprecated and has a new name.

    `func` is the new function and `old_name` is the name of the deprecated
    function.

    Returns
    -------

    deprecated_func
      A function that does the same thing as `func`, but with a docstring
      and a printed message on call which say that the function is
      deprecated and that you should use `func` instead.

    Examples
    --------

    .. code:: python

        # The badly named method 'to_file' is replaced by 'write_file'
        class Clip:
            def write_file(self, some args):
                # blablabla
        Clip.to_file = deprecated_version_of(Clip.write_file, 'to_file')
    """
    # Detect new name of func
    new_name = func.__name__

    warning = (
        "The function ``%s`` is deprecated and is kept temporarily "
        "for backwards compatibility.\nPlease use the new name, "
        "``%s``, instead."
    ) % (old_name, new_name)

    def deprecated_func(*args, **kwargs):
        warnings.warn("MoviePy: " + warning, PendingDeprecationWarning)
        return func(*args, **kwargs)

    deprecated_func.__doc__ = warning

    return deprecated_func


# Non-exhaustive dictionary to store default information.
# Any addition is most welcome.
# Note that 'gif' is complicated to place. From a VideoFileClip point of view,
# it is a video, but from a HTML5 point of view, it is an image.

extensions_dict = {
    "mp4": {"type": "video", "codec": ["libx264", "libmpeg4", "aac"]},
    "mkv": {"type": "video", "codec": ["libx264", "libmpeg4", "aac"]},
    "ogv": {"type": "video", "codec": ["libtheora"]},
    "webm": {"type": "video", "codec": ["libvpx"]},
    "avi": {"type": "video"},
    "mov": {"type": "video", "codec": ["libx264", "prores"]},
    "ogg": {"type": "audio", "codec": ["libvorbis"]},
    "mp3": {"type": "audio", "codec": ["libmp3lame"]},
    "wav": {"type": "audio", "codec": ["pcm_s16le", "pcm_s24le", "pcm_s32le"]},
    "m4a": {"type": "audio", "codec": ["libfdk_aac"]},
    "flac": {"type": "audio", "codec": ["flac"]},
}

for ext in ["jpg", "jpeg", "png", "bmp", "tiff"]:
    extensions_dict[ext] = {"type": "image"}


def find_extension(codec):
    """Returns the correspondent file extension for a codec.

    Parameters
    ----------

    codec : str
      Video or audio codec name.
    """
    if codec in extensions_dict:
        # codec is already the extension
        return codec

    for ext, infos in extensions_dict.items():
        if codec in infos.get("codec", []):
            return ext
    raise ValueError(
        "The audio_codec you chose is unknown by MoviePy. "
        "You should report this. In the meantime, you can "
        "specify a temp_audiofile with the right extension "
        "in write_videofile."
    )


def close_all_clips(objects="globals", types=("audio", "video", "image")):
    """Closes all clips in a context.

    Follows different strategies retrieving the namespace from which the clips
    to close will be retrieved depending on the ``objects`` argument, and filtering
    by type of clips depending on the ``types`` argument.

    Parameters
    ----------

    objects : str or dict, optional
      - If is a string an the value is ``"globals"``, will close all the clips
        contained by the ``globals()`` namespace.
      - If is a dictionary, the values of the dictionary could be clips to close,
        useful if you want to use ``locals()``.

    types : Iterable, optional
      Set of types of clips to close, being "audio", "video" or "image" the supported
      values.
    """
    from moviepy.audio.io.AudioFileClip import AudioFileClip
    from moviepy.video.io.VideoFileClip import VideoFileClip
    from moviepy.video.VideoClip import ImageClip

    CLIP_TYPES = {
        "audio": AudioFileClip,
        "video": VideoFileClip,
        "image": ImageClip,
    }

    if objects == "globals":  # pragma: no cover
        objects = globals()
    if hasattr(objects, "values"):
        objects = objects.values()
    types_tuple = tuple(CLIP_TYPES[key] for key in types)
    for obj in objects:
        if isinstance(obj, types_tuple):
            obj.close()


def no_display_available() -> bool:
    """Return True if we determine the host system has no graphical environment.
    This is usefull to remove tests requiring display, like preview

    ..info::
        Currently this only works for Linux/BSD systems with X11 or wayland.
        It probably works for SunOS, AIX and CYGWIN
    """
    system = platform.system()
    if system in ["Linux", "FreeBSD", "NetBSD", "OpenBSD", "SunOS", "AIX"]:
        if ("DISPLAY" not in os.environ) and ("WAYLAND_DISPLAY" not in os.environ):
            return True

    if "CYGWIN_NT" in system:
        if ("DISPLAY" not in os.environ) and ("WAYLAND_DISPLAY" not in os.environ):
            return True

    return False


def compute_position(
    clip1_size: tuple, clip2_size: tuple, pos: any, relative: bool = False
) -> tuple[int, int]:
    """Return the position to put clip 1 on clip 2 based on both clip size
    and the position of clip 1, as return by clip1.pos() method

    Parameters
    ----------
    clip1_size : tuple
        The width and height of clip1 (e.g., (width, height)).
    clip2_size : tuple
        The width and height of clip2 (e.g., (width, height)).
    pos : Any
        The position of clip1 as returned by the `clip1.pos()` method.
    relative: bool
        Is the position relative (% of clip size), default False.

    Returns
    -------
    tuple[int, int]
        A tuple (x, y) representing the top-left corner of clip1 relative to clip2.

    Notes
    -----
    For more information on `pos`, see the documentation for `VideoClip.with_position`.
    """
    if pos is None:
        pos = (0, 0)

    # preprocess short writings of the position
    if isinstance(pos, str):
        pos = {
            "center": ["center", "center"],
            "left": ["left", "center"],
            "right": ["right", "center"],
            "top": ["center", "top"],
            "bottom": ["center", "bottom"],
        }[pos]
    else:
        pos = list(pos)

    # is the position relative (given in % of the clip's size) ?
    if relative:
        for i, dim in enumerate(clip2_size):
            if not isinstance(pos[i], str):
                pos[i] = dim * pos[i]

    if isinstance(pos[0], str):
        D = {
            "left": 0,
            "center": (clip2_size[0] - clip1_size[0]) / 2,
            "right": clip2_size[0] - clip1_size[0],
        }
        pos[0] = D[pos[0]]

    if isinstance(pos[1], str):
        D = {
            "top": 0,
            "center": (clip2_size[1] - clip1_size[1]) / 2,
            "bottom": clip2_size[1] - clip1_size[1],
        }
        pos[1] = D[pos[1]]

    # Return as int, rounding if necessary
    return (int(pos[0]), int(pos[1]))
````

## File: moviepy/version.py
````python
try:
    from importlib.metadata import version

    __version__ = version("moviepy")
except Exception:
    __version__ = "2.1.2"  # Fallback version if import fails
````

## File: tests/conftest.py
````python
"""Define general test helper attributes and utilities."""

import ast
import contextlib
import functools
import http.server
import importlib
import inspect
import io
import pkgutil
import socketserver
import tempfile
import threading

import numpy as np

import pytest

from moviepy.video.io.VideoFileClip import VideoFileClip


TMP_DIR = tempfile.gettempdir()  # because tempfile.tempdir is sometimes None

# Arbitrary font used in caption testing.
FONT = "media/doc_medias/example.ttf"

# Dir for doc examples medias
DOC_EXAMPLES_MEDIAS_DIR = "media/doc_medias"


@functools.lru_cache(maxsize=None)
def get_video(start_time=0, end_time=1):
    return VideoFileClip("media/big_buck_bunny_432_433.webm").subclipped(
        start_time, end_time
    )


@functools.lru_cache(maxsize=None)
def get_stereo_wave(left_freq=440, right_freq=220):
    def make_stereo_frame(t):
        return np.array(
            [np.sin(left_freq * 2 * np.pi * t), np.sin(right_freq * 2 * np.pi * t)]
        ).T.copy(order="C")

    return make_stereo_frame


@functools.lru_cache(maxsize=None)
def get_mono_wave(freq=440):
    def make_mono_frame(t):
        return np.sin(freq * 2 * np.pi * t)

    return make_mono_frame


@contextlib.contextmanager
def get_static_files_server(port=8000):
    my_server = socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler)
    thread = threading.Thread(target=my_server.serve_forever, daemon=True)
    thread.start()
    yield thread


@functools.lru_cache(maxsize=None)
def get_moviepy_modules():
    """Get all moviepy module names and if each one is a package."""
    response = []
    with contextlib.redirect_stdout(io.StringIO()):
        moviepy_module = importlib.import_module("moviepy")

        modules = pkgutil.walk_packages(
            path=moviepy_module.__path__,
            prefix=moviepy_module.__name__ + ".",
        )

        for importer, modname, ispkg in modules:
            response.append((modname, ispkg))
    return response


def get_functions_with_decorator_defined(code, decorator_name):
    """Get all functions in a code object which have a decorator defined,
    along with the arguments of the function and the decorator.

    Parameters
    ----------

    code : object
      Module or class object from which to retrieve the functions.

    decorator_name : str
      Name of the decorator defined in the functions to search.
    """

    class FunctionsWithDefinedDecoratorExtractor(ast.NodeVisitor):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.functions_with_decorator = []

        def generic_visit(self, node):
            if isinstance(node, ast.FunctionDef) and node.decorator_list:
                for dec in node.decorator_list:
                    if not isinstance(dec, ast.Call) or dec.func.id != decorator_name:
                        continue

                    decorator_argument_names = []
                    if isinstance(dec.args, ast.List):
                        for args in dec.args:
                            decorator_argument_names.extend(
                                [e.value for e in args.elts]
                            )
                    else:
                        for args in dec.args:
                            if isinstance(args, (ast.List, ast.Tuple)):
                                decorator_argument_names.extend(
                                    [e.value for e in args.elts]
                                )
                            else:
                                decorator_argument_names.append(args.value)

                    function_argument_names = [arg.arg for arg in node.args.args]
                    for arg in node.args.kwonlyargs:
                        function_argument_names.append(arg.arg)

                    self.functions_with_decorator.append(
                        {
                            "function_name": node.name,
                            "function_arguments": function_argument_names,
                            "decorator_arguments": decorator_argument_names,
                        }
                    )

            ast.NodeVisitor.generic_visit(self, node)

    modtree = ast.parse(inspect.getsource(code))
    visitor = FunctionsWithDefinedDecoratorExtractor()
    visitor.visit(modtree)
    return visitor.functions_with_decorator


@pytest.fixture
def util():
    class MoviepyTestUtils:
        FONT = FONT
        TMP_DIR = TMP_DIR
        DOC_EXAMPLES_MEDIAS_DIR = DOC_EXAMPLES_MEDIAS_DIR

    return MoviepyTestUtils


@pytest.fixture
def video():
    return get_video


@pytest.fixture
def stereo_wave():
    return get_stereo_wave


@pytest.fixture
def mono_wave():
    return get_mono_wave


@pytest.fixture
def static_files_server():
    return get_static_files_server


@pytest.fixture
def moviepy_modules():
    return get_moviepy_modules


@pytest.fixture
def functions_with_decorator_defined():
    return get_functions_with_decorator_defined
````

## File: tests/README.rst
````
Install testing dependencies: `pip install moviepy[test]`

Run tests: `pytest`
````

## File: tests/test_AudioClips.py
````python
"""Image sequencing clip tests meant to be run with pytest."""

import os

import numpy as np

import pytest

from moviepy.audio.AudioClip import (
    AudioArrayClip,
    AudioClip,
    CompositeAudioClip,
    concatenate_audioclips,
)
from moviepy.audio.io.AudioFileClip import AudioFileClip


def test_audioclip(util, mono_wave):
    filename = os.path.join(util.TMP_DIR, "audioclip.mp3")
    audio = AudioClip(mono_wave(440), duration=2, fps=22050)
    audio.write_audiofile(filename, bitrate="16", logger=None)

    assert os.path.exists(filename)

    AudioFileClip(filename)

    # TODO Write better tests; find out why the following fail
    # assert clip.duration == 2
    # assert clip.fps == 22050
    # assert clip.reader.bitrate == 16


def test_audioclip_io(util):
    filename = os.path.join(util.TMP_DIR, "random.wav")

    # Generate a random audio clip of 4.989 seconds at 44100 Hz,
    # and save it to a file.
    input_array = np.random.random((220000, 2)) * 1.98 - 0.99
    clip = AudioArrayClip(input_array, fps=44100)
    clip.write_audiofile(filename, logger=None)
    # Load the clip.
    # The loaded clip will be slightly longer because the duration is rounded
    # up to 4.99 seconds.
    # Verify that the extra frames are all zero, and the remainder is identical
    # to the original signal.
    clip = AudioFileClip(filename)
    output_array = clip.to_soundarray()
    np.testing.assert_array_almost_equal(
        output_array[: len(input_array)], input_array, decimal=4
    )
    assert (output_array[len(input_array) :] == 0).all()


def test_concatenate_audioclips_render(util, mono_wave):
    """Concatenated AudioClips through ``concatenate_audioclips`` should return
    a clip that can be rendered to a file.
    """
    filename = os.path.join(util.TMP_DIR, "concatenate_audioclips.mp3")

    clip_440 = AudioClip(mono_wave(440), duration=0.01, fps=44100)
    clip_880 = AudioClip(mono_wave(880), duration=0.000001, fps=22050)

    concat_clip = concatenate_audioclips((clip_440, clip_880))
    concat_clip.write_audiofile(filename, logger=None)

    assert concat_clip.duration == clip_440.duration + clip_880.duration


def test_concatenate_audioclips_CompositeAudioClip():
    """Concatenated AudioClips through ``concatenate_audioclips`` should return
    a CompositeAudioClip whose attributes should be consistent:

    - Returns CompositeAudioClip.
    - Their fps is taken from the maximum of their audios.
    - Audios are placed one after other:
      - Duration is the sum of their durations.
      - Ends are the accumulated sum of their durations.
      - Starts are the accumulated sum of their durations, but first start is 0
      and latest is ignored.
    - Channels are the max channels of their clips.
    """
    frequencies = [440, 880, 1760]
    durations = [2, 5, 1]
    fpss = [44100, 22050, 11025]

    clips = [
        AudioClip(
            lambda t: [np.sin(frequency * 2 * np.pi * t)], duration=duration, fps=fps
        )
        for frequency, duration, fps in zip(frequencies, durations, fpss)
    ]

    concat_clip = concatenate_audioclips(clips)

    # should return a CompositeAudioClip
    assert isinstance(concat_clip, CompositeAudioClip)

    # fps of the greatest fps passed into it
    assert concat_clip.fps == 44100

    # audios placed on after other
    assert concat_clip.duration == sum(durations)
    assert list(concat_clip.ends) == list(np.cumsum(durations))
    assert list(concat_clip.starts), list(np.cumsum([0, *durations[:-1]]))

    # channels are maximum number of channels of the clips
    assert concat_clip.nchannels == max(clip.nchannels for clip in clips)


def test_CompositeAudioClip_by__init__():
    """The difference between the CompositeAudioClip returned by
    ``concatenate_audioclips`` and a CompositeAudioClip created using the class
    directly, is that audios in ``concatenate_audioclips`` are played one after
    other and AudioClips passed to CompositeAudioClip can be played at different
    times, it depends on their ``start`` attributes.
    """
    frequencies = [440, 880, 1760]
    durations = [2, 5, 1]
    fpss = [44100, 22050, 11025]
    starts = [0, 1, 2]

    clips = [
        AudioClip(
            lambda t: [np.sin(frequency * 2 * np.pi * t)], duration=duration, fps=fps
        ).with_start(start)
        for frequency, duration, fps, start in zip(frequencies, durations, fpss, starts)
    ]

    compound_clip = CompositeAudioClip(clips)

    # should return a CompositeAudioClip
    assert isinstance(compound_clip, CompositeAudioClip)

    # fps of the greatest fps passed into it
    assert compound_clip.fps == 44100

    # duration depends on clips starts and durations
    ends = [start + duration for start, duration in zip(starts, durations)]
    assert compound_clip.duration == max(ends)
    assert list(compound_clip.ends) == ends
    assert list(compound_clip.starts) == starts

    # channels are maximum number of channels of the clips
    assert compound_clip.nchannels == max(clip.nchannels for clip in clips)


def test_concatenate_audioclip_with_audiofileclip(util, stereo_wave):
    clip1 = AudioClip(
        stereo_wave(left_freq=440, right_freq=880),
        duration=1,
        fps=44100,
    )
    clip2 = AudioFileClip("media/crunching.mp3")

    concat_clip = concatenate_audioclips((clip1, clip2))
    concat_clip.write_audiofile(
        os.path.join(util.TMP_DIR, "concat_clip_with_file_audio.mp3"),
        logger=None,
    )

    assert concat_clip.duration == clip1.duration + clip2.duration


def test_concatenate_audiofileclips(util):
    clip1 = AudioFileClip("media/crunching.mp3").subclipped(1, 4)

    # Checks it works with videos as well
    clip2 = AudioFileClip("media/big_buck_bunny_432_433.webm")
    concat_clip = concatenate_audioclips((clip1, clip2))

    concat_clip.write_audiofile(
        os.path.join(util.TMP_DIR, "concat_audio_file.mp3"),
        logger=None,
    )

    assert concat_clip.duration == clip1.duration + clip2.duration


def test_audioclip_mono_max_volume(mono_wave):
    clip = AudioClip(mono_wave(440), duration=1, fps=44100)
    max_volume = clip.max_volume()
    assert isinstance(max_volume, float)
    assert max_volume > 0


@pytest.mark.parametrize(("nchannels"), (2, 4, 8, 16))
@pytest.mark.parametrize(("channel_muted"), ("left", "right"))
def test_audioclip_stereo_max_volume(nchannels, channel_muted):
    def frame_function(t):
        frame = []
        # build channels (one of each pair muted)
        for i in range(int(nchannels / 2)):
            if channel_muted == "left":
                # if muted channel is left, [0, sound, 0, sound...]
                frame.append(np.sin(t * 0))
                frame.append(np.sin(440 * 2 * np.pi * t))
            else:
                # if muted channel is right, [sound, 0, sound, 0...]
                frame.append(np.sin(440 * 2 * np.pi * t))
                frame.append(np.sin(t * 0))
        return np.array(frame).T

    clip = AudioClip(frame_function, fps=44100, duration=1)
    max_volume = clip.max_volume(stereo=True)
    # if `stereo == True`, `AudioClip.max_volume` returns a Numpy array`
    assert isinstance(max_volume, np.ndarray)
    assert len(max_volume) == nchannels

    # check channels muted and with sound
    for i, channel_max_volume in enumerate(max_volume):
        if i % 2 == 0:
            if channel_muted == "left":
                assert channel_max_volume == 0
            else:
                assert channel_max_volume > 0
        else:
            if channel_muted == "right":
                assert channel_max_volume == 0
            else:
                assert channel_max_volume > 0


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_BitmapClip.py
````python
"""BitmapClip tests."""

import numpy as np

import pytest

from moviepy.video.VideoClip import BitmapClip


def test_clip_generation():
    bitmap = [["RR", "RR"], ["RB", "RB"]]
    expected_frame_array = np.array(
        [
            np.array([[(255, 0, 0), (255, 0, 0)], [(255, 0, 0), (255, 0, 0)]]),
            np.array([[(255, 0, 0), (0, 0, 255)], [(255, 0, 0), (0, 0, 255)]]),
        ]
    )
    unexpected_frame_array = np.array(
        [
            np.array([[(255, 0, 0), (255, 0, 0)], [(255, 0, 0), (255, 0, 1)]]),
            np.array([[(255, 0, 0), (0, 0, 255)], [(255, 0, 0), (0, 0, 255)]]),
        ]
    )

    clip = BitmapClip(bitmap, fps=1)
    frame_array = np.array(list(clip.iter_frames()))

    # Check that frame_list == expected_frame_list
    assert np.array_equal(frame_array, expected_frame_array)

    # Check that frame_list != unexpected_frame_list
    assert not np.array_equal(frame_array, unexpected_frame_array)


def test_setting_fps():
    bitmap = [["R"], ["R"], ["B"], ["B"], ["G"], ["G"]]
    clip = BitmapClip(bitmap, fps=1)

    assert clip.fps == 1
    assert clip.duration == 6


def test_setting_duration():
    bitmap = [["R"], ["R"], ["B"], ["B"], ["G"], ["G"]]
    clip = BitmapClip(bitmap, duration=6)

    assert clip.fps == 1
    assert clip.duration == 6


def test_to_bitmap():
    bitmap = [["R"], ["R"], ["B"], ["B"], ["G"], ["G"]]
    clip1 = BitmapClip(bitmap, fps=0.345)
    clip2 = BitmapClip(bitmap, fps=1)
    clip3 = BitmapClip(bitmap, fps=3.12345)
    assert bitmap == clip1.to_bitmap()
    assert bitmap == clip2.to_bitmap()
    assert bitmap == clip3.to_bitmap()


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_Clip.py
````python
"""Clip tests."""

import copy

import numpy as np

import pytest

from moviepy.Clip import Clip
from moviepy.video.VideoClip import BitmapClip, ColorClip


def test_clip_equality():
    bitmap = [["RR", "RR"], ["RB", "RB"]]
    different_bitmap = [["RR", "RB"], ["RB", "RB"]]
    different_duration_bitmap = [["RR", "RR"], ["RB", "RB"], ["RR", "RR"]]

    clip = BitmapClip(bitmap, fps=1)
    same_clip = BitmapClip(bitmap, fps=1)

    different_clip = BitmapClip(different_bitmap, fps=1)
    different_duration_clip = BitmapClip(different_duration_bitmap, fps=1)

    assert clip == same_clip
    assert clip != different_clip
    assert clip != different_duration_clip
    assert different_clip != different_duration_clip


def test_clip_with_is_mask():
    clip = BitmapClip([["RR", "GG"]], fps=1)
    assert not clip.is_mask

    assert clip.with_is_mask(True).is_mask

    assert not clip.with_is_mask(False).is_mask


@pytest.mark.parametrize(
    (
        "start",
        "end",
        "duration",
        "new_start",
        "change_end",
        "expected_end",
        "expected_duration",
    ),
    (
        (0, 3, 3, 1, True, 4, 3),
        (0, 3, 3, 1, False, 3, 2),  # not change_end
    ),
)
def test_clip_with_start(
    start,
    end,
    duration,
    new_start,
    change_end,
    expected_end,
    expected_duration,
):
    clip = (
        ColorClip(color=(255, 0, 0), size=(2, 2))
        .with_fps(1)
        .with_duration(duration)
        .with_end(end)
        .with_start(start)
    )

    new_clip = clip.with_start(new_start, change_end=change_end)

    assert new_clip.end == expected_end
    assert new_clip.duration == expected_duration


@pytest.mark.parametrize(
    ("duration", "start", "end", "expected_start", "expected_duration"),
    (
        (3, 1, 2, 1, 1),
        (3, 1, None, 1, 3),  # end is None
        (3, None, 4, 1, 3),  # start is None
    ),
)
def test_clip_with_end(duration, start, end, expected_start, expected_duration):
    clip = ColorClip(color=(255, 0, 0), size=(2, 2), duration=duration).with_fps(1)
    if start is not None:
        clip = clip.with_start(start)
    else:
        clip.start = None
    clip = clip.with_end(end)

    assert clip.start == expected_start
    assert clip.duration == expected_duration


@pytest.mark.parametrize(
    (
        "duration",
        "start",
        "end",
        "new_duration",
        "change_end",
        "expected_duration",
        "expected_start",
        "expected_end",
    ),
    (
        (5, None, None, 3, True, 3, 0, 3),
        ("00:00:05", 1, 6, 3, True, 3, 1, 4),  # change end
        ((0, 0, 5), 1, 6, 3, False, 3, 3, 6),  # change start
        (5, None, None, None, False, ValueError, None, None),
    ),
)
def test_clip_with_duration(
    duration,
    start,
    end,
    new_duration,
    change_end,
    expected_duration,
    expected_start,
    expected_end,
):
    clip = ColorClip(color=(255, 0, 0), size=(2, 2)).with_fps(1).with_duration(duration)
    if start is not None:
        clip = clip.with_start(start)
    if end is not None:
        clip = clip.with_end(end)

    if hasattr(expected_duration, "__traceback__"):
        with pytest.raises(expected_duration):
            clip.with_duration(new_duration, change_end=change_end)
    else:
        clip = clip.with_duration(new_duration, change_end=change_end)

        assert clip.duration == expected_duration
        assert clip.start == expected_start
        assert clip.end == expected_end


@pytest.mark.parametrize(
    "copy_func",
    (
        lambda clip: clip.copy(),
        lambda clip: copy.copy(clip),
        lambda clip: copy.deepcopy(clip),
    ),
    ids=(
        "clip.copy()",
        "copy.copy(clip)",
        "copy.deepcopy(clip)",
    ),
)
def test_clip_copy(copy_func):
    """Clip must be copied with `.copy()` method, `copy.copy()` and
    `copy.deepcopy()` (same behaviour).
    """
    clip = Clip()
    other_clip = Clip()

    # shallow copy of clip
    for attr in clip.__dict__:
        setattr(clip, attr, "foo")

    copied_clip = copy_func(clip)

    # assert copied attributes
    for attr in copied_clip.__dict__:
        assert getattr(copied_clip, attr) == getattr(clip, attr)

        # other instances are not edited
        assert getattr(copied_clip, attr) != getattr(other_clip, attr)


@pytest.mark.parametrize(
    ("duration", "start_time", "end_time", "expected_duration"),
    (
        (1, 0, None, 1),
        (3, 0, 2, 2),
        (3, 1, 2, 1),
        (3, -2, 2, 1),  # negative start_time
        (3, 4, None, ValueError),  # start_time > duration
        (3, 3, None, ValueError),  # start_time == duration
        (3, 1, -1, 1),  # negative end_time
        (None, 1, -1, ValueError),  # negative end_time for clip without duration
        (1, 0, 2, ValueError),  # end_time after video end should raise exception
    ),
)
def test_clip_subclip(duration, start_time, end_time, expected_duration):
    if duration is None:
        clip = ColorClip(color=(255, 0, 0), size=(2, 2)).with_fps(1)
    else:
        clip = BitmapClip([["RR", "GG"] for _ in range(duration)], fps=1)

    if hasattr(expected_duration, "__traceback__"):
        with pytest.raises(expected_duration):
            clip.subclipped(start_time=start_time, end_time=end_time)
    else:
        sub_clip = clip.subclipped(start_time=start_time, end_time=end_time)
        assert sub_clip.duration == expected_duration


@pytest.mark.parametrize(
    ("start_time", "end_time", "expected_frames"),
    (
        (
            1,
            2,
            [["RR", "RR"], ["BB", "BB"]],
        ),
        (
            1,
            3,
            [["RR", "RR"]],
        ),
        (
            2,
            3,
            [["RR", "RR"], ["GG", "GG"]],
        ),
        (
            0,
            1,
            [["GG", "GG"], ["BB", "BB"]],
        ),
        (
            0,
            2,
            [["BB", "BB"]],
        ),
    ),
)
def test_clip_cutout(start_time, end_time, expected_frames):
    clip = BitmapClip([["RR", "RR"], ["GG", "GG"], ["BB", "BB"]], fps=1)
    new_clip = clip.with_section_cut_out(start_time, end_time)

    assert new_clip == BitmapClip(expected_frames, fps=1)


def test_clip_memoize():
    clip = BitmapClip([["RR", "RR"], ["GG", "GG"], ["BB", "BB"]], fps=1)

    assert not clip.memoize

    memoize_clip = clip.with_memoize(True)
    assert memoize_clip.memoize

    # get_frame memoizing
    memoize_clip.memoized_t = 5
    memoize_clip.memoized_frame = "foo"

    assert memoize_clip.get_frame(5) == "foo"

    assert isinstance(memoize_clip.get_frame(1), np.ndarray)


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_compositing.py
````python
"""Compositing tests for use with pytest."""

import os

import numpy as np

import pytest

from moviepy import *


class ClipPixelTest:
    ALLOWABLE_COLOR_VARIATION = 3  # from 0-767: how much mismatch do we allow

    def __init__(self, clip):
        self.clip = clip

    def expect_color_at(self, ts, expected, xy=[0, 0]):
        frame = self.clip.frame_function(ts)
        r, g, b = expected
        actual = frame[xy[1]][xy[0]]
        diff = abs(actual[0] - r) + abs(actual[1] - g) + abs(actual[2] - b)

        mismatch = diff > ClipPixelTest.ALLOWABLE_COLOR_VARIATION
        assert (
            not mismatch
        ), "Expected (%02x,%02x,%02x) but got (%02x,%02x,%02x) at timestamp %s" % (
            *expected,
            *actual,
            ts,
        )


def test_clips_array(util):
    red = ColorClip((1024, 800), color=(255, 0, 0))
    green = ColorClip((1024, 800), color=(0, 255, 0))
    blue = ColorClip((1024, 800), color=(0, 0, 255))

    video = clips_array([[red, green, blue]])

    with pytest.raises(ValueError):  # duration not set
        video.with_effects([vfx.Resize(width=480)]).write_videofile(
            os.path.join(util.TMP_DIR, "test_clips_array.mp4")
        )


def test_clips_array_duration(util):
    filename = os.path.join(util.TMP_DIR, "test_clips_array.mp4")

    # NOTE: anyone knows what behaviour this sets ? If yes please replace
    # this comment.
    red = ColorClip((256, 200), color=(255, 0, 0))
    green = ColorClip((256, 200), color=(0, 255, 0))
    blue = ColorClip((256, 200), color=(0, 0, 255))

    video = clips_array([[red, green, blue]]).with_duration(5)
    with pytest.raises(AttributeError):  # fps not set
        video.write_videofile(filename)

    # this one should work correctly
    red.fps = green.fps = blue.fps = 30
    video = clips_array([[red, green, blue]]).with_duration(5)
    video.write_videofile(filename)


def test_concatenate_self(util):
    clip = BitmapClip([["AAA", "BBB"], ["CCC", "DDD"]], fps=1)
    target = BitmapClip([["AAA", "BBB"], ["CCC", "DDD"]], fps=1)

    concatenated = concatenate_videoclips([clip])

    concatenated.write_videofile(
        os.path.join(util.TMP_DIR, "test_concatenate_self.mp4")
    )
    assert concatenated == target


def test_concatenate_floating_point(util):
    """
    >>> print("{0:.20f}".format(1.12))
    1.12000000000000010658

    This test uses duration=1.12 to check that it still works when the clip
    duration is represented as being bigger than it actually is. Fixed in #1195.
    """
    clip = ColorClip([100, 50], color=[255, 128, 64], duration=1.12).with_fps(25.0)
    concat = concatenate_videoclips([clip])
    concat.write_videofile(os.path.join(util.TMP_DIR, "concat.mp4"), preset="ultrafast")


def test_blit_with_opacity():
    # has one second R, one second G, one second B
    size = (2, 2)
    clip1 = (
        ColorClip(size, color=(255, 0, 0), duration=1)
        + ColorClip(size, color=(0, 255, 0), duration=1)
        + ColorClip(size, color=(0, 0, 255), duration=1)
    )

    # overlay green at half opacity during first 2 sec
    clip2 = ColorClip(size, color=(0, 255, 0), duration=2).with_opacity(0.5)
    composite = CompositeVideoClip([clip1, clip2])
    bt = ClipPixelTest(composite)

    # red + 50% green
    bt.expect_color_at(0.5, (0x7F, 0x7F, 0x00))
    # green + 50% green
    bt.expect_color_at(1.5, (0x00, 0xFF, 0x00))
    # blue is after 2s, so keep untouched
    bt.expect_color_at(2.5, (0x00, 0x00, 0xFF))


def test_compositing_masks(util):
    # Has one R 30%, one G 30%, one B 30%
    clip1 = ColorClip((100, 100), (255, 0, 0, 76.5)).with_duration(2)
    clip2 = ColorClip((50, 50), (0, 255, 0, 76.5)).with_duration(2)
    clip3 = ColorClip((25, 25), (0, 0, 255, 76.5)).with_duration(2)

    compostite_clip1 = CompositeVideoClip(
        [clip1, clip2.with_position(("center", "center"))],
        bg_color=None,
    )
    compostite_clip2 = CompositeVideoClip(
        [compostite_clip1, clip3.with_position(("center", "center"))],
        bg_color=None,
    )

    # Load output file and check transparency
    frame = compostite_clip2.mask.get_frame(1)

    # We check opacity with one, two and three layers
    # Allow for a bit of tolerance (about 1%) to account
    # for rounding errors
    opacity1 = frame[50, 10]
    opacity2 = frame[50, 30]
    opacity3 = frame[50, 50]
    assert abs(opacity1 - 0.3) < 0.01
    assert abs(opacity2 - 0.51) < 0.01
    assert abs(opacity3 - 0.657) < 0.01


def test_compositing_with_transparency_colors(util):
    # Has one R 30%, one G 30%, one B 30%
    clip1 = ColorClip((100, 100), (255, 0, 0, 76.5)).with_duration(2)
    clip2 = ColorClip((50, 50), (0, 255, 0, 76.5)).with_duration(2)
    clip3 = ColorClip((25, 25), (0, 0, 255, 76.5)).with_duration(2)

    compostite_clip1 = CompositeVideoClip(
        [clip1, clip2.with_position(("center", "center"))],
        bg_color=None,  # No background color, so it should be transparent
    )
    compostite_clip2 = CompositeVideoClip(
        [compostite_clip1, clip3.with_position(("center", "center"))],
        bg_color=None,
    )

    # Load output file and check transparency
    frame = compostite_clip2.get_frame(1)
    mask = compostite_clip2.mask.get_frame(1)

    # We check color with 1 layer
    # We add a bit of tolerance (about 1%) to account
    # For possible rounding errors
    color1 = frame[50, 10]
    opacity1 = mask[50, 10]
    assert np.allclose(color1, [255, 0, 0], rtol=0.01)
    assert abs(opacity1 - 0.3) < 0.01

    # With 2 layers
    color2 = frame[50, 30]
    opacity2 = mask[50, 30]
    assert np.allclose(color2, [105, 150, 0], rtol=0.01)
    assert abs(opacity2 - 0.51) < 0.01

    # With 3 layers
    color3 = frame[50, 50]
    opacity3 = mask[50, 50]
    assert np.allclose(color3, [57, 82, 116], rtol=0.01)
    assert abs(opacity3 - 0.657) < 0.01


def test_slide_in():
    duration = 0.1
    size = (10, 1)
    fps = 10
    color = (255, 0, 0)

    # left and right sides
    clip = ColorClip(
        color=color,
        duration=duration,
        size=size,
    ).with_fps(fps)

    for side in ["left", "right"]:
        new_clip = CompositeVideoClip(
            [clip.with_effects([vfx.SlideIn(duration, side)])]
        )

        for t in np.arange(0, duration, duration / fps):
            n_reds, n_reds_expected = (0, int(t * 100))

            if t:
                assert n_reds_expected

            if n_reds_expected == 7:  # skip 7 due to inaccurate frame
                continue

            for r, g, b in new_clip.get_frame(t)[0]:
                if r == color[0] and g == color[1] and g == color[2]:
                    n_reds += 1

            assert n_reds == n_reds_expected

    # top and bottom sides
    clip = ColorClip(
        color=color,
        duration=duration,
        size=(size[1], size[0]),
    ).with_fps(fps)

    for side in ["top", "bottom"]:
        new_clip = CompositeVideoClip(
            [clip.with_effects([vfx.SlideIn(duration, side)])]
        )
        for t in np.arange(0, duration, duration / fps):
            n_reds, n_reds_expected = (0, int(t * 100))

            if t:
                assert n_reds_expected

            if n_reds_expected == 7:  # skip 7 due to inaccurate frame
                continue

            for row in new_clip.get_frame(t):
                r, g, b = row[0]

                if r == color[0] and g == color[1] and g == color[2]:
                    n_reds += 1

            assert n_reds == n_reds_expected


def test_slide_out():
    duration = 0.1
    size = (11, 1)
    fps = 10
    color = (255, 0, 0)

    # left and right sides
    clip = ColorClip(
        color=color,
        duration=duration,
        size=size,
    ).with_fps(fps)

    for side in ["left", "right"]:
        new_clip = CompositeVideoClip(
            [clip.with_effects([vfx.SlideOut(duration, side)])]
        )

        for t in np.arange(0, duration, duration / fps):
            n_reds, n_reds_expected = (0, round(11 - t * 100, 6))

            if t:
                assert n_reds_expected

            for r, g, b in new_clip.get_frame(t)[0]:
                if r == color[0] and g == color[1] and g == color[2]:
                    n_reds += 1

            assert n_reds == n_reds_expected

    # top and bottom sides
    clip = ColorClip(
        color=color,
        duration=duration,
        size=(size[1], size[0]),
    ).with_fps(fps)

    for side in ["top", "bottom"]:
        new_clip = CompositeVideoClip(
            [clip.with_effects([vfx.SlideOut(duration, side)])]
        )
        for t in np.arange(0, duration, duration / fps):
            n_reds, n_reds_expected = (0, round(11 - t * 100, 6))

            if t:
                assert n_reds_expected

            for row in new_clip.get_frame(t):
                r, g, b = row[0]

                if r == color[0] and g == color[1] and g == color[2]:
                    n_reds += 1

            assert n_reds == n_reds_expected


def test_concatenate_with_masks(util):
    video_without_mask = (
        ColorClip(size=(10, 10), color=(255, 0, 0)).with_duration(1).with_fps(1)
    )
    video_with_mask = (
        ColorClip(size=(5, 5), color=(0, 255, 0))
        .with_duration(1)
        .with_fps(1)
        .with_mask()
    )

    output = os.path.join(util.TMP_DIR, "test_concatenate_with_masks.mp4")
    concatenate_videoclips([video_without_mask, video_with_mask]).write_videofile(
        output
    )


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_doc_examples.py
````python
"""Try to run all the documentation examples with runpy and check they don't raise
exceptions.
"""

import os
import pathlib
import runpy
import shutil
from contextlib import contextmanager

import pytest

from moviepy.tools import no_display_available


@contextmanager
def cwd(path):
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


# Dir for doc code examples to run
DOC_EXAMPLES_DIR = "docs/_static/code"

# List of examples script to ignore, mostly scripts that are too long
DOC_EXAMPLES_IGNORE = ["trailer.py", "display_in_notebook.py"]

# If no display, also remove all examples using preview
if no_display_available():
    DOC_EXAMPLES_IGNORE.append("preview.py")

scripts = list(pathlib.Path(DOC_EXAMPLES_DIR).resolve().rglob("*.py"))
scripts = dict(zip(map(str, scripts), scripts))  # This make test name more readable


@pytest.mark.parametrize("script", scripts)
def test_doc_examples(util, tmp_path, script):
    if os.path.basename(script) == "preview.py":
        pytest.skip("Skipping preview.py because no display is available")
    print("Try script: ", script)

    if os.path.basename(script) in DOC_EXAMPLES_IGNORE:
        return

    # Lets build a test dir with all medias needed to run our test in
    shutil.copytree(util.DOC_EXAMPLES_MEDIAS_DIR, os.path.join(tmp_path, "doc_tests"))
    test_dir = os.path.join(tmp_path, "doc_tests")

    with cwd(test_dir):
        runpy.run_path(script)


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_ffmpeg_reader.py
````python
"""FFmpeg reader tests meant to be run with pytest."""

import os
import subprocess
import time

import numpy as np

import pytest

from moviepy.audio.AudioClip import AudioClip
from moviepy.config import FFMPEG_BINARY
from moviepy.tools import ffmpeg_escape_filename
from moviepy.video.compositing.CompositeVideoClip import clips_array
from moviepy.video.io.ffmpeg_reader import (
    FFMPEG_VideoReader,
    FFmpegInfosParser,
    ffmpeg_parse_infos,
)
from moviepy.video.io.ffmpeg_tools import ffmpeg_version
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import BitmapClip, ColorClip


def test_ffmpeg_parse_infos():
    d = ffmpeg_parse_infos("media/big_buck_bunny_432_433.webm")
    assert d["duration"] == 1.0
    assert d["audio_fps"] == 44100

    d = ffmpeg_parse_infos("media/pigs_in_a_polka.gif")
    assert d["video_size"] == [314, 273]
    assert d["duration"] == 3.0
    assert not d["audio_found"]

    d = ffmpeg_parse_infos("media/video_with_failing_audio.mp4")
    assert d["audio_found"]
    assert d["audio_fps"] == 44100
    assert d["audio_bitrate"] == 127

    d = ffmpeg_parse_infos("media/crunching.mp3")
    assert d["audio_found"]
    assert d["audio_fps"] == 48000
    assert d["metadata"]["artist"] == "SoundJay.com Sound Effects"

    d = ffmpeg_parse_infos("media/sintel_with_14_chapters.mp4")
    assert d["audio_found"]
    assert d["video_found"]
    assert d["audio_bitrate"]
    assert d["video_bitrate"]


def test_ffmpeg_parse_infos_video_nframes():
    d = ffmpeg_parse_infos("media/big_buck_bunny_0_30.webm")
    assert d["video_n_frames"] == 720

    d = ffmpeg_parse_infos("media/bitmap.mp4")
    assert d["video_n_frames"] == 5


def test_ffmpeg_parse_infos_no_default_stream(util):
    """WMV files don't have "default" streams marked in ffmpeg output.
    Make sure that ffmpeg_parse_infos can handle this case.
    """
    mp4_filepath = os.path.abspath("media/smpte-2997.mp4")
    wmv_filepath = os.path.join(
        util.TMP_DIR, "ffmpeg_parse_infos_no_default_stream-smpte-2997.wmv"
    )

    cmd = [
        FFMPEG_BINARY,
        "-y",
        "-i",
        ffmpeg_escape_filename(mp4_filepath),
        ffmpeg_escape_filename(wmv_filepath),
    ]
    with open(os.devnull, "w") as stderr:
        subprocess.check_call(cmd, stderr=stderr)

    d = ffmpeg_parse_infos(wmv_filepath)

    for key in (
        "default_video_stream_number",
        "default_video_input_number",
        "default_audio_stream_number",
        "default_audio_input_number",
        "video_fps",
        "audio_fps",
    ):
        assert key in d


@pytest.mark.parametrize(
    ("decode_file", "expected_duration"),
    (
        (False, 30),
        (True, 30),
    ),
    ids=(
        "decode_file=False",
        "decode_file=True",
    ),
)
def test_ffmpeg_parse_infos_decode_file(decode_file, expected_duration):
    """Test `decode_file` argument of `ffmpeg_parse_infos` function."""
    d = ffmpeg_parse_infos("media/big_buck_bunny_0_30.webm", decode_file=decode_file)

    # On old version of ffmpeg, duration and video duration was different
    if int(ffmpeg_version()[1].split(".")[0]) < 7:
        expected_duration += 0.02

    assert d["duration"] == expected_duration

    # check metadata is fine
    assert len(d["metadata"]) == 1

    # check input
    assert len(d["inputs"]) == 1

    # check streams
    streams = d["inputs"]["streams"]
    assert len(streams) == 2
    assert streams[0]["stream_type_lower"] == "video"
    assert streams[0]["stream_number"] == 0
    assert streams[0]["fps"] == 24
    assert streams[0]["size"] == [1280, 720]
    assert streams[0]["default"] is True
    assert streams[0]["language"] is None

    assert streams[1]["stream_type_lower"] == "audio"
    assert streams[1]["stream_number"] == 1
    assert streams[1]["fps"] == 44100
    assert streams[1]["default"] is True
    assert streams[1]["language"] is None


def test_ffmpeg_parse_infos_multiple_audio_streams(util, mono_wave):
    """Check that ``ffmpeg_parse_infos`` can parse multiple audio streams."""
    # Create two mono audio files
    clip_440_filepath = os.path.join(
        util.TMP_DIR, "ffmpeg_parse_infos_multiple_streams_440.mp3"
    )
    clip_880_filepath = os.path.join(
        util.TMP_DIR, "ffmpeg_parse_infos_multiple_streams_880.mp3"
    )
    multiple_streams_filepath = os.path.join(
        util.TMP_DIR, "ffmpeg_parse_infos_multiple_streams.mp4"
    )

    clip_440 = AudioClip(mono_wave(440), fps=22050, duration=0.01)
    clip_880 = AudioClip(mono_wave(880), fps=22050, duration=0.01)
    clip_440.write_audiofile(clip_440_filepath)
    clip_880.write_audiofile(clip_880_filepath)

    # create a MP4 file with multiple streams
    cmd = [
        FFMPEG_BINARY,
        "-y",
        "-i",
        clip_440_filepath,
        "-i",
        clip_880_filepath,
        "-map",
        "0:a:0",
        "-map",
        "0:a:0",
        multiple_streams_filepath,
    ]
    with open(os.devnull, "w") as stderr:
        subprocess.check_call(cmd, stderr=stderr)

    # check that `ffmpeg_parse_infos` can parse all the streams data
    d = ffmpeg_parse_infos(multiple_streams_filepath)

    # number of inputs and streams
    assert len(d["inputs"]) == 1
    assert len(d["inputs"]["streams"]) == 2

    default_stream = d["inputs"]["streams"][0]
    ignored_stream = d["inputs"]["streams"][1]

    # default, only the first
    assert default_stream["default"]
    assert not ignored_stream["default"]

    # streams and inputs numbers
    assert default_stream["stream_number"] == 0
    assert ignored_stream["stream_number"] == 1
    assert default_stream["input_number"] == 0
    assert ignored_stream["input_number"] == 0

    # stream type
    assert default_stream["stream_type_lower"] == "audio"
    assert ignored_stream["stream_type_lower"] == "audio"

    # cleanup
    for filepath in [
        clip_440_filepath,
        clip_880_filepath,
        multiple_streams_filepath,
    ]:
        os.remove(filepath)


def test_ffmpeg_parse_infos_metadata(util, mono_wave):
    """Check that `ffmpeg_parse_infos` is able to retrieve metadata from files."""
    filepath = os.path.join(util.TMP_DIR, "ffmpeg_parse_infos_metadata.mkv")
    if os.path.isfile(filepath):
        os.remove(filepath)

    # create video with 2 streams, video and audio
    audioclip = AudioClip(mono_wave(440), fps=22050).with_duration(1)
    videoclip = BitmapClip([["RGB"]], fps=1).with_duration(1).with_audio(audioclip)

    # build metadata key-value pairs which will be passed to ``ffmpeg_params``
    # argument of ``videoclip.write_videofile``
    metadata = {
        "file": {
            "title": "Fóò",
            "comment": "bar",
            "description": "BAZ",
            "synopsis": "Testing",
        },
        "video": {
            "author": "Querty",
            "title": "hello",
            "description": "asdf",
        },
        "audio": {"track": "1", "title": "wtr", "genre": "lilihop"},
    }

    ffmpeg_params = []
    for metadata_type, data in metadata.items():
        option = "-metadata"
        if metadata_type in ["video", "audio"]:
            option += ":s:%s:0" % ("v" if metadata_type == "video" else "a")
        for field, value in data.items():
            ffmpeg_params.extend([option, f"{field}={value}"])

    languages = {
        "audio": "eng",
        "video": "spa",
    }
    ffmpeg_params.extend(
        [
            "-metadata:s:a:0",
            "language=" + languages["audio"],
            "-metadata:s:v:0",
            "language=" + languages["video"],
        ]
    )

    # create file with metadata included
    videoclip.write_videofile(filepath, codec="libx264", ffmpeg_params=ffmpeg_params)

    # get information about created file
    d = ffmpeg_parse_infos(filepath)

    def get_value_from_dict_using_lower_key(field, dictionary):
        """Obtains a value from a dictionary using a key, no matter if the key
        is uppercased in the dictionary. This function is needed because
        some media containers convert to uppercase metadata field names.
        """
        value = None
        for d_field, d_value in dictionary.items():
            if str(d_field).lower() == field:
                value = d_value
                break
        return value

    # assert file metadata
    for field, value in metadata["file"].items():
        assert get_value_from_dict_using_lower_key(field, d["metadata"]) == value

    # assert streams metadata
    streams = {"audio": None, "video": None}
    for stream in d["inputs"]["streams"]:
        streams[stream["stream_type_lower"]] = stream

    for stream_type, stream in streams.items():
        for field, value in metadata[stream_type].items():
            assert (
                get_value_from_dict_using_lower_key(field, stream["metadata"]) == value
            )

    # assert stream languages
    for stream_type, stream in streams.items():
        assert stream["language"] == languages[stream_type]

    os.remove(filepath)


def test_ffmpeg_parse_infos_chapters():
    """Check that `ffmpeg_parse_infos` can parse chapters with their metadata."""
    d = ffmpeg_parse_infos("media/sintel_with_14_chapters.mp4")

    chapters = d["inputs"]["chapters"]

    num_chapters_expected = 14

    assert len(chapters) == num_chapters_expected
    for num in range(0, len(chapters)):
        assert chapters[num]["chapter_number"] == num
        assert chapters[num]["end"] == (num + 1) / 10
        assert chapters[num]["start"] == num / 10
        assert chapters[num]["metadata"]["title"]
        assert isinstance(chapters[num]["metadata"]["title"], str)


def test_ffmpeg_parse_infos_metadata_with_attached_pic():
    """Check that the parser can parse audios with attached pictures.

    Currently, does not distinguish if the video found is an attached picture,
    this test serves mainly to ensure that #1487 issue does not happen again:
    """
    d = ffmpeg_parse_infos("media/with-attached-pic.mp3")

    assert d["audio_bitrate"] == 320
    assert d["audio_found"]
    assert d["audio_fps"] == 44100

    assert len(d["inputs"]) == 1
    streams = d["inputs"]["streams"]
    assert len(streams) == 2
    assert streams[0]["stream_type_lower"] == "audio"
    assert streams[1]["stream_type_lower"] == "video"

    assert len(d["metadata"].keys()) == 7


def test_ffmpeg_parse_video_rotation():
    d = ffmpeg_parse_infos("media/rotated-90-degrees.mp4")
    assert d["video_rotation"] == 90
    assert d["video_size"] == [1920, 1080]


def test_correct_video_rotation(util):
    """See https://github.com/Zulko/moviepy/pull/577"""
    clip = VideoFileClip("media/rotated-90-degrees.mp4").subclipped(0.2, 0.4)

    corrected_rotation_filename = os.path.join(
        util.TMP_DIR,
        "correct_video_rotation.mp4",
    )
    clip.write_videofile(corrected_rotation_filename)

    d = ffmpeg_parse_infos(corrected_rotation_filename)
    assert "video_rotation" not in d
    assert d["video_size"] == [1080, 1920]


def test_ffmpeg_parse_infos_multiline_metadata():
    """Check that the parser can parse multiline metadata values."""
    infos = """Input #0, mov,mp4,m4a,3gp,3g2,mj2, from '/home/110_PREV_FINAL.mov':
  Metadata:
    major_brand     : foo
    minor_version   : 537199360
    compatible_brands: bar
    creation_time   : 2999-08-12 09:00:01
    xmw             : <?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>
                    : <second XML line">
                    :  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/22-rdf-syntax-ns#">
                    :   <rdf:Description rdf:about=""
                    :     xmlns:xmpMM="http://nowhere.ext"
                    :     xmlns:xmpDM="http://nowhere.ext/"
                    :     xmlns:stDim="http://nowhere.ext/Dimensions#"
                    :     xmlns:dc="http://nowhere.ext/dc/elements/1.1/"
                    :    xmpMM:DocumentID="xmw.did:39FA818BE85AE511B9009F953BF804AA"
                    :    xmwMM:InstanceID="xmw.iid:39FA818BE85AE511B9009F953BF804AA"
                    :    xmwDM:videoFrameRate="24.000000"
                    :    xmwDM:videoFieldOrder="Progressive"
                    :    xmwDM:videoPixelAspectRatio="1/1"
                    :    xmwDM:audioSampleRate="44100"
                    :    xmwDM:audioSampleType="16Int"
                    :    xmwDM:audioChannelType="Mono"
                    :    dc:format="QuickTimeline">
                    :    <xmwDM:startTimecode
                    :     xmwDM:timeValue="00:00:00:00"
                    :     xmwDM:timeFormat="24Timecode"/>
                    :    <xmwDM:altTimecode
                    :     xmwDM:timeValue="00:00:00:00"
                    :     xmwDM:timeFormat="24Timecode"/>
                    :    <xmwDM:videoFrameSize
                    :     stDim:w="768"
                    :     stDim:h="576"
                    :     stDim:unit="pixel"/>
                    :   </rdf:Description>
                    :  </rdf:RDF>
                    : </x:xmwmeta>
                    :
                    :
                    : <?xpacket end="w"?>
  Duration: 00:02:10.67, start: 0.000000, bitrate: 26287 kb/s
  Stream #0:0(eng): Video: mjpeg 768x576 26213 kb/s, 24 fps, 24 tbr (default)
    Metadata:
      creation_time   : 2015-09-14 14:57:32
      handler_name    : Foo
                      : Bar
      encoder         : Photo - JPEG
      timecode        : 00:00:00:00
  Stream #0:1(eng): Audio: aac (mp4a / 0x6), 44100 Hz, mono, fltp, 64 kb/s (default)
    Metadata:
      creation_time   : 2015-09-14 14:57:33
      handler_name    : Bar
                      : Foo
      timecode        : 00:00:00:00
  Stream #0:2(eng): Data: none (tmcd / 0x64636D74) (default)
    Metadata:
      creation_time   : 2015-09-14 14:58:24
      handler_name    : Baz
                      : Foo
      timecode        : 00:00:00:00
At least one output file must be specified
"""

    d = FFmpegInfosParser(infos, "foo.mkv").parse()

    # container data
    assert d["audio_bitrate"] == 64
    assert d["audio_found"] is True
    assert d["audio_fps"] == 44100
    assert d["duration"] == 130.67
    assert d["video_duration"] == 130.67
    assert d["video_found"] is True
    assert d["video_fps"] == 24
    assert d["video_n_frames"] == 3136
    assert d["video_size"] == [768, 576]
    assert d["start"] == 0
    assert d["default_audio_input_number"] == 0
    assert d["default_audio_stream_number"] == 1
    assert d["default_data_input_number"] == 0
    assert d["default_data_stream_number"] == 2
    assert d["default_video_input_number"] == 0
    assert d["default_video_stream_number"] == 0

    # container metadata
    assert d["metadata"]["compatible_brands"] == "bar"
    assert d["metadata"]["creation_time"] == "2999-08-12 09:00:01"
    assert d["metadata"]["major_brand"] == "foo"
    assert d["metadata"]["minor_version"] == "537199360"
    assert d["metadata"]["xmw"] == (
        """<?xpacket begin="\ufeff" id="W5M0MpCehiHzreSzNTczkc9d"?>
<second XML line">
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/22-rdf-syntax-ns#">
<rdf:Description rdf:about=""
xmlns:xmpMM="http://nowhere.ext"
xmlns:xmpDM="http://nowhere.ext/"
xmlns:stDim="http://nowhere.ext/Dimensions#"
xmlns:dc="http://nowhere.ext/dc/elements/1.1/"
xmpMM:DocumentID="xmw.did:39FA818BE85AE511B9009F953BF804AA"
xmwMM:InstanceID="xmw.iid:39FA818BE85AE511B9009F953BF804AA"
xmwDM:videoFrameRate="24.000000"
xmwDM:videoFieldOrder="Progressive"
xmwDM:videoPixelAspectRatio="1/1"
xmwDM:audioSampleRate="44100"
xmwDM:audioSampleType="16Int"
xmwDM:audioChannelType="Mono"
dc:format="QuickTimeline">
<xmwDM:startTimecode
xmwDM:timeValue="00:00:00:00"
xmwDM:timeFormat="24Timecode"/>
<xmwDM:altTimecode
xmwDM:timeValue="00:00:00:00"
xmwDM:timeFormat="24Timecode"/>
<xmwDM:videoFrameSize
stDim:w="768"
stDim:h="576"
stDim:unit="pixel"/>
</rdf:Description>
</rdf:RDF>
</x:xmwmeta>


<?xpacket end="w"?>"""
    )

    # streams
    assert len(d["inputs"]) == 1

    streams = d["inputs"]["streams"]
    assert len(streams) == 3

    # video stream
    assert streams[0]["default"] is True
    assert streams[0]["fps"] == 24
    assert streams[0]["input_number"] == 0
    assert streams[0]["language"] == "eng"
    assert streams[0]["stream_number"] == 0
    assert streams[0]["stream_type_lower"] == "video"
    assert streams[0]["size"] == [768, 576]

    assert streams[0]["metadata"]["creation_time"] == "2015-09-14 14:57:32"
    assert streams[0]["metadata"]["encoder"] == "Photo - JPEG"
    assert streams[0]["metadata"]["handler_name"] == "Foo\nBar"
    assert streams[0]["metadata"]["timecode"] == "00:00:00:00"

    # audio stream
    assert streams[1]["default"] is True
    assert streams[1]["fps"] == 44100
    assert streams[1]["input_number"] == 0
    assert streams[1]["language"] == "eng"
    assert streams[1]["stream_number"] == 1
    assert streams[1]["stream_type_lower"] == "audio"

    assert streams[1]["metadata"]["creation_time"] == "2015-09-14 14:57:33"
    assert streams[1]["metadata"]["timecode"] == "00:00:00:00"
    assert streams[1]["metadata"]["handler_name"] == "Bar\nFoo"

    # data stream
    assert streams[2]["default"] is True
    assert streams[2]["input_number"] == 0
    assert streams[2]["language"] == "eng"
    assert streams[2]["stream_number"] == 2
    assert streams[2]["stream_type_lower"] == "data"

    assert streams[2]["metadata"]["creation_time"] == "2015-09-14 14:58:24"
    assert streams[2]["metadata"]["timecode"] == "00:00:00:00"
    assert streams[2]["metadata"]["handler_name"] == "Baz\nFoo"


def test_not_default_audio_stream_audio_bitrate():
    infos = """Input #0, avi, from 'file_example_AVI_1280_1_5MG.avi':
  Metadata:
    encoder         : Lavf57.19.100
  Duration: 00:00:30.61, start: 0.000000, bitrate: 387 kb/s
    Stream #0:0: Video: ..., 30 tbr, 60 tbc
    Stream #0:1: Audio: aac (LC) (...), 48000 Hz, stereo, fltp, 139 kb/s
"""

    d = FFmpegInfosParser(infos, "foo.avi").parse()
    assert d["audio_bitrate"] == 139


def test_stream_deidentation_not_raises_error():
    """Test libavformat reduced streams identation to 2 spaces.

    See https://github.com/FFmpeg/FFmpeg/commit/b7251aed
    """
    infos = """Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'clip.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    encoder         : Lavf58.12.100
  Duration: 01:00:00.00, start: 0.000000, bitrate: 1222 kb/s
  Stream #0:0(und): Video: ..., 30 tbr, 60 tbc
    Metadata:
      handler_name    : VideoHandler
      vendor_id       : [0][0][0][0]
At least one output file must be specified"""

    d = FFmpegInfosParser(infos, "clip.mp4").parse()

    assert d
    assert len(d["inputs"]["streams"]) == 1


def test_stream_square_brackets():
    infos = """
Input #0, mpeg, from 'clip.mp4':
  Duration: 00:02:15.00, start: 52874.498178, bitrate: 266 kb/s
    Stream #0:0[0x1e0]: Video: ..., 25 tbr, 90k tbn, 50 tbc
    Stream #0:1[0x1c0]: Audio: mp2, 0 channels, s16p
At least one output file must be specified"""

    d = FFmpegInfosParser(infos, "clip.mp4").parse()

    assert d
    assert len(d["inputs"]["streams"]) == 2
    assert d["inputs"]["streams"][0]["language"] is None
    assert d["inputs"]["streams"][1]["language"] is None


def test_stream_square_brackets_and_language():
    infos = """
Input #0, mpeg, from 'clip.mp4':
  Duration: 00:02:15.00, start: 52874.498178, bitrate: 266 kb/s
    Stream #0:0[0x1e0](eng): Video: ..., 25 tbr, 90k tbn, 50 tbc
    Stream #0:1[0x1c0](und): Audio: mp2, 0 channels, s16p
At least one output file must be specified"""

    d = FFmpegInfosParser(infos, "clip.mp4").parse()

    assert d
    assert len(d["inputs"]["streams"]) == 2
    assert d["inputs"]["streams"][0]["language"] == "eng"
    assert d["inputs"]["streams"][1]["language"] is None


def test_stream_missing_audio_bitrate():
    infos = """
Input #0, mpeg, from 'clip.mp4':
  Duration: 00:02:15.00, start: 52874.498178, bitrate: 266 kb/s
    Stream #0:0[0x1e0]: Video: ..., 25 tbr, 90k tbn, 50 tbc
    Stream #0:1[0x1c0]: Audio: mp2, 0 channels, s16p
At least one output file must be specified"""

    d = FFmpegInfosParser(infos, "clip.mp4").parse()

    assert d
    assert len(d["inputs"]["streams"]) == 2
    assert d["audio_found"]
    assert d["audio_bitrate"] is None


def test_sequential_frame_pos():
    """test_video.mp4 contains 5 frames at 1 fps.
    Each frame is 1x1 pixels and the sequence is Red, Green, Blue, Black, White.
    The rgb values are not pure due to compression.
    """
    reader = FFMPEG_VideoReader("media/test_video.mp4")
    assert reader.pos == 1

    # Get first frame
    frame_1 = reader.get_frame(0)
    assert reader.pos == 1
    assert np.array_equal(frame_1, [[[254, 0, 0]]])

    # Get a specific sequential frame
    frame_2 = reader.get_frame(1)
    assert reader.pos == 2
    assert np.array_equal(frame_2, [[[0, 255, 1]]])

    # Get next frame. Note `.read_frame()` instead of `.get_frame()`
    frame_3 = reader.read_frame()
    assert reader.pos == 3
    assert np.array_equal(frame_3, [[[0, 0, 255]]])

    # Skip a frame
    skip_frame = reader.get_frame(4)
    assert reader.pos == 5
    assert np.array_equal(skip_frame, [[[255, 255, 255]]])


def test_unusual_order_frame_pos():
    reader = FFMPEG_VideoReader("media/test_video.mp4")
    assert reader.pos == 1

    # Go straight to end
    end_frame = reader.get_frame(4)
    assert reader.pos == 5
    assert np.array_equal(end_frame, [[[255, 255, 255]]])

    # Repeat the previous frame
    second_end_frame = reader.get_frame(4)
    assert reader.pos == 5
    assert np.array_equal(second_end_frame, [[[255, 255, 255]]])

    # Go backwards
    previous_frame = reader.get_frame(3)
    assert reader.pos == 4
    assert np.array_equal(previous_frame, [[[0, 0, 0]]])

    # Go back to start
    start_frame = reader.get_frame(0)
    assert reader.pos == 1
    assert np.array_equal(start_frame, [[[254, 0, 0]]])


def test_large_skip_frame_pos():
    reader = FFMPEG_VideoReader("media/big_buck_bunny_0_30.webm")
    assert reader.fps == 24

    # 10 sec * 24 fps = 240 frames
    reader.get_frame(240 // 24)
    assert reader.pos == 241

    reader.get_frame(719 / 24)
    assert reader.pos == 720

    # Go backwards
    reader.get_frame(120 // 24)
    assert reader.pos == 121


def test_large_small_skip_equal():
    sequential_reader = FFMPEG_VideoReader("media/big_buck_bunny_0_30.webm")
    small_skip_reader = FFMPEG_VideoReader("media/big_buck_bunny_0_30.webm")
    large_skip_reader = FFMPEG_VideoReader("media/big_buck_bunny_0_30.webm")
    assert small_skip_reader.fps == large_skip_reader.fps == sequential_reader.fps == 24

    # Read every frame sequentially
    for t in np.arange(0, 10, 1 / 24):
        sequential_reader.get_frame(t)
    sequential_final_frame = sequential_reader.get_frame(10)

    # Read in increments of 24 frames
    for t in range(10):
        small_skip_reader.get_frame(t)
    small_skip_final_frame = small_skip_reader.get_frame(10)

    # Jumps straight forward 240 frames. This is greater than 100 so it uses
    # FFmpeg to reseek at the right position.
    large_skip_final_frame = large_skip_reader.get_frame(10)

    assert (
        sequential_reader.pos == small_skip_reader.pos == large_skip_reader.pos == 241
    )

    # All frames have gone forward an equal amount, so should be equal
    assert np.array_equal(sequential_final_frame, small_skip_final_frame)
    assert np.array_equal(small_skip_final_frame, large_skip_final_frame)


def test_seeking_beyond_file_end():
    reader = FFMPEG_VideoReader("media/test_video.mp4")
    frame_1 = reader.get_frame(0)

    with pytest.warns(UserWarning, match="Using the last valid frame instead"):
        end_of_file_frame = reader.get_frame(5)
    assert np.array_equal(frame_1, end_of_file_frame)
    assert reader.pos == 6

    # Try again with a jump larger than 100 frames
    # (which triggers different behaviour in `.get_frame()`
    reader = FFMPEG_VideoReader("media/big_buck_bunny_0_30.webm")
    frame_1 = reader.get_frame(0)

    with pytest.warns(UserWarning, match="Using the last valid frame instead"):
        end_of_file_frame = reader.get_frame(30)
    assert np.array_equal(frame_1, end_of_file_frame)
    assert reader.pos == 30 * 24 + 1


def test_release_of_file_via_close(util):
    # Create a random video file.
    red = ColorClip((256, 200), color=(255, 0, 0))
    green = ColorClip((256, 200), color=(0, 255, 0))
    blue = ColorClip((256, 200), color=(0, 0, 255))

    red.fps = green.fps = blue.fps = 10

    # Repeat this so we can see no conflicts.
    for i in range(3):
        # Get the name of a temporary file we can use.
        local_video_filename = os.path.join(
            util.TMP_DIR,
            "test_release_of_file_via_close_%s.mp4" % int(time.time()),
        )

        clip = clips_array([[red, green, blue]]).with_duration(0.5)
        clip.write_videofile(local_video_filename)

        # Open it up with VideoFileClip.
        video = VideoFileClip(local_video_filename)
        video.close()
        clip.close()

        # Now remove the temporary file.
        # This would fail on Windows if the file is still locked.

        # This should succeed without exceptions.
        os.remove(local_video_filename)

    red.close()
    green.close()
    blue.close()


def test_failure_to_release_file(util):
    """Expected to fail. It demonstrates that there *is* a problem with not
    releasing resources when running on Windows.

    The real issue was that, as of movepy 0.2.3.2, there was no way around it.

    See test_resourcerelease.py to see how the close() methods provide a solution.
    """
    # Get the name of a temporary file we can use.
    local_video_filename = os.path.join(
        util.TMP_DIR, "test_release_of_file_%s.mp4" % int(time.time())
    )

    # Repeat this so we can see that the problems escalate:
    for i in range(5):
        # Create a random video file.
        red = ColorClip((256, 200), color=(255, 0, 0))
        green = ColorClip((256, 200), color=(0, 255, 0))
        blue = ColorClip((256, 200), color=(0, 0, 255))

        red.fps = green.fps = blue.fps = 30
        video = clips_array([[red, green, blue]]).with_duration(1)

        try:
            video.write_videofile(local_video_filename)

            # Open it up with VideoFileClip.
            clip = VideoFileClip(local_video_filename)

            # Normally a client would do processing here.

            # All finished, so delete the clipS.
            clip.close()
            video.close()
            del clip
            del video

        except IOError:
            print(
                "On Windows, this succeeds the first few times around the loop"
                " but eventually fails."
            )
            print("Need to shut down the process now. No more tests in this file.")
            return

        try:
            # Now remove the temporary file.
            # This will fail on Windows if the file is still locked.

            # In particular, this raises an exception with PermissionError.
            # In  there was no way to avoid it.

            os.remove(local_video_filename)
            print("You are not running Windows, because that worked.")
        except OSError:  # More specifically, PermissionError in Python 3.
            print("Yes, on Windows this fails.")


def test_read_transparent_video():
    reader = FFMPEG_VideoReader("media/transparent.webm", pixel_format="rgba")

    # Get first frame
    frame = reader.get_frame(0)
    mask = frame[:, :, 3]

    # Check transparency on fully transparent part is 0
    assert mask[10, 10] == 0

    # Check transparency on fully opaque part is 255
    assert mask[100, 100] == 255


def test_frame_seek():
    reader = FFMPEG_VideoReader("media/smpte-2997.mp4", pixel_format="rgba")

    # Get first frame and second frame
    frame = reader.get_frame(0)
    frame2 = reader.get_frame(0.34)

    assert not np.array_equal(frame, frame2)


def test_side_data():
    infos = """Input #0, mov,mp4,m4a,3gp,3g2,mj2, from '/home/ajani/Téléchargements/10CAE6A8-1A7A-488F-8DDD-691F0242A5BD_L0_001_1748075354.671342_o_IMG_1977.MOV':
  Metadata:
    major_brand     : qt
    minor_version   : 0
    compatible_brands: qt
    creation_time   : 2025-05-24T08:27:14.000000Z
    com.apple.quicktime.location.accuracy.horizontal: 15.257182
    com.apple.quicktime.full-frame-rate-playback-intent: 0
    com.apple.quicktime.location.ISO6709: +37.8187+127.0583+097.529/
    com.apple.quicktime.make: Apple
    com.apple.quicktime.model: iPhone 14
    com.apple.quicktime.software: 18.3.2
    com.apple.quicktime.creationdate: 2025-05-24T17:27:14+0900
  Duration: 00:00:16.10, start: 0.000000, bitrate: 8764 kb/s
  Stream #0:0(und): Video: hevc (Main 10) (hvc1 / 0x31637668), yuv420p10le(tv, bt2020nc/bt2020/arib-std-b67), 1920x1080, 8540 kb/s, 30 fps, 30 tbr, 600 tbn, 600 tbc (default)
    Metadata:
      rotate          : 90
      creation_time   : 2025-05-24T08:27:14.000000Z
      handler_name    : Core Media Video
      vendor_id       : [0][0][0][0]
      encoder         : HEVC
    Side data:
      DOVI configuration record: version: 1.0, profile: 8, level: 4, rpu flag: 1, el flag: 0, bl flag: 1, compatibility id: 4
      displaymatrix: rotation of -90.00 degrees
  Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 157 kb/s (default)
    Metadata:
      creation_time   : 2025-05-24T08:27:14.000000Z
      handler_name    : Core Media Audio
      vendor_id       : [0][0][0][0]
  Stream #0:2(und): Data: none (mebx / 0x7862656D), 0 kb/s (default)
    Metadata:
      creation_time   : 2025-05-24T08:27:14.000000Z
      handler_name    : Core Media Metadata
  Stream #0:3(und): Data: none (mebx / 0x7862656D), 0 kb/s (default)
    Metadata:
      creation_time   : 2025-05-24T08:27:14.000000Z
      handler_name    : Core Media Metadata
  Stream #0:4(und): Data: none (mebx / 0x7862656D), 42 kb/s (default)
    Metadata:
      creation_time   : 2025-05-24T08:27:14.000000Z
      handler_name    : Core Media Metadata
  Stream #0:5(und): Data: none (mebx / 0x7862656D), 2 kb/s (default)
    Metadata:
      creation_time   : 2025-05-24T08:27:14.000000Z
      handler_name    : Core Media Metadata
  Stream #0:6(und): Data: none (mebx / 0x7862656D), 0 kb/s (default)
    Metadata:
      creation_time   : 2025-05-24T08:27:14.000000Z
      handler_name    : Core Media Metadata"""

    d = FFmpegInfosParser(infos, "foo.mov").parse()
    assert d["blocks"].childs[1].childs[1].type == "side_data"
    assert (
        d["blocks"].childs[1].childs[1].data["DOVI configuration record"]
        == "version: 1.0, profile: 8, level: 4, rpu flag: 1, el flag: 0, bl flag: 1, compatibility id: 4"
    )


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_ffmpeg_tools.py
````python
"""FFmpeg tools tests for moviepy."""

import os
import shutil

import pytest

from moviepy.video.io.ffmpeg_tools import (
    ffmpeg_extract_subclip,
    ffmpeg_resize,
    ffmpeg_stabilize_video,
    ffmpeg_version,
)
from moviepy.video.io.VideoFileClip import VideoFileClip


def test_ffmpeg_extract_subclip(util):
    extract_subclip_tempdir = os.path.join(
        util.TMP_DIR, "moviepy_ffmpeg_extract_subclip"
    )
    if os.path.isdir(extract_subclip_tempdir):
        shutil.rmtree(extract_subclip_tempdir)
    os.mkdir(extract_subclip_tempdir)

    inputfile = os.path.join(extract_subclip_tempdir, "fire2.mp4")
    shutil.copyfile("media/fire2.mp4", inputfile)

    # default name
    expected_outputfile = os.path.join(extract_subclip_tempdir, "fire2SUB300_500.mp4")
    ffmpeg_extract_subclip(inputfile, 0.3, "00:00:00,5", logger=None)
    assert os.path.isfile(expected_outputfile)

    # custom name
    expected_outputfile = os.path.join(extract_subclip_tempdir, "foo.mp4")
    ffmpeg_extract_subclip(
        inputfile, 0.3, "00:00:00,5", outputfile=expected_outputfile, logger=None
    )
    assert os.path.isfile(expected_outputfile)

    # assert subclip duration
    clip = VideoFileClip(expected_outputfile)
    assert 0.18 <= clip.duration <= 0.22  # not accurate

    if os.path.isdir(extract_subclip_tempdir):
        try:
            shutil.rmtree(extract_subclip_tempdir)
        except PermissionError:
            pass


def test_ffmpeg_resize(util):
    outputfile = os.path.join(util.TMP_DIR, "moviepy_ffmpeg_resize.mp4")
    if os.path.isfile(outputfile):
        os.remove(outputfile)

    expected_size = (30, 30)

    ffmpeg_resize("media/bitmap.mp4", outputfile, expected_size, logger=None)
    assert os.path.isfile(outputfile)

    # overwrite file on old version of ffmpeg
    if int(ffmpeg_version()[1].split(".")[0]) < 7:
        with pytest.raises(OSError):
            ffmpeg_resize("media/bitmap.mp4", outputfile, expected_size, logger=None)

    clip = VideoFileClip(outputfile)
    assert clip.size[0] == expected_size[0]
    assert clip.size[1] == expected_size[1]

    if os.path.isfile(outputfile):
        try:
            os.remove(outputfile)
        except PermissionError:
            pass


def test_ffmpeg_stabilize_video(util):
    stabilize_video_tempdir = os.path.join(util.TMP_DIR, "moviepy_ffmpeg_stabilize")
    if os.path.isdir(stabilize_video_tempdir):
        shutil.rmtree(stabilize_video_tempdir)
    os.mkdir(stabilize_video_tempdir)

    # no output file
    ffmpeg_stabilize_video(
        "media/bitmap.mp4",
        output_dir=stabilize_video_tempdir,
        logger=None,
    )

    expected_filepath = os.path.join(stabilize_video_tempdir, "bitmap_stabilized.mp4")
    assert os.path.isfile(expected_filepath)

    # with output file
    ffmpeg_stabilize_video(
        "media/bitmap.mp4",
        output_dir=stabilize_video_tempdir,
        outputfile="foo.mp4",
        logger=None,
    )
    expected_filepath = os.path.join(stabilize_video_tempdir, "foo.mp4")
    assert os.path.isfile(expected_filepath)

    # don't overwrite file on old version of ffmpeg
    if int(ffmpeg_version()[1].split(".")[0]) < 7:
        with pytest.raises(OSError):
            ffmpeg_stabilize_video(
                "media/bitmap.mp4",
                output_dir=stabilize_video_tempdir,
                outputfile="foo.mp4",
                overwrite_file=False,
                logger=None,
            )

    if os.path.isdir(stabilize_video_tempdir):
        try:
            shutil.rmtree(stabilize_video_tempdir)
        except PermissionError:
            pass


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_ffmpeg_writer.py
````python
"""FFmpeg writer tests of moviepy."""

import multiprocessing
import os

from PIL import Image

import pytest

from moviepy import *
from moviepy.video.compositing.CompositeVideoClip import concatenate_videoclips
from moviepy.video.io.ffmpeg_writer import ffmpeg_write_image, ffmpeg_write_video
from moviepy.video.io.gif_writers import write_gif_with_imageio
from moviepy.video.tools.drawing import color_gradient


@pytest.mark.parametrize(
    "with_mask",
    (False, True),
    ids=("with_mask=False", "with_mask=True"),
)
@pytest.mark.parametrize(
    "write_logfile",
    (False, True),
    ids=("write_logfile=False", "write_logfile=True"),
)
@pytest.mark.parametrize(
    ("codec", "is_valid_codec", "ext"),
    (
        pytest.param(
            "libcrazyfoobar", False, ".mp4", id="codec=libcrazyfoobar-ext=.mp4"
        ),
        pytest.param(None, True, ".mp4", id="codec=default-ext=.mp4"),
        pytest.param("libtheora", False, ".avi", id="codec=libtheora-ext=.mp4"),
    ),
)
@pytest.mark.parametrize(
    "bitrate",
    (None, "5000k"),
    ids=("bitrate=None", "bitrate=5000k"),
)
@pytest.mark.parametrize(
    "threads",
    (None, multiprocessing.cpu_count()),
    ids=("threads=None", "threads=multiprocessing.cpu_count()"),
)
def test_ffmpeg_write_video(
    util,
    codec,
    is_valid_codec,
    ext,
    write_logfile,
    with_mask,
    bitrate,
    threads,
):
    filename = os.path.join(util.TMP_DIR, f"moviepy_ffmpeg_write_video{ext}")
    if os.path.isfile(filename):
        try:
            os.remove(filename)
        except PermissionError:
            pass

    logfile_name = filename + ".log"
    if os.path.isfile(logfile_name):
        os.remove(logfile_name)

    clip = BitmapClip([["R"], ["G"], ["B"]], fps=10).with_duration(0.3)
    if with_mask:
        clip = clip.with_mask(
            BitmapClip([["W"], ["O"], ["O"]], fps=10, is_mask=True).with_duration(0.3)
        )

    kwargs = dict(
        logger=None,
        write_logfile=write_logfile,
    )
    if codec is not None:
        kwargs["codec"] = codec
    if bitrate is not None:
        kwargs["bitrate"] = bitrate
    if threads is not None:
        kwargs["threads"] = threads

    ffmpeg_write_video(clip, filename, 10, **kwargs)

    if is_valid_codec:
        assert os.path.isfile(filename)

        final_clip = VideoFileClip(filename)

        r, g, b = final_clip.get_frame(0)[0][0]
        assert r == 254
        assert g == 0
        assert b == 0

        r, g, b = final_clip.get_frame(0.1)[0][0]
        assert r == (0 if not with_mask else 1)
        assert g == (255 if not with_mask else 1)
        assert b == 1

        r, g, b = final_clip.get_frame(0.2)[0][0]
        assert r == 0
        assert g == 0
        assert b == (255 if not with_mask else 0)

    if write_logfile:
        assert os.path.isfile(logfile_name)


@pytest.mark.parametrize(
    ("size", "logfile", "pixel_format", "expected_result"),
    (
        pytest.param(
            (5, 1),
            False,
            None,
            [[(0, 255, 0), (51, 204, 0), (102, 153, 0), (153, 101, 0), (204, 50, 0)]],
            id="size=(5, 1)",
        ),
        pytest.param(
            (2, 1), False, None, [[(0, 255, 0), (51, 204, 0)]], id="size=(2, 1)"
        ),
        pytest.param(
            (2, 1), True, None, [[(0, 255, 0), (51, 204, 0)]], id="logfile=True"
        ),
        pytest.param(
            (2, 1),
            False,
            "invalid",
            (OSError, "MoviePy error: FFMPEG encountered the following error"),
            id="pixel_format=invalid-OSError",
        ),
    ),
)
def test_ffmpeg_write_image(util, size, logfile, pixel_format, expected_result):
    filename = os.path.join(util.TMP_DIR, "moviepy_ffmpeg_write_image.png")
    if os.path.isfile(filename):
        try:
            os.remove(filename)
        except PermissionError:
            pass

    image_array = color_gradient(
        size,
        (0, 0),
        p2=(5, 0),
        color_1=(255, 0, 0),
        color_2=(0, 255, 0),
    )

    if hasattr(expected_result[0], "__traceback__"):
        with pytest.raises(expected_result[0]) as exc:
            ffmpeg_write_image(
                filename,
                image_array,
                logfile=logfile,
                pixel_format=pixel_format,
            )
        assert expected_result[1] in str(exc.value)
        return
    else:
        ffmpeg_write_image(
            filename,
            image_array,
            logfile=logfile,
            pixel_format=pixel_format,
        )

    assert os.path.isfile(filename)

    if logfile:
        assert os.path.isfile(filename + ".log")
        os.remove(filename + ".log")

    im = Image.open(filename, mode="r")
    for i in range(im.width):
        for j in range(im.height):
            assert im.getpixel((i, j)) == expected_result[j][i]


@pytest.mark.parametrize("loop", (0, 2), ids=("loop=0", "loop=2"))
@pytest.mark.parametrize("clip_class", ("BitmapClip", "ColorClip"))
@pytest.mark.parametrize(
    "with_mask", (False, True), ids=("with_mask=False", "with_mask=True")
)
def test_write_gif(util, clip_class, loop, with_mask):
    filename = os.path.join(util.TMP_DIR, "moviepy_write_gif.gif")
    if os.path.isfile(filename):
        try:
            os.remove(filename)
        except PermissionError:
            pass

    fps = 10

    if clip_class == "BitmapClip":
        original_clip = BitmapClip([["R"], ["G"], ["B"]], fps=fps).with_duration(0.3)
    else:
        original_clip = concatenate_videoclips(
            [
                ColorClip(
                    (1, 1),
                    color=color,
                )
                .with_duration(0.1)
                .with_fps(fps)
                for color in [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
            ]
        )
    if with_mask:
        original_clip = original_clip.with_mask(
            ColorClip((1, 1), color=1, is_mask=True).with_fps(fps).with_duration(0.3)
        )

    write_gif_with_imageio(original_clip, filename, fps=fps, logger=None, loop=loop)

    final_clip = VideoFileClip(filename)

    r, g, b = final_clip.get_frame(0)[0][0]
    assert r == 255
    assert g == 0
    assert b == 0

    r, g, b = final_clip.get_frame(0.1)[0][0]
    assert r == 0
    assert g == 255
    assert b == 0

    r, g, b = final_clip.get_frame(0.2)[0][0]
    assert r == 0
    assert g == 0
    assert b == 255


def test_transparent_video(util):
    # Has one R 30%
    clip = ColorClip((100, 100), (255, 0, 0, 76.5)).with_duration(2)
    filename = os.path.join(util.TMP_DIR, "opacity.webm")

    ffmpeg_write_video(clip, filename, codec="libvpx", fps=5)

    # Load output file and check transparency
    result = VideoFileClip(filename, has_mask=True)

    # Check for mask
    assert result.mask is not None

    # Check correct opacity, allow for some tolerance (about 1%)
    # to consider rounding and compressing error
    frame = result.mask.get_frame(1)
    opacity = frame[50, 50]
    assert abs(opacity - 0.3) < 0.01

    result.close()


def test_write_file_with_spaces(util):
    filename = os.path.join(util.TMP_DIR, "name with spaces.mp4")
    clip = ColorClip((1, 1), color=1, is_mask=True).with_fps(1).with_duration(0.3)
    ffmpeg_write_video(clip, filename, fps=1)
````

## File: tests/test_fx.py
````python
"""MoviePy video and audio effects tests."""

import decimal
import math
import numbers
import os
import random

import numpy as np

import pytest

from moviepy import *
from moviepy.tools import convert_to_seconds


def test_accel_decel():
    pass


def test_blackwhite():
    # Create black/white spectrum ``bw_color_dict`` to compare against it.
    # Colors after ``blackwhite`` FX must be inside this dictionary
    # Note: black/white spectrum is made of colors with same numbers
    # [(0, 0, 0), (1, 1, 1), (2, 2, 2)...]
    bw_color_dict = {}
    for num in range(0, 256):
        bw_color_dict[chr(num + 255)] = (num, num, num)
    color_dict = bw_color_dict.copy()
    # update dictionary with default BitmapClip color_dict values
    color_dict.update(BitmapClip.DEFAULT_COLOR_DICT)

    # add row with random colors in b/w spectrum
    random_row = ""
    for num in range(512, 515):
        # use unique unicode representation for each color
        char = chr(num)
        random_row += char

        # random colors in the b/w spectrum
        color_dict[char] = tuple(random.randint(0, 255) for i in range(3))

    # clip converted below to black/white
    clip = BitmapClip([["RGB", random_row]], color_dict=color_dict, fps=1)

    # for each possible ``preserve_luminosity`` boolean argument value
    for preserve_luminosity in [True, False]:
        # default argument (``RGB=None``)
        clip_bw = clip.with_effects(
            [vfx.BlackAndWhite(preserve_luminosity=preserve_luminosity)]
        )

        bitmap = clip_bw.to_bitmap()
        assert bitmap

        for i, row in enumerate(bitmap[0]):
            for char in row:
                # all characters returned by ``to_bitmap`` are in the b/w spectrum
                assert char in bw_color_dict

                if i == 0:  # pure "RGB" colors are converted to [85, 85, 85]
                    assert char == row[0]  # so are equal

        # custom random ``RGB`` argument
        clip_bw_custom_rgb = clip.with_effects(
            [
                vfx.BlackAndWhite(
                    RGB=(random.randint(0, 255), 0, 0),
                    preserve_luminosity=preserve_luminosity,
                )
            ]
        )
        bitmap = clip_bw_custom_rgb.to_bitmap()
        for i, row in enumerate(bitmap[0]):
            for i2, char in enumerate(row):
                # all characters returned by ``to_bitmap`` are in the b/w spectrum
                assert char in bw_color_dict

                # for clip "RGB" row, two latest converted colors are equal
                if i == 0 and i2 > 0:
                    assert char == row[1] and char == row[2]

        # ``RGB="CRT_phosphor"`` argument
        clip_bw_crt_phosphor = clip.with_effects(
            [
                vfx.BlackAndWhite(
                    RGB="CRT_phosphor", preserve_luminosity=preserve_luminosity
                )
            ]
        )
        bitmap = clip_bw_crt_phosphor.to_bitmap()
        assert bitmap
        for row in bitmap[0]:
            for char in row:
                # all characters returned by ``to_bitmap`` are in the b/w spectrum
                assert char in bw_color_dict


# This currently fails with a with_mask error!
# def test_blink(util):
#     with VideoFileClip("media/big_buck_bunny_0_30.webm").subclip(0,10) as clip:
#       clip1 = blink(clip, 1, 1)
#       clip1.write_videofile(os.path.join(util.TMP_DIR,"blink1.webm"))


def test_multiply_color():
    color_dict = {"H": (0, 0, 200), "L": (0, 0, 50), "B": (0, 0, 255), "O": (0, 0, 0)}
    clip = BitmapClip([["LLO", "BLO"]], color_dict=color_dict, fps=1)

    clipfx = clip.with_effects([vfx.MultiplyColor(4)])
    target = BitmapClip([["HHO", "BHO"]], color_dict=color_dict, fps=1)
    assert target == clipfx


def test_crop():
    # x: 0 -> 4, y: 0 -> 3 inclusive
    clip = BitmapClip([["ABCDE", "EDCBA", "CDEAB", "BAEDC"]], fps=1)

    clip1 = clip.with_effects([vfx.Crop()])
    target1 = BitmapClip([["ABCDE", "EDCBA", "CDEAB", "BAEDC"]], fps=1)
    assert clip1 == target1

    clip2 = clip.with_effects([vfx.Crop(x1=1, y1=1, x2=3, y2=3)])
    target2 = BitmapClip([["DC", "DE"]], fps=1)
    assert clip2 == target2

    clip3 = clip.with_effects([vfx.Crop(y1=2)])
    target3 = BitmapClip([["CDEAB", "BAEDC"]], fps=1)
    assert clip3 == target3

    clip4 = clip.with_effects([vfx.Crop(x1=2, width=2)])
    target4 = BitmapClip([["CD", "CB", "EA", "ED"]], fps=1)
    assert clip4 == target4

    # TODO x_center=1 does not perform correctly
    clip5 = clip.with_effects([vfx.Crop(x_center=2, y_center=2, width=3, height=3)])
    target5 = BitmapClip([["ABC", "EDC", "CDE"]], fps=1)
    assert clip5 == target5

    clip6 = clip.with_effects([vfx.Crop(x_center=2, width=2, y1=1, y2=2)])
    target6 = BitmapClip([["DC"]], fps=1)
    assert clip6 == target6


def test_even_size():
    clip1 = BitmapClip([["ABC", "BCD"]], fps=1)  # Width odd
    clip1even = clip1.with_effects([vfx.EvenSize()])
    target1 = BitmapClip([["AB", "BC"]], fps=1)
    assert clip1even == target1

    clip2 = BitmapClip([["AB", "BC", "CD"]], fps=1)  # Height odd
    clip2even = clip2.with_effects([vfx.EvenSize()])
    target2 = BitmapClip([["AB", "BC"]], fps=1)
    assert clip2even == target2

    clip3 = BitmapClip([["ABC", "BCD", "CDE"]], fps=1)  # Width and height odd
    clip3even = clip3.with_effects([vfx.EvenSize()])
    target3 = BitmapClip([["AB", "BC"]], fps=1)
    assert clip3even == target3


def test_fadein():
    color_dict = {
        "I": (0, 0, 0),
        "R": (255, 0, 0),
        "G": (0, 255, 0),
        "B": (0, 0, 255),
        "W": (255, 255, 255),
    }
    clip = BitmapClip([["R"], ["G"], ["B"]], color_dict=color_dict, fps=1)

    clip1 = clip.with_effects([vfx.FadeIn(1)])  # default initial color
    target1 = BitmapClip([["I"], ["G"], ["B"]], color_dict=color_dict, fps=1)
    assert clip1 == target1

    clip2 = clip.with_effects(
        [vfx.FadeIn(1, initial_color=(255, 255, 255))]
    )  # different initial color
    target2 = BitmapClip([["W"], ["G"], ["B"]], color_dict=color_dict, fps=1)
    assert clip2 == target2


def test_fadeout(util, video):
    clip = video(end_time=0.5)
    clip1 = clip.with_effects([vfx.FadeOut(0.5)])
    clip1.write_videofile(os.path.join(util.TMP_DIR, "fadeout1.webm"))


@pytest.mark.parametrize(
    (
        "t",
        "freeze_duration",
        "total_duration",
        "padding_end",
        "output_frames",
    ),
    (
        # at start, 1 second (default t == 0)
        (
            None,
            1,
            None,
            None,
            ["R", "R", "G", "B"],
        ),
        # at start, 1 second (explicit t)
        (
            0,
            1,
            None,
            None,
            ["R", "R", "G", "B"],
        ),
        # at end, 1 second
        (
            "end",
            1,
            None,
            None,
            ["R", "G", "B", "B"],
        ),
        # at end 1 second, padding end 1 second
        (
            "end",
            1,
            None,
            1,
            ["R", "G", "G", "B"],
        ),
        # at 2nd frame, 1 second
        (
            1,  # second 0 is frame 1, second 1 is frame 2...
            1,
            None,
            None,
            ["R", "G", "G", "B"],
        ),
        # at 2nd frame, 2 seconds
        (
            1,
            2,
            None,
            None,
            ["R", "G", "G", "G", "B"],
        ),
        # `freeze_duration`, `total_duration` are None
        (1, None, None, None, ValueError),
        # `total_duration` 5 at start (2 seconds)
        (None, None, 5, None, ["R", "R", "R", "G", "B"]),
        # total duration 5 at end
        ("end", None, 5, None, ["R", "G", "B", "B", "B"]),
        # total duration 5 padding end
        ("end", None, 5, 1, ["R", "G", "G", "G", "B"]),
    ),
    ids=[
        "at start, 1 second (default t == 0)",
        "at start, 1 second (explicit t)",
        "at end, 1 second",
        "at end 1 second, padding end 1 second",
        "at 2nd frame, 1 second",
        "at 2nd frame, 2 seconds",
        "`freeze_duration`, `total_duration` are None",
        "`total_duration` 5 at start (2 seconds)",
        "`total_duration` 5 at end",
        "`total_duration` 5 padding end",
    ],
)
def test_freeze(t, freeze_duration, total_duration, padding_end, output_frames):
    input_frames = ["R", "G", "B"]
    clip_duration = len(input_frames)

    # create BitmapClip with predefined set of colors, during 1 second each one
    clip = BitmapClip([list(color) for color in input_frames], fps=1).with_duration(
        clip_duration
    )

    # build kwargs passed to `freeze`
    possible_kwargs = {
        "t": t,
        "freeze_duration": freeze_duration,
        "total_duration": total_duration,
        "padding_end": padding_end,
    }
    kwargs = {
        kw_name: kw_value
        for kw_name, kw_value in possible_kwargs.items()
        if kw_value is not None
    }

    # freeze clip
    if hasattr(output_frames, "__traceback__"):
        with pytest.raises(output_frames):
            clip.with_effects([vfx.Freeze(**kwargs)])
        return
    else:
        freezed_clip = clip.with_effects([vfx.Freeze(**kwargs)])

    # assert new duration
    expected_freeze_duration = (
        freeze_duration
        if freeze_duration is not None
        else total_duration - clip_duration
    )
    assert freezed_clip.duration == clip_duration + expected_freeze_duration

    # assert colors are the expected
    for i, color in enumerate(freezed_clip.iter_frames()):
        expected_color = list(BitmapClip.DEFAULT_COLOR_DICT[output_frames[i]])
        assert list(color[0][0]) == expected_color


def test_freeze_region():
    clip = BitmapClip([["AAB", "CCC"], ["BBR", "DDD"], ["CCC", "ABC"]], fps=1)

    # Test region
    clip1 = clip.with_effects([vfx.FreezeRegion(t=1, region=(2, 0, 3, 1))])
    target1 = BitmapClip([["AAR", "CCC"], ["BBR", "DDD"], ["CCR", "ABC"]], fps=1)
    assert clip1 == target1

    # Test outside_region
    clip2 = clip.with_effects([vfx.FreezeRegion(t=1, outside_region=(2, 0, 3, 1))])
    target2 = BitmapClip([["BBB", "DDD"], ["BBR", "DDD"], ["BBC", "DDD"]], fps=1)
    assert clip2 == target2


def test_gamma_corr():
    pass


def test_headblur():
    pass


def test_invert_colors():
    clip = BitmapClip(
        [["AB", "BC"]],
        color_dict={"A": (0, 0, 0), "B": (50, 100, 150), "C": (255, 255, 255)},
        fps=1,
    )

    clip1 = clip.with_effects([vfx.InvertColors()])
    target1 = BitmapClip(
        [["CD", "DA"]],
        color_dict={"A": (0, 0, 0), "D": (205, 155, 105), "C": (255, 255, 255)},
        fps=1,
    )
    assert clip1 == target1


def test_loop(util, video):
    clip = BitmapClip([["R"], ["G"], ["B"]], fps=1)

    clip1 = clip.with_effects([vfx.Loop(n=2)])  # loop 2 times
    target1 = BitmapClip([["R"], ["G"], ["B"], ["R"], ["G"], ["B"]], fps=1)
    assert clip1 == target1

    clip2 = clip.with_effects([vfx.Loop(duration=8)])  # loop 8 seconds
    target2 = BitmapClip(
        [["R"], ["G"], ["B"], ["R"], ["G"], ["B"], ["R"], ["G"]], fps=1
    )
    assert clip2 == target2

    clip3 = clip.with_effects([vfx.Loop()]).with_duration(5)  # infinite loop
    target3 = BitmapClip([["R"], ["G"], ["B"], ["R"], ["G"]], fps=1)
    assert clip3 == target3

    clip = video(start_time=0.2, end_time=0.3)  # 0.1 seconds long
    clip1 = clip.with_effects([vfx.Loop()]).with_duration(0.5)  # infinite looping
    clip1.write_videofile(os.path.join(util.TMP_DIR, "loop1.webm"))

    clip2 = clip.with_effects([vfx.Loop(duration=0.5)])  # loop for 1 second
    clip2.write_videofile(os.path.join(util.TMP_DIR, "loop2.webm"))

    clip3 = clip.with_effects([vfx.Loop(n=3)])  # loop 3 times
    clip3.write_videofile(os.path.join(util.TMP_DIR, "loop3.webm"))

    # Test audio looping
    clip = AudioClip(
        lambda t: np.sin(440 * 2 * np.pi * t) * (t % 1) + 0.5, duration=2.5, fps=44100
    )
    clip1 = clip.with_effects([vfx.Loop(2)])
    # TODO fix AudioClip.__eq__()
    # assert concatenate_audioclips([clip, clip]) == clip1


def test_lum_contrast(util, video):
    clip = video()
    clip1 = clip.with_effects([vfx.LumContrast()])
    clip1.write_videofile(os.path.join(util.TMP_DIR, "lum_contrast1.webm"))

    # what are the correct value ranges for function arguments lum,
    # contrast and contrast_thr?  Maybe we should check for these in
    # lum_contrast.


def test_make_loopable(util, video):
    clip = video()
    clip1 = clip.with_effects([vfx.MakeLoopable(0.4)])

    # We need to set libvpx-vp9 because our test will produce transparency
    clip1.write_videofile(
        os.path.join(util.TMP_DIR, "make_loopable1.webm"), codec="libvpx-vp9"
    )


@pytest.mark.parametrize(
    ("ClipClass"),
    (ColorClip, BitmapClip),
    ids=("ColorClip", "BitmapClip"),
)
@pytest.mark.parametrize(
    (
        "margin_size",
        "margins",  # [left, right, top, bottom]
        "color",
        "expected_result",
    ),
    (
        pytest.param(
            None,
            None,
            None,
            [["RRR", "RRR"], ["RRR", "RRR"]],
            id="default arguments",
        ),
        pytest.param(
            1,
            None,
            None,
            [
                ["OOOOO", "ORRRO", "ORRRO", "OOOOO"],
                ["OOOOO", "ORRRO", "ORRRO", "OOOOO"],
            ],
            id="margin_size=1,color=(0, 0, 0)",
        ),
        pytest.param(
            1,
            None,
            (0, 255, 0),
            [
                ["GGGGG", "GRRRG", "GRRRG", "GGGGG"],
                ["GGGGG", "GRRRG", "GRRRG", "GGGGG"],
            ],
            id="margin_size=1,color=(0, 255, 0)",
        ),
        pytest.param(
            None,
            [1, 0, 0, 0],
            (0, 255, 0),
            [["GRRR", "GRRR"], ["GRRR", "GRRR"]],
            id="left=1,color=(0, 255, 0)",
        ),
        pytest.param(
            None,
            [0, 1, 0, 0],
            (0, 255, 0),
            [["RRRG", "RRRG"], ["RRRG", "RRRG"]],
            id="right=1,color=(0, 255, 0)",
        ),
        pytest.param(
            None,
            [1, 0, 1, 0],
            (0, 255, 0),
            [["GGGG", "GRRR", "GRRR"], ["GGGG", "GRRR", "GRRR"]],
            id="left=1,top=1,color=(0, 255, 0)",
        ),
        pytest.param(
            None,
            [0, 1, 1, 1],
            (0, 255, 0),
            [["GGGG", "RRRG", "RRRG", "GGGG"], ["GGGG", "RRRG", "RRRG", "GGGG"]],
            id="right=1,top=1,bottom=1,color=(0, 255, 0)",
        ),
        pytest.param(
            None,
            [3, 0, 0, 0],
            (255, 255, 255),
            [["WWWRRR", "WWWRRR"], ["WWWRRR", "WWWRRR"]],
            id="left=3,color=(255, 255, 255)",
        ),
        pytest.param(
            None,
            [0, 0, 0, 4],
            (255, 255, 255),
            [
                ["RRR", "RRR", "WWW", "WWW", "WWW", "WWW"],
                ["RRR", "RRR", "WWW", "WWW", "WWW", "WWW"],
            ],
            id="bottom=4,color=(255, 255, 255)",
        ),
    ),
)
def test_margin(ClipClass, margin_size, margins, color, expected_result):
    if ClipClass is BitmapClip:
        clip = BitmapClip([["RRR", "RRR"], ["RRR", "RRR"]], fps=1)
    else:
        clip = ColorClip(color=(255, 0, 0), size=(3, 2), duration=2).with_fps(1)

    # if None, set default argument values
    if color is None:
        color = (0, 0, 0)

    if margins is None:
        margins = [0, 0, 0, 0]
    left, right, top, bottom = margins

    new_clip = clip.with_effects(
        [
            vfx.Margin(
                margin_size=margin_size,
                left=left,
                right=right,
                top=top,
                bottom=bottom,
                color=color,
            )
        ]
    )

    assert new_clip == BitmapClip(expected_result, fps=1)


@pytest.mark.parametrize("image_from", ("np.ndarray", "ImageClip"))
@pytest.mark.parametrize("duration", (None, "random"))
@pytest.mark.parametrize(
    ("color", "mask_color", "expected_color"),
    (
        (
            (0, 0, 0),
            (255, 255, 255),
            (0, 0, 0),
        ),
        (
            (255, 0, 0),
            (0, 0, 255),
            (0, 0, 0),
        ),
        (
            (255, 255, 255),
            (0, 10, 20),
            (0, 10, 20),
        ),
        (
            (10, 10, 10),
            (20, 0, 20),
            (10, 0, 10),
        ),
    ),
)
def test_mask_and(image_from, duration, color, mask_color, expected_color):
    """Checks ``mask_and`` FX behaviour."""
    clip_size = tuple(random.randint(3, 10) for i in range(2))

    if duration == "random":
        duration = round(random.uniform(0, 0.5), 2)

    # test ImageClip and np.ndarray types as mask argument
    clip = ColorClip(color=color, size=clip_size).with_duration(duration)
    mask_clip = ColorClip(color=mask_color, size=clip.size)
    masked_clip = clip.with_effects(
        [
            vfx.MasksAnd(
                mask_clip if image_from == "ImageClip" else mask_clip.get_frame(0)
            )
        ]
    )

    assert masked_clip.duration == clip.duration
    assert np.array_equal(masked_clip.get_frame(0)[0][0], np.array(expected_color))

    # test VideoClip as mask argument
    color_frame, mask_color_frame = (np.array([[color]]), np.array([[mask_color]]))
    clip = VideoClip(lambda t: color_frame).with_duration(duration)
    mask_clip = VideoClip(lambda t: mask_color_frame).with_duration(duration)
    masked_clip = clip.with_effects([vfx.MasksAnd(mask_clip)])

    assert np.array_equal(masked_clip.get_frame(0)[0][0], np.array(expected_color))


def test_mask_color():
    pass


@pytest.mark.parametrize("image_from", ("np.ndarray", "ImageClip"))
@pytest.mark.parametrize("duration", (None, "random"))
@pytest.mark.parametrize(
    ("color", "mask_color", "expected_color"),
    (
        (
            (0, 0, 0),
            (255, 255, 255),
            (255, 255, 255),
        ),
        (
            (255, 0, 0),
            (0, 0, 255),
            (255, 0, 255),
        ),
        (
            (255, 255, 255),
            (0, 10, 20),
            (255, 255, 255),
        ),
        (
            (10, 10, 10),
            (20, 0, 20),
            (20, 10, 20),
        ),
    ),
)
def test_mask_or(image_from, duration, color, mask_color, expected_color):
    """Checks ``mask_or`` FX behaviour."""
    clip_size = tuple(random.randint(3, 10) for i in range(2))

    if duration == "random":
        duration = round(random.uniform(0, 0.5), 2)

    # test ImageClip and np.ndarray types as mask argument
    clip = ColorClip(color=color, size=clip_size).with_duration(duration)
    mask_clip = ColorClip(color=mask_color, size=clip.size)
    masked_clip = clip.with_effects(
        [
            vfx.MasksOr(
                mask_clip if image_from == "ImageClip" else mask_clip.get_frame(0)
            )
        ]
    )

    assert masked_clip.duration == clip.duration
    assert np.array_equal(masked_clip.get_frame(0)[0][0], np.array(expected_color))

    # test VideoClip as mask argument
    color_frame, mask_color_frame = (np.array([[color]]), np.array([[mask_color]]))
    clip = VideoClip(lambda t: color_frame).with_duration(duration)
    mask_clip = VideoClip(lambda t: mask_color_frame).with_duration(duration)
    masked_clip = clip.with_effects([vfx.MasksOr(mask_clip)])

    assert np.array_equal(masked_clip.get_frame(0)[0][0], np.array(expected_color))


def test_mirror_x():
    clip = BitmapClip([["AB", "CD"]], fps=1)
    clip1 = clip.with_effects([vfx.MirrorX()])
    target = BitmapClip([["BA", "DC"]], fps=1)
    assert clip1 == target


def test_mirror_y():
    clip = BitmapClip([["AB", "CD"]], fps=1)
    clip1 = clip.with_effects([vfx.MirrorY()])
    target = BitmapClip([["CD", "AB"]], fps=1)
    assert clip1 == target


def test_painting():
    pass


@pytest.mark.parametrize("apply_to_mask", (True, False))
@pytest.mark.parametrize(
    (
        "size",
        "duration",
        "new_size",
        "width",
        "height",
    ),
    (
        (
            [8, 2],
            1,
            [4, 1],
            None,
            None,
        ),
        (
            [8, 2],
            1,
            None,
            4,
            None,
        ),
        (
            [2, 8],
            1,
            None,
            None,
            4,
        ),
        # neither 'new_size', 'height' or 'width'
        (
            [2, 2],
            1,
            None,
            None,
            None,
        ),
        # `new_size` as scaling factor
        (
            [5, 5],
            1,
            2,
            None,
            None,
        ),
        (
            [5, 5],
            1,
            decimal.Decimal(2.5),
            None,
            None,
        ),
        # arguments as functions
        (
            [2, 2],
            4,
            lambda t: {0: [4, 4], 1: [8, 8], 2: [11, 11], 3: [5, 8]}[t],
            None,
            None,
        ),
        (
            [2, 4],
            2,
            None,
            None,
            lambda t: {0: 3, 1: 4}[t],
        ),
        (
            [5, 2],
            2,
            None,
            lambda t: {0: 3, 1: 4}[t],
            None,
        ),
    ),
)
def test_resize(apply_to_mask, size, duration, new_size, height, width):
    """Checks ``resize`` FX behaviours using all argument"""
    # build expected sizes (using `width` or `height` arguments will be proportional
    # to original size)
    if new_size:
        if hasattr(new_size, "__call__"):
            # function
            expected_new_sizes = [new_size(t) for t in range(duration)]
        elif isinstance(new_size, numbers.Number):
            # scaling factor
            expected_new_sizes = [[int(size[0] * new_size), int(size[1] * new_size)]]
        else:
            # tuple or list
            expected_new_sizes = [new_size]
    elif height:
        if hasattr(height, "__call__"):
            expected_new_sizes = []
            for t in range(duration):
                new_height = height(t)
                expected_new_sizes.append(
                    [int(size[0] * new_height / size[1]), new_height]
                )
        else:
            expected_new_sizes = [[size[0] * height / size[1], height]]
    elif width:
        if hasattr(width, "__call__"):
            expected_new_sizes = []
            for t in range(duration):
                new_width = width(t)
                expected_new_sizes.append(
                    [new_width, int(size[1] * new_width / size[0])]
                )
        else:
            expected_new_sizes = [[width, size[1] * width / size[0]]]
    else:
        expected_new_sizes = None

    clip = ColorClip(size=size, color=(0, 0, 0), duration=duration)
    clip.fps = 1
    mask = ColorClip(size=size, color=0, is_mask=True)
    clip = clip.with_mask(mask)

    # any resizing argument passed, raises `ValueError`
    if expected_new_sizes is None:
        with pytest.raises(ValueError):
            resized_clip = clip.resized(
                new_size=new_size,
                height=height,
                width=width,
                apply_to_mask=apply_to_mask,
            )
        resized_clip = clip
        expected_new_sizes = [size]
    else:
        resized_clip = clip.resized(
            new_size=new_size, height=height, width=width, apply_to_mask=apply_to_mask
        )

    # assert new size for each frame
    for t in range(duration):
        expected_width = expected_new_sizes[t][0]
        expected_height = expected_new_sizes[t][1]

        clip_frame = resized_clip.get_frame(t)

        assert len(clip_frame[0]) == expected_width
        assert len(clip_frame) == expected_height

        mask_frame = resized_clip.mask.get_frame(t)
        if apply_to_mask:
            assert len(mask_frame[0]) == expected_width
            assert len(mask_frame) == expected_height


@pytest.mark.parametrize("unit", ["deg", "rad"])
@pytest.mark.parametrize("resample", ["bilinear", "nearest", "bicubic", "unknown"])
@pytest.mark.parametrize(
    (
        "angle",
        "translate",
        "center",
        "bg_color",
        "expected_frames",
    ),
    (
        (
            0,
            None,
            None,
            None,
            [["AAAA", "BBBB", "CCCC"], ["ABCD", "BCDE", "CDEA"]],
        ),
        (
            90,
            None,
            None,
            None,
            [["ABC", "ABC", "ABC", "ABC"], ["DEA", "CDE", "BCD", "ABC"]],
        ),
        (
            lambda t: 90,
            None,
            None,
            None,
            [["ABC", "ABC", "ABC", "ABC"], ["DEA", "CDE", "BCD", "ABC"]],
        ),
        (
            180,
            None,
            None,
            None,
            [["CCCC", "BBBB", "AAAA"], ["AEDC", "EDCB", "DCBA"]],
        ),
        (
            270,
            None,
            None,
            None,
            [["CBA", "CBA", "CBA", "CBA"], ["CBA", "DCB", "EDC", "AED"]],
        ),
        (
            45,
            (50, 50),
            None,
            (0, 255, 0),
            [
                ["GGGGGG", "GGGGGG", "GGGGGG", "GGGGGG", "GGGGGG", "GGGGGG"],
                ["GGGGGG", "GGGGGG", "GGGGGG", "GGGGGG", "GGGGGG", "GGGGGG"],
            ],
        ),
        (
            45,
            (50, 50),
            (20, 20),
            (255, 0, 0),
            [
                ["RRRRRR", "RRRRRR", "RRRRRR", "RRRRRR", "RRRRRR"],
                ["RRRRRR", "RRRRRR", "RRRRRR", "RRRRRR", "RRRRRR"],
            ],
        ),
        (
            135,
            (-100, -100),
            None,
            (0, 0, 255),
            [
                ["BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB"],
                ["BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB"],
            ],
        ),
    ),
)
def test_rotate(
    angle,
    unit,
    resample,
    translate,
    center,
    bg_color,
    expected_frames,
):
    """Check ``rotate`` FX behaviour against possible combinations of arguments."""
    original_frames = [["AAAA", "BBBB", "CCCC"], ["ABCD", "BCDE", "CDEA"]]

    # angles are defined in degrees, so convert to radians testing ``unit="rad"``
    if unit == "rad":
        if hasattr(angle, "__call__"):
            _angle = lambda t: math.radians(angle(0))
        else:
            _angle = math.radians(angle)
    else:
        _angle = angle
    clip = BitmapClip(original_frames, fps=1)

    kwargs = {
        "unit": unit,
        "resample": resample,
        "translate": translate,
        "center": center,
        "bg_color": bg_color,
    }
    if resample not in ["bilinear", "nearest", "bicubic"]:
        with pytest.raises(ValueError) as exc:
            clip.rotated(_angle, **kwargs)
        assert (
            "'resample' argument must be either 'bilinear', 'nearest' or 'bicubic'"
        ) == str(exc.value)
        return

    # resolve the angle, because if it is a multiple of 90, the rotation
    # can be computed event without an available PIL installation
    if hasattr(_angle, "__call__"):
        _resolved_angle = _angle(0)
    else:
        _resolved_angle = _angle
    if unit == "rad":
        _resolved_angle = math.degrees(_resolved_angle)

    rotated_clip = clip.with_effects([vfx.Rotate(_angle, **kwargs)])
    expected_clip = BitmapClip(expected_frames, fps=1)

    assert rotated_clip.to_bitmap() == expected_clip.to_bitmap()


def test_rotate_nonstandard_angles(util):
    # Test rotate with color clip
    clip = ColorClip([600, 400], [150, 250, 100]).with_duration(1).with_fps(5)
    clip = clip.with_effects([vfx.Rotate(20)])
    clip.write_videofile(os.path.join(util.TMP_DIR, "color_rotate.webm"))


def test_rotate_mask():
    # Prior to https://github.com/Zulko/moviepy/pull/1399
    # all the pixels of the resulting video were 0
    clip = (
        ColorClip(color=0.5, size=(1, 1), is_mask=True)
        .with_fps(1)
        .with_duration(1)
        .with_effects([vfx.Rotate(45)])
    )
    assert clip.get_frame(0)[1][1] != 0


@pytest.mark.parametrize(
    ("unsupported_kwargs",),
    (
        (["bg_color"],),
        (["center"],),
        (["translate"],),
        (["translate", "center"],),
        (["center", "bg_color", "translate"],),
    ),
    ids=(
        "bg_color",
        "center",
        "translate",
        "translate,center",
        "center,bg_color,translate",
    ),
)
def test_rotate_supported_PIL_kwargs(
    unsupported_kwargs,
    monkeypatch,
):
    """Test supported 'rotate' FX arguments by PIL version."""
    pass


def test_scroll():
    pass


def test_multiply_speed():
    clip = BitmapClip([["A"], ["B"], ["C"], ["D"]], fps=1)

    clip1 = clip.with_effects([vfx.MultiplySpeed(0.5)])  # 1/2x speed
    target1 = BitmapClip(
        [["A"], ["A"], ["B"], ["B"], ["C"], ["C"], ["D"], ["D"]], fps=1
    )
    assert clip1 == target1

    clip2 = clip.with_effects([vfx.MultiplySpeed(final_duration=8)])  # 1/2x speed
    target2 = BitmapClip(
        [["A"], ["A"], ["B"], ["B"], ["C"], ["C"], ["D"], ["D"]], fps=1
    )
    assert clip2 == target2

    clip3 = clip.with_effects([vfx.MultiplySpeed(final_duration=12)])  # 1/2x speed
    target3 = BitmapClip(
        [
            ["A"],
            ["A"],
            ["A"],
            ["B"],
            ["B"],
            ["B"],
            ["C"],
            ["C"],
            ["C"],
            ["D"],
            ["D"],
            ["D"],
        ],
        fps=1,
    )
    assert clip3 == target3

    clip4 = clip.with_effects([vfx.MultiplySpeed(2)])  # 2x speed
    target4 = BitmapClip([["A"], ["C"]], fps=1)
    assert clip4 == target4

    clip5 = clip.with_effects([vfx.MultiplySpeed(final_duration=2)])  # 2x speed
    target5 = BitmapClip([["A"], ["C"]], fps=1)
    assert clip5 == target5

    clip6 = clip.with_effects([vfx.MultiplySpeed(4)])  # 4x speed
    target6 = BitmapClip([["A"]], fps=1)
    assert (
        clip6 == target6
    ), f"{clip6.duration} {target6.duration} {clip6.fps} {target6.fps}"


def test_supersample():
    pass


def test_time_mirror():
    clip = BitmapClip([["AA", "AA"], ["BB", "BB"], ["CC", "CC"]], fps=1)

    clip1 = clip.with_effects([vfx.TimeMirror()])
    target1 = BitmapClip([["CC", "CC"], ["BB", "BB"], ["AA", "AA"]], fps=1)
    assert clip1 == target1

    clip2 = BitmapClip([["AA", "AA"], ["BB", "BB"], ["CC", "CC"], ["DD", "DD"]], fps=1)

    clip3 = clip2.with_effects([vfx.TimeMirror()])
    target3 = BitmapClip(
        [["DD", "DD"], ["CC", "CC"], ["BB", "BB"], ["AA", "AA"]], fps=1
    )
    assert clip3 == target3


def test_time_symmetrize():
    clip = BitmapClip(
        [
            ["AA", "AA"],
            ["BB", "BB"],
            ["CC", "CC"],
            ["DD", "DD"],
            ["EE", "EE"],
            ["FF", "FF"],
        ],
        fps=2,
    )

    clip1 = clip.with_effects([vfx.TimeSymmetrize()])
    target1 = BitmapClip(
        [
            ["AA", "AA"],
            ["BB", "BB"],
            ["CC", "CC"],
            ["DD", "DD"],
            ["EE", "EE"],
            ["FF", "FF"],
            ["FF", "FF"],
            ["EE", "EE"],
            ["DD", "DD"],
            ["CC", "CC"],
            ["BB", "BB"],
            ["AA", "AA"],
        ],
        fps=1,
    )
    assert clip1 == target1


def test_audio_normalize():
    clip = AudioFileClip("media/crunching.mp3")
    clip = clip.with_effects([afx.AudioNormalize()])
    assert clip.max_volume() == 1


def test_audio_normalize_muted():
    z_array = np.array([0.0])
    frame_function = lambda t: z_array
    clip = AudioClip(frame_function, duration=1, fps=44100)
    clip = clip.with_effects([afx.AudioNormalize()])
    assert np.array_equal(clip.to_soundarray(), z_array)


@pytest.mark.parametrize(
    ("sound_type", "factor", "duration", "start_time", "end_time"),
    (
        pytest.param(
            "stereo",
            0,
            None,
            None,
            None,
            id="stereo-0",
        ),
        pytest.param(
            "stereo",
            2,
            None,
            None,
            None,
            id="stereo-2",
        ),
        pytest.param(
            "mono",
            3,
            None,
            None,
            None,
            id="mono-3",
        ),
        pytest.param(
            "stereo",
            0,
            0.2,
            "00:00:00,1",
            None,
            id="stereo-0-start=.1",
        ),
        pytest.param(
            "stereo",
            0,
            0.3,
            None,
            (0, 0, 0.2),
            id="stereo-0-end=.2",
        ),
        pytest.param(
            "stereo",
            0,
            0.3,
            0.1,
            0.2,
            id="stereo-0-start=.1-end=.2",
        ),
        pytest.param(
            "mono",
            0,
            0.3,
            0.2,
            None,
            id="mono-0-start=.2",
        ),
        pytest.param(
            "mono",
            0,
            0.2,
            None,
            "00:00:00.1",
            id="mono-0-end=.1",
        ),
        pytest.param(
            "mono",
            2,
            0.3,
            0.1,
            0.2,
            id="mono-0-start=.1-end=.2",
        ),
    ),
)
def test_multiply_volume_audioclip(
    sound_type,
    factor,
    duration,
    start_time,
    end_time,
):
    if sound_type == "stereo":
        frame_function = lambda t: np.array(
            [
                np.sin(440 * 2 * np.pi * t),
                np.sin(160 * 2 * np.pi * t),
            ]
        ).T.copy(order="C")
    else:
        frame_function = lambda t: [np.sin(440 * 2 * np.pi * t)]

    clip = AudioClip(
        frame_function,
        duration=duration if duration else 0.1,
        fps=22050,
    )
    clip_array = clip.to_soundarray()

    clip_transformed = clip.with_effects(
        [
            afx.MultiplyVolume(
                factor,
                start_time=start_time,
                end_time=end_time,
            )
        ]
    )
    clip_transformed_array = clip_transformed.to_soundarray()

    assert len(clip_transformed_array)

    if hasattr(clip_array, "shape") and len(clip_array.shape) > 1:
        # stereo clip
        left_channel_transformed = clip_transformed_array[:, 0]
        right_channel_transformed = clip_transformed_array[:, 1]

        if start_time is None and end_time is None:
            expected_left_channel_transformed = clip_array[:, 0] * factor
            expected_right_channel_transformed = clip_array[:, 1] * factor
        else:
            start_time = convert_to_seconds(start_time) if start_time else clip.start
            end_time = convert_to_seconds(end_time) if end_time else clip.end

            expected_left_channel_transformed = np.array([])
            expected_right_channel_transformed = np.array([])
            for i, frame in enumerate(clip_array):
                t = i / clip.fps
                transformed_frame = frame * (
                    factor if start_time <= t <= end_time else 1
                )
                expected_left_channel_transformed = np.append(
                    expected_left_channel_transformed,
                    transformed_frame[0],
                )
                expected_right_channel_transformed = np.append(
                    expected_right_channel_transformed,
                    transformed_frame[1],
                )

        assert len(left_channel_transformed)
        assert len(expected_left_channel_transformed)
        assert np.array_equal(
            left_channel_transformed,
            expected_left_channel_transformed,
        )

        assert len(right_channel_transformed)
        assert len(expected_right_channel_transformed)
        assert np.array_equal(
            right_channel_transformed,
            expected_right_channel_transformed,
        )

    else:
        # mono clip

        if start_time is None and end_time is None:
            expected_clip_transformed_array = clip_array * factor
        else:
            start_time = convert_to_seconds(start_time) if start_time else clip.start
            end_time = convert_to_seconds(end_time) if end_time else clip.end

            expected_clip_transformed_array = np.array([])
            for i, frame in enumerate(clip_array[0]):
                t = i / clip.fps
                transformed_frame = frame * (
                    factor if start_time <= t <= end_time else 1
                )
                expected_clip_transformed_array = np.append(
                    expected_clip_transformed_array,
                    transformed_frame,
                )
            expected_clip_transformed_array = np.array(
                [
                    expected_clip_transformed_array,
                ]
            )

        assert len(expected_clip_transformed_array)

        assert np.array_equal(
            expected_clip_transformed_array,
            clip_transformed_array,
        )


def test_multiply_volume_videoclip():
    start_time, end_time = (0.1, 0.2)

    clip = (
        VideoFileClip("media/chaplin.mp4")
        .subclipped(0, 0.3)
        .with_effects(
            [
                afx.MultiplyVolume(
                    0,
                    start_time=start_time,
                    end_time=end_time,
                )
            ]
        )
    )
    clip_soundarray = clip.audio.to_soundarray()

    assert len(clip_soundarray)

    expected_silence = np.zeros(clip_soundarray.shape[1])

    for i, frame in enumerate(clip_soundarray):
        t = i / clip.audio.fps
        if start_time <= t <= end_time:
            assert np.array_equal(frame, expected_silence)
        else:
            assert not np.array_equal(frame, expected_silence)


def test_multiply_stereo_volume():
    clip = AudioFileClip("media/crunching.mp3")

    # stereo mute
    clip_left_channel_muted = clip.with_effects([afx.MultiplyStereoVolume(left=0)])
    clip_right_channel_muted = clip.with_effects(
        [afx.MultiplyStereoVolume(right=0, left=2)]
    )

    left_channel_muted = clip_left_channel_muted.to_soundarray()[:, 0]
    right_channel_muted = clip_right_channel_muted.to_soundarray()[:, 1]

    z_channel = np.zeros(len(left_channel_muted))

    assert np.array_equal(left_channel_muted, z_channel)
    assert np.array_equal(right_channel_muted, z_channel)

    # stereo level doubled
    left_channel_doubled = clip_right_channel_muted.to_soundarray()[:, 0]
    expected_left_channel_doubled = clip.to_soundarray()[:, 0] * 2
    assert np.array_equal(left_channel_doubled, expected_left_channel_doubled)

    # mono muted
    sinus_wave = lambda t: [np.sin(440 * 2 * np.pi * t)]
    mono_clip = AudioClip(sinus_wave, duration=1, fps=22050)
    muted_mono_clip = mono_clip.with_effects([afx.MultiplyStereoVolume(left=0)])
    mono_channel_muted = muted_mono_clip.to_soundarray()

    z_channel = np.zeros(len(mono_channel_muted))
    assert np.array_equal(mono_channel_muted, z_channel)

    # mono doubled
    mono_clip = AudioClip(sinus_wave, duration=1, fps=22050)
    doubled_mono_clip = mono_clip.with_effects(
        [afx.MultiplyStereoVolume(left=None, right=2)]
    )  # using right
    mono_channel_doubled = doubled_mono_clip.to_soundarray()
    d_channel = mono_clip.to_soundarray() * 2
    assert np.array_equal(mono_channel_doubled, d_channel)


@pytest.mark.parametrize(
    ("duration", "offset", "n_repeats", "decay"),
    (
        (0.1, 0.2, 11, 0),
        (0.4, 2, 5, 2),
        (0.5, 0.6, 3, -1),
        (0.3, 1, 7, 4),
    ),
)
def test_audio_delay(stereo_wave, duration, offset, n_repeats, decay):
    """Check that creating a short pulse of audio, the delay converts to a sound
    with the volume level in the form `-_-_-_-_-`, being `-` pulses expressed by
    `duration` argument and `_` being chunks of muted audio. Keep in mind that this
    way of test the FX only works if `duration <= offset`, but as does not make sense
    create a delay with `duration > offset`, this is enough for our purposes.

    Note that decayment values are not tested here, but are created using
    `multiply_volume`, should be OK.
    """
    # limits of this test
    assert n_repeats > 0  # some repetition, if not does not make sense
    assert duration <= offset  # avoid wave distortion
    assert not offset * 1000000 % 2  # odd offset -> no accurate muted chunk size

    # stereo audio clip
    clip = AudioClip(
        frame_function=stereo_wave(left_freq=440, right_freq=880),
        duration=duration,
        fps=44100,
    )
    clip_array = clip.to_soundarray()

    # stereo delayed clip
    delayed_clip = clip.with_effects(
        [afx.AudioDelay(offset=offset, n_repeats=n_repeats, decay=decay)]
    )
    delayed_clip_array = delayed_clip.to_soundarray()

    # size of chunks with audios
    sound_chunk_size = clip_array.shape[0]
    # muted chunks size
    muted_chunk_size = int(sound_chunk_size * offset / duration) - sound_chunk_size

    zeros_expected_chunk_as_muted = np.zeros((muted_chunk_size, 2))

    decayments = np.linspace(1, max(0, decay), n_repeats)

    for i in range(n_repeats + 1):  # first clip, is not part of the repeated ones
        if i == n_repeats:
            # the delay ends in sound, so last muted chunk does not exists
            break

        # sound chunk
        sound_start_at = i * sound_chunk_size + i * muted_chunk_size
        sound_ends_at = sound_start_at + sound_chunk_size

        # first sound chunk
        if i == 0:
            assert np.array_equal(
                delayed_clip_array[:, :][sound_start_at:sound_ends_at],
                clip.with_effects([afx.MultiplyVolume(decayments[i])]).to_soundarray(),
            )

        # muted chunk
        mute_starts_at = sound_ends_at + 1
        mute_ends_at = mute_starts_at + muted_chunk_size

        assert np.array_equal(
            delayed_clip_array[:, :][mute_starts_at:mute_ends_at],
            zeros_expected_chunk_as_muted,
        )

        # check muted bounds
        assert not np.array_equal(
            delayed_clip_array[:, :][mute_starts_at - 1 : mute_ends_at],
            zeros_expected_chunk_as_muted,
        )

        assert not np.array_equal(
            delayed_clip_array[:, :][mute_starts_at : mute_ends_at + 1],
            zeros_expected_chunk_as_muted,
        )


@pytest.mark.parametrize("sound_type", ("stereo", "mono"))
@pytest.mark.parametrize("fps", (44100, 22050))
@pytest.mark.parametrize(
    ("clip_duration", "fadein_duration"),
    (
        (
            (0.2, 0.1),
            (1, "00:00:00,4"),
            (0.3, 0.13),
        )
    ),
)
def test_audio_fadein(
    mono_wave, stereo_wave, sound_type, fps, clip_duration, fadein_duration
):
    if sound_type == "stereo":
        frame_function = stereo_wave(left_freq=440, right_freq=160)
    else:
        frame_function = mono_wave(440)

    clip = AudioClip(frame_function, duration=clip_duration, fps=fps)
    new_clip = clip.with_effects([afx.AudioFadeIn(fadein_duration)])

    # first frame is muted
    first_frame = new_clip.get_frame(0)
    if sound_type == "stereo":
        assert len(first_frame) > 1
        for value in first_frame:
            assert value == 0.0
    else:
        assert first_frame == 0.0

    fadein_duration = convert_to_seconds(fadein_duration)

    n_parts = 10

    # cut transformed part into subclips and check the expected max_volume for
    # each one
    time_foreach_part = fadein_duration / n_parts
    start_times = np.arange(0, fadein_duration, time_foreach_part)
    for i, start_time in enumerate(start_times):
        end_time = start_time + time_foreach_part
        subclip_max_volume = new_clip.subclipped(start_time, end_time).max_volume()

        possible_value = (i + 1) / n_parts
        assert round(subclip_max_volume, 2) in [
            possible_value,
            round(possible_value - 0.01, 5),
        ]

    # cut non transformed part into subclips and check the expected max_volume
    # for each one (almost 1)
    time_foreach_part = (clip_duration - fadein_duration) / n_parts
    start_times = np.arange(fadein_duration, clip_duration, time_foreach_part)
    for i, start_time in enumerate(start_times):
        end_time = start_time + time_foreach_part
        subclip_max_volume = new_clip.subclipped(start_time, end_time).max_volume()

        assert round(subclip_max_volume, 4) == 1


@pytest.mark.parametrize("sound_type", ("stereo", "mono"))
@pytest.mark.parametrize("fps", (44100, 22050))
@pytest.mark.parametrize(
    ("clip_duration", "fadeout_duration"),
    (
        (
            (0.2, 0.1),
            (0.7, "00:00:00,4"),
            (0.3, 0.13),
        )
    ),
)
def test_audio_fadeout(
    mono_wave, stereo_wave, sound_type, fps, clip_duration, fadeout_duration
):
    if sound_type == "stereo":
        frame_function = stereo_wave(left_freq=440, right_freq=160)
    else:
        frame_function = mono_wave(440)

    clip = AudioClip(frame_function, duration=clip_duration, fps=fps)
    new_clip = clip.with_effects([afx.AudioFadeOut(fadeout_duration)])

    fadeout_duration = convert_to_seconds(fadeout_duration)

    n_parts = 10

    # cut transformed part into subclips and check the expected max_volume for
    # each one
    time_foreach_part = fadeout_duration / n_parts
    start_times = np.arange(
        clip_duration - fadeout_duration,
        clip_duration,
        time_foreach_part,
    )
    for i, start_time in enumerate(start_times):
        end_time = start_time + time_foreach_part
        subclip_max_volume = new_clip.subclipped(start_time, end_time).max_volume()

        possible_value = 1 - i * 0.1
        assert round(subclip_max_volume, 2) in [
            round(possible_value, 2),
            round(possible_value - 0.01, 5),
        ]

    # cut non transformed part into subclips and check the expected max_volume
    # for each one (almost 1)
    time_foreach_part = (clip_duration - fadeout_duration) / n_parts
    start_times = np.arange(0, clip_duration - fadeout_duration, time_foreach_part)
    for i, start_time in enumerate(start_times):
        end_time = start_time + time_foreach_part
        subclip_max_volume = new_clip.subclipped(start_time, end_time).max_volume()

        assert round(subclip_max_volume, 4) == 1


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_ImageSequenceClip.py
````python
"""Image sequencing clip tests meant to be run with pytest."""

import os

import pytest

from moviepy.video.io.ImageSequenceClip import ImageSequenceClip


def test_1(util):
    images = []
    durations = []

    for i in range(5):
        durations.append(i)
        images.append("media/python_logo.png")
        durations.append(i)
        images.append("media/python_logo_upside_down.png")

    with ImageSequenceClip(images, durations=durations) as clip:
        assert clip.duration == sum(durations)
        clip.write_videofile(
            os.path.join(util.TMP_DIR, "ImageSequenceClip1.mp4"), fps=30, logger=None
        )


def test_2():
    images = []
    durations = []

    durations.append(1)
    images.append("media/python_logo.png")
    durations.append(2)
    images.append("media/matplotlib_demo1.png")

    # images are not the same size..
    with pytest.raises(Exception):
        ImageSequenceClip(images, durations=durations).close()


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_issues.py
````python
"""Issue tests meant to be run with pytest."""

import os

import numpy as np

import pytest

from moviepy import *


try:
    import matplotlib.pyplot
except ImportError:
    matplotlib = None
else:
    matplotlib = True


def test_issue_145():
    video = ColorClip((800, 600), color=(255, 0, 0)).with_duration(5)
    with pytest.raises(Exception):
        concatenate_videoclips([video], method="composite")


def test_issue_190():
    # from PIL import Image
    #
    # filename = os.path.join(util.TMP_DIR, "issue_190.png")
    # Image.new('L', (800,600), 'white').save(filename)
    #
    # from imageio import imread
    # image = imread(filename)
    #
    # clip = ImageSequenceClip([image, image], fps=1)
    # clip.write_videofile(os.path.splitext(filename)[0] + ".mp4"))
    pass


def test_issue_285():
    clip_1, clip_2, clip_3 = (
        ImageClip("media/python_logo.png", duration=10),
        ImageClip("media/python_logo.png", duration=10),
        ImageClip("media/python_logo.png", duration=10),
    )
    merged_clip = concatenate_videoclips([clip_1, clip_2, clip_3])
    assert merged_clip.duration == 30


def test_issue_334(util):
    # NOTE: this is horrible. Any simpler version ?
    last_move = None
    last_move1 = None

    lis = [
        (0.0, 113, 167, 47),
        (0.32, 138, 159, 47),
        (0.44, 152, 144, 47),
        (0.48, 193, 148, 47),
        (0.6, 193, 148, 47),
        (0.76, 205, 138, 55),
        (0.88, 204, 121, 63),
        (0.92, 190, 31, 127),
        (1.2, 183, 59, 127),
        (1.4, 137, 22, 127),
        (1.52, 137, 22, 127),
        (1.72, 129, 67, 127),
        (1.88, 123, 69, 127),
        (2.04, 131, 123, 63),
        (2.24, 130, 148, 63),
        (2.48, 130, 148, 63),
        (2.8, 138, 180, 63),
        (3.0, 138, 180, 63),
        (3.2, 146, 192, 63),
        (3.28, 105, 91, 151),
        (3.44, 105, 91, 151),
        (3.72, 11, 48, 151),
        (3.96, 5, 78, 151),
        (4.32, 4, 134, 1),
        (4.6, 149, 184, 48),
        (4.8, 145, 188, 48),
        (5.0, 154, 217, 48),
        (5.08, 163, 199, 48),
        (5.2, 163, 199, 48),
        (5.32, 164, 187, 48),
        (5.48, 163, 200, 48),
        (5.76, 163, 200, 48),
        (5.96, 173, 199, 48),
        (6.0, 133, 172, 48),
        (6.04, 128, 165, 48),
        (6.28, 128, 165, 48),
        (6.4, 129, 180, 48),
        (6.52, 133, 166, 48),
        (6.64, 133, 166, 48),
        (6.88, 144, 183, 48),
        (7.0, 153, 174, 48),
        (7.16, 153, 174, 48),
        (7.24, 153, 174, 48),
        (7.28, 253, 65, 104),
        (7.64, 253, 65, 104),
        (7.8, 279, 116, 80),
        (8.0, 290, 105, 80),
        (8.24, 288, 124, 80),
        (8.44, 243, 102, 80),
        (8.56, 243, 102, 80),
        (8.8, 202, 107, 80),
        (8.84, 164, 27, 104),
        (9.0, 164, 27, 104),
        (9.12, 121, 9, 104),
        (9.28, 77, 33, 104),
        (9.32, 52, 23, 104),
        (9.48, 52, 23, 104),
        (9.64, 33, 46, 104),
        (9.8, 93, 49, 104),
        (9.92, 93, 49, 104),
        (10.16, 173, 19, 104),
        (10.2, 226, 173, 48),
        (10.36, 226, 173, 48),
        (10.48, 211, 172, 48),
        (10.64, 208, 162, 48),
        (10.92, 220, 171, 48),
    ]

    lis1 = [
        (0.0, 113, 167, 47),
        (0.32, 138, 159, 47),
        (0.44, 152, 144, 47),
        (0.48, 193, 148, 47),
        (0.6, 193, 148, 47),
        (0.76, 205, 138, 55),
        (0.88, 204, 121, 63),
        (0.92, 190, 31, 127),
        (1.2, 183, 59, 127),
        (1.4, 137, 22, 127),
        (1.52, 137, 22, 127),
        (1.72, 129, 67, 127),
        (1.88, 123, 69, 127),
        (2.04, 131, 123, 63),
        (2.24, 130, 148, 63),
        (2.48, 130, 148, 63),
        (2.8, 138, 180, 63),
        (3.0, 138, 180, 63),
        (3.2, 146, 192, 63),
        (3.28, 105, 91, 151),
        (3.44, 105, 91, 151),
        (3.72, 11, 48, 151),
        (3.96, 5, 78, 151),
        (4.32, 4, 134, 1),
        (4.6, 149, 184, 48),
        (4.8, 145, 188, 48),
        (5.0, 154, 217, 48),
        (5.08, 163, 199, 48),
        (5.2, 163, 199, 48),
        (5.32, 164, 187, 48),
        (5.48, 163, 200, 48),
        (5.76, 163, 200, 48),
        (5.96, 173, 199, 48),
        (6.0, 133, 172, 48),
        (6.04, 128, 165, 48),
        (6.28, 128, 165, 48),
        (6.4, 129, 180, 48),
        (6.52, 133, 166, 48),
        (6.64, 133, 166, 48),
        (6.88, 144, 183, 48),
        (7.0, 153, 174, 48),
        (7.16, 153, 174, 48),
        (7.24, 153, 174, 48),
        (7.28, 253, 65, 104),
        (7.64, 253, 65, 104),
        (7.8, 279, 116, 80),
        (8.0, 290, 105, 80),
        (8.24, 288, 124, 80),
        (8.44, 243, 102, 80),
        (8.56, 243, 102, 80),
        (8.8, 202, 107, 80),
        (8.84, 164, 27, 104),
        (9.0, 164, 27, 104),
        (9.12, 121, 9, 104),
        (9.28, 77, 33, 104),
        (9.32, 52, 23, 104),
        (9.48, 52, 23, 104),
        (9.64, 33, 46, 104),
        (9.8, 93, 49, 104),
        (9.92, 93, 49, 104),
        (10.16, 173, 19, 104),
        (10.2, 226, 173, 48),
        (10.36, 226, 173, 48),
        (10.48, 211, 172, 48),
        (10.64, 208, 162, 48),
        (10.92, 220, 171, 48),
    ]

    def posi(t):
        global last_move
        if len(lis) == 0:
            return (last_move[1], last_move[2])
        if t >= lis[0][0]:
            last_move = item = lis.pop(0)
            return (item[1], item[2])
        else:
            if len(lis) > 0:
                dura = lis[0][0] - last_move[0]
                now = t - last_move[0]
                w = (lis[0][1] - last_move[1]) * (now / dura)
                h = (lis[0][2] - last_move[2]) * (now / dura)
                return (last_move[1] + w, last_move[2] + h)
            return (last_move[1], last_move[2])

    def size(t):
        global last_move1
        if len(lis1) == 0:
            return (last_move1[3], last_move1[3] * 1.33)
        if t >= lis1[0][0]:
            last_move1 = item = lis1.pop(0)
            return (item[3], item[3] * 1.33)
        else:
            if len(lis) > 0:
                dura = lis1[0][0] - last_move1[0]
                now = t - last_move1[0]
                s = (lis1[0][3] - last_move1[3]) * (now / dura)
                nsw = last_move1[3] + s
                nsh = nsw * 1.33
                return (nsw, nsh)
            return (last_move1[3], last_move1[3] * 1.33)

    avatar = VideoFileClip("media/big_buck_bunny_432_433.webm", has_mask=True)
    avatar.audio = None
    maskclip = ImageClip("media/afterimage.png", is_mask=True, transparent=True)
    avatar.with_mask(maskclip)  # must set maskclip here..
    concatenated = avatar * 3

    tt = VideoFileClip("media/big_buck_bunny_0_30.webm").subclipped(0, 3)
    # TODO: Setting mask here does not work:
    # .with_mask(maskclip).resize(size)])
    final = CompositeVideoClip(
        [tt, concatenated.with_position(posi).with_effects([vfx.Resize(size)])]
    )
    final.duration = tt.duration
    final.write_videofile(os.path.join(util.TMP_DIR, "issue_334.mp4"), fps=10)


def test_issue_354():
    with ImageClip("media/python_logo.png") as clip:
        clip.duration = 10
        crosstime = 1

        fadecaption = clip.with_effects(
            [vfx.CrossFadeIn(crosstime), vfx.CrossFadeOut(crosstime)]
        )
        CompositeVideoClip([clip, fadecaption]).close()


def test_issue_359(util):
    with ColorClip((800, 600), color=(255, 0, 0)).with_duration(0.2) as video:
        video.fps = 30
        video.write_gif(filename=os.path.join(util.TMP_DIR, "issue_359.gif"))


def test_issue_407():
    red = ColorClip((800, 600), color=(255, 0, 0)).with_duration(5)
    red.fps = 30

    assert red.fps == 30
    assert red.w == 800
    assert red.h == 600
    assert red.size == (800, 600)

    # ColorClip has no fps attribute.
    green = ColorClip((640, 480), color=(0, 255, 0)).with_duration(2)
    blue = ColorClip((640, 480), color=(0, 0, 255)).with_duration(2)

    assert green.w == blue.w == 640
    assert green.h == blue.h == 480
    assert green.size == blue.size == (640, 480)

    with pytest.raises(AttributeError):
        green.fps

    with pytest.raises(AttributeError):
        blue.fps

    video = concatenate_videoclips([red, green, blue])
    assert video.fps == red.fps


def test_issue_416():
    # ColorClip has no fps attribute.
    green = ColorClip((640, 480), color=(0, 255, 0)).with_duration(2)
    video1 = concatenate_videoclips([green])
    assert video1.fps is None


def test_issue_417():
    # failed in python2
    cad = "media/python_logo.png"
    myclip = ImageClip(cad).resized(new_size=[1280, 660])
    CompositeVideoClip([myclip], size=(1280, 720))


def test_issue_470(util):
    wav_filename = os.path.join(util.TMP_DIR, "moviepy_issue_470.wav")

    audio_clip = AudioFileClip("media/crunching.mp3")

    # end_time is out of bounds
    with pytest.raises(ValueError):
        subclip = audio_clip.subclipped(start_time=6, end_time=9)
        subclip.write_audiofile(wav_filename, write_logfile=True)

    # but this one should work..
    subclip = audio_clip.subclipped(start_time=6, end_time=8)
    subclip.write_audiofile(wav_filename, write_logfile=True)


def test_issue_547():
    red = ColorClip((640, 480), color=(255, 0, 0)).with_duration(1)
    green = ColorClip((640, 480), color=(0, 255, 0)).with_duration(2)
    blue = ColorClip((640, 480), color=(0, 0, 255)).with_duration(3)

    video = concatenate_videoclips([red, green, blue], method="compose")
    assert video.duration == 6
    assert video.mask.duration == 6

    video = concatenate_videoclips([red, green, blue])
    assert video.duration == 6


def test_issue_636():
    with VideoFileClip("media/big_buck_bunny_0_30.webm").subclipped(0, 11) as video:
        with video.subclipped(0, 1) as _:
            pass


def test_issue_655():
    video_file = "media/fire2.mp4"
    for subclip in [(0, 2), (1, 2), (2, 2.10)]:
        with VideoFileClip(video_file) as v:
            with v.subclipped(1, 2) as _:
                pass
            next(v.subclipped(*subclip).iter_frames())
    assert True


def test_issue_1682(util):
    filename = "media/big_buck_bunny_0_30.webm"
    clip = VideoFileClip(filename)
    clip = clip.with_section_cut_out(1, 9)
    output_video_filepath = os.path.join(
        util.TMP_DIR, "big_buck_bunny_0_30_cutout.webm"
    )
    clip.write_videofile(output_video_filepath)


def test_issue_1682_2(util):
    filename = "media/rain.mp3"
    clip = AudioFileClip(filename)
    clip = clip.with_section_cut_out(10, 17)
    output_audio_filepath = os.path.join(util.TMP_DIR, "rain_cutout.mp3")
    clip.write_audiofile(output_audio_filepath)


def test_issue_2269(util):
    filename = "media/big_buck_bunny_0_30.webm"
    clip = VideoFileClip(filename).subclipped(0, 3)
    color_clip = ColorClip((500, 200), (255, 0, 0, 255)).with_duration(3)
    txt_clip_with_margin = TextClip(
        text="Hello",
        font=util.FONT,
        font_size=72,
        stroke_color="white",
        stroke_width=10,
        margin=(10, 5, 0, 0),
        text_align="center",
    ).with_duration(3)

    comp1 = CompositeVideoClip(
        [color_clip, txt_clip_with_margin.with_position(("center", "center"))],
        bg_color=None,  # No background color, so it should be transparent
    )
    comp2 = CompositeVideoClip(
        [clip, comp1.with_position(("center", "center"))],
        bg_color=None,  # No background color, so it should be transparent
    )

    # If transparency work as expected, this pixel should be pure red at 2 seconds
    frame = comp2.get_frame(2)
    pixel = frame[334, 625]

    # We add a bit of tolerance (about 1%) to account
    # For possible rounding errors
    assert np.allclose(pixel, [255, 0, 0], rtol=0.01)


def test_issue_2269_2(util):
    clip1 = ColorClip((200, 200), (255, 0, 0)).with_duration(3)
    clip2 = ColorClip((100, 100), (0, 255, 0, 76.5)).with_duration(3)
    clip3 = ColorClip((50, 50), (0, 0, 255, 76.5)).with_duration(3)

    compostite_clip1 = CompositeVideoClip(
        [clip1, clip2.with_position(("center", "center"))],
        bg_color=None,
    )
    compostite_clip2 = CompositeVideoClip(
        [compostite_clip1, clip3.with_position(("center", "center"))],
        bg_color=None,
    )

    # If transparency work as expected the clip should match thoses colors
    frame = compostite_clip2.get_frame(2)
    pixel1 = frame[100, 10]
    pixel2 = frame[100, 60]
    pixel3 = frame[100, 100]

    # We add a bit of tolerance (about 1%) to account
    # For possible rounding errors
    assert np.allclose(pixel1, [255, 0, 0], rtol=0.01)
    assert np.allclose(pixel2, [179, 76, 0], rtol=0.01)
    assert np.allclose(pixel3, [126, 53, 76], rtol=0.01)


def test_issue_2269_3(util):
    # This time all clips have transparency
    clip1 = ColorClip((200, 200), (255, 0, 0, 76.5)).with_duration(3)
    clip2 = ColorClip((100, 100), (0, 255, 0, 76.5)).with_duration(3)
    clip3 = ColorClip((50, 50), (0, 0, 255, 76.5)).with_duration(3)

    compostite_clip1 = CompositeVideoClip(
        [clip1, clip2.with_position(("center", "center"))],
        bg_color=None,
    )
    compostite_clip2 = CompositeVideoClip(
        [compostite_clip1, clip3.with_position(("center", "center"))],
        bg_color=None,
    )

    # If transparency work as expected the clip transparency should be between 0.3 and 0.657
    frame = compostite_clip2.mask.get_frame(2)
    pixel1 = frame[100, 10]
    pixel2 = frame[100, 60]
    pixel3 = frame[100, 100]
    assert pixel1 == 0.3
    assert pixel2 == 0.51
    assert pixel3 == 0.657


def test_issue_2160(util):
    filename = "media/-video-with-dash-.mp4"
    clip = VideoFileClip(filename)
    output_video_filepath = os.path.join(
        util.TMP_DIR, "big_buck_bunny_0_30_cutout.webm"
    )
    clip.write_videofile(output_video_filepath)


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_PR.py
````python
"""Pull request tests meant to be run with pytest."""

import os
from pathlib import Path

import pytest

from moviepy import *
from moviepy.video.tools.interpolators import Trajectory
from moviepy.video.tools.subtitles import SubtitlesClip


def test_PR_339(util):
    # In caption mode.
    TextClip(
        font=util.FONT,
        text="foo",
        color="white",
        size=(640, 480),
        method="caption",
        text_align="center",
        font_size=25,
    ).close()

    # In label mode.
    TextClip(text="foo", font=util.FONT, method="label", font_size=25).close()


def test_PR_373(util):
    result = Trajectory.load_list("media/traj.txt")

    Trajectory.save_list(result, os.path.join(util.TMP_DIR, "traj1.txt"))

    result1 = Trajectory.load_list(os.path.join(util.TMP_DIR, "traj1.txt"))

    assert len(result[0].tt) == len(result1[0].tt)
    for i in range(len(result[0].tt)):
        assert result[0].tt[i] == result1[0].tt[i]

    assert len(result[0].xx) == len(result1[0].xx)
    for i in range(len(result[0].xx)):
        assert result[0].xx[i] == result1[0].xx[i]

    assert len(result[0].yy) == len(result1[0].yy)
    for i in range(len(result[0].yy)):
        assert result[0].yy[i] == result1[0].yy[i]


def test_PR_458(util):
    clip = ColorClip([1000, 600], color=(60, 60, 60), duration=2)
    clip.write_videofile(os.path.join(util.TMP_DIR, "test.mp4"), logger=None, fps=30)
    clip.close()


def test_PR_515():
    # Won't actually work until video is in download_media
    with VideoFileClip("media/fire2.mp4", fps_source="tbr") as clip:
        assert clip.fps == 90000
    with VideoFileClip("media/fire2.mp4", fps_source="fps") as clip:
        assert clip.fps == 10.51


def test_PR_528(util):
    with ImageClip("media/vacation_2017.jpg") as clip:
        new_clip = clip.with_effects([vfx.Scroll(w=1000, x_speed=50)])
        new_clip = new_clip.with_duration(0.2)
        new_clip.fps = 24
        new_clip.write_videofile(os.path.join(util.TMP_DIR, "pano.mp4"), logger=None)


def test_PR_529():
    # print(ffmpeg_tools.ffplay_version())
    print(ffmpeg_tools.ffmpeg_version())
    with VideoFileClip("media/fire2.mp4") as video_clip:
        assert video_clip.rotation == 180


def test_PR_610():
    """Test that the max fps of video clips is used for the composite video clip."""
    clip1 = ColorClip((640, 480), color=(255, 0, 0)).with_duration(1)
    clip2 = ColorClip((640, 480), color=(0, 255, 0)).with_duration(1)
    clip1.fps = 24
    clip2.fps = 25
    composite = CompositeVideoClip([clip1, clip2])
    assert composite.fps == 25


def test_PR_1137_video(util, video):
    """Test support for path-like objects as arguments for VideoFileClip."""
    with video(start_time=0.2, end_time=0.24) as video:
        video.write_videofile(Path(util.TMP_DIR) / "pathlike.mp4", logger=None)
        assert isinstance(video.filename, str)


def test_PR_1137_audio(util):
    """Test support for path-like objects as arguments for AudioFileClip."""
    with AudioFileClip(Path("media/crunching.mp3")) as audio:
        audio.write_audiofile(Path(util.TMP_DIR) / "pathlike.mp3")
        assert isinstance(audio.filename, str)


def test_PR_1137_image():
    """Test support for path-like objects as arguments for ImageClip."""
    ImageClip(Path("media/vacation_2017.jpg")).close()


def test_PR_1137_subtitles(util):
    """Test support for path-like objects as arguments for SubtitlesClip."""

    def make_textclip(txt):
        return TextClip(
            font=util.FONT,
            text=txt,
            font_size=24,
            color="white",
            stroke_color="black",
            stroke_width=1,
        )

    SubtitlesClip(Path("media/subtitles.srt"), make_textclip=make_textclip).close()


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_SubtitlesClip.py
````python
"""SubtitlesClip tests."""

import os

import pytest

from moviepy.video.compositing.CompositeVideoClip import (
    CompositeVideoClip,
    concatenate_videoclips,
)
from moviepy.video.tools.subtitles import SubtitlesClip, file_to_subtitles
from moviepy.video.VideoClip import ColorClip, TextClip


MEDIA_SUBTITLES_DATA = [
    ([0.0, 1.0], "Red!"),
    ([2.0, 3.5], "More Red!"),
    ([5.0, 6.0], "Green!"),
    ([7.0, 8.0], "Blue"),
    ([9.0, 10.0], "More Blue!"),
]

MEDIA_SUBTITLES_UNICODE_DATA = [
    ([0, 5.0], "ÁÉíöÙ"),
]


def test_subtitles(util):
    red = ColorClip((800, 600), color=(255, 0, 0)).with_duration(10)
    green = ColorClip((800, 600), color=(0, 255, 0)).with_duration(10)
    blue = ColorClip((800, 600), color=(0, 0, 255)).with_duration(10)
    myvideo = concatenate_videoclips([red, green, blue])
    assert myvideo.duration == 30

    generator = lambda txt: TextClip(
        text=txt,
        font=util.FONT,
        size=(800, 600),
        font_size=24,
        method="caption",
        vertical_align="bottom",
        color="white",
    )

    subtitles = SubtitlesClip("media/subtitles.srt", make_textclip=generator)
    final = CompositeVideoClip([myvideo, subtitles])
    final.subclipped(0, 0.5).write_videofile(
        os.path.join(util.TMP_DIR, "subtitles.mp4"),
        fps=5,
        logger=None,
    )

    assert subtitles.subtitles == MEDIA_SUBTITLES_DATA

    subtitles = SubtitlesClip(MEDIA_SUBTITLES_DATA, make_textclip=generator)
    assert subtitles.subtitles == MEDIA_SUBTITLES_DATA


def test_file_to_subtitles():
    assert MEDIA_SUBTITLES_DATA == file_to_subtitles("media/subtitles.srt")


def test_file_to_subtitles_unicode():
    assert MEDIA_SUBTITLES_UNICODE_DATA == file_to_subtitles(
        "media/subtitles-unicode.srt", encoding="utf-8"
    )


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_TextClip.py
````python
"""TextClip tests."""

import os

import numpy as np

import pytest

from moviepy import *


def test_duration(util):
    clip = TextClip(text="hello world", size=(1280, 720), color="white", font=util.FONT)
    clip = clip.with_duration(5)
    assert clip.duration == 5
    clip.close()

    clip2 = clip.with_effects([vfx.Blink(duration_on=1, duration_off=1)])
    clip2 = clip2.with_duration(5)
    assert clip2.duration == 5


def test_text_filename_arguments_consistence(util):
    """Passing ``text`` or ``filename`` we obtain the same result."""
    clip_from_text = (
        TextClip(
            text="Hello",
            size=(20, 20),
            color="#000",
            bg_color="#FFF",
            method="caption",
            font=util.FONT,
        )
        .with_fps(1)
        .with_duration(1)
    )

    with open(os.path.join(util.TMP_DIR, "text-for-clip.txt"), "w") as f:
        f.write("Hello")

    clip_from_file = (
        TextClip(
            text="Hello",
            size=(20, 20),
            color="#000",
            bg_color="#FFF",
            method="caption",
            font=util.FONT,
        )
        .with_fps(1)
        .with_duration(1)
    )

    frames_from_text = list(clip_from_text.iter_frames())
    frames_from_file = list(clip_from_file.iter_frames())
    assert len(frames_from_text) == 1
    assert len(frames_from_file) == 1
    assert np.equal(frames_from_text[0], frames_from_file[0]).all()


@pytest.mark.parametrize(
    "method", ("caption", "label"), ids=("method=caption", "method=label")
)
def test_no_text_nor_filename_arguments(method, util):
    expected_error_msg = "^No text nor filename provided$"
    with pytest.raises(ValueError, match=expected_error_msg):
        TextClip(
            size=(20, 20),
            color="#000",
            bg_color="#FFF",
            font=util.FONT,
            method=method,
        )


@pytest.mark.xfail(reason="Autosizing might not work great with new Pillow versions")
def test_label_autosizing(util):
    # We test with about all possible letters
    text = "abcdefghijklmnopqrstuvwxyzáàâäãåāæąēéèêëīíìîïñōóòôöõøœęý\
    ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÂÄÃÅĀÆĄĒÉÈÊËĪÍÌÎÏÑŌÓÒÔÖÕØŒĘÝ"
    text += "\nabcdefghijklmnopqrstuvwxyzáàâäãåāæąēéèêëīíìîïñōóòôöõøœęý\
        ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÂÄÃÅĀÆĄĒÉÈÊËĪÍÌÎÏÑŌÓÒÔÖÕØŒĘÝ"
    text += "\nabcdefghijklmnopqrstuvwxyzáàâäãåāæąēéèêëīíìîïñōóòôöõøœęý\
        ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÂÄÃÅĀÆĄĒÉÈÊËĪÍÌÎÏÑŌÓÒÔÖÕØŒĘÝ"

    text_clip_margin = TextClip(
        util.FONT,
        method="label",
        font_size=40,
        text=text,
        color="red",
        bg_color="black",
        stroke_width=3,
        stroke_color="white",
        margin=(1, 1),
    ).with_duration(1)
    text_clip_no_margin = TextClip(
        util.FONT,
        method="label",
        font_size=40,
        text=text,
        color="red",
        bg_color="black",
        stroke_width=3,
        stroke_color="white",
    ).with_duration(1)

    margin_frame = text_clip_margin.get_frame(1)
    no_margin_frame = text_clip_no_margin.get_frame(1)

    # The idea is, if autosizing work as expected, frame with 1px margin will
    # have black color all around, where frame without margin will have white somewhere
    first_row, last_row = (margin_frame[0], margin_frame[-1])
    first_column, last_column = (margin_frame[:, 0], margin_frame[:, -1])

    # We add a bit of tolerance (about 1%) to account for possible rounding errors
    # print(first_row, last_row, first_column, last_column)
    assert np.allclose(first_row, [0, 0, 0], rtol=0.01)
    assert np.allclose(last_row, [0, 0, 0], rtol=0.01)
    assert np.allclose(first_column, [0, 0, 0], rtol=0.01)
    assert np.allclose(last_column, [0, 0, 0], rtol=0.01)

    # We actually check on three pixels border, because some fonts
    # always add a 1px padding all arround and some rounding error can make it two
    first_three_rows, last_three_rows = (no_margin_frame[:3], no_margin_frame[-3:])
    first_three_columns, last_three_columns = (
        no_margin_frame[:, :3],
        no_margin_frame[:, -3:],
    )

    # We add a bit of tolerance (about 1%) to account for possible rounding errors
    assert not np.allclose(first_three_rows, [0, 0, 0], rtol=0.01)
    assert not np.allclose(last_three_rows, [0, 0, 0], rtol=0.01)
    assert not np.allclose(first_three_columns, [0, 0, 0], rtol=0.01)
    assert not np.allclose(last_three_columns, [0, 0, 0], rtol=0.01)


def test_no_font(util):
    # Try make a clip with default font
    clip = TextClip(text="Hello world !", font_size=20, color="white")
    clip.show(1)
    assert clip.size[0] > 10


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_tools.py
````python
"""Tool tests meant to be run with pytest. Taken from PR #121 (grimley517)."""

import contextlib
import importlib
import io
import os
import shutil
import sys

import pytest

import moviepy.tools as tools


@pytest.mark.parametrize(
    ("given", "expected"),
    [
        ("libx264", "mp4"),
        ("libmpeg4", "mp4"),
        ("libtheora", "ogv"),
        ("libvpx", "webm"),
        ("jpeg", "jpeg"),
    ],
)
def test_find_extensions(given, expected):
    """Test for find_extension function."""
    assert tools.find_extension(given) == expected


def test_find_extensions_not_found():
    """Test for raising error if codec not in dictionaries."""
    with pytest.raises(ValueError):  # asking for a silly video format
        tools.find_extension("flashvideo")


@pytest.mark.parametrize(
    "given, expected",
    [
        (15.4, 15.4),
        ((1, 21.5), 81.5),
        ((1, 1, 2), 3662),
        ([1, 1, 2], 3662),
        ("01:01:33.5", 3693.5),
        ("01:01:33.045", 3693.045),
        ("01:01:33,5", 3693.5),
        ("1:33", 93.0),
        ("33.4", 33.4),
        (None, None),
    ],
)
def test_cvsecs(given, expected):
    """Test the convert_to_seconds function outputs correct times as per
    the docstring.
    """
    assert tools.convert_to_seconds(given) == expected


@pytest.mark.skipif(not shutil.which("echo"), reason="not in Unix")
@pytest.mark.parametrize("command", ("echo", "jbdshfuygvhbsdvfghew"))
def test_subprocess_call(command):
    if command == "echo":
        tools.subprocess_call(command, logger=None)
    else:
        with pytest.raises(IOError):
            tools.subprocess_call(command, logger=None)


@pytest.mark.parametrize(
    "given, expected",
    [
        ("-filenamethatstartswithdash-.mp4", "./-filenamethatstartswithdash-.mp4"),
        ("-path/that/starts/with/dash.mp4", "./-path/that/starts/with/dash.mp4"),
        ("file-name-.mp4", "file-name-.mp4"),
        ("/absolute/path/to/-file.mp4", "/absolute/path/to/-file.mp4"),
        ("filename with spaces.mp4", "filename with spaces.mp4"),
    ],
)
def test_ffmpeg_escape_filename(given, expected):
    """Test the ffmpeg_escape_filename function outputs correct paths as per
    the docstring.
    """
    assert tools.ffmpeg_escape_filename(given) == expected


@pytest.mark.parametrize("os_name", (os.name, "nt"))
def test_cross_platform_popen_params(os_name, monkeypatch):
    tools_module = importlib.import_module("moviepy.tools")
    monkeypatch.setattr(tools_module, "OS_NAME", os_name)

    params = tools_module.cross_platform_popen_params({})
    assert len(params) == (1 if os_name == "nt" else 0)


@pytest.mark.parametrize("old_name", ("bar", "foo"))
def test_deprecated_version_of(old_name):
    def to_file(*args, **kwargs):
        return

    func = tools.deprecated_version_of(to_file, old_name)

    expected_warning_message = (
        f"MoviePy: The function ``{old_name}`` is deprecated and is kept"
        " temporarily for backwards compatibility.\nPlease use the new name"
        f", ``{to_file.__name__}``, instead."
    )

    with pytest.warns(PendingDeprecationWarning) as record:
        func(1, b=2)

    assert len(record) > 0
    assert record[0].message.args[0] == expected_warning_message


@pytest.mark.skipif(os.name != "posix", reason="Doesn't works in Windows")
@pytest.mark.parametrize(
    ("ffmpeg_binary", "ffmpeg_binary_error"),
    (
        pytest.param("ffmpeg-imageio", None, id="FFMPEG_BINARY=ffmpeg-imageio"),
        pytest.param("auto-detect", None, id="FFMPEG_BINARY=auto-detect"),
        pytest.param(
            "foobarbazimpossible",
            (IOError, "No such file or directory:"),
            id="FFMPEG_BINARY=foobarbazimpossible",
        ),
    ),
)
def test_config(
    util,
    ffmpeg_binary,
    ffmpeg_binary_error,
):
    if "moviepy.config" in sys.modules:
        del sys.modules["moviepy.config"]

    if ffmpeg_binary_error is not None and os.path.isfile(ffmpeg_binary):
        os.remove(ffmpeg_binary)
    prev_ffmpeg_binary = os.environ.get("FFMPEG_BINARY")
    os.environ["FFMPEG_BINARY"] = ffmpeg_binary

    if ffmpeg_binary_error is not None:
        with pytest.raises(ffmpeg_binary_error[0]) as exc:
            importlib.import_module("moviepy.config")
        assert ffmpeg_binary_error[1] in str(exc.value)

    if prev_ffmpeg_binary is not None:
        os.environ["FFMPEG_BINARY"] = prev_ffmpeg_binary

    if "moviepy.config" in sys.modules:
        del sys.modules["moviepy.config"]


def test_config_check():
    if "moviepy.config" in sys.modules:
        del sys.modules["moviepy.config"]

    try:
        dotenv_module = importlib.import_module("dotenv")
    except ImportError:
        dotenv_module = None
    else:
        with open(".env", "w") as f:
            f.write("")

    moviepy_config_module = importlib.import_module("moviepy.config")

    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout):
        moviepy_config_module.check()

    output = stdout.getvalue()

    assert "MoviePy: ffmpeg successfully found in" in output

    if dotenv_module:
        assert os.path.isfile(".env")
        os.remove(".env")
        assert ".env file content at" in output
        del sys.modules["dotenv"]

    if "moviepy.config" in sys.modules:
        del sys.modules["moviepy.config"]


@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8 or greater")
@pytest.mark.parametrize(
    "decorator_name",
    ("convert_parameter_to_seconds", "convert_path_to_string"),
)
def test_decorators_argument_converters_consistency(
    moviepy_modules, functions_with_decorator_defined, decorator_name
):
    """Checks that for all functions that have a decorator defined (like
    ``@convert_parameter_to_seconds``), the parameters passed to the decorator
    correspond to the parameters taken by the function.

    This test is util to prevent next case in which the parameter names doesn't
    match between the decorator and the function definition:

    >>> @convert_parameter_to_seconds(['foo'])
    >>> def whatever_function(bar):  # bar not converted to seconds
    ...     pass

    Some wrong definitions remained unnoticed in the past before this test was
    added.
    """
    with contextlib.redirect_stdout(io.StringIO()):
        for modname, ispkg in moviepy_modules():
            if ispkg:
                continue

            try:
                module = importlib.import_module(modname)
            except ImportError:
                continue

            functions_with_decorator = functions_with_decorator_defined(
                module,
                decorator_name,
            )

            for function_data in functions_with_decorator:
                for argument_name in function_data["decorator_arguments"]:
                    funcname = function_data["function_name"]
                    assert argument_name in function_data["function_arguments"], (
                        f"Wrong argument name '{argument_name}' in"
                        f" '@{decorator_name}' decorator for function"
                        f" '{funcname}' found inside module '{modname}'"
                    )

                assert function_data["decorator_arguments"]
                assert function_data["function_arguments"]


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_VideoClip.py
````python
"""VideoClip tests."""

import copy
import os

import numpy as np
from PIL import Image

import pytest

from moviepy import *
from moviepy.tools import convert_to_seconds


def test_aspect_ratio():
    clip = BitmapClip([["AAA", "BBB"]], fps=1)
    assert clip.aspect_ratio == 1.5


@pytest.mark.parametrize(
    ("duration", "fps", "expected_n_frames"),
    (
        (1, 60, 60),
        (0.1, 100, 10),
        (2.4, 60, 144),
    ),
)
def test_n_frames(duration, fps, expected_n_frames):
    clip = VideoClip(duration=duration).with_fps(fps)
    assert clip.n_frames == expected_n_frames


def test_with_audio(stereo_wave):
    clip = VideoClip(duration=1).with_fps(1)
    assert clip.audio is None

    audio_clip = AudioClip(stereo_wave(), duration=1, fps=22050)
    assert clip.with_audio(audio_clip).audio is audio_clip


def test_without_audio(stereo_wave):
    audio_clip = AudioClip(stereo_wave(), duration=1, fps=22050)
    clip = VideoClip(duration=1).with_fps(1).with_audio(audio_clip)

    assert clip.audio is audio_clip
    assert clip.without_audio().audio is None


def test_check_codec(util, video):
    clip = video()
    location = os.path.join(util.TMP_DIR, "not_a_video.mas")
    try:
        clip.write_videofile(location)
    except ValueError as e:
        assert (
            "MoviePy couldn't find the codec associated with the filename."
            " Provide the 'codec' parameter in write_videofile." in str(e)
        )


def test_write_frame_errors(util, video):
    """Checks error cases return helpful messages."""
    clip = video()
    location = os.path.join(util.TMP_DIR, "unlogged-write.mp4")
    with pytest.raises(IOError) as e:
        clip.write_videofile(location, codec="nonexistent-codec")
    assert (
        "The video export failed because FFMPEG didn't find the specified"
        " codec for video or audio" in str(e.value)
    ), e.value

    autogenerated_location = "unlogged-writeTEMP_MPY_wvf_snd.mp3"
    if os.path.exists(autogenerated_location):
        os.remove(autogenerated_location)


def test_write_frame_errors_with_redirected_logs(util, video):
    """Checks error cases return helpful messages even when logs redirected.
    See https://github.com/Zulko/moviepy/issues/877
    """
    clip = video()
    location = os.path.join(util.TMP_DIR, "logged-write.mp4")
    with pytest.raises(IOError) as e:
        clip.write_videofile(location, codec="nonexistent-codec", write_logfile=True)
    assert (
        "The video export failed because FFMPEG didn't find the specified"
        " codec for video or audio" in str(e.value)
    )

    autogenerated_location_mp3 = "logged-writeTEMP_MPY_wvf_snd.mp3"
    autogenerated_location_log = autogenerated_location_mp3 + ".log"
    for fp in [autogenerated_location_mp3, autogenerated_location_log]:
        if os.path.exists(fp):
            os.remove(fp)


def test_write_videofiles_with_temp_audiofile_path(util):
    clip = VideoFileClip("media/big_buck_bunny_432_433.webm").subclipped(0.2, 0.5)
    location = os.path.join(util.TMP_DIR, "temp_audiofile_path.webm")
    temp_location = os.path.join(util.TMP_DIR, "temp_audiofile")
    if not os.path.exists(temp_location):
        os.mkdir(temp_location)
    clip.write_videofile(location, temp_audiofile_path=temp_location, remove_temp=False)
    assert os.path.isfile(location)
    contents_of_temp_dir = os.listdir(temp_location)
    assert any(file.startswith("temp_audiofile_path") for file in contents_of_temp_dir)


def test_write_videofiles_audio_codec_error(util, video):
    """Checks error cases return helpful messages."""
    clip = video()
    location = os.path.join(util.TMP_DIR, "unlogged-write.mp4")
    with pytest.raises(IOError) as e:
        clip.write_videofile(
            location, audio="media/crunching.mp3", audio_codec="nonexistent-codec"
        )
    assert (
        "The video export failed because FFMPEG didn't find the specified"
        " codec for video or audio" in str(e.value)
    ), e.value

    autogenerated_location = "unlogged-writeTEMP_MPY_wvf_snd.mp3"
    if os.path.exists(autogenerated_location):
        os.remove(autogenerated_location)


@pytest.mark.parametrize("mask_color", (0, 0.5, 0.8, 1))
@pytest.mark.parametrize(
    "with_mask",
    (False, True),
    ids=("mask", ""),
)
@pytest.mark.parametrize("t", (0, "00:00:01", (0, 0, 2)), ids=("t=0", "t=1", "t=2"))
@pytest.mark.parametrize(
    "frames",
    (
        pytest.param(
            [["RR", "RR"], ["GG", "GG"], ["BB", "BB"]],
            id="RGB 2x2",
        ),
        pytest.param(
            [["O", "O"], ["W", "W"], ["B", "B"]],
            id="OWB 2x1",
        ),
    ),
)
def test_save_frame(util, with_mask, t, mask_color, frames):
    filename = os.path.join(util.TMP_DIR, "moviepy_VideoClip_save_frame.png")
    if os.path.isfile(filename):
        try:
            os.remove(filename)
        except PermissionError:
            pass

    width, height = (len(frames[0][0]), len(frames[0]))

    clip = BitmapClip(frames, fps=1)
    if with_mask:
        mask = ColorClip(color=mask_color, is_mask=True, size=(width, height))
        clip = clip.with_mask(mask)

    clip.save_frame(filename, t)

    t = int(convert_to_seconds(t))

    # expected RGB
    e_r, e_g, e_b = BitmapClip.DEFAULT_COLOR_DICT[frames[t][0][0]]

    im = Image.open(filename, mode="r")
    assert im.width == width
    assert im.height == height

    for i in range(im.width):
        for j in range(im.height):
            rgba = im.getpixel((i, j))
            if len(rgba) == 4:
                r, g, b, a = rgba
            else:
                r, g, b = rgba

            assert r == e_r
            assert g == e_g
            assert b == e_b

            if with_mask:
                assert round(a / 254, 2) == mask_color


def test_write_image_sequence(util, video):
    clip = video(start_time=0.2, end_time=0.24)
    locations = clip.write_images_sequence(os.path.join(util.TMP_DIR, "frame%02d.png"))
    for location in locations:
        assert os.path.isfile(location)


def test_write_gif(util, video):
    clip = video(start_time=0.2, end_time=0.8)
    location = os.path.join(util.TMP_DIR, "imageio_gif.gif")
    clip.write_gif(location)
    assert os.path.isfile(location)


def test_with_sub_effetcs(util):
    clip = VideoFileClip("media/big_buck_bunny_0_30.webm").subclipped(0, 1)
    new_clip = clip.with_effects_on_subclip([vfx.MultiplySpeed(0.5)])
    location = os.path.join(util.TMP_DIR, "with_effects_on_subclip.mp4")
    new_clip.write_videofile(location)
    assert os.path.isfile(location)


def test_oncolor(util):
    # It doesn't need to be a ColorClip
    clip = ColorClip(size=(100, 60), color=(255, 0, 0), duration=0.5)
    on_color_clip = clip.with_background_color(size=(200, 160), color=(0, 0, 255))
    location = os.path.join(util.TMP_DIR, "oncolor.mp4")
    on_color_clip.write_videofile(location, fps=24)
    assert os.path.isfile(location)

    # test constructor with default arguments
    clip = ColorClip(size=(100, 60), is_mask=True)
    clip = ColorClip(size=(100, 60), is_mask=False)

    # negative test
    with pytest.raises(Exception):
        clip = ColorClip(size=(100, 60), color=(255, 0, 0), is_mask=True)

    with pytest.raises(Exception):
        clip = ColorClip(size=(100, 60), color=0.4, ismask=False)

    with pytest.raises(Exception):
        clip = ColorClip(size=(100, 60), color="black")


def test_setaudio(util):
    clip = ColorClip(size=(100, 60), color=(255, 0, 0), duration=0.5)
    frame_function_440 = lambda t: [np.sin(440 * 2 * np.pi * t)]
    audio = AudioClip(frame_function_440, duration=0.5)
    audio.fps = 44100
    clip = clip.with_audio(audio)
    location = os.path.join(util.TMP_DIR, "setaudio.mp4")
    clip.write_videofile(location, fps=24)
    assert os.path.isfile(location)


def test_setaudio_with_audiofile(util):
    clip = ColorClip(size=(100, 60), color=(255, 0, 0), duration=0.5)
    audio = AudioFileClip("media/crunching.mp3").subclipped(0, 0.5)
    clip = clip.with_audio(audio)
    location = os.path.join(util.TMP_DIR, "setaudiofile.mp4")
    clip.write_videofile(location, fps=24)
    assert os.path.isfile(location)


def test_setopacity(util, video):
    clip = video(start_time=0.2, end_time=0.6)
    clip = clip.with_opacity(0.5)
    clip = clip.with_background_color(size=(1000, 1000), color=(0, 0, 255), opacity=0.8)
    location = os.path.join(util.TMP_DIR, "setopacity.mp4")
    clip.write_videofile(location)
    assert os.path.isfile(location)


def test_with_layer_index():
    bottom_clip = BitmapClip([["ABC"], ["BCA"], ["CAB"]], fps=1).with_layer_index(1)
    top_clip = BitmapClip([["DEF"], ["EFD"]], fps=1).with_layer_index(2)

    composite_clip = CompositeVideoClip([bottom_clip, top_clip])
    reversed_composite_clip = CompositeVideoClip([top_clip, bottom_clip])

    # Make sure that the order of clips makes no difference to the composite clip
    assert composite_clip.subclipped(0, 2) == reversed_composite_clip.subclipped(0, 2)

    # Make sure that only the 'top' clip is kept
    assert top_clip.subclipped(0, 2) == composite_clip.subclipped(0, 2)

    # Make sure that it works even when there is only one clip playing at that time
    target_clip = BitmapClip([["DEF"], ["EFD"], ["CAB"]], fps=1)
    assert composite_clip == target_clip


def test_compositing_with_same_layers():
    bottom_clip = BitmapClip([["ABC"], ["BCA"]], fps=1)
    top_clip = BitmapClip([["DEF"], ["EFD"]], fps=1)

    composite_clip = CompositeVideoClip([bottom_clip, top_clip])
    reversed_composite_clip = CompositeVideoClip([top_clip, bottom_clip])

    assert composite_clip == top_clip
    assert reversed_composite_clip == bottom_clip


def test_toimageclip(util, video):
    clip = video(start_time=0.2, end_time=0.6)
    clip = clip.to_ImageClip(t=0.1, duration=0.4)
    location = os.path.join(util.TMP_DIR, "toimageclip.mp4")
    clip.write_videofile(location, fps=24)
    assert os.path.isfile(location)


def test_withoutaudio(video):
    clip = video(start_time=0.2, end_time=0.6)
    new_clip = clip.without_audio()
    assert new_clip.audio is None


def test_setfps_withoutchangeduration(video):
    clip = video()
    # The sum is unique for each frame, so we can use it as a frame-ID
    # to check which frames are being preserved
    clip_sums = [f.sum() for f in clip.iter_frames()]

    clip2 = clip.with_fps(48)
    clip2_sums = [f.sum() for f in clip2.iter_frames()]
    assert clip2_sums[::2] == clip_sums
    assert clip2.duration == clip.duration


def test_setfps_withchangeduration(video):
    clip = video(end_time=0.2)
    # The sum is unique for each frame, so we can use it as a frame-ID
    # to check which frames are being preserved
    clip_sums = [f.sum() for f in clip.iter_frames()]

    clip2 = clip.with_fps(48, change_duration=True)
    clip2_sums = [f.sum() for f in clip2.iter_frames()]
    assert clip2_sums == clip_sums
    assert clip2.duration == clip.duration / 2


def test_copied_videoclip_write_videofile(util):
    """Check if a copied ``VideoClip`` instance can render a file which has
    the same features as the copied clip when opening with ``VideoFileClip``.
    """
    clip = BitmapClip([["RRR", "GGG", "BBB"]], fps=1)
    copied_clip = clip.copy()

    output_filepath = os.path.join(util.TMP_DIR, "copied_videoclip_from_bitmap.webm")
    copied_clip.write_videofile(output_filepath)
    copied_clip_from_file = VideoFileClip(output_filepath)

    assert list(copied_clip.size) == copied_clip_from_file.size
    assert copied_clip.duration == copied_clip_from_file.duration


@pytest.mark.parametrize(
    "copy_func",
    (
        lambda clip: clip.copy(),
        lambda clip: copy.copy(clip),
        lambda clip: copy.deepcopy(clip),
    ),
    ids=("clip.copy()", "copy.copy(clip)", "copy.deepcopy(clip)"),
)
def test_videoclip_copy(copy_func):
    """It must be possible to do a mixed copy of VideoClip using ``clip.copy()``,
    ``copy.copy(clip)`` and ``copy.deepcopy(clip)``.
    """
    clip = VideoClip()
    other_clip = VideoClip()

    for attr in clip.__dict__:
        # mask and audio are shallow copies that should be initialized
        if attr in ("mask", "audio"):
            if attr == "mask":
                nested_object = BitmapClip([["R"]], duration=0.01)
            else:
                nested_object = AudioClip(
                    lambda t: [np.sin(880 * 2 * np.pi * t)], duration=0.01, fps=44100
                )
            setattr(clip, attr, nested_object)
        else:
            setattr(clip, attr, "foo")

    copied_clip = copy_func(clip)

    # VideoClip attributes are copied
    for attr in copied_clip.__dict__:
        value = getattr(copied_clip, attr)
        assert value == getattr(clip, attr)

        # other instances are not edited
        assert value != getattr(other_clip, attr)

        # shallow copies of mask and audio
        if attr in ("mask", "audio"):
            for nested_attr in value.__dict__:
                assert getattr(value, nested_attr) == getattr(
                    getattr(clip, attr), nested_attr
                )

    # nested objects of instances copies are not edited
    assert other_clip.mask is None
    assert other_clip.audio is None


def test_afterimage(util):
    ai = ImageClip("media/afterimage.png")
    masked_clip = ai.with_effects([vfx.MaskColor(color=[0, 255, 1])])  # for green
    some_background_clip = ColorClip((800, 600), color=(255, 255, 255))
    final_clip = CompositeVideoClip(
        [some_background_clip, masked_clip], use_bgclip=True
    ).with_duration(0.2)

    filename = os.path.join(util.TMP_DIR, "afterimage.mp4")
    final_clip.write_videofile(filename, fps=30, logger=None)


def test_add():
    clip = VideoFileClip("media/fire2.mp4")
    new_clip = clip[0:1] + clip[1.5:2]
    assert new_clip.duration == 1.5
    assert np.array_equal(new_clip[1.1], clip[1.6])


def test_slice_tuples():
    clip = VideoFileClip("media/fire2.mp4")
    new_clip = clip[0:1, 1.5:2]
    assert new_clip.duration == 1.5
    assert np.array_equal(new_clip[1.1], clip[1.6])


def test_slice_mirror():
    clip = VideoFileClip("media/fire2.mp4")
    new_clip = clip[::-1]
    assert new_clip.duration == clip.duration
    assert np.array_equal(new_clip[0], clip[clip.duration])


def test_slice_speed():
    clip = BitmapClip([["A"], ["B"], ["C"], ["D"]], fps=1)
    clip1 = clip[::0.5]  # 1/2x speed
    target1 = BitmapClip(
        [["A"], ["A"], ["B"], ["B"], ["C"], ["C"], ["D"], ["D"]], fps=1
    )
    assert clip1 == target1


def test_mul():
    clip = VideoFileClip("media/fire2.mp4")
    new_clip = clip[0:1] * 2.5
    assert new_clip.duration == 2.5
    assert np.array_equal(new_clip[1.1], clip[0.1])


def test_and():
    clip = VideoFileClip("media/fire2.mp4")
    maskclip = ImageClip("media/afterimage.png", is_mask=True, transparent=True)
    clip_with_mask = clip & maskclip
    assert clip_with_mask.mask is maskclip


def test_or(util):
    clip1 = BitmapClip([["R"]], fps=1)
    clip2 = BitmapClip([["G"]], fps=1)
    target = BitmapClip([["RG"]], fps=1)
    result = clip1 | clip2
    assert result == target


def test_truediv(util):
    clip1 = BitmapClip([["R"]], fps=1)
    clip2 = BitmapClip([["G"]], fps=1)
    target = BitmapClip([["R", "G"]], fps=1)
    result = clip1 / clip2
    assert result == target


def test_matmul(util):
    clip1 = BitmapClip([["RG"]], fps=1)
    target = BitmapClip([["R", "G"]], fps=1)
    result = clip1 @ 270
    assert result == target


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_VideoFileClip.py
````python
"""Video file clip tests meant to be run with pytest."""

import copy
import os
from pathlib import Path

import pytest

from moviepy.video.compositing.CompositeVideoClip import clips_array
from moviepy.video.io.errors import VideoCorruptedError
from moviepy.video.io.ffmpeg_tools import ffmpeg_copy
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ColorClip


def test_setup(util):
    """Test VideoFileClip setup."""
    filename = os.path.join(util.TMP_DIR, "test.mp4")

    red = ColorClip((256, 200), color=(255, 0, 0))
    green = ColorClip((256, 200), color=(0, 255, 0))
    blue = ColorClip((256, 200), color=(0, 0, 255))

    red.fps = green.fps = blue.fps = 10
    with clips_array([[red, green, blue]]).with_duration(5) as video:
        video.write_videofile(filename, logger=None)

    assert os.path.exists(filename)

    clip = VideoFileClip(filename)
    assert clip.duration == 5
    assert clip.fps == 10
    assert clip.size == [256 * 3, 200]
    assert clip.reader.bitrate == 2


def test_ffmpeg_resizing():
    """Test FFmpeg resizing, to include downscaling."""
    video_file = "media/big_buck_bunny_432_433.webm"
    target_resolutions = [(128, 128), (128, None), (None, 128), (None, 256)]
    for target_resolution in target_resolutions:
        video = VideoFileClip(video_file, target_resolution=target_resolution)
        frame = video.get_frame(0)
        for target, observed in zip(target_resolution[::-1], frame.shape):
            if target is not None:
                assert target == observed
        video.close()


def test_copied_videofileclip_write_videofile(util):
    """Check that a copied ``VideoFileClip`` can be renderizable using
    ``write_videofile``, opened from that render and the new video shares
    the same data that the original clip.
    """
    input_video_filepath = "media/big_buck_bunny_432_433.webm"
    output_video_filepath = os.path.join(util.TMP_DIR, "copied_videofileclip.mp4")

    clip = VideoFileClip(input_video_filepath).subclipped(0, 1)
    copied_clip = clip.copy()

    copied_clip.write_videofile(output_video_filepath)

    assert os.path.exists(output_video_filepath)
    copied_clip_from_file = VideoFileClip(output_video_filepath)

    assert copied_clip.fps == copied_clip_from_file.fps
    assert list(copied_clip.size) == copied_clip_from_file.size
    assert isinstance(copied_clip.reader, type(copied_clip_from_file.reader))


def test_videofileclip_safe_deepcopy(monkeypatch):
    """Attempts to do a deepcopy of a VideoFileClip will do a mixed copy,
    being redirected to ``__copy__`` method of ``VideoClip``, see the
    documentation of ``VideoFileClip.__deepcopy__`` for more information
    about this.
    """
    clip = VideoFileClip("media/chaplin.mp4")

    # patch __copy__ in the clip
    def fake__copy__():
        return "foo"

    monkeypatch.setattr(clip, "__copy__", fake__copy__)

    # this should not raise any exception (see `VideoFileClip.__deepcopy__`)
    assert copy.deepcopy(clip) == "foo"


def test_ffmpeg_transparency_mask(util):
    """Test VideoFileClip and FFMPEG reading of video with transparency."""
    video_file = "media/transparent.webm"

    video = VideoFileClip(video_file, has_mask=True)

    assert video.mask is not None

    mask_frame = video.mask.get_frame(0)
    assert mask_frame[100, 100] == 1.0
    assert mask_frame[10, 10] == 0

    video.close()


def test_no_duration_raise_io_error():
    with pytest.raises(
        VideoCorruptedError,
        match="Could not parse duration from 'N/A, start: 0.000000, bitrate: N/A",
    ):
        VideoFileClip("media/no_duration.webm")


def test_no_duration_re_encode_can_be_opened(util):
    target = Path(util.TMP_DIR).joinpath("re_encoded.webm")
    ffmpeg_copy("media/no_duration.webm", target)
    VideoFileClip(target)


if __name__ == "__main__":
    pytest.main()
````

## File: tests/test_videotools.py
````python
"""Video file clip tests meant to be run with pytest."""

import importlib
import math
import os
import shutil
import sys

import numpy as np

import pytest

from moviepy import *
from moviepy.audio.tools.cuts import find_audio_period
from moviepy.video.tools.credits import CreditsClip
from moviepy.video.tools.cuts import (
    FramesMatch,
    FramesMatches,
    detect_scenes,
    find_video_period,
)
from moviepy.video.tools.drawing import circle, color_gradient, color_split
from moviepy.video.tools.interpolators import Interpolator, Trajectory


try:
    importlib.import_module("ipython.display")
except ImportError:
    ipython_available = False
else:
    ipython_available = True
    del sys.modules["ipython.display"]


def test_credits(util):
    credit_file = (
        "# This is a comment\n"
        "# The next line says : leave 4 blank lines\n"
        ".blank 2\n"
        "\n"
        "..Executive Story Editor\n"
        "MARCEL DURAND\n"
        "\n"
        ".blank 2\n"
        "\n"
        "..Associate Producers\n"
        "MARTIN MARCEL\n"
        "DIDIER MARTIN\n"
        "\n"
        "..Music Supervisor\n"
        "JEAN DIDIER\n"
    )

    file_location = os.path.join(util.TMP_DIR, "credits.txt")
    vid_location = os.path.join(util.TMP_DIR, "credits.mp4")
    with open(file_location, "w") as file:
        file.write(credit_file)

    image = CreditsClip(
        file_location, 600, gap=100, stroke_color="blue", stroke_width=5, font=util.FONT
    )
    image = image.with_duration(3)
    image.write_videofile(vid_location, fps=24, logger=None)
    assert image.mask
    assert os.path.isfile(vid_location)


def test_detect_scenes():
    """Test that a cut is detected between concatenated red and green clips."""
    red = ColorClip((640, 480), color=(255, 0, 0)).with_duration(1)
    green = ColorClip((640, 480), color=(0, 200, 0)).with_duration(1)
    video = concatenate_videoclips([red, green])

    cuts, luminosities = detect_scenes(video, fps=10, logger=None)

    assert len(cuts) == 2


def test_find_video_period():
    clip = (
        VideoFileClip("media/chaplin.mp4")
        .subclipped(0, 0.5)
        .with_effects([vfx.Loop(2)])
    )  # fps=25

    # you need to increase the fps to get correct results
    assert round(find_video_period(clip, fps=70), 6) == 0.5


@pytest.mark.parametrize(
    ("bitmap", "distance_threshold", "max_duration", "expected_matches"),
    (
        pytest.param(
            [
                ["RRR", "GGG", "BBB"],
                ["WWW", "WWW", "WWW"],
                ["WWW", "WWW", "WWW"],
                ["WWW", "WWW", "WWW"],
                ["RRR", "GGG", "BBB"],
                ["RRR", "GGG", "BBB"],
                ["WWW", "WWW", "WWW"],
                ["RRR", "GGG", "BBB"],
                ["WWW", "WWW", "WWW"],
            ],
            1,
            math.inf,
            [
                (1, 2, 0, 0),
                (1, 3, 0, 0),
                (2, 3, 0, 0),
                (0, 4, 0, 0),
                (0, 5, 0, 0),
                (4, 5, 0, 0),
                (1, 6, 0, 0),
                (2, 6, 0, 0),
                (3, 6, 0, 0),
                (0, 7, 0, 0),
                (4, 7, 0, 0),
                (5, 7, 0, 0),
                (1, 8, 0, 0),
                (2, 8, 0, 0),
                (3, 8, 0, 0),
                (6, 8, 0, 0),
            ],
            id="distance_threshold=1-max_duration=math.inf",
        ),
        pytest.param(
            [
                ["RRR", "GGG", "BBB"],
                ["WWW", "WWW", "WWW"],
                ["WWW", "WWW", "WWW"],
                ["WWW", "WWW", "WWW"],
                ["RRR", "GGG", "BBB"],
                ["RRR", "GGG", "BBB"],
                ["WWW", "WWW", "WWW"],
                ["RRR", "GGG", "BBB"],
                ["WWW", "WWW", "WWW"],
            ],
            1,
            2,
            [
                (1, 2, 0, 0),
                (1, 3, 0, 0),
                (2, 3, 0, 0),
                (4, 5, 0, 0),
                (5, 7, 0, 0),
                (6, 8, 0, 0),
            ],
            id="distance_threshold=1-max_duration=2",
        ),
        pytest.param(
            [
                ["RRR", "GGG", "BBB"],
                ["RRR", "GGG", "BBR"],
                ["RRR", "GGG", "BBB"],
                ["RRR", "GGG", "BRR"],
            ],
            70,
            2,
            [
                (0, 2, 0, 0),
                (0, 1, 69.4022, 69.4022),
                (1, 2, 69.4022, 69.4022),
                (1, 3, 69.4022, 69.4022),
            ],
            id="distance_threshold=70-max_duration=2",
        ),
    ),
)
def test_FramesMatches_from_clip(
    bitmap,
    expected_matches,
    distance_threshold,
    max_duration,
):
    clip = BitmapClip(bitmap, fps=1)

    matching_frames = FramesMatches.from_clip(
        clip,
        distance_threshold,
        max_duration,
        logger=None,
    )

    assert matching_frames
    assert isinstance(matching_frames, FramesMatches)
    assert isinstance(matching_frames[0], FramesMatch)

    for i, match in enumerate(matching_frames):
        for j, n in enumerate(match):
            assert round(n, 4) == expected_matches[i][j]


def test_FramesMatches_filter():
    input_matching_frames = [
        FramesMatch(1, 2, 0, 0),
        FramesMatch(1, 2, 0.8, 0.8),
        FramesMatch(1, 2, 0.8, 0),
    ]
    expected_matching_frames = [FramesMatch(1, 2, 0, 0)]
    matching_frames_filter = lambda x: not x.min_distance and not x.max_distance

    matching_frames = FramesMatches(input_matching_frames).filter(
        matching_frames_filter
    )

    assert len(matching_frames) == len(expected_matching_frames)
    for i, frames_match in enumerate(matching_frames):
        assert frames_match == expected_matching_frames[i]


def test_FramesMatches_save_load(util):
    input_matching_frames = [
        FramesMatch(1, 2, 0, 0),
        FramesMatch(1, 2, 0.8, 0),
        FramesMatch(1, 2, 0.8, 0.8),
    ]
    expected_frames_matches_file_content = """1.000	2.000	0.000	0.000
1.000	2.000	0.800	0.000
1.000	2.000	0.800	0.800
"""

    outputfile = os.path.join(util.TMP_DIR, "moviepy_FramesMatches_save_load.txt")

    # save
    FramesMatches(input_matching_frames).save(outputfile)

    with open(outputfile, "r") as f:
        assert f.read() == expected_frames_matches_file_content

    # load
    for i, frames_match in enumerate(FramesMatches.load(outputfile)):
        assert frames_match == input_matching_frames[i]


@pytest.mark.parametrize(
    ("n", "percent", "expected_result"),
    (
        pytest.param(1, None, FramesMatch(1, 2, 0, 0), id="n=1"),
        pytest.param(
            2,
            None,
            FramesMatches([FramesMatch(1, 2, 0, 0), FramesMatch(2, 3, 0, 0)]),
            id="n=2",
        ),
        pytest.param(
            1,
            50,
            FramesMatches([FramesMatch(1, 2, 0, 0), FramesMatch(2, 3, 0, 0)]),
            id="percent=50",
        ),
    ),
)
def test_FramesMatches_best(n, percent, expected_result):
    assert (
        FramesMatches(
            [
                FramesMatch(1, 2, 0, 0),
                FramesMatch(2, 3, 0, 0),
                FramesMatch(4, 5, 0, 0),
                FramesMatch(5, 6, 0, 0),
            ]
        ).best(n=n, percent=percent)
        == expected_result
    )


@pytest.mark.parametrize(
    (
        "filename",
        "subclip",
        "match_threshold",
        "min_time_span",
        "nomatch_threshold",
        "expected_result",
    ),
    (
        pytest.param(
            "media/chaplin.mp4",
            (1, 3),
            1,
            2,
            0,
            FramesMatches(
                [
                    FramesMatch(0.52, 3.44, 0, 0),
                    FramesMatch(0.6400, 3.3200, 0.0000, 0.0000),
                    FramesMatch(0.7600, 3.2000, 0.0000, 0.0000),
                    FramesMatch(0.9200, 3.0400, 0.0000, 0.0000),
                ]
            ),
            id="(media/chaplin.mp4)(1, 3).fx(time_mirror)",
        ),
    ),
)
def test_FramesMatches_select_scenes(
    filename,
    subclip,
    match_threshold,
    min_time_span,
    nomatch_threshold,
    expected_result,
):
    video_clip = VideoFileClip(filename)
    if subclip is not None:
        video_clip = video_clip.subclipped(subclip[0], subclip[1])
    clip = concatenate_videoclips(
        [video_clip.with_effects([vfx.TimeMirror()]), video_clip]
    )
    result = FramesMatches.from_clip(clip, 10, 3, logger=None).select_scenes(
        match_threshold,
        min_time_span,
        nomatch_threshold=nomatch_threshold,
    )

    assert len(result) == len(expected_result)
    assert result == expected_result


@pytest.mark.skip
def test_FramesMatches_write_gifs(util):
    video_clip = VideoFileClip("media/chaplin.mp4").subclipped(0, 0.2)
    clip = concatenate_videoclips(
        [video_clip.with_effects([vfx.TimeMirror()]), video_clip]
    )

    # add matching frame starting at start < clip.start which should be ignored
    matching_frames = FramesMatches.from_clip(clip, 10, 3, logger=None)
    matching_frames.insert(0, FramesMatch(-1, -0.5, 0, 0))
    matching_frames = matching_frames.select_scenes(
        1,
        0.01,
        nomatch_threshold=0,
    )

    gifs_dir = os.path.join(util.TMP_DIR, "moviepy_FramesMatches_write_gifs")
    if os.path.isdir(gifs_dir):
        shutil.rmtree(gifs_dir)
    os.mkdir(gifs_dir)
    assert os.path.isdir(gifs_dir)

    matching_frames.write_gifs(clip, gifs_dir, logger=None)

    gifs_filenames = os.listdir(gifs_dir)
    assert len(gifs_filenames) == 7

    for filename in gifs_filenames:
        filepath = os.path.join(gifs_dir, filename)
        assert os.path.isfile(filepath)

        with open(filepath, "rb") as f:
            assert len(f.readline())

        end, start = filename.split(".")[0].split("_")
        end, start = (int(end), int(start))
        assert isinstance(end, int)
        assert isinstance(end, int)

    try:
        shutil.rmtree(gifs_dir)
    except PermissionError:
        pass


@pytest.mark.parametrize(
    (
        "size",
        "p1",
        "p2",
        "vector",
        "radius",
        "color_1",
        "color_2",
        "shape",
        "offset",
        "expected_result",
    ),
    (
        pytest.param(
            (6, 1),
            (1, 1),
            (5, 1),
            None,
            None,
            0,
            1,
            "linear",
            0,
            np.array([[1.0, 1.0, 0.75, 0.5, 0.25, 0.0]]),
            id="p1-p2-linear-color_1=0-color_2=1",
        ),
        pytest.param(
            (6, 1),
            (1, 1),
            None,
            (4, 0),
            None,
            0,
            1,
            "linear",
            0,
            np.array([[1.0, 1.0, 0.75, 0.5, 0.25, 0.0]]),
            id="p1-vector-linear-color_1=0-color_2=1",
        ),
        pytest.param(
            (6, 1),
            (1, 1),
            (5, 1),
            None,
            None,
            (255, 0, 0),
            (0, 255, 0),
            "linear",
            0,
            np.array(
                [
                    [
                        [
                            0,
                            255,
                            0,
                        ],
                        [
                            0,
                            255,
                            0,
                        ],
                        [
                            63.75,
                            191.25,
                            0,
                        ],
                        [
                            127.5,
                            127.5,
                            0,
                        ],
                        [
                            191.25,
                            63.75,
                            0,
                        ],
                        [
                            255,
                            0,
                            0,
                        ],
                    ]
                ]
            ),
            id="p1-p2-linear-color_1=R-color_2=G",
        ),
        pytest.param(
            (3, 1),
            (1, 1),
            (5, 1),
            None,
            None,
            0,
            1,
            "bilinear",
            0,
            np.array([[0.75, 1, 0.75]]),
            id="p1-p2-bilinear-color_1=0-color_2=1",
        ),
        pytest.param(
            (5, 1),
            (1, 1),
            (3, 1),
            None,
            None,
            0,
            1,
            "bilinear",
            0,
            np.array([[0.5, 1.0, 0.5, 0.0, 0.0]]),
            id="p1-p2-bilinear-color_1=0-color_2=1",
        ),
        pytest.param(
            (5, 1),
            (1, 1),
            None,
            [2, 0],
            None,
            0,
            1,
            "bilinear",
            0,
            np.array([[0.5, 1.0, 0.5, 0.0, 0.0]]),
            id="p1-vector-bilinear-color_1=0-color_2=1",
        ),
        pytest.param(
            (5, 1),
            (1, 1),
            None,
            [2, 0],
            None,
            (255, 0, 0),
            (0, 255, 0),
            "bilinear",
            0,
            np.array(
                [
                    [
                        [127.5, 127.5, 0],
                        [0, 255, 0],
                        [127.5, 127.5, 0],
                        [255, 0, 0],
                        [255, 0, 0],
                    ]
                ]
            ),
            id="p1-vector-bilinear-color_1=R-color_2=G",
        ),
        pytest.param(
            (5, 1),
            (1, 1),
            None,
            None,
            None,
            0,
            1,
            "bilinear",
            0,
            (ValueError, "You must provide either 'p2' or 'vector'"),
            id="p2=None-vector=None-bilinear-ValueError",
        ),
        pytest.param(
            (5, 1),
            (1, 1),
            None,
            None,
            None,
            0,
            1,
            "linear",
            0,
            (ValueError, "You must provide either 'p2' or 'vector'"),
            id="p2=None-vector=None-linear-ValueError",
        ),
        pytest.param(
            (5, 1),
            (1, 1),
            None,
            None,
            None,
            0,
            1,
            "invalid",
            0,
            (
                ValueError,
                "Invalid shape, should be either 'radial', 'linear' or 'bilinear'",
            ),
            id="shape=invalid-ValueError",
        ),
        pytest.param(
            (5, 5),
            (1, 1),
            None,
            None,
            1,
            0,
            1,
            "radial",
            0,
            np.array(
                [
                    [1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                ]
            ),
            id="p1-radial-radius=1-color_1=0-color_2=1",
        ),
        pytest.param(
            (5, 5),
            (1, 1),
            None,
            None,
            1,
            (255, 0, 0),
            (0, 255, 0),
            "radial",
            0,
            np.array(
                [
                    [[0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]],
                    [[0, 255, 0], [255, 0, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]],
                    [[0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]],
                    [[0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]],
                    [[0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]],
                ]
            ),
            id="p1-radial-radius=1-color_1=R-color_2=G",
        ),
        pytest.param(
            (5, 5),
            (3, 3),
            None,
            None,
            0,
            0,
            1,
            "radial",
            0,
            np.array(
                [
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                ]
            ),
            id="p1-radial-radius=0-color_1=0-color_2=1",
        ),
    ),
)
def test_color_gradient(
    size,
    p1,
    p2,
    vector,
    radius,
    color_1,
    color_2,
    shape,
    offset,
    expected_result,
):
    if isinstance(expected_result, np.ndarray):
        result = color_gradient(
            size,
            p1,
            p2=p2,
            vector=vector,
            radius=radius,
            color_1=color_1,
            color_2=color_2,
            shape=shape,
            offset=offset,
        )

        assert expected_result.shape == result.shape
        assert np.array_equal(result, expected_result)

        if shape == "radial":
            circle_result = circle(
                size,
                p1,
                radius,
                color=color_1,
                bg_color=color_2,
            )
            assert np.array_equal(result, circle_result)
    else:
        if isinstance(expected_result, (list, tuple)):
            expected_error, expected_message = expected_result
        else:
            expected_error, expected_message = (expected_result, None)

        with pytest.raises(expected_error) as exc:
            color_gradient(
                size,
                p1,
                p2=p2,
                vector=vector,
                radius=radius,
                color_1=color_1,
                color_2=color_2,
                shape=shape,
                offset=offset,
            )
        if expected_message is not None:
            assert str(exc.value) == expected_message


@pytest.mark.parametrize(
    (
        "size",
        "x",
        "y",
        "p1",
        "p2",
        "vector",
        "color_1",
        "color_2",
        "gradient_width",
        "expected_result",
    ),
    (
        pytest.param(
            (3, 4),
            1,
            None,
            None,
            None,
            None,
            (255, 0, 0),
            (0, 255, 0),
            0,
            np.array(
                [
                    [[255, 0, 0], [0, 255, 0], [0, 255, 0]],
                    [[255, 0, 0], [0, 255, 0], [0, 255, 0]],
                    [[255, 0, 0], [0, 255, 0], [0, 255, 0]],
                    [[255, 0, 0], [0, 255, 0], [0, 255, 0]],
                ]
            ),
            id="x=1-color_1=R-color_2=G",
        ),
        pytest.param(
            (3, 4),
            1,
            None,
            None,
            None,
            None,
            0,
            1,
            0,
            np.array([[0, 1, 1], [0, 1, 1], [0, 1, 1], [0, 1, 1]]),
            id="x=1-color_1=0-color_2=1",
        ),
        pytest.param(
            (2, 2),
            None,
            1,
            None,
            None,
            None,
            (255, 0, 0),
            (0, 255, 0),
            0,
            np.array([[[255, 0, 0], [255, 0, 0]], [[0, 255, 0], [0, 255, 0]]]),
            id="y=1-color_1=R-color_2=G",
        ),
        pytest.param(
            (2, 2),
            None,
            1,
            None,
            None,
            None,
            0,
            1,
            0,
            np.array([[0, 0], [1, 1]]),
            id="y=1-color_1=0-color_2=1",
        ),
        pytest.param(
            (3, 2),
            2,
            None,
            None,
            None,
            None,
            0,
            1,
            1,
            np.array([[0, 0, 1], [0, 0, 1]]),
            id="x=2-color_1=0-color_2=1-gradient_width=1",
        ),
        pytest.param(
            (2, 3),
            None,
            2,
            None,
            None,
            None,
            0,
            1,
            1,
            np.array([[0, 0], [0, 0], [1, 1]]),
            id="y=2-color_1=0-color_2=1-gradient_width=1",
        ),
        pytest.param(
            (3, 3),
            None,
            None,
            (0, 1),
            (0, 0),
            None,
            0,
            0.75,
            3,
            np.array([[0.75, 0.75, 0.75], [0.75, 0.75, 0.75], [0.75, 0.75, 0.75]]),
            id="p1-p2-color_1=0-color_2=0.75-gradient_width=3",
        ),
    ),
)
def test_color_split(
    size,
    x,
    y,
    p1,
    p2,
    vector,
    color_1,
    color_2,
    gradient_width,
    expected_result,
):
    result = color_split(
        size,
        x=x,
        y=y,
        p1=p1,
        p2=p2,
        vector=vector,
        color_1=color_1,
        color_2=color_2,
        gradient_width=gradient_width,
    )

    assert np.array_equal(result, expected_result)


@pytest.mark.parametrize(
    ("ttss", "tt", "ss", "left", "right", "interpolation_results"),
    (
        pytest.param(
            [[0, 3], [1, 4], [2, 5]],
            None,
            None,
            -1,
            6,
            {
                3: 6,
                4: 6,  # right
                -1: -1,
                -2: -1,  # left
                1: 4,
                2: 5,  # values
            },
            id="ttss",
        ),
        pytest.param(
            None,
            [0, 1, 2],
            [3, 4, 5],
            -1,
            39,
            {
                3: 39,
                4: 39,  # right
                -1: -1,
                -2: -1,  # left
                1: 4,
                2: 5,  # values
            },
            id="tt-ss",
        ),
    ),
)
def test_Interpolator(ttss, tt, ss, left, right, interpolation_results):
    interpolator = Interpolator(ttss=ttss, tt=tt, ss=ss, left=left, right=right)
    for value, expected_result in interpolation_results.items():
        assert interpolator(value) == expected_result


@pytest.mark.parametrize(
    ("tt", "xx", "yy", "interpolation_results"),
    (
        pytest.param(
            [0, 1, 2],
            [0, 2, 3],
            [0, 2, 3],
            {0.5: [1, 1], 1: [2, 2], 4: [3, 3], -1: [0, 0]},
            id="simple",
        ),
        pytest.param(
            [0, 1, 2],
            [0, -5, -3],
            [-2, 2, -5],
            {0.5: [-2.5, 0], 1: [-5, 2], 4: [-3, -5], -1: [0, -2]},
            id="negative",
        ),
    ),
)
def test_Trajectory(tt, xx, yy, interpolation_results):
    trajectory = Trajectory(tt, xx, yy)
    for value, expected_result in interpolation_results.items():
        assert np.array_equal(trajectory(value), np.array(expected_result))


def test_Trajectory_addx():
    trajectory = Trajectory([0, 1], [0], [0, 1]).addx(1)
    assert len(trajectory.xx) == 1
    assert trajectory.xx[0] == 1


def test_Trajectory_addy():
    trajectory = Trajectory([0, 1], [0], [0, 1]).addy(1)
    assert len(trajectory.yy) == 2
    assert trajectory.yy[0] == 1
    assert trajectory.yy[1] == 2


def test_Trajectory_from_to_file(util):
    filename = os.path.join(util.TMP_DIR, "moviepy_Trajectory_from_to_file.txt")
    if os.path.isfile(filename):
        try:
            os.remove(filename)
        except PermissionError:
            pass

    trajectory_file_content = """# t(ms)	x	y
0	554	100
166	474	90
333	384	91
"""

    with open(filename, "w") as f:
        f.write(trajectory_file_content)

    trajectory = Trajectory.from_file(filename)

    assert np.array_equal(trajectory.xx, np.array([554, 474, 384]))
    assert np.array_equal(trajectory.yy, np.array([100, 90, 91]))
    assert np.array_equal(trajectory.tt, np.array([0, 0.166, 0.333]))

    trajectory.to_file(filename)

    with open(filename, "r") as f:
        assert f.read() == "\n".join(trajectory_file_content.split("\n")[1:])


@pytest.mark.parametrize(
    ("clip", "filetype", "fps", "maxduration", "t", "expected_error"),
    (
        pytest.param(
            AudioClip(
                lambda t: np.array(
                    [np.sin(440 * 2 * np.pi * t), np.sin(220 * 2 * np.pi * t)]
                ).T.copy(order="C"),
                duration=0.2,
                fps=44100,
            ),
            None,
            None,
            None,
            None,
            None,
            id="AudioClip",
        ),
        pytest.param(
            VideoFileClip("media/bitmap.mp4"),
            None,
            None,
            None,
            None,
            None,
            id="VideoFileClip",
        ),
        pytest.param(
            BitmapClip([["RR", "RR"], ["GG", "GG"]], duration=0.25),
            None,
            4,
            None,
            None,
            None,
            id="BitmapClip",
        ),
        pytest.param(
            ImageClip("media/python_logo.png"),
            None,
            None,
            None,
            None,
            None,
            id="ImageClip(.png)",
        ),
        pytest.param(
            ImageClip(os.path.join("media", "pigs_in_a_polka.gif")),
            None,
            None,
            None,
            None,
            None,
            id="ImageClip(.gif)",
        ),
        pytest.param(
            os.path.join("media", "pigs_in_a_polka.gif"),
            None,
            None,
            None,
            None,
            None,
            id="filename(.gif)",
        ),
        pytest.param(
            os.path.join("media", "vacation_2017.jpg"),
            None,
            None,
            None,
            None,
            None,
            id="filename(.jpg)",
        ),
        pytest.param(
            os.path.join("{tempdir}", "moviepy_ipython_display.foo"),
            None,  # unknown filetype
            None,
            None,
            None,
            (ValueError, "No file type is known for the provided file."),
            id="filename(.foo)",
        ),
        pytest.param(
            os.path.join("{tempdir}", "moviepy_ipython_display.foo"),
            "video",  # unsupported filetype for '.foo' extension
            None,
            None,
            None,
            (
                ValueError,
                "This video extension cannot be displayed in the IPython Notebook.",
            ),
            id="filename(.foo)[filetype=video]",
        ),
        pytest.param(
            VideoFileClip("media/bitmap.mp4"),
            "video",
            None,
            0,
            None,
            (
                ValueError,
                "You can increase 'maxduration', by passing 'maxduration'",
            ),
            id="VideoFileClip(.mp4)[filetype=video, maxduration > clip.duration]",
        ),
        pytest.param(
            type("FakeClip", (), {})(),
            None,
            None,
            None,
            None,
            (ValueError, "Unknown class for the clip. Cannot embed and preview"),
            id="FakeClip",
        ),
        pytest.param(
            VideoFileClip("media/chaplin.mp4").subclipped(0, 1),
            None,
            None,
            None,
            0.5,
            None,
            id="VideoFileClip(.mp4)[filetype=video, t=0.5]",
        ),
        pytest.param(
            ImageClip("media/pigs_in_a_polka.gif"),
            None,
            None,
            None,
            0.2,
            None,
            id="ImageClip(.gif)[t=0.2]",
        ),
    ),
)
def test_ipython_display(
    util, clip, filetype, fps, maxduration, t, expected_error, monkeypatch
):
    # TODO: fix ipython tests
    pass


@pytest.mark.skipif(
    ipython_available,
    reason="ipython must not be installed in order to run this test",
)
def test_ipython_display_not_available():
    # TODO: fix ipython tests
    pass


@pytest.mark.parametrize("wave_type", ("mono", "stereo"))
def test_find_audio_period(mono_wave, stereo_wave, wave_type):
    if wave_type == "mono":
        wave1 = mono_wave(freq=400)
        wave2 = mono_wave(freq=100)
    else:
        wave1 = stereo_wave(left_freq=400, right_freq=220)
        wave2 = stereo_wave(left_freq=100, right_freq=200)
    clip = CompositeAudioClip(
        [
            AudioClip(frame_function=wave1, duration=0.3, fps=22050),
            AudioClip(frame_function=wave2, duration=0.3, fps=22050).with_effects(
                [afx.MultiplyVolume(0, end_time=0.1)]
            ),
        ]
    )

    loop_clip = clip.with_effects([vfx.Loop(4)])
    assert round(find_audio_period(loop_clip), 6) == pytest.approx(0.29932, 0.1)


if __name__ == "__main__":
    pytest.main()
````

## File: .gitignore
````
# Partially based on
# https://github.com/github/gitignore/blob/main/Python.gitignore

# OS-specific
.DS_Store

# IDEs
.idea
.project
.pydevproject
.sublime-project
.vscode

# Python dev tooling
.mr.developer.cfg
.python-version

# Cache, temp. files
__pycache__/
.cache/
*.py[cod]
*~

# C extensions
*.so

# Distribution / packaging
build/
develop-eggs/
dist/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# System misc.
bin
*.tar.gz

# Installer logs
pip-log.txt

# Unit test / coverage reports
.tox/
.coverage
nosetests.xml

# Media files for testing
tests/media/

# Translations
*.mo

# Documentation
docs/build/

# Publishing
.pypirc
````

## File: .pre-commit-config.yaml
````yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black
        language_version: python3
        files: \.py$
  - repo: https://github.com/PyCQA/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args:
          - '--filter-files'
        files: \.py$
  - repo: https://github.com/PyCQA/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        additional_dependencies:
          - flake8-absolute-import>=1.0
          - flake8-docstrings>=1.7.0
          - flake8-rst-docstrings>=0.3
          - flake8-implicit-str-concat==0.4.0
        args:
          - --ignore=E501 # Black will force a line length of 88 when possible
        name: flake8-test
        files: \.py$
````

## File: .readthedocs.yml
````yaml
# .readthedocs.yml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Build documentation in the docs/ directory with Sphinx
sphinx:
  configuration: docs/conf.py

# Build documentation with MkDocs
#mkdocs:
#  configuration: mkdocs.yml

# Optionally set the version of Python and requirements required to build your docs
python:
  version: 3.7
  install:
      - method: pip
        path: .
        extra_requirements:
           - doc
````

## File: appveyor.yml
````yaml
build: off

test_script:
- true
````

## File: CHANGELOG.md
````markdown
# Changelog

All notable changes to this project will be documented in this file.

The format from v2.0.0 onwards is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/zulko/moviepy/tree/master)

### Important Announcements
For performances reason a very minor change to the API of CompositeVideoClip have been made, setting the default background color as rgb (0, 0, 0), instead of previous None.
This mean you need to specifically set `bg_color=None` if you want to generate a video with a transparent background.

### Fixed
- Strongly improve performances to make them more consistent with thoses of v1
- Fix circular reference in ImageSequenceClip leading to memory leak
- Fix TextClip broken with Pillow > 11.2
- `pixel_format` parameter was ignored when calling ffmpeg writer, as referenced in PR #2359
- Fix incorrect handling of lines with a format different from "key: value" during FFmpeg infos parsing (see #2311, #1860, #2418, #2470)

### Added
- Possibility to select audio track when reading a file (#2429)

### Changed 
- Rewrite FFmpegInfosParser to use indentation and block extractions instead of a state machine (PR #2470)

## v2.2.1

### Fixed
Pillow mitigations (try/except for newer versions of pillow).

## v2.2

[Full Changelog](https://github.com/zulko/moviepy/compare/v2.0.0.dev2...HEAD)

### Important Announcements

### Added <!-- for new features -->
- Add support for flac codec
- Add codecs to .mov files
- Add background radius to text clips
- Support pillow 11
- Add support for Pillow default font on textclip
- Add support for ffmpeg v7

### Changed <!-- for changes in existing functionality -->
- Subclipping outside of clip boundaries now raise an exception
- Freeze effect no longer remove start and end
- Add a parameter to define audio codec of a clip

### Deprecated <!-- for soon-to-be removed features -->

### Removed <!-- for now removed features -->

### Fixed <!-- for any bug fixes -->
- Fix ffmpeg reading crash when invalid metadata (see pr #2311)
- Fix GPU h264_nvenc encoding not working.
- Improve perfs of decorator by pre-computing arguments
- Fix textclip being cut or of impredictable height (see issues #2325, #2260 and #2268)
- TextClip now properly breaklines on text without spaces, such as chinese (see #2260)
- Fix TimeMirror and TimeSymmetrize cutting last second of clip
- ImageSequenceClip was wrong when calculating fps with duration and no fps (see issue #2351)
- More consistent frame seek (see issue #2115 and PR #2117)
- Fix audiopreview not working with ffplay >= 7.0.0
- Fix ffmpeg_reader not selecting a default stream (see PR #2114) 

## [v2.1.2](https://github.com/zulko/moviepy/tree/master)

[Full Changelog](https://github.com/zulko/moviepy/compare/v2.1.2...HEAD)

### Important Announcements

Compositing and rendering of video with transparency was bugged for a long long time (probably since start of the project), if you had encountered any issue with transparency in the past we strongly suggest you to try this new release.

### Added <!-- for new features -->
- Add codec extraction during ffmpeg meta parsing if available

### Changed <!-- for changes in existing functionality -->

### Deprecated <!-- for soon-to-be removed features -->

### Removed <!-- for now removed features -->

### Fixed <!-- for any bug fixes -->
- Massive refactor and fixing of ffmpeg reader and writer for transparency support, all transparency was actually buggy, both during rendering and reading. 
- Complete refactor of CompositeVideoClip compositing to properly support tranparency with CompositeVideoClip including one or more CompositeVideoClip, and transparency in general who was completly buggy (just so many issue related, for more info take a look at pr #2307)
- Fix issue #2305: Change stroke_width from float 0.5 to int 1
- Fix issue #2160 where filenames starting with `-` crashed file saving
- Fix issue #2247 with default mask erronous size of 1 by 1




## [v2.0.0.dev2](https://github.com/zulko/moviepy/tree/v2.0.0.dev2) (2020-10-05)

[Full Changelog](https://github.com/zulko/moviepy/compare/v2.0.0.dev1...v2.0.0.dev2)

There are still no major breaking changes compared to v1.0.3. Expect them to come in the next dev update.
Any new changes made to the master branch will now be instantly reflected at https://moviepy.readthedocs.io, which is where documentation for all versions will be in the future. [\#1328](https://github.com/Zulko/moviepy/pull/1328)
Install with `pip install moviepy --pre --upgrade`.

### Added <!-- for new features -->
- New `pix_fmt` parameter in `VideoFileClip`, `VideoClip.write_videofile()`, `VideoClip.write_gif()` that allows passing a custom `pix_fmt` parameter such as `"bgr24"` to FFmpeg [\#1237](https://github.com/Zulko/moviepy/pull/1237)
- New `change_duration` parameter in `Clip.set_fps()` that allows changing the video speed to match the new fps [\#1329](https://github.com/Zulko/moviepy/pull/1329)

### Changed <!-- for changes in existing functionality -->
- `ffmpeg_parse_infos()` and `VideoFileClip` now have optional `decode_file` parameter that ensures that the detected duration is correct, but may take a long time to run [\#1063](https://github.com/Zulko/moviepy/pull/1063), [\#1222](https://github.com/Zulko/moviepy/pull/1222)
- `ffmpeg_parse_infos()` and `VideoFileClip` now use `fps` metadata instead of `tbr` to detect a video's fps value [\#1222](https://github.com/Zulko/moviepy/pull/1222)
- `FFMPEG_AudioReader.close_proc()` -> `FFMPEG_AudioReader.close()` for consistency with `FFMPEG_VideoReader` [\#1220](https://github.com/Zulko/moviepy/pull/1220)

### Fixed <!-- for any bug fixes -->
- Fixed `ffmpeg_tools.ffmpeg_extract_subclip` creating clips with incorrect duration metadata [\#1317](https://github.com/Zulko/moviepy/pull/1317)
- `OSError: MoviePy error: failed to read the first frame of video file...` would occasionally occur for no reason [\#1220](https://github.com/Zulko/moviepy/pull/1220)
- Fixed warnings being suppressed [\#1191](https://github.com/Zulko/moviepy/pull/1191)
- Fixed `UnicodeDecodeError` crash when file metadata contained non-UTF8 characters [\#959](https://github.com/Zulko/moviepy/pull/959)


## [v2.0.0.dev1](https://github.com/zulko/moviepy/tree/v2.0.0.dev1) (2020-06-04)

[Full Changelog](https://github.com/zulko/moviepy/compare/v1.0.3...v2.0.0.dev1)

This development version introduces many bug-fixes and changes. Please note that there may be large backwards-incompatible changes between dev versions! 
The online documentation has not been updated to reflect the changes in the v2.0.0 branch, so for help on how to use the new features please refer to the docstrings in the source code.
Install with `pip install moviepy --pre --upgrade`.

### Important Announcements
- Support removed for Python versions 2.7, 3.4 & 3.5 [\#1103](https://github.com/Zulko/moviepy/pull/1103), [\#1106](https://github.com/Zulko/moviepy/pull/1106)
- If you were previously setting custom locations for FFmpeg or ImageMagick in ``config_defaults.py`` and MoviePy still cannot autodetect the binaries, you will need to switch to the new method using enviroment variables. [\#1109](https://github.com/Zulko/moviepy/pull/1109)
- All previously deprecated methods and parameters have been removed [\#1115](https://github.com/Zulko/moviepy/pull/1115)

### Added <!-- for new features -->
- BitmapClip allows creating of custom frames using strings of letters
- Clips can now be tested for equality with other clips using `==`. This checks whether every frame of the two clips are identical
- Support for path-like objects as an option wherever filenames are passed in as arguments [\#1137](https://github.com/Zulko/moviepy/pull/1137)
- Autodetect ImageMagick executable on Windows [\#1109](https://github.com/Zulko/moviepy/pull/1109)
- Optionally configure paths to FFmpeg and ImageMagick binaries with environment variables or a ``.env`` file [\#1109](https://github.com/Zulko/moviepy/pull/1109)
- Optional `encoding` parameter in `SubtitlesClip` [\#1043](https://github.com/Zulko/moviepy/pull/1043)
- Added new `ffmpeg_stabilize_video()` function in `ffmpeg_tools`
- Optional `temp_audiofile_path` parameter in `VideoClip.write_videofile()` to specify where the temporary audiofile should be created [\#1144](https://github.com/Zulko/moviepy/pull/1144)
- `VideoClip.set_layer()` to specify the layer of the clip for use when creating a `CompositeVideoClip` [\#1176](https://github.com/Zulko/moviepy/pull/1176)
- `ffmpeg_parse_infos` additionally returns `"video_bitrate"` and `"audio_bitrate"` values [\#930](https://github.com/Zulko/moviepy/pull/930)
- Access to the source video's bitrate in a `VideoFileClip` or `AudioFileClip` through `videoclip.reader.bitrate` and `audioclip.reader.bitrate` [\#930](https://github.com/Zulko/moviepy/pull/930)

### Changed <!-- for changes in existing functionality -->
- `vfx.scroll` arguments `w` and `h` have had their order swapped. The correct order is now `w, h` but it is preferable to explicitly use keyword arguments
- Removed extra `.` in the output file name of `ffmpeg_extract_subclip()` when `targetname` is not specified [\#939](https://github.com/Zulko/moviepy/pull/939)

### Removed <!-- for now removed features -->
- Support removed for Python versions 2.7, 3.4 & 3.5
- Setting paths to ImageMagick and FFMpeg binaries in ``config_defaults.py`` is no longer possible [\#1109](https://github.com/Zulko/moviepy/pull/1109)
- Removed ``config.get_setting()`` and ``config.change_settings()`` functions [\#1109](https://github.com/Zulko/moviepy/pull/1109)
- All previously deprecated methods and parameters [\#1115](https://github.com/Zulko/moviepy/pull/1115):
    - `AudioClip.to_audiofile()` -> use `AudioClip.write_audiofile()`
    - `VideoClip.to_videofile()` -> use `VideoClip.write_videofile()`
    - `VideoClip.to_images_sequence()` -> use `VideoClip.write_images_sequence()`
    - `concatenate()` -> use `concatenate_videoclips()`
    - `verbose` parameter in `AudioClip.write_audiofile()`, `ffmpeg_audiowriter()`, `VideoFileClip()`, `VideoClip.write_videofile()`, `VideoClip.write_images_sequence()`, `ffmpeg_write_video()`, `write_gif()`, `write_gif_with_tempfiles()`, `write_gif_with_image_io()` -> Instead of `verbose=False`, use `logger=None`
    - `verbose_print()` -> no replacement
    - `col` parameter in `ColorClip()` -> use `color`

### Fixed <!-- for any bug fixes -->
- When using `VideoClip.write_videofile()` with `write_logfile=True`, errors would not be properly reported [\#890](https://github.com/Zulko/moviepy/pull/890)
- `TextClip.list("color")` now returns a list of bytes, not strings [\#1119](https://github.com/Zulko/moviepy/pull/1119)
- `TextClip.search("colorname", "color")` does not crash with a TypeError [\#1119](https://github.com/Zulko/moviepy/pull/1119)
- `vfx.even_size` previously created clips with odd sizes [\#1124](https://github.com/Zulko/moviepy/pull/1124)
- `IndexError` in `vfx.freeze`, `vfx.time_mirror` and `vfx.time_symmetrize` [\#1124](https://github.com/Zulko/moviepy/pull/1124)
- Using `rotate()` with a `ColorClip` no longer crashes [\#1139](https://github.com/Zulko/moviepy/pull/1139)
- `AudioFileClip` would not generate audio identical to the original file [\#1108](https://github.com/Zulko/moviepy/pull/1108)
- Fixed `TypeError` when using `filename` instead of `txt` parameter in `TextClip` [\#1201](https://github.com/Zulko/moviepy/pull/1201)
- Several issues resulting from incorrect time values due to floating point errors [\#1195](https://github.com/Zulko/moviepy/pull/1195), for example:
    - Blank frames at the end of clips [\#210](https://github.com/Zulko/moviepy/pull/210)
    - Sometimes getting `IndexError: list index out of range` when using `concatenate_videoclips` [\#646](https://github.com/Zulko/moviepy/pull/646)
- Applying `resize` with a non-constant `newsize` to a clip with a mask would remove the mask [\#1200](https://github.com/Zulko/moviepy/pull/1200)
- Using `color_gradient()` would crash with `ValueError: The truth value of an array with more than one element is ambiguous` [\#1212](https://github.com/Zulko/moviepy/pull/1212)


## [v1.0.3](https://github.com/zulko/moviepy/tree/v1.0.3) (2020-05-07)

[Full Changelog](https://github.com/zulko/moviepy/compare/v1.0.2...v1.0.3)

Bonus release to fix critical error when working with audio: `AttributeError: 'NoneType' object has no attribute 'stdout'` [\#1185](https://github.com/Zulko/moviepy/pull/1185)


## [v1.0.2](https://github.com/zulko/moviepy/tree/v1.0.2) (2020-03-26)

[Full Changelog](https://github.com/zulko/moviepy/compare/v1.0.1...v1.0.2)

Note that this is likely to be the last release before v2.0, which will drop support for Python versions 2.7, 3.4 & 3.5 and will introduce other backwards-incompatible changes.

**Notable bug fixes:**

- Fixed bug that meant that some VideoFileClips were created without audio [\#968](https://github.com/Zulko/moviepy/pull/968)
- Fixed bug so now the `slide_out` effect works [\#795](https://github.com/Zulko/moviepy/pull/795)


**Fixed bugs:**

- Fixed potential crash trying to call the logger string as a function [\#1082](https://github.com/Zulko/moviepy/pull/1082) ([tburrows13](https://github.com/tburrows13))
- Get ffmpeg to use all audio streams [\#1008](https://github.com/Zulko/moviepy/pull/1008) ([vmaliaev](https://github.com/vmaliaev))
- Reorder FFMPEG\_VideoWriter command arguments [\#968](https://github.com/Zulko/moviepy/pull/968) ([ThePhonon](https://github.com/ThePhonon))
- Test that the temporary audio file exists [\#958](https://github.com/Zulko/moviepy/pull/958) ([ybenitezf](https://github.com/ybenitezf))
- Fix slide out [\#795](https://github.com/Zulko/moviepy/pull/795) ([knezi](https://github.com/knezi))
- Correct the error message to new filename. [\#1057](https://github.com/Zulko/moviepy/pull/1057) ([jwg4](https://github.com/jwg4))

**Merged pull requests:**

- Remove timer in stdout flushing test [\#1091](https://github.com/Zulko/moviepy/pull/1091) ([tburrows13](https://github.com/tburrows13))
- Update github issue and PR templates [\#1087](https://github.com/Zulko/moviepy/pull/1087) ([tburrows13](https://github.com/tburrows13))
- Clean up imports [\#1084](https://github.com/Zulko/moviepy/pull/1084) ([tburrows13](https://github.com/tburrows13))
- refactor Pythonic sake [\#1077](https://github.com/Zulko/moviepy/pull/1077) ([mgaitan](https://github.com/mgaitan))
- Upgrade pip by calling via python \(in appveyor\). [\#1067](https://github.com/Zulko/moviepy/pull/1067) ([jwg4](https://github.com/jwg4))
- Improve afx.audio\_normalize documentation [\#1046](https://github.com/Zulko/moviepy/pull/1046) ([dspinellis](https://github.com/dspinellis))
- Add Travis support for Python 3.7 and 3.8 [\#1018](https://github.com/Zulko/moviepy/pull/1018) ([tburrows13](https://github.com/tburrows13))
- Hide pygame support prompt [\#1017](https://github.com/Zulko/moviepy/pull/1017) ([tburrows13](https://github.com/tburrows13))

**Closed issues:**

- ImageSequenceClip   write\_videofile [\#1098](https://github.com/Zulko/moviepy/issues/1098)
- Formatting code with Black [\#1097](https://github.com/Zulko/moviepy/issues/1097)
- Make effects be callable classes [\#1096](https://github.com/Zulko/moviepy/issues/1096)
- URGENT - Documentation is inaccessible [\#1086](https://github.com/Zulko/moviepy/issues/1086)
- Drop support for python \< 3.6 [\#1081](https://github.com/Zulko/moviepy/issues/1081)
- TextClip filenotfounderror winerror2 [\#1080](https://github.com/Zulko/moviepy/issues/1080)
- unable to create video from images [\#1074](https://github.com/Zulko/moviepy/issues/1074)
- Crash on loading the video, windows 10 [\#1071](https://github.com/Zulko/moviepy/issues/1071)
- Audio Issue while concatenate\_videoclips'ing ImageClip and VideoFileClip \(contains audio already\) [\#1064](https://github.com/Zulko/moviepy/issues/1064)
- AttributeError: 'NoneType' object has no attribute 'stdout' [\#1054](https://github.com/Zulko/moviepy/issues/1054)
- Overlay a video on top of an image with Moviepy [\#1053](https://github.com/Zulko/moviepy/issues/1053)
- get\_frame fails if not an early frame [\#1052](https://github.com/Zulko/moviepy/issues/1052)
- from google.colab import drive drive.mount\('/content/drive'\)  import cv2 import numpy as np from skimage import morphology from IPython import display import PIL  image = cv2.imread\('/content/drive/My Drive/CAR3/11.JPG',cv2.IMREAD\_COLOR\)  from google.colab.patches import cv2\_imshow  \#image = cv2.resize\(image,\(384,192\)\)  cv2\_imshow\(image\) [\#1051](https://github.com/Zulko/moviepy/issues/1051)
- Segmentation fault \(core dumped\) [\#1048](https://github.com/Zulko/moviepy/issues/1048)
- zip over two iter\_frames functions doesn't render proper result [\#1047](https://github.com/Zulko/moviepy/issues/1047)
- CompositeVideoClip\(\[xxx\]\).rotate\(90\)  ValueError: axes don't match array [\#1042](https://github.com/Zulko/moviepy/issues/1042)
- to\_soundarray Index error [\#1034](https://github.com/Zulko/moviepy/issues/1034)
- write\_videofile does not add audio [\#1032](https://github.com/Zulko/moviepy/issues/1032)
- moviepy.video.io.VideoFileClip.VideoFileClip.set\_audio does not set audio [\#1030](https://github.com/Zulko/moviepy/issues/1030)
- loop for concatenate\_videoclips [\#1027](https://github.com/Zulko/moviepy/issues/1027)
- How to resize ImageClip? [\#1004](https://github.com/Zulko/moviepy/issues/1004)
- Pygame pollutes stdio with spammy message [\#985](https://github.com/Zulko/moviepy/issues/985)
- Issue with ffmpeg version [\#934](https://github.com/Zulko/moviepy/issues/934)
- No release notes for 1.0.0? [\#917](https://github.com/Zulko/moviepy/issues/917)
- Imageio's new use of imageio-ffmpeg [\#908](https://github.com/Zulko/moviepy/issues/908)
- `ModuleNotFound: No module named 'imageio\_ffmpeg'`, or imageio v2.5.0 is breaking ffmpeg detection in config [\#906](https://github.com/Zulko/moviepy/issues/906)
- CompositeVideoClip has no audio [\#876](https://github.com/Zulko/moviepy/issues/876)
- Handling of the ffmpeg dependency [\#859](https://github.com/Zulko/moviepy/issues/859)
- 'ffmpeg-linux64-v3.3.1' was not found on your computer; downloading it now. [\#839](https://github.com/Zulko/moviepy/issues/839)
- Typo in variable name in transitions.py\(t\_s instead of ts\) [\#692](https://github.com/Zulko/moviepy/issues/692)
- version 0.2.3.2 TypeError: must be str, not bytes [\#650](https://github.com/Zulko/moviepy/issues/650)
- AWS Lambda - Moviepy Error -  [\#638](https://github.com/Zulko/moviepy/issues/638)
- Adding conda-forge package [\#616](https://github.com/Zulko/moviepy/issues/616)
- Several YouTube examples in Gallery page are unable to load. [\#600](https://github.com/Zulko/moviepy/issues/600)
- ffmpeg not installed on Mac [\#595](https://github.com/Zulko/moviepy/issues/595)
- FFMPEG not downloaded [\#493](https://github.com/Zulko/moviepy/issues/493)
- Fix documentation [\#482](https://github.com/Zulko/moviepy/issues/482)
- Moviepy is producing garbled videos [\#356](https://github.com/Zulko/moviepy/issues/356)
- Help with contributing to the documentation? [\#327](https://github.com/Zulko/moviepy/issues/327)
- audio custom filter documentation? [\#267](https://github.com/Zulko/moviepy/issues/267)
- Mistake in doc,  clips.html part. [\#136](https://github.com/Zulko/moviepy/issues/136)


## [v1.0.1](https://github.com/zulko/moviepy/tree/v1.0.1) (2019-10-01)

[Full Changelog](https://github.com/zulko/moviepy/compare/v1.0.0...v1.0.1)

**Implemented enhancements:**

- Thoughts on re-routing tqdm progress bar for external use? [\#412](https://github.com/Zulko/moviepy/issues/412)
- Progress bar [\#128](https://github.com/Zulko/moviepy/issues/128)

**Fixed bugs:**

- More resilient Windows CI regarding fetching ImageMagick binaries [\#941](https://github.com/Zulko/moviepy/pull/941) ([Overdrivr](https://github.com/Overdrivr))
- \[docker\] drop the not needed download and symlink of ffmpeg [\#916](https://github.com/Zulko/moviepy/pull/916) ([das7pad](https://github.com/das7pad))

**Closed issues:**

- website video examples broken videos [\#1019](https://github.com/Zulko/moviepy/issues/1019)
- Audio glitches when using concatenate\_videoclips. [\#1005](https://github.com/Zulko/moviepy/issues/1005)
- txt\_clip = TextClip\(filename='learn.srt'\) --bug:TypeError: stat: path should be string, bytes, os.PathLike or integer, not NoneType [\#984](https://github.com/Zulko/moviepy/issues/984)
- txt\_clip = TextClip\(filename='learn.srt'\) --bug:TypeError: stat: path should be string, bytes, os.PathLike or integer, not NoneType [\#983](https://github.com/Zulko/moviepy/issues/983)
- txt\_clip = TextClip\(filename='learn.srt'\)path should be string, bytes, os.PathLike or integer, not NoneType [\#982](https://github.com/Zulko/moviepy/issues/982)
- write\_videofile writes blank black when writing grayscale [\#973](https://github.com/Zulko/moviepy/issues/973)
- i dont understand this question [\#967](https://github.com/Zulko/moviepy/issues/967)
- Thank you guys! [\#957](https://github.com/Zulko/moviepy/issues/957)
- Saving an opencv stream [\#953](https://github.com/Zulko/moviepy/issues/953)
- Issue with reader not being defined [\#950](https://github.com/Zulko/moviepy/issues/950)
- On Windows, ImageMagick needs to be installed with Utility mode for the convert.exe file to exist [\#937](https://github.com/Zulko/moviepy/issues/937)
- extract subtitles [\#932](https://github.com/Zulko/moviepy/issues/932)
- ffmpeg\_parse\_infos silently hangs on Windows when MP4 file contains enough metadata [\#926](https://github.com/Zulko/moviepy/issues/926)
- crop missing from moviepy.video.fx.all [\#914](https://github.com/Zulko/moviepy/issues/914)
- Segmentation Error on VPS [\#912](https://github.com/Zulko/moviepy/issues/912)
- Error when installing with imageio [\#911](https://github.com/Zulko/moviepy/issues/911)
- Backwards compatibility [\#889](https://github.com/Zulko/moviepy/issues/889)
- frozen seconds in beginning of subclip using ffmpeg\_extract\_subclip\(\) [\#847](https://github.com/Zulko/moviepy/issues/847)
- \[Errno 3\] No such process : on Windows Sub Linux \(ubuntu 16.x\) [\#765](https://github.com/Zulko/moviepy/issues/765)
- Progress bar newline error in Jupyter [\#740](https://github.com/Zulko/moviepy/issues/740)
- Refer to magick on https://zulko.github.io/moviepy/install.html [\#689](https://github.com/Zulko/moviepy/issues/689)
- Configure Appveyor support [\#628](https://github.com/Zulko/moviepy/issues/628)
- tqdm progress bar write\_videofile send to iterator [\#568](https://github.com/Zulko/moviepy/issues/568)
- ffmpeg\_extract\_subclip returns black frames [\#508](https://github.com/Zulko/moviepy/issues/508)
- Windows: specifying path to ImageMagick in config\_defaults.py [\#378](https://github.com/Zulko/moviepy/issues/378)
- AttributeError: 'NoneType' object has no attribute 'start' [\#191](https://github.com/Zulko/moviepy/issues/191)
- ImageMagick write gif success but no file found  [\#113](https://github.com/Zulko/moviepy/issues/113)

**Merged pull requests:**

- Create v1.0.1 [\#1023](https://github.com/Zulko/moviepy/pull/1023) ([tburrows13](https://github.com/tburrows13))
- Update maintainer list in the README [\#1022](https://github.com/Zulko/moviepy/pull/1022) ([tburrows13](https://github.com/tburrows13))
- fixed small error in 'Clip' documentation [\#1002](https://github.com/Zulko/moviepy/pull/1002) ([thomasmatt88](https://github.com/thomasmatt88))
- Specify Coverage version explicitly. [\#987](https://github.com/Zulko/moviepy/pull/987) ([Julian-O](https://github.com/Julian-O))
- Updating Docs for ImageMagick Installing Guide [\#980](https://github.com/Zulko/moviepy/pull/980) ([ABODFTW](https://github.com/ABODFTW))
- Several ImageMagick related bug fixes [\#972](https://github.com/Zulko/moviepy/pull/972) ([KiLLAAA](https://github.com/KiLLAAA))
- Auto-detect image magick latest 6.9.X-Y version [\#936](https://github.com/Zulko/moviepy/pull/936) ([Overdrivr](https://github.com/Overdrivr))
- Windows-based testing [\#931](https://github.com/Zulko/moviepy/pull/931) ([Overdrivr](https://github.com/Overdrivr))
- Fix formatting in logger [\#929](https://github.com/Zulko/moviepy/pull/929) ([tnoff](https://github.com/tnoff))
- Fix for \#926 [\#927](https://github.com/Zulko/moviepy/pull/927) ([Overdrivr](https://github.com/Overdrivr))
- Invalid video URL in docs/getting\_started/compositing [\#921](https://github.com/Zulko/moviepy/pull/921) ([gepcel](https://github.com/gepcel))
- Do not install tests in site-packages [\#880](https://github.com/Zulko/moviepy/pull/880) ([cgohlke](https://github.com/cgohlke))
- FIX changed order of specifications -ss befor -i for ffmpeg\_extract\_subclip\(\) [\#848](https://github.com/Zulko/moviepy/pull/848) ([grszkthfr](https://github.com/grszkthfr))

## [v1.0.0](https://github.com/zulko/moviepy/tree/v1.0.0) (2019-02-17)

[Full Changelog](https://github.com/zulko/moviepy/compare/v0.2.3.5...v1.0.0)

**Closed issues:**

- Can't overlay gizeh animation onto video with transparency/mask [\#898](https://github.com/Zulko/moviepy/issues/898)
- \[0.2.4.0\] Garbled audio when exporting mp3 from mp4? [\#891](https://github.com/Zulko/moviepy/issues/891)
- Error with VideoFileClip\(filePath\) [\#868](https://github.com/Zulko/moviepy/issues/868)
- I am trying to run this code [\#867](https://github.com/Zulko/moviepy/issues/867)
- Out of memory exception [\#862](https://github.com/Zulko/moviepy/issues/862)
- simple problem on the first step: importing moviepy.editor [\#852](https://github.com/Zulko/moviepy/issues/852)
- MoviePy insert multiple images in a video [\#840](https://github.com/Zulko/moviepy/issues/840)
- Videogrep can't works with Moviepy in Windows [\#834](https://github.com/Zulko/moviepy/issues/834)
- File "\<stdin\>", line 1 error [\#832](https://github.com/Zulko/moviepy/issues/832)
- ImageMagick error - Ubuntu 16.04  [\#831](https://github.com/Zulko/moviepy/issues/831)
- Combining thousands of small clips into one file [\#827](https://github.com/Zulko/moviepy/issues/827)
- TypeError: 'ImageClip' object is not iterable [\#824](https://github.com/Zulko/moviepy/issues/824)
- OSError: \[WinError 6\] The handle is invalid... concatenating clips [\#823](https://github.com/Zulko/moviepy/issues/823)
- How to add audio tracks. not to replace it. [\#822](https://github.com/Zulko/moviepy/issues/822)
- Missing 'ffmpeg-win32-v3.2.4.exe' [\#821](https://github.com/Zulko/moviepy/issues/821)
- No sound with an audio clip add to an video in quicktime [\#820](https://github.com/Zulko/moviepy/issues/820)
- Pip fails when trying to install [\#812](https://github.com/Zulko/moviepy/issues/812)
- PermissionError after trying to delete a file after it's purpose is done [\#810](https://github.com/Zulko/moviepy/issues/810)
- video clip from URI [\#780](https://github.com/Zulko/moviepy/issues/780)
- Fails on FreeBSD [\#756](https://github.com/Zulko/moviepy/issues/756)
- inconsistent behaviour of clip.get\_frame\(\) [\#751](https://github.com/Zulko/moviepy/issues/751)
- Error with write\_videofile [\#727](https://github.com/Zulko/moviepy/issues/727)
- Trying to use moviepy on lambda, but has problem with ffmpeg [\#642](https://github.com/Zulko/moviepy/issues/642)
- Unexpected Behavior With negative t\_start in Subclip [\#341](https://github.com/Zulko/moviepy/issues/341)
- Could not find a format to read the specified file in mode 'i'  [\#219](https://github.com/Zulko/moviepy/issues/219)
- WindowsError\[5\] and AttributeError Exception [\#170](https://github.com/Zulko/moviepy/issues/170)
- Can't make VideoFileClip 'utf8' [\#169](https://github.com/Zulko/moviepy/issues/169)
- Rendered output missing first frame [\#155](https://github.com/Zulko/moviepy/issues/155)
- Incorrect output when concatenate\_videoclips two quicktime videos [\#144](https://github.com/Zulko/moviepy/issues/144)
- a bytes object is recognised as a string [\#120](https://github.com/Zulko/moviepy/issues/120)

**Merged pull requests:**

- New version of imageio with imageio\_ffmpeg for python 3.4+ [\#907](https://github.com/Zulko/moviepy/pull/907) ([Zulko](https://github.com/Zulko))
- fix typo that introduces audio regression [\#894](https://github.com/Zulko/moviepy/pull/894) ([chrox](https://github.com/chrox))
- modified max duration error for better understanding [\#875](https://github.com/Zulko/moviepy/pull/875) ([kapilkd13](https://github.com/kapilkd13))
- Fixed typo in docstring for VideoClip class [\#871](https://github.com/Zulko/moviepy/pull/871) ([Armcollector](https://github.com/Armcollector))
- Fix a small typing error [\#845](https://github.com/Zulko/moviepy/pull/845) ([yuvallanger](https://github.com/yuvallanger))

## [v0.2.3.5](https://github.com/zulko/moviepy/tree/v0.2.3.5) (2018-05-31)

[Full Changelog](https://github.com/zulko/moviepy/compare/v0.2.3.4...v0.2.3.5)

**Fixed bugs:**

- Removed Hz from audio\_fps match in ffmpeg\_parse\_infos [\#665](https://github.com/Zulko/moviepy/pull/665) ([qmac](https://github.com/qmac))

**Closed issues:**

- 100% of GIF does not convert to MP4, gets cut short. [\#802](https://github.com/Zulko/moviepy/issues/802)
- How to add audio track to MP4? [\#794](https://github.com/Zulko/moviepy/issues/794)
- ffmpeg 4.0 NVIDIA NVDEC-accelerated Support ? [\#790](https://github.com/Zulko/moviepy/issues/790)
- Help!!!! errors during installation on Mac [\#788](https://github.com/Zulko/moviepy/issues/788)
- Blink fx uses deprecated\(?\) method `with\_mask\(\)` [\#786](https://github.com/Zulko/moviepy/issues/786)
- Built-in file downloader downloads files repeatedly? [\#779](https://github.com/Zulko/moviepy/issues/779)
- Error in compositing video and SubtitlesClip by CompositeVideoClip  [\#778](https://github.com/Zulko/moviepy/issues/778)
- SubtitlesClip [\#777](https://github.com/Zulko/moviepy/issues/777)
- Video Background [\#774](https://github.com/Zulko/moviepy/issues/774)

**Merged pull requests:**

- fixing the git remote syntax in documentions [\#887](https://github.com/Zulko/moviepy/pull/887) ([ishandutta2007](https://github.com/ishandutta2007))
- Progress bar optional for GIF creation [\#799](https://github.com/Zulko/moviepy/pull/799) ([mdfirman](https://github.com/mdfirman))
- Added contributing guide and issue template [\#792](https://github.com/Zulko/moviepy/pull/792) ([tburrows13](https://github.com/tburrows13))

## [v0.2.3.4](https://github.com/zulko/moviepy/tree/v0.2.3.4) (2018-04-22)

[Full Changelog](https://github.com/zulko/moviepy/compare/v0.2.3.3...v0.2.3.4)

**Closed issues:**

- fail to install [\#771](https://github.com/Zulko/moviepy/issues/771)
- install moviepy [\#758](https://github.com/Zulko/moviepy/issues/758)
- How to prepend hexadecimal data to a binary file? [\#757](https://github.com/Zulko/moviepy/issues/757)
- It’s time for a new release [\#742](https://github.com/Zulko/moviepy/issues/742)
- wrong video duration value when concatenating videos with method = compose [\#574](https://github.com/Zulko/moviepy/issues/574)

**Merged pull requests:**

- Added `fullscreen` parameter to `preview\(\)` [\#773](https://github.com/Zulko/moviepy/pull/773) ([tburrows13](https://github.com/tburrows13))
- add pcm\_s24le codec [\#769](https://github.com/Zulko/moviepy/pull/769) ([lsde](https://github.com/lsde))

## [v0.2.3.3](https://github.com/zulko/moviepy/tree/v0.2.3.3) (2018-04-17)

[Full Changelog](https://github.com/zulko/moviepy/compare/v0.2.3.2...v0.2.3.3)

**Implemented enhancements:**

- Use feature detection instead of version detection [\#721](https://github.com/Zulko/moviepy/pull/721) ([cclauss](https://github.com/cclauss))
- Fixed Optional Progress Bar in cuts/detect\_scenes [\#587](https://github.com/Zulko/moviepy/pull/587) ([scherroman](https://github.com/scherroman))
- Fix travis build and enable pip caching [\#561](https://github.com/Zulko/moviepy/pull/561) ([mbeacom](https://github.com/mbeacom))
- Avoid mutable default arguments [\#553](https://github.com/Zulko/moviepy/pull/553) ([mbeacom](https://github.com/mbeacom))
- add ImageSequenceClip image size exception  [\#550](https://github.com/Zulko/moviepy/pull/550) ([earney](https://github.com/earney))

**Fixed bugs:**

- Added ffmpeg download when importing moviepy.editor [\#731](https://github.com/Zulko/moviepy/pull/731) ([tburrows13](https://github.com/tburrows13))
- Fixed bugs, neater code, changed docstrings in audiofiles [\#722](https://github.com/Zulko/moviepy/pull/722) ([tburrows13](https://github.com/tburrows13))
- Resolve undefined name execfile in Python 3 [\#718](https://github.com/Zulko/moviepy/pull/718) ([cclauss](https://github.com/cclauss))
- Fix credits, added tests [\#716](https://github.com/Zulko/moviepy/pull/716) ([tburrows13](https://github.com/tburrows13))
- res —\> size to align with line 62 [\#710](https://github.com/Zulko/moviepy/pull/710) ([cclauss](https://github.com/cclauss))
- Add gap=0 to align with lines 40, 97, and 98 [\#709](https://github.com/Zulko/moviepy/pull/709) ([cclauss](https://github.com/cclauss))
- import numpy as np for lines 151 and 178 [\#708](https://github.com/Zulko/moviepy/pull/708) ([cclauss](https://github.com/cclauss))
- Convert advanced\_tools.py to valid Python [\#707](https://github.com/Zulko/moviepy/pull/707) ([cclauss](https://github.com/cclauss))
- Added missing '%' operator for string formatting. [\#686](https://github.com/Zulko/moviepy/pull/686) ([taylorjdawson](https://github.com/taylorjdawson))
- Addressing \#655 [\#656](https://github.com/Zulko/moviepy/pull/656) ([gyglim](https://github.com/gyglim))
- initialize proc to None [\#637](https://github.com/Zulko/moviepy/pull/637) ([gyglim](https://github.com/gyglim))
- sometimes tempfile.tempdir is None, so use tempfile.gettempdir\(\) function instead [\#633](https://github.com/Zulko/moviepy/pull/633) ([earney](https://github.com/earney))
- Issue629 [\#630](https://github.com/Zulko/moviepy/pull/630) ([Julian-O](https://github.com/Julian-O))
- Fixed bug in Clip.set\_duration\(\) [\#613](https://github.com/Zulko/moviepy/pull/613) ([kencochrane](https://github.com/kencochrane))
- Fixed typo in the slide\_out transition [\#612](https://github.com/Zulko/moviepy/pull/612) ([kencochrane](https://github.com/kencochrane))
- Exceptions do not have a .message attribute. [\#603](https://github.com/Zulko/moviepy/pull/603) ([Julian-O](https://github.com/Julian-O))
- Issue \#574, fix duration of masks when using concatenate\(.., method="compose"\) [\#585](https://github.com/Zulko/moviepy/pull/585) ([earney](https://github.com/earney))
- Fix out of bounds error [\#570](https://github.com/Zulko/moviepy/pull/570) ([shawwn](https://github.com/shawwn))
- fixed ffmpeg error reporting on Python 3 [\#565](https://github.com/Zulko/moviepy/pull/565) ([narfdotpl](https://github.com/narfdotpl))
- Add int\(\) wrapper to scroll to prevent floats [\#528](https://github.com/Zulko/moviepy/pull/528) ([tburrows13](https://github.com/tburrows13))
- Fix issue \#464, repeated/skipped frames in ImageSequenceClip [\#494](https://github.com/Zulko/moviepy/pull/494) ([neitzal](https://github.com/neitzal))
- fixes \#248 issue with VideoFileClip\(\) not reading all frames [\#251](https://github.com/Zulko/moviepy/pull/251) ([aldilaff](https://github.com/aldilaff))

**Closed issues:**

- Overly Restrictive Requirements [\#767](https://github.com/Zulko/moviepy/issues/767)
- Using a gif as an ImageClip? [\#764](https://github.com/Zulko/moviepy/issues/764)
- How can I include a moving 'arrow' in a clip? [\#762](https://github.com/Zulko/moviepy/issues/762)
- How to call moviepy.video.fx.all.crop\(\) ? [\#760](https://github.com/Zulko/moviepy/issues/760)
- ImportError: Imageio Pillow requires Pillow, not PIL!  [\#748](https://github.com/Zulko/moviepy/issues/748)
- Fail to call VideoFileClip\(\) because of WinError 6 [\#746](https://github.com/Zulko/moviepy/issues/746)
- concatenate\_videoclips with fadein fadeout [\#743](https://github.com/Zulko/moviepy/issues/743)
- Ignore - sorry! [\#739](https://github.com/Zulko/moviepy/issues/739)
- Image becomes blurr with high fps [\#735](https://github.com/Zulko/moviepy/issues/735)
- Https protocol not found with ffmpeg [\#732](https://github.com/Zulko/moviepy/issues/732)
- Storing Processed Video clip takes a long time [\#726](https://github.com/Zulko/moviepy/issues/726)
- image corruption when concatenating images of different sizes [\#725](https://github.com/Zulko/moviepy/issues/725)
- How to install MoviePy on OS High Sierra [\#706](https://github.com/Zulko/moviepy/issues/706)
- Issue when running the first example of text overlay in ubuntu 16.04 with python3 [\#703](https://github.com/Zulko/moviepy/issues/703)
- Extracting frames [\#702](https://github.com/Zulko/moviepy/issues/702)
- Error - The handle is invalid - Windows Only [\#697](https://github.com/Zulko/moviepy/issues/697)
- ImageMagick not detected by moviepy while using SubtitlesClip [\#693](https://github.com/Zulko/moviepy/issues/693)
- Textclip is not working at all [\#691](https://github.com/Zulko/moviepy/issues/691)
- Remove Python 3.3 testing ? [\#688](https://github.com/Zulko/moviepy/issues/688)
- In idle, 25 % CPU [\#676](https://github.com/Zulko/moviepy/issues/676)
- Audio error [\#675](https://github.com/Zulko/moviepy/issues/675)
- Insert a ImageClip in a CompositeVideoClip. How to add nil audio [\#669](https://github.com/Zulko/moviepy/issues/669)
- Issue with nesting context managers [\#655](https://github.com/Zulko/moviepy/issues/655)
- Output video is garbled, single frames output are fine [\#651](https://github.com/Zulko/moviepy/issues/651)
- 'missing handle' error [\#644](https://github.com/Zulko/moviepy/issues/644)
- issue with proc being None [\#636](https://github.com/Zulko/moviepy/issues/636)
- Looping parameter is missing from write\_gif\_with\_image\_io\(\) [\#629](https://github.com/Zulko/moviepy/issues/629)
- would it be optionally possible to use pgmagick package ? \(instead of ImageMagick binary\) [\#625](https://github.com/Zulko/moviepy/issues/625)
- concatenate\_videoclips\(\) can't handle TextClips [\#622](https://github.com/Zulko/moviepy/issues/622)
- Writing movie one frame at a time [\#619](https://github.com/Zulko/moviepy/issues/619)
- Fatal Python error: PyImport\_GetModuleDict: no module dictionary! [\#618](https://github.com/Zulko/moviepy/issues/618)
- line 54, in requires\_duration return [\#601](https://github.com/Zulko/moviepy/issues/601)
- test\_duration\(\) fails in test\_TextClip\(\) [\#598](https://github.com/Zulko/moviepy/issues/598)
- Geting framesize from moviepy [\#571](https://github.com/Zulko/moviepy/issues/571)
- Write\_videofile results in 1930x1080 even when I force clip.resize\(width=1920,height=1080\) before write\_videofile [\#547](https://github.com/Zulko/moviepy/issues/547)
- Is there one potential bug in FFMPEG\_READER? [\#546](https://github.com/Zulko/moviepy/issues/546)
- vfx.scroll giving TypeError: slice indices must be integers or None or have an \_\_index\_\_ method [\#527](https://github.com/Zulko/moviepy/issues/527)
- AttributeError: AudioFileClip instance has no attribute 'afx' [\#513](https://github.com/Zulko/moviepy/issues/513)
- ImageSequenceClip repeats frames depending on fps [\#464](https://github.com/Zulko/moviepy/issues/464)
- manual\_tracking format issue [\#373](https://github.com/Zulko/moviepy/issues/373)
- resize video when time changed trigger a error [\#334](https://github.com/Zulko/moviepy/issues/334)
- WindowsError: \[Error 5\] Access is denied [\#294](https://github.com/Zulko/moviepy/issues/294)
- TypeError in Adding Soundtrack [\#279](https://github.com/Zulko/moviepy/issues/279)
- IndexError when converting audio to\_soundarray\(\) [\#246](https://github.com/Zulko/moviepy/issues/246)
- Defaults fail for ImageSequenceClip\(\) [\#218](https://github.com/Zulko/moviepy/issues/218)
- Unable to use unicode strings with Python 2 [\#76](https://github.com/Zulko/moviepy/issues/76)
- audio normalization [\#32](https://github.com/Zulko/moviepy/issues/32)
- Unclosed processes. [\#19](https://github.com/Zulko/moviepy/issues/19)

**Merged pull requests:**

- transitions.py: pep8 and a change to docstring [\#754](https://github.com/Zulko/moviepy/pull/754) ([tburrows13](https://github.com/tburrows13))
- Make TextClip work on Travis CI [\#747](https://github.com/Zulko/moviepy/pull/747) ([tburrows13](https://github.com/tburrows13))
- Added tests, new duration arg in to\_ImageClip\(\) [\#724](https://github.com/Zulko/moviepy/pull/724) ([tburrows13](https://github.com/tburrows13))
- let there be \(more\) colour [\#723](https://github.com/Zulko/moviepy/pull/723) ([bashu](https://github.com/bashu))
- Resolve undefined name unicode in Python 3 [\#717](https://github.com/Zulko/moviepy/pull/717) ([cclauss](https://github.com/cclauss))
- Credits.py PEP 8 [\#715](https://github.com/Zulko/moviepy/pull/715) ([tburrows13](https://github.com/tburrows13))
- Added info about tag wiki [\#714](https://github.com/Zulko/moviepy/pull/714) ([tburrows13](https://github.com/tburrows13))
- Remove testing support for Python 3.3, closes \#688 [\#713](https://github.com/Zulko/moviepy/pull/713) ([tburrows13](https://github.com/tburrows13))
- More PEP8 compliance [\#712](https://github.com/Zulko/moviepy/pull/712) ([tburrows13](https://github.com/tburrows13))
- More PEP8 compliance [\#711](https://github.com/Zulko/moviepy/pull/711) ([tburrows13](https://github.com/tburrows13))
- flake8 test to find syntax errors, undefined names [\#705](https://github.com/Zulko/moviepy/pull/705) ([cclauss](https://github.com/cclauss))
- fix typo [\#687](https://github.com/Zulko/moviepy/pull/687) ([msrks](https://github.com/msrks))
- Update Readme.rst [\#671](https://github.com/Zulko/moviepy/pull/671) ([rlphillips](https://github.com/rlphillips))
- Update Dockerfile to add requests module [\#664](https://github.com/Zulko/moviepy/pull/664) ([edouard-mangel](https://github.com/edouard-mangel))
- fixed typo in library include [\#652](https://github.com/Zulko/moviepy/pull/652) ([Goddard](https://github.com/Goddard))
- Use max fps for CompositeVideoClip [\#610](https://github.com/Zulko/moviepy/pull/610) ([scherroman](https://github.com/scherroman))
- Add audio normalization function [\#609](https://github.com/Zulko/moviepy/pull/609) ([dspinellis](https://github.com/dspinellis))
- \#600: Several YouTube examples in Gallery page won't load. [\#606](https://github.com/Zulko/moviepy/pull/606) ([Julian-O](https://github.com/Julian-O))
- Two small corrections to documentation. [\#605](https://github.com/Zulko/moviepy/pull/605) ([Julian-O](https://github.com/Julian-O))
- PEP 8 compatible [\#582](https://github.com/Zulko/moviepy/pull/582) ([gpantelis](https://github.com/gpantelis))
- add additional ImageSequenceClip test [\#551](https://github.com/Zulko/moviepy/pull/551) ([earney](https://github.com/earney))
- General tests cleanup [\#549](https://github.com/Zulko/moviepy/pull/549) ([mbeacom](https://github.com/mbeacom))
- Update docs [\#548](https://github.com/Zulko/moviepy/pull/548) ([tburrows13](https://github.com/tburrows13))
- add tests for most fx functions [\#545](https://github.com/Zulko/moviepy/pull/545) ([earney](https://github.com/earney))

## [v0.2.3.2](https://github.com/zulko/moviepy/tree/v0.2.3.2) (2017-04-13)

[Full Changelog](https://github.com/zulko/moviepy/compare/v0.2.3.1...v0.2.3.2)

**Implemented enhancements:**

- Requirements adjustments [\#530](https://github.com/Zulko/moviepy/issues/530)
- Modify setup.py handling [\#531](https://github.com/Zulko/moviepy/pull/531) ([mbeacom](https://github.com/mbeacom))
- Resolve documentation build errors [\#526](https://github.com/Zulko/moviepy/pull/526) ([mbeacom](https://github.com/mbeacom))

**Closed issues:**

- Youtube videos fail to load in documentation [\#536](https://github.com/Zulko/moviepy/issues/536)
- unicodeDecoderError by running the setup.py during moviepy pip install [\#532](https://github.com/Zulko/moviepy/issues/532)
- Documentation build failures [\#525](https://github.com/Zulko/moviepy/issues/525)
- Index is out of bounds - AudioFileClip [\#521](https://github.com/Zulko/moviepy/issues/521)
- Should we push another version? [\#481](https://github.com/Zulko/moviepy/issues/481)
- Add matplotlib example to the user guide? [\#421](https://github.com/Zulko/moviepy/issues/421)
- Fails to list fx after freezing an app with moviepy [\#274](https://github.com/Zulko/moviepy/issues/274)
- Documentation doesn't match ffmpeg presets [\#232](https://github.com/Zulko/moviepy/issues/232)

**Merged pull requests:**

- add opencv dependency since headblur effect depends on it. [\#540](https://github.com/Zulko/moviepy/pull/540) ([earney](https://github.com/earney))
- create tests for blackwhite, colorx, fadein, fadeout [\#539](https://github.com/Zulko/moviepy/pull/539) ([earney](https://github.com/earney))
- add crop tests [\#538](https://github.com/Zulko/moviepy/pull/538) ([earney](https://github.com/earney))
- Fix youtube video rendering in documentation [\#537](https://github.com/Zulko/moviepy/pull/537) ([mbeacom](https://github.com/mbeacom))
- Update docs [\#535](https://github.com/Zulko/moviepy/pull/535) ([tburrows13](https://github.com/tburrows13))
- add test for Issue 334, PR 336 [\#534](https://github.com/Zulko/moviepy/pull/534) ([earney](https://github.com/earney))
- issue-212: add rotation info from metadata [\#529](https://github.com/Zulko/moviepy/pull/529) ([taddyhuo](https://github.com/taddyhuo))
- Added another project using MoviePy [\#509](https://github.com/Zulko/moviepy/pull/509) ([justswim](https://github.com/justswim))
- added doc for working with matplotlib [\#465](https://github.com/Zulko/moviepy/pull/465) ([flothesof](https://github.com/flothesof))
- fix issue \#334 [\#336](https://github.com/Zulko/moviepy/pull/336) ([bluedazzle](https://github.com/bluedazzle))
- Add progress\_bar option to write\_images\_sequence [\#300](https://github.com/Zulko/moviepy/pull/300) ([achalddave](https://github.com/achalddave))
- write\_videofile preset choices doc [\#282](https://github.com/Zulko/moviepy/pull/282) ([gcandal](https://github.com/gcandal))

## [v0.2.3.1](https://github.com/zulko/moviepy/tree/v0.2.3.1) (2017-04-05)

[Full Changelog](https://github.com/zulko/moviepy/compare/v0.2.2.13...v0.2.3.1)

**Implemented enhancements:**

- \[Windows users: help !\] Finding ImageMagick automatically on windows [\#80](https://github.com/Zulko/moviepy/issues/80)
- Save to Amazon S3 [\#6](https://github.com/Zulko/moviepy/issues/6)
- Fix for cleaning up os calls through Popen [\#501](https://github.com/Zulko/moviepy/pull/501) ([gyglim](https://github.com/gyglim))
- pick highest fps when concatenating [\#416](https://github.com/Zulko/moviepy/pull/416) ([BrianLee608](https://github.com/BrianLee608))

**Closed issues:**

- concatenate\_videoclips\(\[clip1,clip2\]\) results in a clip where the second clip is skewed and has severe lines [\#520](https://github.com/Zulko/moviepy/issues/520)
- FFMPEG crashes if the script is a .pyw [\#517](https://github.com/Zulko/moviepy/issues/517)
- VideoFileClip instance has no attribute 'reader' [\#512](https://github.com/Zulko/moviepy/issues/512)
- Adding emoji with moviepy [\#507](https://github.com/Zulko/moviepy/issues/507)
- How to remove original audio from the video file ? [\#504](https://github.com/Zulko/moviepy/issues/504)
- Duration Format With Moviepy [\#502](https://github.com/Zulko/moviepy/issues/502)
- AttributeError: 'numpy.ndarray' object has no attribute 'tobytes' [\#499](https://github.com/Zulko/moviepy/issues/499)
- Possible to create out of bounds subclip [\#470](https://github.com/Zulko/moviepy/issues/470)
- New install... VideoFileClip\("x.mp4"\).subclip\(0,13\) gives "reader not defined error" [\#461](https://github.com/Zulko/moviepy/issues/461)
- Bytes-like object is required, not 'str' in version 0.2.2.13 [\#455](https://github.com/Zulko/moviepy/issues/455)
- Can't import gifs into moviepy [\#452](https://github.com/Zulko/moviepy/issues/452)
-  AudioFileClip [\#448](https://github.com/Zulko/moviepy/issues/448)
- Error with Pillow [\#445](https://github.com/Zulko/moviepy/issues/445)
- Moviepy AttributeError: 'NoneType' object has no attribute 'shape' [\#439](https://github.com/Zulko/moviepy/issues/439)
- This is what exception.... [\#437](https://github.com/Zulko/moviepy/issues/437)
- when I from moviepy.editor import \*,  There cause exception,That's why....... [\#436](https://github.com/Zulko/moviepy/issues/436)
- No available fonts in moviepy [\#426](https://github.com/Zulko/moviepy/issues/426)
- Project maintenance, mgmt, workflow etc. [\#422](https://github.com/Zulko/moviepy/issues/422)
- Cannot run in a django project on apache [\#420](https://github.com/Zulko/moviepy/issues/420)
- error 'unicode' object has no attribute 'shape' [\#417](https://github.com/Zulko/moviepy/issues/417)
- VideoClip has no attribute fps error when trying to concatenate [\#407](https://github.com/Zulko/moviepy/issues/407)
- The Travis tester seems to be failing [\#406](https://github.com/Zulko/moviepy/issues/406)
- Slow motion video massively sped up [\#404](https://github.com/Zulko/moviepy/issues/404)
- moviepy not able to find installed ffmpeg    bug? [\#396](https://github.com/Zulko/moviepy/issues/396)
- Cannot open audio: AttributeError: 'NoneType' object has no attribute 'start' [\#393](https://github.com/Zulko/moviepy/issues/393)
- DirectoryClip??? Where is it? [\#385](https://github.com/Zulko/moviepy/issues/385)
- TypeError: 'float' object cannot be interpreted as an integer [\#376](https://github.com/Zulko/moviepy/issues/376)
- Minor Documentation typo in VideoFileClip [\#375](https://github.com/Zulko/moviepy/issues/375)
- Documentation Update: VideoTools [\#372](https://github.com/Zulko/moviepy/issues/372)
- TextClip.list\('color'\) failed to return color list [\#371](https://github.com/Zulko/moviepy/issues/371)
- ValueError: Invalid value for quantizer: 'wu' [\#368](https://github.com/Zulko/moviepy/issues/368)
- Parameter color in ColorClip [\#366](https://github.com/Zulko/moviepy/issues/366)
- Different size videos [\#365](https://github.com/Zulko/moviepy/issues/365)
- Bug in write\_gif [\#359](https://github.com/Zulko/moviepy/issues/359)
- Add support for dithering GIF output [\#358](https://github.com/Zulko/moviepy/issues/358)
- VideoFileClip instance has no attribute 'coreader' [\#357](https://github.com/Zulko/moviepy/issues/357)
- crossfadeout "Attribute 'duration' not set" [\#354](https://github.com/Zulko/moviepy/issues/354)
- ffmpeg\_parse\_infos fails while parsing tbr [\#352](https://github.com/Zulko/moviepy/issues/352)
- No audio when adding Mp3 to VideoFileClip MoviePy [\#350](https://github.com/Zulko/moviepy/issues/350)
- ImportError: No module named tracking \(OS: 10.11.6 "El Capitan", Python 2.7.12\) [\#348](https://github.com/Zulko/moviepy/issues/348)
- AAC support for mp4 [\#344](https://github.com/Zulko/moviepy/issues/344)
- Moviepy not compatible with Python 3.2 [\#333](https://github.com/Zulko/moviepy/issues/333)
- Attribute Error \(Raspberry Pi\) [\#332](https://github.com/Zulko/moviepy/issues/332)
- ImageSequenceClip: Error when fps not provided but durations provided [\#326](https://github.com/Zulko/moviepy/issues/326)
- CI Testing [\#325](https://github.com/Zulko/moviepy/issues/325)
- Pythonanywhere Moviepy [\#324](https://github.com/Zulko/moviepy/issues/324)
- Documentation for resize parameter is wrong [\#319](https://github.com/Zulko/moviepy/issues/319)
- ImageClip's with default settings can not be concatenated [\#314](https://github.com/Zulko/moviepy/issues/314)
- librelist does not work [\#309](https://github.com/Zulko/moviepy/issues/309)
- Broken Gallery in Documentation [\#304](https://github.com/Zulko/moviepy/issues/304)
- File IOError when trying to extract subclips from mov file on Ubuntu [\#303](https://github.com/Zulko/moviepy/issues/303)
- write\_gif failing [\#296](https://github.com/Zulko/moviepy/issues/296)
- Python2 unicode\_literals errors [\#293](https://github.com/Zulko/moviepy/issues/293)
- concatenate ImageClip  [\#285](https://github.com/Zulko/moviepy/issues/285)
- Resize not working [\#272](https://github.com/Zulko/moviepy/issues/272)
- VideoFileClip instance has no attribute 'reader' [\#255](https://github.com/Zulko/moviepy/issues/255)
- stretch image to size of frame [\#250](https://github.com/Zulko/moviepy/issues/250)
- ffprobe metadata on video file clips [\#249](https://github.com/Zulko/moviepy/issues/249)
- Credits1 is not working - gap missing, isTransparent flag not available [\#247](https://github.com/Zulko/moviepy/issues/247)
- Generating Gif from images [\#240](https://github.com/Zulko/moviepy/issues/240)
- permission denied [\#233](https://github.com/Zulko/moviepy/issues/233)
- receive the video advancement mounting \(Ex: in %\) [\#224](https://github.com/Zulko/moviepy/issues/224)
- Import of MoviePy and Mayavi causes a segfault [\#223](https://github.com/Zulko/moviepy/issues/223)
- Video overlay \(gauges...\) [\#222](https://github.com/Zulko/moviepy/issues/222)
- OSError: \[WinError 193\] %1 n’est pas une application Win32 valide [\#221](https://github.com/Zulko/moviepy/issues/221)
- Warning: skimage.filter is deprecated [\#214](https://github.com/Zulko/moviepy/issues/214)
- TextClip.list\('color'\) fails [\#200](https://github.com/Zulko/moviepy/issues/200)
- External FFmpeg issues [\#193](https://github.com/Zulko/moviepy/issues/193)
- Video and Audio are out of sync after write [\#192](https://github.com/Zulko/moviepy/issues/192)
- Broken image on PyPI [\#187](https://github.com/Zulko/moviepy/issues/187)
- ImageSequenceClip from OpenEXR file sequence generate black Clip video [\#186](https://github.com/Zulko/moviepy/issues/186)
- Loading video from url [\#185](https://github.com/Zulko/moviepy/issues/185)
- Wrong number of frames in .gif file [\#181](https://github.com/Zulko/moviepy/issues/181)
- Converting mp4 to ogv error in bitrate [\#174](https://github.com/Zulko/moviepy/issues/174)
- embed clip in a jupyter notebook [\#160](https://github.com/Zulko/moviepy/issues/160)
- How to create a video from a sequence of images without writing them on memory [\#159](https://github.com/Zulko/moviepy/issues/159)
- LaTeX strings [\#156](https://github.com/Zulko/moviepy/issues/156)
- UnboundLocalError in video/compositing/concatenate.py [\#145](https://github.com/Zulko/moviepy/issues/145)
- Crop a Video with four different coodinate pairs [\#142](https://github.com/Zulko/moviepy/issues/142)
- global name 'colorGradient' is not defined [\#141](https://github.com/Zulko/moviepy/issues/141)
- rotating image animation producing error [\#130](https://github.com/Zulko/moviepy/issues/130)
- bug introduced in 0.2.2.11? [\#129](https://github.com/Zulko/moviepy/issues/129)
- Getting a TypeError in FramesMatch [\#126](https://github.com/Zulko/moviepy/issues/126)
- moviepy is awesome [\#125](https://github.com/Zulko/moviepy/issues/125)
- Concanate clips with different size [\#124](https://github.com/Zulko/moviepy/issues/124)
- TextClip.list\('font'\) raises TypeError in Python 3 [\#117](https://github.com/Zulko/moviepy/issues/117)
- Attempt to Download freeimage failing [\#111](https://github.com/Zulko/moviepy/issues/111)
- Invalid buffer size, packet size \< expected frame\_size [\#109](https://github.com/Zulko/moviepy/issues/109)
- imageio has permission problems as WSGI user on Amazon Web Server [\#106](https://github.com/Zulko/moviepy/issues/106)
- transparency bug in concatenate\_videoclips\(\) [\#103](https://github.com/Zulko/moviepy/issues/103)
- Possibility to avoid code duplication [\#99](https://github.com/Zulko/moviepy/issues/99)
- Memory Leak In VideoFileClip [\#96](https://github.com/Zulko/moviepy/issues/96)

**Merged pull requests:**

- create test for Trajectory.save\_list/load\_list [\#523](https://github.com/Zulko/moviepy/pull/523) ([earney](https://github.com/earney))
- add Dockerfile [\#522](https://github.com/Zulko/moviepy/pull/522) ([earney](https://github.com/earney))
- Add fps\_source option for \#404 [\#516](https://github.com/Zulko/moviepy/pull/516) ([tburrows13](https://github.com/tburrows13))
- Minor Modifications [\#515](https://github.com/Zulko/moviepy/pull/515) ([gpantelis](https://github.com/gpantelis))
- \#485 followup [\#514](https://github.com/Zulko/moviepy/pull/514) ([tburrows13](https://github.com/tburrows13))
- Correcting text [\#510](https://github.com/Zulko/moviepy/pull/510) ([gpantelis](https://github.com/gpantelis))
- Add aspect\_ratio @property to VideoClip [\#503](https://github.com/Zulko/moviepy/pull/503) ([scherroman](https://github.com/scherroman))
- add test for ffmpeg\_parse\_info [\#498](https://github.com/Zulko/moviepy/pull/498) ([earney](https://github.com/earney))
- add scipy for py2.7 on travis-ci [\#497](https://github.com/Zulko/moviepy/pull/497) ([earney](https://github.com/earney))
- add file\_to\_subtitles test [\#496](https://github.com/Zulko/moviepy/pull/496) ([earney](https://github.com/earney))
- add a subtitle test [\#495](https://github.com/Zulko/moviepy/pull/495) ([earney](https://github.com/earney))
- add afterimage example [\#491](https://github.com/Zulko/moviepy/pull/491) ([earney](https://github.com/earney))
- add doc example to tests [\#490](https://github.com/Zulko/moviepy/pull/490) ([earney](https://github.com/earney))
- Allow resizing frames in ffmpeg when reading [\#489](https://github.com/Zulko/moviepy/pull/489) ([gyglim](https://github.com/gyglim))
- Fix class name in AudioClip doc strings [\#488](https://github.com/Zulko/moviepy/pull/488) ([withpower](https://github.com/withpower))
- convert POpen stderr.read to communicate [\#487](https://github.com/Zulko/moviepy/pull/487) ([earney](https://github.com/earney))
- add tests for find\_video\_period [\#486](https://github.com/Zulko/moviepy/pull/486) ([earney](https://github.com/earney))
- refer to MoviePy as library \(was: module\) [\#484](https://github.com/Zulko/moviepy/pull/484) ([keikoro](https://github.com/keikoro))
- include requirements file for docs [\#483](https://github.com/Zulko/moviepy/pull/483) ([keikoro](https://github.com/keikoro))
- add test for issue 354; duration not set [\#478](https://github.com/Zulko/moviepy/pull/478) ([earney](https://github.com/earney))
- Issue 470, reading past audio file EOF [\#476](https://github.com/Zulko/moviepy/pull/476) ([earney](https://github.com/earney))
- Issue 285,  error adding durations \(int and None\). [\#472](https://github.com/Zulko/moviepy/pull/472) ([earney](https://github.com/earney))
- Issue 359,  fix default opt argument to work with imageio and ImageMagick [\#471](https://github.com/Zulko/moviepy/pull/471) ([earney](https://github.com/earney))
- Add tests for TextClip [\#469](https://github.com/Zulko/moviepy/pull/469) ([earney](https://github.com/earney))
- Issue 467;  fix  Nameerror with copy function.  Added issue to tests.. [\#468](https://github.com/Zulko/moviepy/pull/468) ([earney](https://github.com/earney))
- Small improvements to docs pages, docs usage [\#463](https://github.com/Zulko/moviepy/pull/463) ([keikoro](https://github.com/keikoro))
- Fix mixed content [\#462](https://github.com/Zulko/moviepy/pull/462) ([keikoro](https://github.com/keikoro))
- fix Issue 368..  ValueError: Invalid value for quantizer: 'wu' [\#460](https://github.com/Zulko/moviepy/pull/460) ([earney](https://github.com/earney))
- add testing to verify the width,height \(size\) are correct. [\#459](https://github.com/Zulko/moviepy/pull/459) ([earney](https://github.com/earney))
- Adds `progress\_bar` option to `write\_audiofile\(\)` to complement \#380  [\#458](https://github.com/Zulko/moviepy/pull/458) ([tburrows13](https://github.com/tburrows13))
- modify tests to use ColorClip's new color argument \(instead of col\) [\#457](https://github.com/Zulko/moviepy/pull/457) ([earney](https://github.com/earney))
- add ImageSequenceClip tests [\#456](https://github.com/Zulko/moviepy/pull/456) ([earney](https://github.com/earney))
- Add some tests for VideoFileClip [\#453](https://github.com/Zulko/moviepy/pull/453) ([earney](https://github.com/earney))
- add test\_compositing.py [\#451](https://github.com/Zulko/moviepy/pull/451) ([earney](https://github.com/earney))
- add test for tools [\#450](https://github.com/Zulko/moviepy/pull/450) ([earney](https://github.com/earney))
- fix issue 448; AudioFileClip 90k tbr error [\#449](https://github.com/Zulko/moviepy/pull/449) ([earney](https://github.com/earney))
- add testing with travis-ci [\#447](https://github.com/Zulko/moviepy/pull/447) ([earney](https://github.com/earney))
- fix YouTube embeds in docs [\#446](https://github.com/Zulko/moviepy/pull/446) ([keikoro](https://github.com/keikoro))
- Move PR test to test\_PR.py file [\#444](https://github.com/Zulko/moviepy/pull/444) ([earney](https://github.com/earney))
- Test issue 407 \(video has a valid fps after concatenate function\) [\#443](https://github.com/Zulko/moviepy/pull/443) ([earney](https://github.com/earney))
- add test for PR306. [\#440](https://github.com/Zulko/moviepy/pull/440) ([earney](https://github.com/earney))
- fix issue 417..  unicode has no attribute shape  \(error in python 2\) [\#438](https://github.com/Zulko/moviepy/pull/438) ([earney](https://github.com/earney))
- fix Issue \#385 ,  no DirectoryClip class [\#434](https://github.com/Zulko/moviepy/pull/434) ([earney](https://github.com/earney))
- add test file for pull requests. [\#433](https://github.com/Zulko/moviepy/pull/433) ([earney](https://github.com/earney))
- put DEVNULL into compat.py [\#432](https://github.com/Zulko/moviepy/pull/432) ([earney](https://github.com/earney))
- test for issue \#145 [\#431](https://github.com/Zulko/moviepy/pull/431) ([earney](https://github.com/earney))
- fix PR \#413 . \(issue \#357\) [\#429](https://github.com/Zulko/moviepy/pull/429) ([earney](https://github.com/earney))
- fix issue 145.  raise Exception when concatenate method != chain or c… [\#428](https://github.com/Zulko/moviepy/pull/428) ([earney](https://github.com/earney))
- Readme improvements [\#425](https://github.com/Zulko/moviepy/pull/425) ([keikoro](https://github.com/keikoro))
- `Colorclip` changed `col`\>`color` [\#424](https://github.com/Zulko/moviepy/pull/424) ([tburrows13](https://github.com/tburrows13))
- Revert "small recipe \(mirroring a video\)" [\#414](https://github.com/Zulko/moviepy/pull/414) ([Zulko](https://github.com/Zulko))
- fixes \#357.  confusing error about coreader, when media file does not exist [\#413](https://github.com/Zulko/moviepy/pull/413) ([earney](https://github.com/earney))
- move PY3 to new compat.py file [\#411](https://github.com/Zulko/moviepy/pull/411) ([earney](https://github.com/earney))
- Fix Issue \#373 Trajectory.save\_list [\#394](https://github.com/Zulko/moviepy/pull/394) ([dermusikman](https://github.com/dermusikman))
- bug presented [\#390](https://github.com/Zulko/moviepy/pull/390) ([TonyChen0724](https://github.com/TonyChen0724))
- Incorporated optional progress\_bar flag for writing video to file [\#380](https://github.com/Zulko/moviepy/pull/380) ([wingillis](https://github.com/wingillis))
- Audio error handling made failsafe [\#377](https://github.com/Zulko/moviepy/pull/377) ([gyglim](https://github.com/gyglim))
- Fix issue \#354 [\#355](https://github.com/Zulko/moviepy/pull/355) ([groundflyer](https://github.com/groundflyer))
- Fixed resize documentation issue \#319 [\#346](https://github.com/Zulko/moviepy/pull/346) ([jmisacube](https://github.com/jmisacube))
- Added AAC codec to mp4 [\#345](https://github.com/Zulko/moviepy/pull/345) ([jeromegrosse](https://github.com/jeromegrosse))
- Add a test case. [\#339](https://github.com/Zulko/moviepy/pull/339) ([drewm1980](https://github.com/drewm1980))
- ImageSequenceClip: Check for fps and durations rather than fps and du… [\#331](https://github.com/Zulko/moviepy/pull/331) ([jeromegrosse](https://github.com/jeromegrosse))
- Handle bytes when listing fonts in VideoClip.py [\#306](https://github.com/Zulko/moviepy/pull/306) ([Zowie](https://github.com/Zowie))
- fix deprecation message [\#302](https://github.com/Zulko/moviepy/pull/302) ([mgaitan](https://github.com/mgaitan))
- Fix for \#274  [\#275](https://github.com/Zulko/moviepy/pull/275) ([nad2000](https://github.com/nad2000))
- Update README.rst [\#254](https://github.com/Zulko/moviepy/pull/254) ([tcyrus](https://github.com/tcyrus))
- small recipe \(mirroring a video\) [\#243](https://github.com/Zulko/moviepy/pull/243) ([zodman](https://github.com/zodman))
- Document inherited members in reference documentation [\#236](https://github.com/Zulko/moviepy/pull/236) ([achalddave](https://github.com/achalddave))
- fixed module hierarchy for Trajectory [\#215](https://github.com/Zulko/moviepy/pull/215) ([bwagner](https://github.com/bwagner))
- Fixed missing list [\#211](https://github.com/Zulko/moviepy/pull/211) ([LunarLanding](https://github.com/LunarLanding))
- Fixed copy-paste typo [\#197](https://github.com/Zulko/moviepy/pull/197) ([temerick](https://github.com/temerick))

## [v0.2.2.13](https://github.com/zulko/moviepy/tree/v0.2.2.13) (2017-02-15)

[Full Changelog](https://github.com/zulko/moviepy/compare/v0.2.2.12...v0.2.2.13)

**Implemented enhancements:**

- Add `self.filename` as a `VideoFileClip` attribute [\#405](https://github.com/Zulko/moviepy/pull/405) ([tburrows13](https://github.com/tburrows13))

**Closed issues:**

- keep github releases in sync with PyPI [\#398](https://github.com/Zulko/moviepy/issues/398)
- accidentally opened, sorry [\#397](https://github.com/Zulko/moviepy/issues/397)
- BrokenPipeError [\#349](https://github.com/Zulko/moviepy/issues/349)
- Bug in ffmpeg\_audiowriter.py for python 3 [\#335](https://github.com/Zulko/moviepy/issues/335)
- concatenate.py - Python3 incompatible [\#313](https://github.com/Zulko/moviepy/issues/313)

**Merged pull requests:**

- fix issue \#313, make concatenate\_videoclips python 3 compatible. [\#410](https://github.com/Zulko/moviepy/pull/410) ([earney](https://github.com/earney))
- Update maintainer section in README [\#409](https://github.com/Zulko/moviepy/pull/409) ([mbeacom](https://github.com/mbeacom))
- fix issue \#401 [\#403](https://github.com/Zulko/moviepy/pull/403) ([earney](https://github.com/earney))
- ensures int arguments to np.reshape; closes \#383 [\#384](https://github.com/Zulko/moviepy/pull/384) ([tyarkoni](https://github.com/tyarkoni))
- on\_color function docstring has wrong parameter [\#244](https://github.com/Zulko/moviepy/pull/244) ([cblument](https://github.com/cblument))

## [v0.2.2.12](https://github.com/zulko/moviepy/tree/v0.2.2.12) (2017-01-30)

[Full Changelog](https://github.com/zulko/moviepy/compare/v0.2.2...v0.2.2.12)

**Implemented enhancements:**

- Update version and readme to include maintainers section [\#395](https://github.com/Zulko/moviepy/pull/395) ([mbeacom](https://github.com/mbeacom))

**Closed issues:**

- Numpy 1.12.0 Breaks VideoFileClip [\#392](https://github.com/Zulko/moviepy/issues/392)
- read\_chunk\(\) breaks in numpy 1.12.0 [\#383](https://github.com/Zulko/moviepy/issues/383)
- Intel MKL FATAL ERROR: Cannot load libmkl\_avx.so or libmkl\_def.so [\#379](https://github.com/Zulko/moviepy/issues/379)
- Memory Error [\#370](https://github.com/Zulko/moviepy/issues/370)
- module 'cv2' has no attribute 'resize' [\#369](https://github.com/Zulko/moviepy/issues/369)
- Unable to load a gif created by moviepy. Fault of avconv? [\#337](https://github.com/Zulko/moviepy/issues/337)
- write\_videofile Error [\#330](https://github.com/Zulko/moviepy/issues/330)
- Does Moviepy work with a Raspberry Pi? [\#322](https://github.com/Zulko/moviepy/issues/322)
- moviepy.video.fx.all fadein and fadeout does not fade to any other color than black? [\#321](https://github.com/Zulko/moviepy/issues/321)
- Imageio: 'ffmpeg.osx' was not found on your computer; downloading it now. [\#320](https://github.com/Zulko/moviepy/issues/320)
- is there a way to composite a video with a alpha channel? [\#317](https://github.com/Zulko/moviepy/issues/317)
- ffmpeg never dies [\#312](https://github.com/Zulko/moviepy/issues/312)
- Mask Getting Called Multiple Times [\#299](https://github.com/Zulko/moviepy/issues/299)
- write\_videofile gets stuck [\#284](https://github.com/Zulko/moviepy/issues/284)
- zero-size array to reduction operation minimum which has no identity [\#269](https://github.com/Zulko/moviepy/issues/269)
- nvenc encoder nvidia [\#264](https://github.com/Zulko/moviepy/issues/264)
- Avoid writing to disk with ImageSequenceClip [\#261](https://github.com/Zulko/moviepy/issues/261)
- MemoryError [\#259](https://github.com/Zulko/moviepy/issues/259)
- Create multiple subclips using times from CSV file [\#257](https://github.com/Zulko/moviepy/issues/257)
- write\_videofile results in "No such file or directory: OSError" on AWS Lambda instance [\#256](https://github.com/Zulko/moviepy/issues/256)
- Pillow 3.0.0 drops support for `tostring\(\)` in favour of `tobytes\(\)` [\#241](https://github.com/Zulko/moviepy/issues/241)
- Add Environment Variable to overwrite FFMPEG\_BINARY [\#237](https://github.com/Zulko/moviepy/issues/237)
- Clip::subclip vs ffmpeg\_extract\_subclip? [\#235](https://github.com/Zulko/moviepy/issues/235)
- Moviepy - win2k8 64 install errors [\#234](https://github.com/Zulko/moviepy/issues/234)
- How to install MoviePy on a remote SSH server without an A/V card? [\#230](https://github.com/Zulko/moviepy/issues/230)
- Failed to read duration of file, Samsung S6 MP4s [\#226](https://github.com/Zulko/moviepy/issues/226)
- MoviePy error: FFMPEG permission error [\#220](https://github.com/Zulko/moviepy/issues/220)
- White artifacts around the image when rotating an ImageClip with a mask or just a png with transparency in angles that are not 0, 90, 180, 270 \( Added Examples to reproduce it \) [\#216](https://github.com/Zulko/moviepy/issues/216)
- Error when using ffmpeg\_movie\_from\_frames "global name 'bitrate' is not defined" [\#208](https://github.com/Zulko/moviepy/issues/208)
- Is it possible to write infinite looping videos? [\#206](https://github.com/Zulko/moviepy/issues/206)
- Problem creating VideoFileClip from URL on server [\#204](https://github.com/Zulko/moviepy/issues/204)
- Animate TextClip text value [\#199](https://github.com/Zulko/moviepy/issues/199)
- ffmpeg not available under Ubuntu 14.04 [\#189](https://github.com/Zulko/moviepy/issues/189)
- Zoom effect trembling [\#183](https://github.com/Zulko/moviepy/issues/183)
- How to match the speed of a gif after converting to a video [\#173](https://github.com/Zulko/moviepy/issues/173)
- \[Feature Request\] Zoom and Rotate [\#166](https://github.com/Zulko/moviepy/issues/166)
- Speed optimisation using multiple processes [\#163](https://github.com/Zulko/moviepy/issues/163)
- Invalid Syntax Error [\#161](https://github.com/Zulko/moviepy/issues/161)
- AudioFileClip bombs on file read [\#158](https://github.com/Zulko/moviepy/issues/158)
- Hamac example gives subprocess error [\#152](https://github.com/Zulko/moviepy/issues/152)
- unable to overwrite audio [\#151](https://github.com/Zulko/moviepy/issues/151)
- Error in /video/fx/freeze\_region.py [\#146](https://github.com/Zulko/moviepy/issues/146)
- Convert gif to video has back background at the end of the video [\#143](https://github.com/Zulko/moviepy/issues/143)
- How to conditionally chain effects? [\#138](https://github.com/Zulko/moviepy/issues/138)
- \[Feature Request\] Write output using newlines [\#137](https://github.com/Zulko/moviepy/issues/137)
- 。 [\#135](https://github.com/Zulko/moviepy/issues/135)
- How can add my logo to right top of entire mp4 video using moviepy ? [\#127](https://github.com/Zulko/moviepy/issues/127)
- numpy error on trying to concatenate [\#123](https://github.com/Zulko/moviepy/issues/123)
- NameError: global name 'clip' is not defined [\#114](https://github.com/Zulko/moviepy/issues/114)
- typo in line 626, in on\_color. elf is good for christmas, bad for function [\#107](https://github.com/Zulko/moviepy/issues/107)
- API request: clip.rotate [\#105](https://github.com/Zulko/moviepy/issues/105)
- Use graphicsmagick where available [\#90](https://github.com/Zulko/moviepy/issues/90)
- Packaging ffmpeg binary with moviepy [\#85](https://github.com/Zulko/moviepy/issues/85)
- Running VideoFileClip multiple times in django gives me error [\#73](https://github.com/Zulko/moviepy/issues/73)
- FFMPEG binary not found. [\#60](https://github.com/Zulko/moviepy/issues/60)

**Merged pull requests:**

- Fix \#164 - Resolve ffmpeg zombie processes [\#374](https://github.com/Zulko/moviepy/pull/374) ([mbeacom](https://github.com/mbeacom))
- Updated resize function to use cv2.INTER\_LINEAR when upsizing images … [\#268](https://github.com/Zulko/moviepy/pull/268) ([kuchi](https://github.com/kuchi))
- Read FFMPEG\_BINARY and/or IMAGEMAGICK\_BINARY environment variables [\#238](https://github.com/Zulko/moviepy/pull/238) ([dkarchmer](https://github.com/dkarchmer))
- Fixing a minor typo. [\#205](https://github.com/Zulko/moviepy/pull/205) ([TheNathanBlack](https://github.com/TheNathanBlack))
- Fixed minor typos in the docs [\#196](https://github.com/Zulko/moviepy/pull/196) ([bertyhell](https://github.com/bertyhell))
- added check for resolution before processing video stream [\#188](https://github.com/Zulko/moviepy/pull/188) ([ryanfox](https://github.com/ryanfox))
- Support for SRT files with any kind of newline [\#171](https://github.com/Zulko/moviepy/pull/171) ([factorial](https://github.com/factorial))
- Delete duplicated import os [\#168](https://github.com/Zulko/moviepy/pull/168) ([jsseb](https://github.com/jsseb))
- set correct lastindex variable in mask\_make\_frame [\#165](https://github.com/Zulko/moviepy/pull/165) ([Dennovin](https://github.com/Dennovin))
- fix to work with python3 [\#162](https://github.com/Zulko/moviepy/pull/162) ([laurentperrinet](https://github.com/laurentperrinet))
- poor error message from ffmpeg\_reader.py [\#157](https://github.com/Zulko/moviepy/pull/157) ([ryanfox](https://github.com/ryanfox))
- fixing region parameter on freeze\_region [\#147](https://github.com/Zulko/moviepy/pull/147) ([savannahniles](https://github.com/savannahniles))
- Typo [\#133](https://github.com/Zulko/moviepy/pull/133) ([rishabhjain](https://github.com/rishabhjain))
- setup.py: Link to website and state license [\#132](https://github.com/Zulko/moviepy/pull/132) ([techtonik](https://github.com/techtonik))
- Issue \#126 Fix FramesMatch repr and str. [\#131](https://github.com/Zulko/moviepy/pull/131) ([filipochnik](https://github.com/filipochnik))
- auto detection of ImageMagick binary on Windows [\#118](https://github.com/Zulko/moviepy/pull/118) ([carlodri](https://github.com/carlodri))
- Minor grammatical and spelling changes [\#115](https://github.com/Zulko/moviepy/pull/115) ([grimley517](https://github.com/grimley517))
- typo fix [\#108](https://github.com/Zulko/moviepy/pull/108) ([stonebig](https://github.com/stonebig))
- additional safe check in close\_proc [\#100](https://github.com/Zulko/moviepy/pull/100) ([Eloar](https://github.com/Eloar))
- Allows user to pass additional parameters to ffmpeg when writing audio clips [\#94](https://github.com/Zulko/moviepy/pull/94) ([jdelman](https://github.com/jdelman))

## [v0.2.2](https://github.com/zulko/moviepy/tree/v0.2.2) (2014-12-11)

[Full Changelog](https://github.com/zulko/moviepy/compare/98a2e81757f221bd12216b5dd4cf8ce340d3164c...v0.2.2)

**Closed issues:**

- Incorrect size being sent to ffmpeg [\#102](https://github.com/Zulko/moviepy/issues/102)
- Can't unlink file after audio extraction [\#97](https://github.com/Zulko/moviepy/issues/97)
- Hangs if using ImageMagick to write\_gif [\#93](https://github.com/Zulko/moviepy/issues/93)
- Segfault for import moviepy.editor, but not for import moviepy [\#92](https://github.com/Zulko/moviepy/issues/92)
- Is there a way to create the gif faster? [\#88](https://github.com/Zulko/moviepy/issues/88)
- syntax error with moviepy [\#87](https://github.com/Zulko/moviepy/issues/87)
- Issue in config.py [\#83](https://github.com/Zulko/moviepy/issues/83)
- not working with some youtube videos [\#82](https://github.com/Zulko/moviepy/issues/82)
- Can't add Chinese text 中文, it will become "??" in the movie file. [\#79](https://github.com/Zulko/moviepy/issues/79)
- don't read \*.mp4 file [\#75](https://github.com/Zulko/moviepy/issues/75)
- FileNotFound VideoFileClip exception, followed all the installation instructions [\#72](https://github.com/Zulko/moviepy/issues/72)
- write\_videofile jumps [\#71](https://github.com/Zulko/moviepy/issues/71)
- Problems with complex mask [\#70](https://github.com/Zulko/moviepy/issues/70)
- supress console window of popen calls if used with cx\_freeze win32gui [\#68](https://github.com/Zulko/moviepy/issues/68)
- set all filehandles to make moviepy work in cx\_freeze win32gui [\#67](https://github.com/Zulko/moviepy/issues/67)
- Setting conf.py ffmpeg path on the fly from python [\#66](https://github.com/Zulko/moviepy/issues/66)
- gif\_writers.py uses an undefined constant [\#64](https://github.com/Zulko/moviepy/issues/64)
- set\_duration ignored on TextClip [\#63](https://github.com/Zulko/moviepy/issues/63)
- Write\_Gif returns errno 2 [\#62](https://github.com/Zulko/moviepy/issues/62)
- "Bad File Descriptor" when creating VideoFileClip [\#61](https://github.com/Zulko/moviepy/issues/61)
- Create a mailing list [\#59](https://github.com/Zulko/moviepy/issues/59)
- Closing VideoFileClip [\#57](https://github.com/Zulko/moviepy/issues/57)
- TextClips can cause an Exception if the text argument starts with a '@' [\#56](https://github.com/Zulko/moviepy/issues/56)
- Cannot convert mov to gif [\#55](https://github.com/Zulko/moviepy/issues/55)
- Problem with writing audio [\#51](https://github.com/Zulko/moviepy/issues/51)
- ffmpeg\_writer.py [\#50](https://github.com/Zulko/moviepy/issues/50)
- VideoFileClip error [\#49](https://github.com/Zulko/moviepy/issues/49)
- VideoFileClip opens file with wrong width [\#48](https://github.com/Zulko/moviepy/issues/48)
- Change speed of clip based on a curve? [\#46](https://github.com/Zulko/moviepy/issues/46)
- 'to\_gif' raises IOError/OSError when no 'program' parameter is given [\#43](https://github.com/Zulko/moviepy/issues/43)
- Enhancement: loading animated gifs, passing frame range to subclip\(\) [\#40](https://github.com/Zulko/moviepy/issues/40)
- ImageClip is broken [\#39](https://github.com/Zulko/moviepy/issues/39)
- Error: wrong indices in video buffer. Maybe buffer too small. [\#38](https://github.com/Zulko/moviepy/issues/38)
- It makes pygame crash [\#37](https://github.com/Zulko/moviepy/issues/37)
- Can not load the fonts [\#36](https://github.com/Zulko/moviepy/issues/36)
- Tabs in python code [\#35](https://github.com/Zulko/moviepy/issues/35)
- Windows 8 Error [\#34](https://github.com/Zulko/moviepy/issues/34)
- infinite audio loop [\#33](https://github.com/Zulko/moviepy/issues/33)
- Specifying pix\_fmt on FFMPEG call [\#27](https://github.com/Zulko/moviepy/issues/27)
- on\_color fails with TypeError when given a col\_opacity parameter [\#25](https://github.com/Zulko/moviepy/issues/25)
-  'ValueError: I/O operation on closed file' [\#23](https://github.com/Zulko/moviepy/issues/23)
- Too stupid to rotate :D [\#22](https://github.com/Zulko/moviepy/issues/22)
- FFMPEG Error on current Debian Wheezy x64 [\#21](https://github.com/Zulko/moviepy/issues/21)
- Possible memory leak [\#18](https://github.com/Zulko/moviepy/issues/18)
- Windows - Unable to export simple sequence to gif [\#16](https://github.com/Zulko/moviepy/issues/16)
- Problems with preview + missing explanation of crop + resize not working [\#15](https://github.com/Zulko/moviepy/issues/15)
- AssertionError in ffmpeg\_reader.py [\#14](https://github.com/Zulko/moviepy/issues/14)
- ffmpeg hangs [\#13](https://github.com/Zulko/moviepy/issues/13)
- Python 3.3.3 - invalid syntax error [\#12](https://github.com/Zulko/moviepy/issues/12)
- something went wrong with the audio writing, Exit code 1 [\#10](https://github.com/Zulko/moviepy/issues/10)
- `error: string:` When trying to import from moviepy [\#9](https://github.com/Zulko/moviepy/issues/9)
- Reading video on Ubuntu 13.10 does not work [\#8](https://github.com/Zulko/moviepy/issues/8)
- List decorator and pygame as dependencies on PyPI [\#4](https://github.com/Zulko/moviepy/issues/4)
- "list index out of range" error or Arch Linux x86-64 [\#3](https://github.com/Zulko/moviepy/issues/3)
- IndexError? [\#2](https://github.com/Zulko/moviepy/issues/2)
- Can't write a movie with default codec [\#1](https://github.com/Zulko/moviepy/issues/1)

**Merged pull requests:**

- - changed none to None due to NameError [\#95](https://github.com/Zulko/moviepy/pull/95) ([Eloar](https://github.com/Eloar))
- Fix a typo in a ValueError message [\#91](https://github.com/Zulko/moviepy/pull/91) ([naglis](https://github.com/naglis))
- Changed all "== None" and "!= None" [\#89](https://github.com/Zulko/moviepy/pull/89) ([diegocortassa](https://github.com/diegocortassa))
- 'Crop' fix [\#81](https://github.com/Zulko/moviepy/pull/81) ([ccarlo](https://github.com/ccarlo))
- fix lost threads parameter from merge [\#78](https://github.com/Zulko/moviepy/pull/78) ([bobatsar](https://github.com/bobatsar))
- VideoClip.write\_videofile\(\) accepts new param: ffmpeg\_params that is put directly into ffmpeg command line [\#77](https://github.com/Zulko/moviepy/pull/77) ([aherok](https://github.com/aherok))
- make compatible with cx\_freeze in gui32 mode [\#69](https://github.com/Zulko/moviepy/pull/69) ([bobatsar](https://github.com/bobatsar))
- Fix typo in error message [\#53](https://github.com/Zulko/moviepy/pull/53) ([mekza](https://github.com/mekza))
- Fixed write\_logfile/verbose arguments [\#47](https://github.com/Zulko/moviepy/pull/47) ([KyotoFox](https://github.com/KyotoFox))
- typo [\#42](https://github.com/Zulko/moviepy/pull/42) ([tasinttttttt](https://github.com/tasinttttttt))
- Tempfile [\#31](https://github.com/Zulko/moviepy/pull/31) ([dimatura](https://github.com/dimatura))
- Fixed small typo in docs [\#30](https://github.com/Zulko/moviepy/pull/30) ([dimatura](https://github.com/dimatura))
- Fixed syntax error in io/imageMagick\_tools.py [\#29](https://github.com/Zulko/moviepy/pull/29) ([dimatura](https://github.com/dimatura))
- added -pix\_fmt yuv420p to ffmpeg args if codec is libx264 [\#28](https://github.com/Zulko/moviepy/pull/28) ([chunder](https://github.com/chunder))
- added support for aac audio codec [\#26](https://github.com/Zulko/moviepy/pull/26) ([chunder](https://github.com/chunder))
- Hopefully fixes issue \#13 for everyone. [\#24](https://github.com/Zulko/moviepy/pull/24) ([oxivanisher](https://github.com/oxivanisher))
- Reduced ffmpeg logging to prevent hanging [\#20](https://github.com/Zulko/moviepy/pull/20) ([JoshdanG](https://github.com/JoshdanG))
- fix typo in close\_proc [\#17](https://github.com/Zulko/moviepy/pull/17) ([kenchung](https://github.com/kenchung))
- PEP8 : ffmpeg\_reader [\#11](https://github.com/Zulko/moviepy/pull/11) ([tacaswell](https://github.com/tacaswell))
- Update resize.py [\#7](https://github.com/Zulko/moviepy/pull/7) ([minosniu](https://github.com/minosniu))
- Update crash\_course.rst [\#5](https://github.com/Zulko/moviepy/pull/5) ([mgaitan](https://github.com/mgaitan))



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
````

## File: CONTRIBUTING.md
````markdown
# MoviePy's Contribution Guidelines

## Communication on GitHub

- Keep messages on GitHub issues and pull requests on-topic and to the point. Be aware that each comment triggers a notification which gets sent out to a number of people.
  - Opinions are OK.
  - For longer or more in-depth discussions, use the [MoviePy Gitter](https://gitter.im/movie-py/Lobby). If these discussions lead to a decision, like a merge/reject, please leave a message on the relevant MoviePy issue to document the outcome of the discussion/the reason for the decision.
- Do not push any commit that changes the API without prior discussion.

## Preparing for development

- Fork the official MoviePy repository to your own GitHub account:  
Use the "Fork" button in the top right corner of the GitHub interface while viewing [the official MoviePy](https://github.com/Zulko/moviepy) repository.
- Use your fork as the basis for cloning the repository to your local machine: `$ git clone URL_TO_YOUR_FORK`  
You can get the appropriate URL (SSH- or HTTPS-based) by using the green "Code" button located at the top right of the repository view while looking at your fork. By default, Git refers to any remote you clone from – i.e. in this case your fork on GitHub – as `origin`.
- Enter your local clone and add the official MoviePy repository as a second remote, with alias `upstream`:  
`$ git remote add upstream git@github.com:Zulko/moviepy.git` (using SSL) _or_   
`$ git remote add upstream https://github.com/Zulko/moviepy.git` (using HTTPS).
- Install the library inside a [virtual environment](https://docs.python.org/3/tutorial/venv.html) with all dependencies included using `$ pip install -e ".[optional,doc,test,lint]"`
- Configure pre-commit hooks running `$ pre-commit install`

## Coding conventions, code quality
 
- Respect [PEP8](https://www.python.org/dev/peps/pep-0008/) conventions.
- Add just the "right" amount of comments. Try to write auto-documented code with very explicit variable names.
- If you introduce new functionality or fix a bug, document it in the docstring or with code comments.
- MoviePy's team adopted [pre-commit](https://pre-commit.com/) to run code checks using black, flake8 and isort, so make sure that you've configured the pre-commit hooks with `pre-commit install`. 


## Standard contribution workflow

### Local development
- Keep your local `master` branch up-to-date with the official repo's master by periodically fetching/pulling it:  
`$ git pull upstream master`
- Never make changes on `master` directly, but branch off into separate develop branches:  
`$ git checkout --branch YOUR_DEVELOP_BRANCH`  
Ideally, these are given names which function as keywords for what you are working on, and are prefixed with `fix_` (for bug fixes), `feature_` or something similarly appropriate and descriptive.
- Base any changes you submit on the most recent `master`.

More detailed explanation of the last point:

It is likely that the official repo's `master` branch will move on (get updated, have other PRs merged into it) while you are working on your changes. Before creating a pull request, you will have to make sure your changes are not based on outdated code. For this reason, it makes sense to avoid falling "too much behind" while developing by rebasing your local `master` branch at intervals. Make sure your `master` branch is in sync with the official `master` branch (as per the first point), then, while checked into your develop branch, run: `$ git rebase master`

If you **haven't rebased before**, make sure to **familiarise yourself** with the concept.

### Submitting Pull Requests

You do not have to have finished your feature or bug fix before submitting a PR; just mention that it still is a work in progress.

Before submitting PRs:

- run the test suite over your code to expose any problems: `$ pytest`
- push your local develop branch to your GitHub fork `$ git push origin YOUR_DEVELOP_BRANCH`

When you now look at your forked repo on your GitHub account, you will see GitHub suggest branches for sending pull requests to the official `Zulko/moviepy` repository.

Once you open a PR, you will be presented with a template which you are asked to fill out. You are encouraged to add any additional information which helps provide further context to your changes, and to link to any issues or PRs which your pull request references or is informed by.

On submitting your PR, an automated test suite runs over your submission, which might take a few minutes to complete. In a next step, a MoviePy maintainer will review your code and, if necessary, help you to get it merge-ready.
````

## File: Dockerfile
````dockerfile
FROM python:3

# Install ffmpeg to get ffplay using system package manager
RUN apt-get -y update && apt-get -y install ffmpeg

# Install some special fonts we use in testing, etc..
RUN apt-get -y install fonts-liberation

RUN apt-get install -y locales && \
    locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8

ENV LC_ALL C.UTF-8

# Update pip
RUN pip install --upgrade pip

ADD . /moviepy
RUN cd /moviepy && pip install . && pip install .[test] && pip install .[doc] && pip install .[lint]
````

## File: LICENCE.txt
````
The MIT License (MIT)

Copyright (c) 2015 Zulko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
````

## File: MANIFEST.in
````
include *.txt
recursive-include docs *
include *.rst
````

## File: pyproject.toml
````toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "moviepy"
version = "2.1.2"
description = "Video editing with Python"
readme = "README.md"
license = { text = "MIT License" }
authors = [{ name = "Zulko 2025" }]
keywords = ["video", "editing", "audio", "compositing", "ffmpeg"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Multimedia",
    "Topic :: Multimedia :: Sound/Audio",
    "Topic :: Multimedia :: Sound/Audio :: Analysis",
    "Topic :: Multimedia :: Video",
    "Topic :: Multimedia :: Video :: Capture",
    "Topic :: Multimedia :: Video :: Conversion",
]
dependencies = [
    "decorator>=4.0.2,<6.0",
    "imageio>=2.5,<3.0",
    "imageio_ffmpeg>=0.2.0",
    "numpy>=1.25.0",
    "proglog<=1.0.0",
    "python-dotenv>=0.10",
    "pillow>=9.2.0",
]

[project.optional-dependencies]
doc = [
    "numpydoc<2.0",
    "Sphinx==6.*",
    "pydata-sphinx-theme==0.13",
    "sphinx_design",
]
test = [
    "coveralls>=3.0,<4.0",
    "pytest-cov>=2.5.1,<3.0",
    "pytest>=3.0.0,<7.0.0",
]
lint = [
    "black>=23.7.0",
    "flake8>=6.0.0",
    "flake8-absolute-import>=1.0",
    "flake8-docstrings>=1.7.0",
    "flake8-rst-docstrings>=0.3",
    "flake8-implicit-str-concat==0.4.0",
    "isort>=5.12",
    "pre-commit>=3.3",
]

[tool.setuptools.packages.find]
include = ["moviepy*"]
exclude = ["media", "tests", "docs"]
````

## File: README.md
````markdown
# MoviePy


[![MoviePy page on the Python Package Index](https://badge.fury.io/py/moviepy.svg)](https://pypi.org/project/moviepy/) [![Discuss MoviePy on Gitter](https://img.shields.io/gitter/room/movie-py/gitter?color=46BC99&logo=gitter)](Gitter_) [![Build status on gh-actions](https://img.shields.io/github/actions/workflow/status/Zulko/moviepy/test_suite.yml?logo=github)](https://github.com/Zulko/moviepy/actions/workflows/test_suite.yml) [![Code coverage from coveralls.io](https://img.shields.io/coveralls/github/Zulko/moviepy/master?logo=coveralls)](https://coveralls.io/github/Zulko/moviepy?branch=master)

> [!NOTE]
> MoviePy recently upgraded to v2.0, introducing major breaking changes. You can consult the last v1 docs [here](https://zulko.github.io/moviepy/v1.0.3/) but beware that v1 is no longer maintained. For more info on how to update your code from v1 to v2, see [this guide](https://zulko.github.io/moviepy/getting_started/updating_to_v2.html).

MoviePy (online documentation [here](https://zulko.github.io/moviepy/)) is a Python library for video editing: cuts, concatenations, title insertions, video compositing (a.k.a. non-linear editing), video processing, and creation of custom effects.

MoviePy can read and write all the most common audio and video formats, including GIF, and runs on Windows/Mac/Linux, with Python 3.9+.

# Example

In this example we open a video file, select the subclip between 10 and
20 seconds, add a title at the center of the screen, and write the
result to a new file:

``` python
from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# Load file example.mp4 and keep only the subclip from 00:00:10 to 00:00:20
# Reduce the audio volume to 80% of its original volume

clip = (
    VideoFileClip("long_examples/example2.mp4")
    .subclipped(10, 20)
    .with_volume_scaled(0.8)
)

# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip(
    font="Arial.ttf",
    text="Hello there!",
    font_size=70,
    color='white'
).with_duration(10).with_position('center')

# Overlay the text clip on the first video clip
final_video = CompositeVideoClip([clip, txt_clip])
final_video.write_videofile("result.mp4")
```

# How MoviePy works

Under the hood, MoviePy imports media (video frames, images, sounds) and converts them into Python objects (numpy arrays) so that every pixel becomes accessible, and video or audio effects can be defined in just a few lines of code (see the [built-in effects]() for examples).

The library also provides ways to mix clips together (concatenations, playing clips side by side or on top of each other with transparency, etc.). The final clip is then encoded back into mp4/webm/gif/etc.

This makes MoviePy very flexible and approachable, albeit slower than using ffmpeg directly due to heavier data import/export operations.  


# Installation

Intall moviepy with `pip install moviepy`. For additional installation options, such as a custom FFMPEG or for previewing, see [this section](https://zulko.github.io/moviepy/getting_started/install.html). For development, clone that repo locally and install with `pip install -e .`

# Documentation

The online documentation ([here](https://zulko.github.io/moviepy/)) is automatically built at every push to the master branch. To build the documentation locally, install the extra dependencies via `pip install moviepy[doc]`, then go to the `docs` folder and run `make html`.

# Contribute

MoviePy is open-source software originally written by
[Zulko](https://github.com/Zulko) and released under the MIT licence.
The project is hosted on [GitHub](https://github.com/Zulko/moviepy),
where everyone is welcome to contribute and open issues or give feedback Please read our [Contributing
Guidelines](https://github.com/Zulko/moviepy/blob/master/CONTRIBUTING.md).
To ask for help or simply discuss usage and examples, use [our Reddit channel](https://www.reddit.com/r/moviepy/).

# Maintainers

## Active maintainers
-   [Zulko](https://github.com/Zulko) (owner)
-   [@osaajani](https://github.com/OsaAjani) led the development of v2 ([MR](https://github.com/Zulko/moviepy/pull/2024))
-   [@tburrows13](https://github.com/tburrows13)
-   [@keikoro](https://github.com/keikoro)

## Past maintainers and thanks
-   [@mgaitan](https://github.com/mgaitan)
-   [@earney](https://github.com/earney)
-   [@mbeacom](https://github.com/mbeacom)
-   [@overdrivr](https://github.com/overdrivr)
-   [@ryanfox](https://github.com/ryanfox)
-   [@mondeja](https://github.com/mondeja)

**Maintainers wanted!** this library has only been kept afloat by the involvement of its maintainers, and there are times where none of us have enough bandwidth. We'd love to hear about developers interested in giving a hand and solving some of the issues (especially the ones that affect you) or reviewing pull requests. Open
an issue or contact us directly if you are interested. Thanks!
````

## File: setup.cfg
````
[flake8]
max-line-length = 88
extend-ignore =
    # Black compatibility
    E203,
    W503,
    # allow lambda expressions
    E731,
    # don't require docstrings for public packages
    D104,
    # don't require docstrings for magic methods
    D105,
    # don't require summary and description in docstrings
    D205,
    # allow first line of docstrings not ending in period (too much limited)
    D400,
    # allow first line of docstrings being not imperative (too much intrusive)
    D401,
    # allow blank lines between section headers and their content in docstrings
    D412,
    # allow composed `__all__` statements
    RST902,
    # allow 'from moviepy import *' in editor.py
    F403, F405
per-file-ignores =
    # allow imports not placed at the top of the file
    # allow 'from moviepy import *' in editor.py
    moviepy/editor.py: E402, F403, F405
    # the version file doesn't require module docstring
    moviepy/version.py: D100
    # FX modules don't require module docstring
    moviepy/audio/fx/*.py: D100
    moviepy/video/fx/*.py: D100
    # tests doesn't require docstring (although is recommended)
    tests/*.py: D101,D102,D103
    # examples don't require module docstring
    # allow 'from moviepy import *' in examples
    examples/*.py: D100, F403, F405
docstring-convention = numpy

# Complexity should be decreased before uncomment:
#max-complexity = 10

[isort]
profile = black
lines_after_imports = 2
combine_as_imports = True
py_version = 39
known_tests_third_party = pytest
sections = STDLIB,THIRDPARTY,TESTS_THIRD_PARTY,FIRSTPARTY,LOCALFOLDER

[coverage:report]
exclude_lines =
    pragma: no cover
````
