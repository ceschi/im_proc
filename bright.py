#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
from matplotlib import pyplot as plt
import shutil
import os 
from os.path import join
from PIL import Image, ImageEnhance
import time as timer


# In[6]:


alp = 3.5 # 4 works fine
bet = 3
wd = os.getcwd()
photo_files = [i for i in os.listdir(wd) if os.path.isfile(join( wd, i ) )]
photo_files.remove('bright.ipynb')

dest_path = join(wd, 'bright_frames')


# In[7]:


if os.path.isdir('./bright_frames'):
    print('Folder already present')
else:
    os.mkdir('bright_frames')
    print('Folder created')


# In[8]:


start_loop = timer.time()

for i in photo_files:
    img = Image.open(i)
    enhance_bright = ImageEnhance.Brightness(img)
    bright_up = enhance_bright.enhance(alp)
    enhance_contrast = ImageEnhance.Contrast(bright_up)
    final_img = enhance_contrast.enhance(bet)
    pathname = join(dest_path, i)
    final_img.save(pathname)
    
    
end_loop = timer.time()
print('loop with %s files done in %f minutes' %
      (len(photo_files), (end_loop - start_loop)/60)
      )

