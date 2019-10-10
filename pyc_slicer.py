'''
This script takes a video,
slices it into single frames
and performs modifications 
at the frame level
'''


import cv2, os

# set counter and flag
success = True
count = 1

# reads in the video
vid = cv2.VideoCapture()

# paths and folders
wd = os.getcwd()

if os.path.isdir("frames"):
    print("Frames folder already present.")
else:
    os.mkdir("./frames")

pth = os.path.join(wd, "frames")


# framer loop
while success:
    
    # pick frame
    success,image = vid.read()

    # names and path
    tit = "frame%d.jpg" % count
    nam = os.path.join(pth,tit)

    ####
    # perform stuff
    ####
    
    # save as JPG
    cv2.imwrite(nam, image)
    # in case one wants to see frames
    #cv2.imshow('ImageWindow',image)

    # break
    if cv2.waitKey(10) == 27:
        break
    count += 1  