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

main.py continue-video [-h] -i INPUT_VIDEO [-o OUTPUT_DIR] prompt

client.py

```