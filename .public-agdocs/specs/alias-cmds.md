currently:
    continue-video: only takes input video
        - TODO: make prompt optional
    extend-video:
        - frame-based, but takes video path as input
        - num_vids, can scale 
    video:
        - completely open to -i, -v, -l
        - could separate the pure gen from video continue

desired:
    nomenclature:
        - gen video input=frame src=img-gen
        - gen video input=frame src=prev-video
        - gen video input=video src=prev-video