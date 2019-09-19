
from scipy.spatial.distance import euclidean
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2
import os.path


def show_images(images):
	for i, img in enumerate(images):
		cv2.namedWindow('Image'+ str(i), cv2.WINDOW_NORMAL)
		cv2.resizeWindow('Image'+ str(i), 640, 480)
		cv2.imshow("Image" + str(i), img)
	cv2.waitKey(0)
	#cv2.destroyAllWindows()

img_path = "botao_colado/1.jpg"
filename = os.path.split(img_path)

# Read image and preprocess
image = cv2.imread(img_path)
   
## Aplica os respectivos filtros
#kernel = np.ones((9,9),np.float32)/15	
#filter2D = cv2.filter2D(image,-1,kernel)
#cv2.imwrite("image_test.png", filter2D)
#gray = cv2.cvtColor(filter2D, cv2.COLOR_BGR2GRAY)

ret,thresh1 = cv2.threshold(image,80,255,cv2.THRESH_BINARY)
gray = cv2.cvtColor(thresh1, cv2.COLOR_BGR2GRAY)

#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Image2", gray)
#cv2.waitKey(0)

blur = cv2.GaussianBlur(gray, (9, 9), 0)
#blur = cv2.GaussianBlur(gray, (11, 11), 0)
show_images([blur])



edged = cv2.Canny(blur, 50, 150)
#edged = cv2.Canny(blur, 60, 90)
show_images([edged])


edged = cv2.dilate(edged, None, iterations=1)
show_images([edged])


edged = cv2.erode(edged, None, iterations=1)
show_images([edged])

# Find contours
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
#print(cnts)
# Sort contours from left to right as leftmost contour is reference object
(cnts, _) = contours.sort_contours(cnts)

# Remove contours which are not large enough
cnts = [x for x in cnts if cv2.contourArea(x) > 100]

# Reference object dimensions
# Here for reference I have used a 2cm x 2cm square
ref_object = cnts[0]
box = cv2.minAreaRect(ref_object)
box = cv2.boxPoints(box)
box = np.array(box, dtype="int")
box = perspective.order_points(box)
(tl, tr, br, bl) = box
dist_in_pixel = euclidean(tl, tr)
dist_in_cm = 2
pixel_per_cm = dist_in_pixel/dist_in_cm

centroide=list()

# Draw remaining contours
for cnt in cnts:
	box = cv2.minAreaRect(cnt)
	area = cv2.contourArea(cnt)
	if area>10000:
		# calculate moments for each contour
		M = cv2.moments(cnt)
		# calculate x,y coordinate of center
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		centroide.append([cX,cY])
		print(cX,cY)
		print(area)
		
		box = cv2.boxPoints(box)
		box = np.array(box, dtype="int")
		box = perspective.order_points(box)
		(tl, tr, br, bl) = box

		cv2.drawContours(image, [box.astype("int")], -1, (0, 0, 255), 10)
		mid_pt_horizontal = (tl[0] + int(abs(tr[0] - tl[0])/2), tl[1] + int(abs(tr[1] - tl[1])/2))
		mid_pt_verticle = (tr[0] + int(abs(tr[0] - br[0])/2), tr[1] + int(abs(tr[1] - br[1])/2))
		wid = euclidean(tl, tr)/pixel_per_cm
		ht = euclidean(tr, br)/pixel_per_cm
		cv2.putText(image, "{:.1f}cm".format(wid), (int(mid_pt_horizontal[0] - 15), int(mid_pt_horizontal[1] - 10)), 
			cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0), 2)
		cv2.putText(image, "{:.1f}cm".format(ht), (int(mid_pt_verticle[0] + 10), int(mid_pt_verticle[1])), 
			cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0), 2)


x0=centroide[1][0]
y0=centroide[1][1]
x1=centroide[2][0]
y1=centroide[2][1]


cor_line = (0, 255, 255)
lineThickness = 5
cv2.line(image, (x0, y0), (x1, y1), cor_line, lineThickness)
dist_in_pixel2 = euclidean(x0, x1)
dist_in_pixel2=dist_in_pixel2/pixel_per_cm

x_novo = int(abs(x0-x1)/2)+x0
y_novo = int(abs(y0-y1)/2)+y0+100
print(x_novo)
print(y_novo)
cv2.putText(image, "{:.1f}cm".format(dist_in_pixel2), (x_novo, y_novo), 
			cv2.FONT_HERSHEY_SIMPLEX, 5, cor_line, 20)

print(dist_in_pixel2)


print(filename)
cv2.imwrite("image_init_v2_"+filename[1], image)


show_images([image])
