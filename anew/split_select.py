import cv2
from sys import argv
import os
from os.path import join
import shutil
import time
from matplotlib import pyplot as plt
import numpy as np

# store args from script cmd
video_file = argv[1]
tol = float(argv[2])

# where are you?
wd = os.getcwd()

# create folders for splits and selected
name = os.path.basename(video_file)
name = os.path.splitext(name)[0]

frms = join(wd,name + '_frames')
if os.path.isdir(frms):
    print('\nFrames folder already present.')
else:
    os.mkdir(frms)

slct = join(wd,'_selected_frames')
if os.path.isdir(slct):
    print('\nFolder for selected frames already present.')
else:
    os.mkdir(slct)
    

# Part I: split the video in frames

# open conn to video
video_cap = cv2.VideoCapture(video_file)
success, image = video_cap.read()
count = 0

# loop over frames
split_1 = time.time()
while success:
    cv2.imwrite(join(frms, 'frame_%d.jpg' % count), image)
    success, image = video_cap.read()
    count += 1
    
split_2 = time.time()
    
print('\nDone with splitting frames. It took %d seconds and generated about %d files.' %
         (round(split_2 - split_1), count)
     )

# Part II: select frames with some brightness level
frames_list = [i for i in os.listdir(frms) if os.path.isfile(join(frms, i))]

selected = []

select_1 = time.time()

for l in frames_list:
    img = plt.imread(join(frms, l))
    threshold = np.mean(img, axis = 2).mean()
    
    if threshold >= tol:
        selected.append(l)
        shutil.copy(join(frms, l), join(slct, l))

select_2 = time.time()

print('\nSelection with %d threshold done. It took %d seconds, filtered %d files out of %d.' %
     (tol, round(select_2-select_1), len(selected), len(frames_list)))