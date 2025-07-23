create an imageclient.models.generate_images call in a function in main.py
look at demo.py for an existing generate_videos example
here's the docs for doing a simple
```
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

response = client.models.generate_images(
    model='imagen-4.0-generate-preview-06-06',
    prompt='Robot holding a red skateboard',
    config=types.GenerateImagesConfig(
        number_of_images= 4,
    )
)
for generated_image in response.generated_images:
  generated_image.image.show()
```
- use: MODEL = "imagen-4.0-ultra-generate-preview-06-06"
create a cli in main for calling this function with a prompt arg and other optional params
have the image(s) created be downloaded to data/tmp and parametrize where they go
