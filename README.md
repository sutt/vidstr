# Vidstr

Create continuous loop videos from cli.

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
get_frame.py [-h] [--frame {first,last}] [-o OUTPUT] video_path

main.py image [-h] [-n NUMBER_OF_IMAGES] [-o OUTPUT_DIR] prompt

main.py video [-h] [-i INPUT_IMAGE] [-v INPUT_VIDEO] [-o OUTPUT_DIR] prompt

main.py video [-h] [-i INPUT_IMAGE] [-v INPUT_VIDEO] [-o OUTPUT_DIR] prompt

main.py continue-video [-h] -i INPUT_VIDEO [-o OUTPUT_DIR] prompt

client.py

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