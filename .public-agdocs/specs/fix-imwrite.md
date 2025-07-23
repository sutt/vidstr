(vidstr) user@DESKTOP-1EB4G00:~/dev/smol-projs/vidstr$ python get_frame.py data/tmp/video_0.mp4 --frame "first" -o data/tmp | clipout
Traceback (most recent call last):
  File "/home/user/dev/smol-projs/vidstr/get_frame.py", line 82, in <module>
    main()
  File "/home/user/dev/smol-projs/vidstr/get_frame.py", line 78, in main
    get_frame(args.video_path, args.frame, args.output)
  File "/home/user/dev/smol-projs/vidstr/get_frame.py", line 47, in get_frame
    cv2.imwrite(output_path, image)
cv2.error: OpenCV(4.12.0) /io/opencv/modules/imgcodecs/src/loadsave.cpp:1051: error: (-2:Unspecified error) could not find a writer for the specified extension in function 'imwrite_'
