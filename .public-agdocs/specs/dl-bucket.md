add functionality to download created products from gcs bucket.

for example video_gen with vertex often exports to a gcs bucket. that product should be downloaded to the (default or specified) output directory with a unique fn.

Assume the the script does have access via ADC to the relevant GCP project and bucket, as can be seen in client.py with vertex connection.