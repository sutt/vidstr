Running the convert to gif gets stuck for mutliple minutes and never terminates. Debug and fix

user@DESKTOP-1EB4G00:~/dev/smol-projs/vidstr$ uv run util/mp4_to_gif.py notes/tmp/loop.fire.style-1.mp4 
MoviePy - Building file notes/tmp/loop.fire.style-1.gif with imageio.
^CTraceback (most recent call last):                                                       
  File "/home/user/dev/smol-projs/vidstr/util/mp4_to_gif.py", line 39, in <module>
    main()
  File "/home/user/dev/smol-projs/vidstr/util/mp4_to_gif.py", line 32, in main
    convert_mp4_to_gif(args.input_file, output_file, args.fps)
  File "/home/user/dev/smol-projs/vidstr/util/mp4_to_gif.py", line 10, in convert_mp4_to_gif
    clip.write_gif(gif_path, fps=fps, loop=0)
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/decorator.py", line 235, in fun
    return caller(func, *(extras + args), **kw)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/moviepy/decorators.py", line 53, in requires_duration
    return func(clip, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/decorator.py", line 235, in fun
    return caller(func, *(extras + args), **kw)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/moviepy/decorators.py", line 24, in convert_masks_to_RGB
    return func(clip, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/decorator.py", line 235, in fun
    return caller(func, *(extras + args), **kw)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/moviepy/decorators.py", line 102, in wrapper
    return func(*new_args, **new_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/moviepy/video/VideoClip.py", line 519, in write_gif
    write_gif_with_imageio(
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/decorator.py", line 235, in fun
    return caller(func, *(extras + args), **kw)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/moviepy/decorators.py", line 53, in requires_duration
    return func(clip, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/decorator.py", line 235, in fun
    return caller(func, *(extras + args), **kw)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/moviepy/decorators.py", line 153, in wrapper
    return func(clip, *new_args, **new_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/moviepy/video/io/gif_writers.py", line 15, in write_gif_with_imageio
    with iio.imopen(filename, "w", plugin="pillow") as writer:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/imageio/core/v3_plugin_api.py", line 367, in __exit__
    self.close()
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/imageio/plugins/pillow.py", line 144, in close
    self._flush_writer()
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/imageio/plugins/pillow.py", line 485, in _flush_writer
    primary_image.save(self._request.get_file(), **self.save_args)
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/PIL/Image.py", line 2588, in save
    save_handler(self, fp, filename)
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/PIL/GifImagePlugin.py", line 790, in _save_all
    _save(im, fp, filename, save_all=True)
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/PIL/GifImagePlugin.py", line 803, in _save
    if not save_all or not _write_multiple_frames(im, fp, palette):
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/PIL/GifImagePlugin.py", line 672, in _write_multiple_frames
    im_frame = _normalize_mode(im_frame.copy())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/PIL/GifImagePlugin.py", line 527, in _normalize_mode
    im = im.convert("P", palette=Image.Palette.ADAPTIVE)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/dev/smol-projs/vidstr/.venv/lib/python3.12/site-packages/PIL/Image.py", line 1097, in convert
    im = self.im.quantize(colors)
         ^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt