
Here's a traceback from a current run at new functionality, what could be wrong? add possible fixes and debugging statements.

> python main.py --vertex video -v data/dump/stadium-1.mp4  'camera continues to pan across the stadium of cheering fans' 
        Using initial video from: data/dump/stadium-1.mp4
        Waiting for video generation to complete...
        File "/home/user/dev/smol-projs/vidstr/main.py", line 96, in generate_video
            video = operation.response.generated_videos[0]
        AttributeError: 'NoneType' object has no attribute 'generated_videos'