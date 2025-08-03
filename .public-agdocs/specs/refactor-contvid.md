refactor the continue-video command to work like extend-video.  
- One main difference: whereas extend-video uses a frame to run "video -i <first_frame>" continue-video will do "video -v <first_video>".
    - since we're continuing a video, no need to get_frame and extract a frame
    - the downloaded video will be already have been concatenated with the previous video, so no need to perform that functionality here.
- make prompt argument use -p flag instead of being positional and make it optional
- add an -n argument to repeat this process multiple times