import cv2
import numpy as np



cv2.namedWindow('Image2', cv2.WINDOW_NORMAL)
#cv2.resizeWindow('Image2', 640, 480)
cv2.resizeWindow('Image2', 800, 600)

img = cv2.imread('botao_colado/1.jpg')

ret, imgf = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


## Aplica os respectivos filtros
#kernel = np.ones((8,8),np.float32)/25
#filter2D = cv2.filter2D(img,-1,kernel)




cv2.imshow('Image2', imgf)

cv2.waitKey(0)