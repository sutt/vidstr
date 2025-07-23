Use the following example documentation (and the reference in demo.py) to create a create video function that can be called in main cli. add logic to switch between create image and create video. add the starting image argument of the video as an optional parameter that will be loaded from the filesystem.

import time
from google import genai

client = genai.Client()

prompt = "Panning wide shot of a calico kitten sleeping in the sunshine"

# Step 1: Generate an image with Imagen
imagen = client.models.generate_images(
    model="imagen-3.0-generate-002",
    prompt=prompt,
)

# Step 2: Generate video with Veo 2 using the image
operation = client.models.generate_videos(
    model="veo-2.0-generate-001",
    prompt=prompt,
    image=imagen.generated_images[0].image,
)

# Poll the operation status until the video is ready
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the video
video = operation.response.generated_videos[0]
client.files.download(file=video.video)
video.video.save("veo2_with_image_input.mp4")
print("Generated video saved to veo2_with_image_input.mp4")