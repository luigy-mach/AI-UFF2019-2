import cv2
import numpy as np

filename = '/home/luigy/analise_imagens/data/split_videos/imagen1_crop.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# find Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)



# define the criteria to stop and refine the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
print(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]
print(res[:,1][0],res[:,0][0])
print(res[:,3][2],res[:,2][2])
#cv2.line(img,(res[:,1][0],res[:,0][0]),(res[:,3][2],res[:,2][2]),(255,0,0),5)
cv2.line(img,(0,0),(566,555),(255,0,0),5)
cv2.imwrite('out_imagen.png',img)