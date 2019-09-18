import cv2
import glob
import numpy as np
import sys
import os.path



#import cv2

import glob
import numpy as np
import sys
import os.path
import random

from PIL import Image

import cv2


cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image', 640, 480)


cap = cv2.VideoCapture('/home/luigy/analise_imagens/data/split_videos/video3.mp4')
name_crop='/home/luigy/analise_imagens/data/split_videos/video3/'

if (cap.isOpened()==False): 
    print("Error opening video stream or file")
ret, frame = cap.read()

count_frame=0

frameRate=cap.get(5)
nomeFrame=cap.get(1)
print(frameRate)
print(nomeFrame)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        nfile = '{0:06}'.format(count_frame)
        cv2.imwrite(name_crop+nfile+'.png',frame)
        count_frame+=1   
        cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
        cv2.imshow('Image', frame)
        cv2.waitKey(1)
    else:
        break 
