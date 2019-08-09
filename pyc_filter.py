# python script to select images



# import a bunch of pkgs and fcts

import skimage
from skimage import data, io
import numpy as np
from matplotlib import pyplot as plt
import shutil


import os, sys
import time as timer

start_t = timer.time()

###################################
tol = 1.8 # tolerance level, critical!
###################################


# cool, go to test dir
os.chdir(r"C:\Users\emanu\jpy_ntbs\pics")

# get a list of all files excluding folders
# make sure it's only jpg later

photo_files = [i for i in os.listdir(os.getcwd()) if os.path.isfile( os.path.join( os.getcwd(), i ) )]

# now create apposite dir if
# not existent already
if os.path.isdir('./filter_dir'):
    print('Folder already present')
else:
    os.mkdir('filter_dir')
    print('Folder created')

# this will expand to get all photos' names
# that are good
good_ones =[]
dest_path = r"C:\Users\emanu\jpy_ntbs\pics\filter_dir"

# now, the big big loop

start_loop = timer.time()

for i in photo_files:    
    img = plt.imread(i)
    thresh = np.mean(img, axis = 2).mean()
    
    if thresh>=tol:
        good_ones.append(i)
        cp_path = os.path.join(os.getcwd(), i)
        shutil.copy(cp_path, os.path.join(dest_path, i))

end_loop = timer.time()


start_moving = timer.time()
#for j in good_ones:
 #   cp_path = os.path.join(os.getcwd(), j)
  #  shutil.copy(cp_path, os.path.join(dest_path, j))
    
end_moving = timer.time()

print('loop with %s files done in %f minutes: %d files were kept!\n\nMoving took %f seconds' %
      (len(photo_files), (end_loop - start_loop)/60, len(good_ones), (end_moving - start_moving)))