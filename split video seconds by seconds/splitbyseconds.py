import cv2
import math

import cv2
import glob
import numpy as np
import sys
import os.path




videoFile = "video2.mp4"
imagesFolder = "/home/luigy/analise_imagens/Analise-imagen/split_videos/video2_2/"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
count=0
while(cap.isOpened()):
	frameId = cap.get(1) #current frame number
	ret, frame = cap.read()
	if (ret != True):
		break
	if (frameId % math.floor(frameRate) == 0):
		nfile = '{0:06}'.format(count)
		filename=imagesFolder+str(count)+'.jpg'
		cv2.imwrite(filename, frame)
		count+=1
cap.release()
print("Done!")



