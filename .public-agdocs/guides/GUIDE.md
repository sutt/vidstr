# Vidstr 
Utilize google-genai client to to query and generate veo and imagegen models.


### model conventions
- for image generation utilize model: "imagen-4.0-ultra-generate-preview-06-06"
    - docs: https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-ultra-generate-preview-06-06
- for video generation utilize mode: "veo-2.0-generate-001"
    - docs: https://cloud.google.com/vertex-ai/generative-ai/docs/models/veo/2-0-generate-001

### client api documentation
- there is a copy of the readme from the github project for the package (https://raw.githubusercontent.com/googleapis/python-genai/refs/heads/main/README.md) in python-genai.md,
- additional documentation is available on the web at:
    - https://googleapis.github.io/python-genai/index.html
    - https://googleapis.github.io/python-genai/genai.html
    - https://github.com/googleapis/python-genai

### api conventions
- Will have some functionality for gemini api-key auth and some vertex auth. Default is gemini api key auth.

### coding agent guidance
- should be available in AGENTS.md