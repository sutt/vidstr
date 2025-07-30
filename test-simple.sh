# test the main functionality
# uses directories: 
# - data/simple-test/
# - data/simple-test-output/

# make sure to activate environment before running
# source .venv/bin/activate

# run this to reset
# rm data/simple-test-output/*

# Start tests...

echo "# create image ----"
python main.py image -o data/simple-test-output 'an astronuat riding a horse'
echo ""

echo "# create video (simple) ----"
python main.py video -o data/simple-test-output 'an astronaut riding a horse'
echo ""

echo "# create video (starting frame) ----"
python main.py video -i data/simple-test/stub_river1_first_frame.png -o data/simple-test-output  'moving shot, from boat moving down the river camera pans across lush forest and wildlife'
echo ""

echo "# create video (starting video, on vertex) ----"
python main.py --vertex video -v data/simple-test/river1.mp4 -o data/simple-test-output  ''
echo ""

echo "# continue-video (with starting frame) ----"
python main.py continue-video -i data/simple-test/river1.mp4 -o data/simple-test-output  'moving shot, from boat moving down the river camera pans across lush forest and wildlife'
echo ""

echo "# create video (starting frame + last frame) ----"
python main.py --vertex video -i data/simple-test/stub_river1_last_frame.png -l data/simple-test/stub_river1_first_frame.png -o data/simple-test-output 'moving shot, from boat moving down the river camera pans across lush forest and wildlife'
echo ""

echo "# get_frame.py: first frame both ways ----"
python get_frame.py --frame first -o data/simple-test-output data/simple-test/river1.mp4
python get_frame.py -n 0          -o data/simple-test-output data/simple-test/river1.mp4
git diff --no-index data/simple-test-output/river1_first_frame.png data/simple-test-output/river1_frame_0.png
echo "no output from the above git diff command is expected behavior"
echo ""

echo "final result of output dir ----"
ls data/simple-test-output