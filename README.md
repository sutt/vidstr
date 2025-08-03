# Vidstr

Create continuous loop videos from cli.

See [simple tutorial](./docs/tutorial-v1.md) for loops in the docs.

### Resources
See write-up on initial progress building with [Agro](https://github.com/sutt/agro): [Agro-Builds-Vidster-1](https://github.com/sutt/agro/blob/master/docs/case-studies/aba-vidster-1.md), which contains a write-up of findings from this [agro experiment](https://github.com/sutt/demo-agro-ext-lib) for using non standard-lib packages.

Also, see [DevLog](./docs/dev-log-v1.md)

### Setup

Add 

```bash
# set either this one for gemini api mode on client
GEMINI_API_KEY=123...
# or set these to the vertex-ai project and account
GOOGLE_GENAI_USE_VERTEXAI=true
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
```
Run `python client.py` to verify auth.

#### gcloud ADC

```
gcloud config list  # if not set to right project/account
gcloud config set project YOUR_PROJECT_ID
gcloud config set account YOUR_ACCOUNT_EMAIL

gcloud auth application-default login --no-browser
```
- copy command to windows gcloud, paste something like a callback to loclahost:8085 back into wsl2 terminal (will also need to mods config default in windows gcloud)
- should produce /home/user/.config/gcloud/application_Default_credentials.json

### Commands

```
usage: main.py [-h] [--vertex] [-c CONFIG]
               {image,video,continue-video,extend-video,loop-video} ...

Generate images or video from a text prompt.

positional arguments:
  {image,video,continue-video,extend-video,loop-video}
                        sub-command help
    image               Generate images.
    video               Generate a video.
    continue-video      Continue a video from previous video (mutli-turn).
    extend-video        Extend a video from last frame (multi-turn).
    loop-video          Create a looping video by generating a transition from
                        the last to the first frame.

options:
  -h, --help            show this help message and exit
  --vertex              Use Vertex AI instead of Gemini API.
  -c CONFIG, --config CONFIG
                        Path to a profile.yaml for custom configuration.

```

```
# utils
client.py

get_frame.py [-h] [--frame {first,last}] [-n NUM_FRAME] [-o OUTPUT] video_path

# direct generation
main.py [-c CONFIG] [--vertex] image [-n NUMBER_OF_IMAGES] [-o OUTPUT_DIR] prompt

main.py [-c CONFIG] [--vertex] video [-i INPUT_IMAGE] [-l LAST_FRAME] [-v INPUT_VIDEO] [-o OUTPUT_DIR] prompt

# generation helpers
main.py extend-video -v VIDEO [-n NUM_VIDS] -p PROMPT

main.py continue-video -v VIDEO [-n NUM_VIDS] [-p PROMPT]

main.py loop-video -v VIDEO_INPUT -p PROMPT
```

### Scripting

Add this bash script to your path to call this package anywhere:

**vidstr**
```bash
#!/bin/bash
# Pass the original working directory as an environment variable
VIDSTR_CALLER_DIR="$PWD" uv run --directory /path/to/vidstr "$@"
```

### Configs

Defaults for models and parameters load from [config.yaml](./config.yaml).

Add a `profile.yaml` to override any settings here:
- You can point to this file with `-c` on main.py
- The default location is repo root to avoid the -c flag.
- The main default location for this profile, if specifying an output dir (with `-o` flag in commands) is within the output dir itself, e.g. `python main.py video -o data/tmp 'astronaut riding a horse'` will look to load `data/tmp/profile.yaml` if it exists.

**config.yaml**
```yaml
# Default configuration for video generation
video_generation:
  model: "veo-2.0-generate-001" # alternative: "veo-3.0-generate-preview"
  number_of_videos: 1
  duration_seconds: 8
  aspect_ratio: "16:9"
  enhance_prompt: true
  # all settings below not supported in gemini-api, only vertex, 
  # leave below fields commented out for compatibility
  # seed: 42
  # negative_prompt: ""
  # person_generation: "allow" # "allow" or "disallow"
  # fps: 24
  # generate_audio: false
  # not supported in vertex-api either
  # resolution: "720p" # e.g., "1080p", "720p"  # 1080p not supported veo-2
  # compression_quality: "OPTIMIZED" # "LOSELESS"

# Default configuration for image generation
image_generation:
  model: "imagen-4.0-generate-preview-06-06" # alternative: "imagen-4.0-ultra-generate-preview-06-06"
  number_of_images: 1
  aspect_ratio: "16:9" # "1:1", "3:4", "4:3", "9:16", "16:9"
  guidance_scale: 7.5
  person_generation: "ALLOW_ADULT" # "DONT_ALLOW", "ALLOW_ADULT", "ALLOW_ALL"
  output_mime_type: "image/png" # "image/png" or "image/jpeg"
  # all settings below not supported in gemini-api, only vertex, 
  # leave below fields commented out for compatibility
  # language: "en" # "auto", "en", "ja", "ko", "hi", "zh", "pt", "es"
  # enhance_prompt: true
  # seed: 42
  # negative_prompt: ""

# Default workspace settings:
workspace_setting:
  gcs_output_bucket: "gs://hello-world-123"
  local_output_dir: "data/"

```

### Testing setup

Run `./test-simple.sh` to do all operations:

```
$ ./test-simple.sh 
# create image ----
Connecting to Gemini API...
Generating 1 image(s) for prompt: 'an astronuat riding a horse'
Saved image to data/simple-test-output/image_0.png

# create video (simple) ----
Connecting to Gemini API...
Generating video for prompt: 'an astronaut riding a horse'
Waiting for video generation to complete...
Downloading video to data/simple-test-output/video.mp4...
Saved video to data/simple-test-output/video.mp4

# create video (starting frame) ----
Connecting to Gemini API...
Generating video for prompt: 'moving shot, from boat moving down the river camera pans across lush forest and wildlife'
Using initial image from: data/simple-test/stub_river1_first_frame.png
Waiting for video generation to complete...
Downloading video to data/simple-test-output/video-0001.mp4...
Saved video to data/simple-test-output/video-0001.mp4

# create video (starting video, on vertex) ----
Connecting to Vertex AI project:aigen-1-465619 location:us-central1
Generating video for prompt: ''
Using initial video from: data/simple-test/river1.mp4
Using bucket output: gs://hello-world-123/river1-d8fdc34a
Waiting for video generation to complete...
Video generated and saved to GCS bucket: gs://hello-world-123/river1-d8fdc34a/10779344510781587145/sample_0.mp4

# continue-video (with starting frame) ----
Connecting to Gemini API...
Continuing video from 'data/simple-test/river1.mp4' with prompt: 'moving shot, from boat moving down the river camera pans across lush forest and wildlife'
Extracting last frame to data/simple-test-output/last_frame.png...
Saved last frame to data/simple-test-output/last_frame.png
Generating video for prompt: 'moving shot, from boat moving down the river camera pans across lush forest and wildlife'
Using initial image from: data/simple-test-output/last_frame.png
Waiting for video generation to complete...
Downloading video to data/simple-test-output/video-0002.mp4...
Saved video to data/simple-test-output/video-0002.mp4

final result of output dir ----
image_0.png  last_frame.png  video-0001.mp4  video-0002.mp4  video.mp4
```

# Simple Tutorial for Vidstr
_August 2, 2025_

We'll create a simple fireplace looped video here. It's not the coolest, but it pretty fool proof and requires a small number of steps.

> **Note**: We'll be using Veo2 in this tutorial since using sophisticated paramaters for video generation is not yet Generally Available for Veo3.

### Setup

First, enable scripting be following the [scripting section](./../README.md#scripting) in the readme. Now you can call vistr in any directory and read/write files there.

Then setup the authentication in the `.env`. For this tutorial you will need **vertex** authentication since it uses the `last_frame` parameter for video generation.

Now create a fresh directory where you'll create and re-use assets:

```bash
mkdir my-first-loop
cd my-first-loop
```

### Setup the workspace

1.) Create some helper files:

```bash
touch gen.sh profile.yaml instruct.img.conf instruct.vid.conf
chmod +x gen.sh
```
These files will:
- `gen.sh` this is were you'll 

2.) Now add starter content to these files:

Into **profile.yaml**

_This will override the settings in the [default config](../config.yaml)._

```yaml
image_generation:
  aspect_ratio: "16:9"
video_generation:
  duration_seconds: 5
  aspect_ratio: "16:9"
```

Into **gen.sh**

_This will be used to run reproducible vidstr commands. Note the top section is utility function we'll copy into each new workspace but are not strictly nec._

```bash
## utility functions ----
run_logged() {
    PYTHONUNBUFFERED=1 stdbuf -oL -eL "$@" 2>&1 | tee -a log.log
}

read_prompt() {
    # remove comments ("#"), line breaks and whitespace 
    local file="$1"
    if [[ ! -f "$file" ]]; then
        echo "Error: File not found: $file" >&2
        return 1
    fi
    grep -v '^\s*#' "$file" | tr '\n' ' ' | sed 's/  */ /g' | sed 's/^ *//;s/ *$//'
}

## intital image choice ----
PROMPT=$(read_prompt instruct.img.conf)
ARGS=(
    main.py
    image
    -n 4
    "$PROMPT"
)
run_logged vidstr "${ARGS[@]}"
```

Into **instruct.img.conf**

_This is where you put the prompt for the inital images you create._

```conf
a fireplace with a medium size fire
```

> **Tip**: You can use multi-line and comments to iterate on your prompts, see the [Appendix](./tutorial-v1.md#appendix) section on this.

### Generate initial images

Since images are 100x cheaper than videos, let's generate some initial images so we can get the best style

Run `./gen.sh` to execute the program which should generate `image-001.png, ... image-004.png` into your current working directory.

The output will look like this:

```bash
Connecting to Gemini API...
Loading profile settings from: /home/user/dev/smol-projs/art-vidstr/pkgs/river.1/profile.yaml
Loading profile settings from: /home/user/dev/smol-projs/art-vidstr/pkgs/river.1/profile.yaml
Generating 4 image(s) for prompt: 'photograph from a boat moving down the river in tropical forest'
Saved image to /home/user/dev/smol-projs/art-vidstr/pkgs/river.1/image-001.png
Saved image to /home/user/dev/smol-projs/art-vidstr/pkgs/river.1/image-002.png
Saved image to /home/user/dev/smol-projs/art-vidstr/pkgs/river.1/image-003.png
Saved image to /home/user/dev/smol-projs/art-vidstr/pkgs/river.1/image-004.png
```
> **Note**: When you run the script a `log.log` file will be created which should contain all the stdout and stderr that your commands produce. This is useful for debugging and referencing and reproducing how you generated the assets

Look through each of these pictures, either create more by running the script again, and/or refining the prompt in `instruct.img.conf` when you have the image that looks like the video you want to create move onto the next step...

> **Tip**: You may want to augment your image generation by setting in `profile.yaml` the image_generation.model parameter to `"imagen-4.0-ultra-generate-preview-06-06"` which is the best model available currently.

![img-002.png](./docs/assets/image-002.png)
![img-003.png](./docs/assets/image-003.png)

### Generate first video

Head back to your **gen.sh** and comment out the generate images functionality and adding the new functionality. Assuming the image you like is image-003.png

```bash
## intital image choice ----
# PROMPT=$(read_prompt instruct.img.2.conf)
# ARGS=(
#     main.py
#     # --vertex
#     image
#     -n 4
#     # -n 1
#     "$PROMPT"
# )
# run_logged vidstr "${ARGS[@]}"

## gen video #1
PROMPT=$(read_prompt instruct.vid.1.conf)
BASE_IMG="image-003.png"
ARGS=(
    main.py
    video
    -i "$BASE_IMG"
    "$PROMPT"
)
run_logged vidstr "${ARGS[@]}"
```

And add a video prompt here (separate from the image prompt) which will include camera directions in addition to the content desired:

**instruct.vid.conf**

```conf
a stationary camera 
with no zoom in and no zoom out 
observes the fire in the fireplace burning
```

_Giving instructions to abstain from camera movement is important here since it make looping easier and smoother._

Now run `./gen.sh` again which should create `video-001.mp4` of 5 seconds (that was set in profile.yaml). It will also appended the operations to `log.log`. 

If the video looks good move onto the next step...

![fire1.gif](./docs/assets/fire1.gif)

### Generate second video "loopback"

Let's modify the **gen.sh** by commenting out the previous section and running another video creation command `loop-video`.

```bash
## gen video #1
#PROMPT=$(read_prompt instruct.vid.1.conf)
#BASE_IMG="image-003.png"
#ARGS=(
#    main.py
#    video
#    -i "$BASE_IMG"
#    "$PROMPT"
#)
#run_logged vidstr "${ARGS[@]}"
# create loop back off of video001

PROMPT=$(read_prompt instruct.vid.conf)
BASE_VID="video-001.mp4"
ARGS=(
    main.py
    loop-video
    -v "$BASE_VID"
    -p "$PROMPT"
)
run_logged vidstr "${ARGS[@]}"
```

When this runs you'll notice two files are created: `tmp.loop_first_frame-001.png` and `tmp.loop_last_frame-001.png`. These correspond to the first and last frame of the first video are used as targets for this loop back video.

Take a look at this video, if it matches the style of the first video well enough, let's move onto our last step...

![fire2.gif](./docs/assets/fire2.gif)

> **Tip**: You'll also notice we're using the same prompt file for this video as the original video. That's fine here since there's nothing new we're adding in here but you can change this to assist the loop back. Also we're keeping this video as 5 seconds, but ordinarily the loop back video should be a max duration (8 seconds) to give it the most chance to smoothly transition to desired ending frame.

### Concatenate videos to create infinite loop

Combine the initial video with the loopback to create an infinite loop. We're using `vidstr concat_vid.py` script to do this which uses opencv under the hood.

```bash
# turn to videos into a 2x loop
VID1="video-001.mp4"
VID2="video-002.mp4"
OUTPUT_FN="loop.fireplace-1.mp4"
ARGS=(
    concat_vid.py
    --files "$VID1", "$VID2"
    -o tmp.both.mp4
)
run_logged vidstr "${ARGS[@]}"
ARGS=(
    concat_vid.py
    --files tmp.both.mp4, tmp.both.mp4
    -o "$OUTPUT_FN"
)
run_logged vidstr "${ARGS[@]}"
```

This has now created a 20 second video - `loop-fireplace-1.mp4` of two full loops:
- video-001: (5 sec)
- video-002: (5 sec)
- video-001: (5 sec)
- video-002: (5 sec)

We can inspect this for any transitions that aren't smooth and reproduce videos as nec.

_Congrats if you've made it this far, now cozy up to the fire and ponder what you could create next!_

![fire-loop-1.gif](./docs/assets/fire-loop-1.gif)

### Appendix

##### Using .conf files for prompts

Getting the right image often requires iterating on prompts, the best way to have fine control here is to use multiple lines to comment things in and out. However image and video models don't understand multilines and ignoring comments so that's what the `read_prompt` utility function in the gen.sh script does.

Here's an example of one where there was experiment with _what_ the artist wanted and _how_ the artist was requesting to the model to get it.

```conf
# moving shot from inside driving car 
POV drivers seat
at night
no rain
# # rainy night
# # no windshield wipers
# # windshield wipers off
# # no windshield wipers
cruising medium speed
building move by in the background
# vintage sports car
no motion blur
```

When this .conf file is read in by the script, it passes the video generation prompt parameter a single-line prompt with the commented lines removed, in this case:

> POV drivers seat at night no rain cruising medium speed building move by in the background no motion blur

The reason we use `.conf` extension is because it enables the commenting in/out with shortcut keys (VScode), but doesn't run langserver errors for natural language.