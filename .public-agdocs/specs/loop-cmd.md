Add a "loop-video" command to main.py.

This command has the following args:
- optional: -o / --output-dir OUTPUT_DIR
- required: -v / --video-input VIDEO_PATH
- required: -p / --prompt (or positionally last) PROMPT

This command will implement the existing functionality represented by the pseudo code below:
last_frame = get_frame(VIDEO_PATH, frame_type="last")
first_frame = get_frame(VIDEO_PATH, frame_type="first")
client = get_client(vertex=True)
generate_video(
    client, 
    prompt=PROMPT, 
    input_image_path=last_frame,  # yes, set this to last_frame
    last_frame_path=first_frame,  # yes, set this to first_frame
)

