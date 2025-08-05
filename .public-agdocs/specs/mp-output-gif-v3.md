Specs:
Create a util module with its own cli that takes an mp4 and outputs a gif: make mp4_to_gif.py at root
- use the moviepy package to do this. 
    - moviepy 2.2.1 is currently installed.
- the output gif should be set to infinite play 
- the output gif should use unique_fn functionality to increment a counter if the file already exists
- Add an fps cli param for this util
- add the associated vidstr VIDSTR_CALLER_DIR directory overrides that all the other modules do.
- add pytests for the main functionality in this request
- a test mp4 is availble at ./docs/test-assets/demo.mp4

Acceptance Criteria:
- create output valid demo-001.gif in docs/test-assets (or similiarly named asset)
    - make sure this file has a > 0 kB size to ensure it's working
- new tests are written for the functionality
- all tests pass (or tests are marked as xfail)

Worflows:
- continue running commands and tests until you are able to meet the acceptance criteria
- use --fps 2 for call to the mp4_to_gif utility (to make processing faster) and use the demo video assets i docs/test-assets/demo.mp4 as the input.
- you may mark tests XFAIL if you can't get them to run succesfully