let's control the base filenames for the output of assets and vary these by the command that is outputting them:
image: img.gen
video:
- w/o any: -i, -v, -l: vid.gen
- w/: -i: vid.cont
- w/: -i -l: vid.loop
- w/: -v: vid.extend