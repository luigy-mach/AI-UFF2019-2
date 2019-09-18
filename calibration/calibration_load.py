
import numpy as np
import cv2
import glob

cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image', 600,400)


# Load previously saved data
with np.load('1/calib.npz') as X:
    mtx, dist, rvecs, tvecs = [X[i] for i in ('mtx','dist','rvecs','tvecs')]

print (mtx, dist, rvecs, tvecs)


# Load one of the test images
#img = cv2.imread('1/right1.jpeg')
img = cv2.imread('1/left1.jpeg')
h, w = img.shape[:2]

# Obtain the new camera matrix and undistort the image
newCameraMtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
undistortedImg = cv2.undistort(img, mtx, dist, None, newCameraMtx)

# Crop the undistorted image
# x, y, w, h = roi
# undistortedImg = undistortedImg[y:y + h, x:x + w]

# Display the final result
#cv2.imshow('Image', np.hstack((img, undistortedImg)))
cv2.imshow('Image', np.hstack(( undistortedImg,img)))
cv2.waitKey(0)
cv2.destroyAllWindows()