import cv2
import numpy as np



cv2.namedWindow('Image2', cv2.WINDOW_NORMAL)
#cv2.resizeWindow('Image2', 640, 480)
cv2.resizeWindow('Image2', 800, 600)

img = cv2.imread('botao_colado/1.jpg')

img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# convert the YUV image back to RGB format
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Image2', img)
cv2.waitKey(0)
cv2.imshow('Image2', img_output)

cv2.waitKey(0)