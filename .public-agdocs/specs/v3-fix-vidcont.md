
Here's a traceback from a current run at new functionality, what could be wrong? add possible fixes and debugging statements.

> python main.py --vertex video -v data/dump/stadium-1.mp4  'camera continues to pan across the stadium of cheering fans' 
        Using initial video from: data/dump/stadium-1.mp4
        Waiting for video generation to complete...
        File "/home/user/dev/smol-projs/vidstr/main.py", line 96, in generate_video
            video = operation.response.generated_videos[0]
        AttributeError: 'NoneType' object has no attribute 'generated_videos'

use the following documentation of how the vertex-api works to help fix and debug. Do not implemented buckets in your solution but instead focus on differences in syntax of reponse obj, etc

import time
from google import genai
from google.genai.types import GenerateVideosConfig, Video

client = genai.Client()

# TODO(developer): Update and un-comment below line
# output_gcs_uri = "gs://your-bucket/your-prefix"

operation = client.models.generate_videos(
    model="veo-2.0-generate-001",
    prompt="a butterfly flies in and lands on the flower",
    video=Video(
        uri="gs://cloud-samples-data/generative-ai/video/flower.mp4",
    ),
    config=GenerateVideosConfig(
        aspect_ratio="16:9",
        output_gcs_uri=output_gcs_uri,
    ),
)

while not operation.done:
    time.sleep(15)
    operation = client.operations.get(operation)
    print(operation)

if operation.response:
    print(operation.result.generated_videos[0].video.uri)

# Example response:
# gs://your-bucket/your-prefix