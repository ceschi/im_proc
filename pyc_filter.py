
'''
Very simple script to split videos
in their frames and then do things
on single frames
'''


# import a bunch of pkgs and fcts

# import skimage
# from skimage import data, io
import numpy as np
from matplotlib import pyplot as plt
import shutil
from progressbar import ProgressBar

import os
from os.path import join
import time as timer

pbar = ProgressBar()
start_t = timer.time()

###################################
tol = 1.8 # tolerance level, critical!
###################################


# cool, go to test dir
# os.chdir(r"C:\Users\emanu\jpy_ntbs\pics"))

# now, the script shall operate within
# the folder where the frames are,
# so it mainly works on local wd

wd = os.getcwd()

# get a list of all files excluding folders
# make sure it's only jpg later

photo_files = [i for i in os.listdir(wd) if os.path.isfile(join( wd, i ) )]
photo_files.remove('pyc_filter.py')


# now create apposite dir if
# not existent already
if os.path.isdir('./selected_frames'):
    print('Folder already present')
else:
    os.mkdir('selected_frames')
    print('Folder created')

# this will expand to get all photos' names
# that are good
good_ones =[]
dest_path = join(wd, 'selected_frames')

# now, the big big loop

start_loop = timer.time()

for i in pbar(photo_files):    
    img = plt.imread(i)
    thresh = np.mean(img, axis = 2).mean()
    
    if thresh>=tol:
        good_ones.append(i)
        cp_path = join(wd, i)
        shutil.copy(cp_path, join(dest_path, i))

end_loop = timer.time()




print('loop with %s files done in %f minutes: %d files were kept!' %
      (len(photo_files), (end_loop - start_loop)/60, len(good_ones))
      )