# Vidstr

Create continuous loop videos from cli.

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
get_frame.py [--frame {first,last}] [-o OUTPUT] video_path

main.py [-c CONFIG] [--vertex] image [-n NUMBER_OF_IMAGES] [-o OUTPUT_DIR] prompt

main.py [-c CONFIG] [--vertex] video [-i INPUT_IMAGE] [-l LAST_FRAME] [-v INPUT_VIDEO] [-o OUTPUT_DIR] prompt

main.py [-c CONFIG] continue-video [-h] -i INPUT_VIDEO [-o OUTPUT_DIR] prompt

client.py
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