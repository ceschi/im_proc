#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2, os
vid = cv2.VideoCapture('schifo_10_8.mp4')

success = True
count = 1;

wd = os.getcwd()

if os.path.isdir("frames_schifo"):
    print("ok")
else:
    os.mkdir("./frames_schifo")

pth = os.path.join(wd, "frames_schifo")

while success:
    success,image = vid.read()
    tit = "frame%d.jpg" % count
    nam = os.path.join(pth,tit)
    cv2.imwrite(nam, image)     # save frame as JPEG file
    #cv2.imshow('ImageWindow',image)
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
        break
    count += 1  

