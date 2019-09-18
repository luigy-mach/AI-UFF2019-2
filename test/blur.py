import cv2
import numpy
# read image
#src = cv2.imread('/home/img/python.png', cv2.IMREAD_UNCHANGED)
src = cv2.imread('/home/luigy/AI-UFF2019-2/1000.jpg')

# apply guassian blur on src image
#dst = cv2.GaussianBlur(src,(5,5),cv2.BORDER_DEFAULT)
dst = cv2.GaussianBlur(src,(15,15),cv2.BORDER_DEFAULT)
 
# display input and output image
cv2.imshow("Gaussian Smoothing",numpy.hstack((src, dst)))
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image