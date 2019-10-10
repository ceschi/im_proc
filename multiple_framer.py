#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os, cv2
from os.path import join
import numpy as np
from PIL import Image, ImageEnhance

wd = os.getcwd() + '\stories\\'


files_list = [i for i in os.listdir(wd) if os.path.isfile(join(wd,i))]

tot_files = 1;
tot_frames = 1;

for i in files_list:
    
    if os.path.splitext(i)[-1].lower() == '.mp4':
        infile = wd + '\\' + i
        outdir = wd + '\\' + os.path.splitext(i)[0]
        os.mkdir(outdir)
        vid = cv2.VideoCapture(infile)
        success = True
        
        while success:
            
            success, image = vid.read()
            title = 'frame_%d.jpg' % tot_frames
            name = join(outdir, title)
            image = cv2.add(image,np.array([65.0]))
            # operate on the frame
            '''
            # ImageEnhance has better outcome,
            # but does not take cv2 images
            # as input: needs workaround
            img = Image.open(image)
            enhancebright = ImageEnhance.Brightness(img)
            img_bri = enhancebright.enhance(4)
            final_img = img_bri
            final_img.
            '''
            cv2.imwrite(name, image)
            
            if cv2.waitKey(10) == 27:
                
                break
                
            tot_frames += 1
    tot_frames = 1
    tot_files += 1

print('DONE! Processed %d files.' % tot_files)


# In[ ]:





# In[ ]:




