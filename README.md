This repository contains our code for AIC19 track3 at CVPRW19.

Requirements:
    Python 3
    Caffe
    Opencv 3
    Pytorch 0.4

1. Run bg.py to produce background and frontgroung frames for every videos, and save them in ./test_bg_imgs and ./test_fg_imgs respectively.

2. Run detection on all test videos in "./detection" directory.

3. Run all scripts in ./preprocess directory to make video masks, locate_stuck and filter unsuitable bboxes.

4. Run tracking codes to obtain the final results in './SOT'
