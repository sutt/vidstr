create an option to connect to vertex ai with the client, with the following hep from the documentation:
>client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

- add the nec env vars to .env.example
- create a function that establishes a test connection to see if auth works for the client and the api