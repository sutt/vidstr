import argparse
import os
import time
import uuid
import yaml
import json
import re

from dotenv import load_dotenv
from google import genai
from google.genai import types
from get_frame import get_frame
from client import get_client, download_from_gcs
from concat_vid import concatenate_videos
# from PIL import Image

load_dotenv()


def load_config(
    section: str, profile_path: str | None = None, default_config_path="config.yaml"
):
    """Loads a config section from YAML files, with profile overriding defaults."""
    # Load defaults
    config = {}
    if os.path.exists(default_config_path):
        with open(default_config_path, "r") as f:
            default_yaml = yaml.safe_load(f)
            if default_yaml:
                config = default_yaml.get(section, {})

    # Load profile and override
    if profile_path and os.path.exists(profile_path):
        print(f"Loading profile settings from: {profile_path}")
        with open(profile_path, "r") as f:
            profile_yaml = yaml.safe_load(f)
            if profile_yaml:
                profile_section = profile_yaml.get(section, {})
                config.update(profile_section)

    return config


def get_unique_filepath(filepath):
    """
    Generates a unique filepath by appending an incremental counter.
    It strips numeric suffixes (e.g., '_123') from the base filename first.
    e.g., 'image.png' -> 'image-001.png', 'image_01.png' -> 'image-001.png'
    """
    directory, filename = os.path.split(filepath)
    name, ext = os.path.splitext(filename)

    # Strip numeric suffix like _123 from the end of the name
    name = re.sub(r"_\d+$", "", name)

    counter = 1
    while True:
        new_filename = f"{name}-{counter:03d}{ext}"
        new_filepath = os.path.join(directory, new_filename)
        if not os.path.exists(new_filepath):
            return new_filepath
        counter += 1




def generate_images(client: genai.Client, prompt: str, output_dir: str, config: dict):
    """Generates images from a prompt and saves them to a directory."""
    config = config.copy()
    image_model = config.pop("model", "imagen-4.0-generate-preview-06-06")
    number_of_images = config.get("number_of_images", 1)
    print(f"Generating {number_of_images} image(s) for prompt: '{prompt}'")

    os.makedirs(output_dir, exist_ok=True)

    response = client.models.generate_images(
        model=image_model,
        prompt=prompt,
        config=types.GenerateImagesConfig(**config),
    )

    mime_type_ext = {
        "image/png": ".png",
        "image/jpeg": ".jpg",
    }
    ext = mime_type_ext.get(config.get("output_mime_type"), ".png")

    for i, generated_image in enumerate(response.generated_images):
        image_path = os.path.join(output_dir, f"image_{i}{ext}")
        unique_image_path = get_unique_filepath(image_path)
        generated_image.image.save(unique_image_path)
        print(f"Saved image to {unique_image_path}")


def generate_video(
    client: genai.Client,
    prompt: str,
    output_dir: str,
    input_image_path: str | None,
    input_video_path: str | None,
    last_frame_path: str | None,
    config: dict,
    gcs_output_bucket: str,
):
    """Generates a video from a prompt and saves it to a directory."""
    print(f"Generating video for prompt: '{prompt}'")

    os.makedirs(output_dir, exist_ok=True)

    input_image = None
    if input_image_path:
        print(f"Using initial image from: {input_image_path}")
        input_image = types.Image.from_file(location=input_image_path)

    last_frame = None
    if last_frame_path:
        print(f"Using last frame from: {last_frame_path}")
        last_frame = types.Image.from_file(location=last_frame_path)

    input_video = None
    if input_video_path:
        print(f"Using initial video from: {input_video_path}")
        input_video = types.Video.from_file(location=input_video_path)

    is_vertex = os.environ.get("GOOGLE_GENAI_USE_VERTEXAI") == "true"
    
    # Generate unique filename for bucket output
    prefix = "video"
    if input_video_path:
        prefix = os.path.splitext(os.path.basename(input_video_path))[0]
    elif input_image_path:
        prefix = os.path.splitext(os.path.basename(input_image_path))[0]
    unique_id = str(uuid.uuid4())[:8]
    bucket_output_uri = f"{gcs_output_bucket}/{prefix}-{unique_id}"

    # Configure operation based on whether we're using Vertex AI
    video_config = config.copy()
    video_model = video_config.pop("model", "veo-2.0-generate-001")
    if last_frame:
        video_config["last_frame"] = last_frame

    if is_vertex:
        video_config["output_gcs_uri"] = bucket_output_uri
        operation = client.models.generate_videos(
            model=video_model,
            prompt=prompt,
            image=input_image,
            video=input_video,
            config=types.GenerateVideosConfig(**video_config),
        )
        print(f"Using bucket output: {bucket_output_uri}")
    else:
        operation = client.models.generate_videos(
            model=video_model,
            prompt=prompt,
            image=input_image,
            video=input_video,
            config=types.GenerateVideosConfig(**video_config),
        )

    print("Waiting for video generation to complete...")
    while not operation.done:
        time.sleep(10)
        operation = client.operations.get(operation)


    if operation.error:
        print(f"ERROR: Video generation failed: {json.dumps(operation.error)}")
        return None

    if is_vertex:
        # For Vertex AI with bucket output, the video is in the GCS bucket
        video = operation.result.generated_videos[0]
        gcs_uri = video.video.uri
        print(f"Video generated and saved to GCS bucket: {gcs_uri}")

        video_path = os.path.join(output_dir, "video.mp4")
        unique_video_path = get_unique_filepath(video_path)
        print(f"Downloading video from GCS to {unique_video_path}...")
        download_from_gcs(gcs_uri, unique_video_path)
        return unique_video_path
    else:
        # For Gemini API, check operation.response
        if not operation.response:
            print("ERROR: Video generation completed but returned no response.")
            return None
            
        video = operation.response.generated_videos[0]
        video_path = os.path.join(output_dir, "video.mp4")
        unique_video_path = get_unique_filepath(video_path)
        print(f"Downloading video to {unique_video_path}...")
        client.files.download(file=video.video)
        video.video.save(unique_video_path)
        print(f"Saved video to {unique_video_path}")
        return unique_video_path


def loop_video(
    client: genai.Client,
    prompt: str,
    output_dir: str,
    input_video_path: str,
    config: dict,
    gcs_output_bucket: str,
):
    """Creates a looping video by generating a transition from the last frame to the first frame."""
    print(f"Creating a loop for video '{input_video_path}' with prompt: '{prompt}'")

    if not os.path.exists(input_video_path):
        print(f"Error: Input video not found at {input_video_path}")
        return

    os.makedirs(output_dir, exist_ok=True)

    last_frame_path = get_unique_filepath(
        os.path.join(output_dir, "tmp.loop_last_frame.png")
    )
    print(f"Extracting last frame to {last_frame_path}...")
    get_frame(
        video_path=input_video_path, frame_type="last", output_path=last_frame_path
    )

    first_frame_path = get_unique_filepath(
        os.path.join(output_dir, "tmp.loop_first_frame.png")
    )
    print(f"Extracting first frame to {first_frame_path}...")
    get_frame(
        video_path=input_video_path, frame_type="first", output_path=first_frame_path
    )

    # Now call generate_video with the extracted frames
    return generate_video(
        client=client,
        prompt=prompt,
        output_dir=output_dir,
        input_image_path=last_frame_path,
        input_video_path=None,
        last_frame_path=first_frame_path,
        config=config,
        gcs_output_bucket=gcs_output_bucket,
    )


def continue_video(
    client: genai.Client,
    prompt: str,
    output_dir: str,
    input_video_path: str,
    num_vids: int,
    config: dict,
    gcs_output_bucket: str,
):
    """Continues a video from a prompt and an existing video."""
    if not os.path.exists(input_video_path):
        print(f"Error: Input video not found at {input_video_path}")
        return

    # Keep track of all video parts for concatenation
    video_parts = [input_video_path]
    current_video = input_video_path

    for i in range(num_vids):
        print(f"\n--- Continuing video: iteration {i + 1}/{num_vids} ---")
        print(f"Using '{current_video}' as input.")

        # Now call generate_video with the video
        new_video_path = generate_video(
            client=client,
            prompt=prompt,
            output_dir=output_dir,
            input_image_path=None,
            input_video_path=current_video,
            last_frame_path=None,
            config=config,
            gcs_output_bucket=gcs_output_bucket,
        )

        if not new_video_path:
            print("Failed to generate video continuation. Aborting.")
            return

        print(f"Generated new video segment: {new_video_path}")
        video_parts.append(new_video_path)
        current_video = new_video_path

    if len(video_parts) > 1:
        print(f"\n--- Concatenating {len(video_parts)} video parts ---")
        timestamp = time.strftime("%H%M%S")
        output_filename = f"concat-{timestamp}.mp4"
        output_path = os.path.join(output_dir, output_filename)

        try:
            concatenate_videos(video_files=video_parts, output_path=output_path)
            print(f"Successfully created extended video: {output_path}")
        except Exception as e:
            print(f"Error during concatenation: {e}")
    else:
        print("No new videos were generated to concatenate.")


def extend_video(
    client: genai.Client,
    prompt: str,
    num_vids: int,
    input_video_path: str,
    config: dict,
    gcs_output_bucket: str,
):
    """Extends a video by generating continuations and concatenating them."""
    if not os.path.exists(input_video_path):
        print(f"Error: Input video not found at {input_video_path}")
        return

    output_dir = os.path.dirname(input_video_path)
    if not output_dir:
        output_dir = "."

    # Keep track of all video parts for concatenation
    video_parts = [input_video_path]
    current_video = input_video_path

    for i in range(num_vids):
        print(f"\n--- Extending video: iteration {i + 1}/{num_vids} ---")
        print(f"Using '{current_video}' as input.")

        last_frame_path = os.path.join(output_dir, "last_frame.png")
        print(f"Extracting last frame to {last_frame_path}...")
        get_frame(
            video_path=current_video, frame_type="last", output_path=last_frame_path
        )

        # Now call generate_video with the extracted frame
        new_video_path = generate_video(
            client=client,
            prompt=prompt,
            output_dir=output_dir,
            input_image_path=last_frame_path,
            input_video_path=None,
            last_frame_path=None,
            config=config,
            gcs_output_bucket=gcs_output_bucket,
        )

        if not new_video_path:
            print("Failed to generate video continuation. Aborting.")
            return

        print(f"Generated new video segment: {new_video_path}")
        video_parts.append(new_video_path)
        current_video = new_video_path

    if len(video_parts) > 1:
        print(f"\n--- Concatenating {len(video_parts)} video parts ---")
        timestamp = time.strftime("%H%M%S")
        output_filename = f"concat-{timestamp}.mp4"
        output_path = os.path.join(output_dir, output_filename)

        try:
            concatenate_videos(video_files=video_parts, output_path=output_path)
            print(f"Successfully created extended video: {output_path}")
        except Exception as e:
            print(f"Error during concatenation: {e}")
    else:
        print("No new videos were generated to concatenate.")


def main():
    workspace_config = load_config("workspace_setting")
    gcs_output_bucket = workspace_config.get("gcs_output_bucket", "gs://default-bucket")
    
    # Use caller's directory if called via vidstr script, 
    # otherwise use config,see README.md#scripting
    if "VIDSTR_CALLER_DIR" in os.environ:
        local_output_dir = os.environ["VIDSTR_CALLER_DIR"]
    else:
        local_output_dir = workspace_config.get("local_output_dir", "data/tmp")

    parser = argparse.ArgumentParser(
        description="Generate images or video from a text prompt."
    )
    parser.add_argument(
        "--vertex", action="store_true", help="Use Vertex AI instead of Gemini API."
    )
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        help="Path to a profile.yaml for custom configuration.",
    )
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="sub-command help"
    )

    # Image generation subcommand
    parser_image = subparsers.add_parser("image", help="Generate images.")
    parser_image.add_argument(
        "prompt", type=str, help="The text prompt for image generation."
    )
    parser_image.add_argument(
        "-n",
        "--number-of-images",
        type=int,
        default=None,
        help="Number of images to generate.",
    )
    parser_image.add_argument(
        "-o",
        "--output-dir",
        type=str,
        default=local_output_dir,
        help="Directory to save generated images.",
    )

    # Video generation subcommand
    parser_video = subparsers.add_parser("video", help="Generate a video.")
    parser_video.add_argument(
        "prompt", type=str, help="The text prompt for video generation."
    )
    parser_video.add_argument(
        "-i",
        "--input-image",
        type=str,
        help="Path to an initial image for the video.",
    )
    parser_video.add_argument(
        "-v",
        "--input-video",
        type=str,
        help="Path to an initial video for video extension.",
    )
    parser_video.add_argument(
        "-l",
        "--last-frame",
        type=str,
        help="Path to an image to use as the last frame for interpolation.",
    )
    parser_video.add_argument(
        "-o",
        "--output-dir",
        type=str,
        default=local_output_dir,
        help="Directory to save generated video.",
    )

    # Video continuation subcommand
    parser_continue_video = subparsers.add_parser(
        "continue-video", help="Continue a video from its last frame."
    )
    parser_continue_video.add_argument(
        "-p",
        "--prompt",
        type=str,
        default="",
        help="The text prompt for video generation.",
    )
    parser_continue_video.add_argument(
        "-i",
        "--input-video",
        type=str,
        required=True,
        help="Path to an existing video to continue from.",
    )
    parser_continue_video.add_argument(
        "-n",
        "--num-vids",
        type=int,
        default=1,
        help="Number of video segments to generate and append.",
    )
    parser_continue_video.add_argument(
        "-o",
        "--output-dir",
        type=str,
        default=local_output_dir,
        help="Directory to save generated video and last frame.",
    )

    # Video extension subcommand
    parser_extend_video = subparsers.add_parser(
        "extend-video", help="Extend a video from last frame (multi-turn)."
    )
    parser_extend_video.add_argument(
        "-v",
        "--video",
        type=str,
        required=True,
        help="Path to an existing video to extend from.",
    )
    parser_extend_video.add_argument(
        "-n",
        "--num-vids",
        type=int,
        default=1,
        help="Number of video segments to generate and append.",
    )
    parser_extend_video.add_argument(
        "-p",
        "--prompt",
        type=str,
        required=True,
        help="The text prompt for video generation.",
    )

    # Video looping subcommand
    parser_loop_video = subparsers.add_parser(
        "loop-video",
        help="Create a looping video by generating a transition from the last to the first frame.",
    )
    parser_loop_video.add_argument(
        "-v",
        "--video-input",
        type=str,
        required=True,
        help="Path to an existing video to loop.",
    )
    parser_loop_video.add_argument(
        "-p",
        "--prompt",
        type=str,
        required=True,
        help="The text prompt for video generation.",
    )
    parser_loop_video.add_argument(
        "-o",
        "--output-dir",
        type=str,
        default=local_output_dir,
        help="Directory to save generated video and frames.",
    )

    args = parser.parse_args()

    # Resolve relative paths against caller's directory
    if "VIDSTR_CALLER_DIR" in os.environ:
        caller_dir = os.environ["VIDSTR_CALLER_DIR"]
        
        # Resolve output directory
        if hasattr(args, "output_dir") and args.output_dir and not os.path.isabs(args.output_dir):
            args.output_dir = os.path.join(caller_dir, args.output_dir)
        
        # Resolve input paths
        if hasattr(args, "input_image") and args.input_image and not os.path.isabs(args.input_image):
            args.input_image = os.path.join(caller_dir, args.input_image)
        
        if hasattr(args, "input_video") and args.input_video and not os.path.isabs(args.input_video):
            args.input_video = os.path.join(caller_dir, args.input_video)
        
        if hasattr(args, "last_frame") and args.last_frame and not os.path.isabs(args.last_frame):
            args.last_frame = os.path.join(caller_dir, args.last_frame)
        
        if hasattr(args, "video") and args.video and not os.path.isabs(args.video):
            args.video = os.path.join(caller_dir, args.video)
        
        if hasattr(args, "video_input") and args.video_input and not os.path.isabs(args.video_input):
            args.video_input = os.path.join(caller_dir, args.video_input)

    if args.vertex:
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "true"
    else:
        # CLI flag takes precedence, default to Gemini API
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "false"

    # Determine profile path
    profile_path = None
    if args.config:
        if os.path.exists(args.config):
            profile_path = args.config
        else:
            print(f"Warning: Specified profile file not found: {args.config}")
    else:
        # Search in output_dir then root
        search_paths = []
        if hasattr(args, "output_dir") and args.output_dir:
            search_paths.append(os.path.join(args.output_dir, "profile.yaml"))
        search_paths.append("profile.yaml")

        for p in search_paths:
            if os.path.exists(p):
                profile_path = p
                break

    client = get_client()
    video_config = load_config("video_generation", profile_path=profile_path)
    image_config = load_config("image_generation", profile_path=profile_path)

    if args.command == "image":
        if args.number_of_images is not None:
            image_config["number_of_images"] = args.number_of_images

        generate_images(
            client=client,
            prompt=args.prompt,
            output_dir=args.output_dir,
            config=image_config,
        )
    elif args.command == "video":
        generate_video(
            client=client,
            prompt=args.prompt,
            output_dir=args.output_dir,
            input_image_path=args.input_image,
            input_video_path=args.input_video,
            last_frame_path=args.last_frame,
            config=video_config,
            gcs_output_bucket=gcs_output_bucket,
        )
    elif args.command == "continue-video":
        continue_video(
            client=client,
            prompt=args.prompt,
            output_dir=args.output_dir,
            input_video_path=args.input_video,
            num_vids=args.num_vids,
            config=video_config,
            gcs_output_bucket=gcs_output_bucket,
        )
    elif args.command == "extend-video":
        extend_video(
            client=client,
            prompt=args.prompt,
            num_vids=args.num_vids,
            input_video_path=args.video,
            config=video_config,
            gcs_output_bucket=gcs_output_bucket,
        )
    elif args.command == "loop-video":
        # client must be vertex for last_frame property
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "true"
        client = get_client()
        loop_video(
            client=client,
            prompt=args.prompt,
            output_dir=args.output_dir,
            input_video_path=args.video_input,
            config=video_config,
            gcs_output_bucket=gcs_output_bucket,
        )


if __name__ == "__main__":
    main()
