# test the main functionality
# uses directories: 
# - data/simple-test/
# - data/simple-test-output/

# run this to reset
# rm data/simple-test-output/*

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

echo "final result of output dir ----"
ls data/simple-test-output