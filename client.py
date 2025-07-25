import os
import google.genai as genai
from google.cloud import storage


def get_client() -> genai.Client:
    """
    Initializes and returns the genai.Client, configured for either
    Gemini API or Vertex AI based on environment variables.
    """
    use_vertex = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "false").lower() == "true"

    if use_vertex:
        project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
        location = os.environ.get("GOOGLE_CLOUD_LOCATION")
        if not project_id or not location:
            raise ValueError(
                "For Vertex AI, GOOGLE_CLOUD_PROJECT and GOOGLE_CLOUD_LOCATION must be set."
            )
        print(f"Connecting to Vertex AI project:{project_id} location:{location}")
        client = genai.Client(vertexai=True, project=project_id, location=location)
    else:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY must be set for Gemini API.")
        print("Connecting to Gemini API...")
        client = genai.Client(api_key=api_key)

    return client


def test_connection(client: genai.Client):
    """
    Tests the connection to the API by listing available models.
    """
    try:
        print("Testing connection by listing models...")
        next(client.models.list())
        print("Successfully connected.")
        return True
    except Exception as e:
        print(f"Connection test failed: {e}")
        return False


def download_from_gcs(gcs_uri: str, destination_file_path: str):
    """
    Downloads a file from a GCS URI to a local path.
    gcs_uri should be in the format gs://bucket_name/path/to/blob
    """
    if not gcs_uri.startswith("gs://"):
        raise ValueError(f"Invalid GCS URI: {gcs_uri}. Must start with gs://")

    # Using ADC, no explicit credentials needed if running in a configured environment
    storage_client = storage.Client()

    try:
        bucket_name, blob_name = gcs_uri[5:].split("/", 1)
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        # Ensure the destination directory exists
        destination_dir = os.path.dirname(destination_file_path)
        if destination_dir:
            os.makedirs(destination_dir, exist_ok=True)

        blob.download_to_filename(destination_file_path)
        print(f"Successfully downloaded {gcs_uri} to {destination_file_path}")
    except Exception as e:
        print(f"Failed to download {gcs_uri}. Error: {e}")
        raise


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    client = get_client()
    test_connection(client)
