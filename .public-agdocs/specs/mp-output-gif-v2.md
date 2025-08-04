Create a util module with its own cli that takes an mp4 and outputs a gif: make mp4_to_gif.py at root
- use the moviepy package to do this. moviepy 2.2.1 is currently installed.
- the output gif should be set to infinite play 
- the output gif should use unique_fn functionality to increment a counter if the file already exists
- add the associated vidstr VIDSTR_CALLER_DIR directory overrides that all the other modules do.
- add pytests for this functionality.
- a test mp4 is availble at ./docs/assets/loop.fire.style-1.mp4