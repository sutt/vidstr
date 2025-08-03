Create a module concat_vid.py in this workspace which will concatenate multiple videos (of the mp4 variety).
- Create the module such that it can be run by cli as a script, or imported into main to be used within other commands.
- Basic cli guidance for concat_vid.py: 
    - must supply one the following:
        - optional arg: --files [vid_path_1, vid_path_2, etc] (comma separated or other standard practice form to pass multiple paths to videos)
        - optional arg: --dir [path/to/vidfiles/] (concatenate all mp4's in this directory)
    - if --files supplied: concatenate the videos in order they are passed.
    - if --dir supplied: concatenate the videos in ASC alphabetic order, e.g: if the dir pass has {vid-1.mp4, vid-3.mp4, vid-2.mp4} concatenate them as [vid-1, vid-2, vid3].
- Raise warnings or errors as nec when completing the task.
- Add tests for edge behaviors.
- Suggested to utilize pypi package MoviePy with method moviepy.video.compositing.CompositeVideoClip.concatenate_videoclips.
    - help docs available here: https://zulko.github.io/moviepy/reference/reference/moviepy.video.compositing.CompositeVideoClip.concatenate_videoclips.html#moviepy.video.compositing.CompositeVideoClip.concatenate_videoclips
    - help pasted below:

Help docs:
moviepy.video.compositing.CompositeVideoClip.concatenate_videoclips
moviepy.video.compositing.CompositeVideoClip.concatenate_videoclips(clips, method='chain', transition=None, bg_color=None, is_mask=False, padding=0)[source]
Concatenates several video clips.

Returns a video clip made by clip by concatenating several video clips. (Concatenated means that they will be played one after another).

There are two methods:

method=”chain”: will produce a clip that simply outputs the frames of the successive clips, without any correction if they are not of the same size of anything. If none of the clips have masks the resulting clip has no mask, else the mask is a concatenation of masks (using completely opaque for clips that don’t have masks, obviously). If you have clips of different size and you want to write directly the result of the concatenation to a file, use the method “compose” instead.

method=”compose”, if the clips do not have the same resolution, the final resolution will be such that no clip has to be resized. As a consequence the final clip has the height of the highest clip and the width of the widest clip of the list. All the clips with smaller dimensions will appear centered. The border will be transparent if mask=True, else it will be of the color specified by bg_color.

The clip with the highest FPS will be the FPS of the result clip.

Parameters
:
clips – A list of video clips which must all have their duration attributes set.

method – “chain” or “compose”: see above.

transition – A clip that will be played between each two clips of the list.

bg_color – Only for method=’compose’. Color of the background. Set to None for a transparent clip

padding – Only for method=’compose’. Duration during two consecutive clips. Note that for negative padding, a clip will partly play at the same time as the clip it follows (negative padding is cool for clips who fade in on one another). A non-null padding automatically sets the method to compose.





