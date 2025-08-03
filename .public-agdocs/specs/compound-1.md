Build an "extend-video" command into main.py that takes as input:
-v / --video <input_video>
-n / --num-vids <num_vids> 
-p / --prompt <prompt>
--vertex (optional)

Then perform this loop <num_vids> times:
python main.py [--vertex] continue-video -i <input_video> -o <filepath for input_video>
(if --vertex is specified in extend-video command then add the vertex flag to the continue-video invokation)

Finally run:
python concat_vid.py --dir <filepath for input_video> -o <filepath for input_video/concat-{ctime MM:SS}.mp4>

Don't call these processes by shelling out / doing cli but instead use the functions which these commands implement.