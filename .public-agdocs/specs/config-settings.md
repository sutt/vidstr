Add the following to config.yaml:

# Default workspace settings:
workspace_setting:
  gcs_output_bucket: "gs://hello-world-123"
  local_output_dir: "data/"

And pipe these config loads into main.py
- local_output_dir is overwritten by cli args