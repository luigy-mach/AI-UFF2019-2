
from scipy.spatial.distance import euclidean
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2

cv2.namedWindow('Image2', cv2.WINDOW_NORMAL)
#cv2.resizeWindow('Image2', 640, 480)
cv2.resizeWindow('Image2', 800, 600)


#img_path = "fotos2/4.jpeg"
#img_path = "botao_colado/final.jpg"
img_path = "botao_colado/chanel_l.jpg"


# Read image and preprocess
image = cv2.imread(img_path)

   
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Image2", gray)
#cv2.waitKey(0)


blur = cv2.GaussianBlur(gray, (9, 9), 0)
#cv2.imshow("Image2", blur)
#cv2.waitKey(0)


#edged = cv2.Canny(blur, 50, 100)
edged = cv2.Canny(blur, 30, 60)
#cv2.imshow("Image2", edged)
#cv2.waitKey(0)

edged = cv2.dilate(edged, None, iterations=1)
#cv2.imshow("Image2", edged)
#cv2.waitKey(0)

edged = cv2.erode(edged, None, iterations=1)
cv2.imshow("Image2", edged)
cv2.waitKey(0)
