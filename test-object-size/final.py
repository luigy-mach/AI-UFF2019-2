
from scipy.spatial.distance import euclidean
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2

#cv2.namedWindow('Image2', cv2.WINDOW_NORMAL)
#cv2.resizeWindow('Image2', 640, 480)

# Function to show array of images (intermediate results)
def show_images(images):
	#print(images)
	for i, img in enumerate(images):
		cv2.namedWindow('Image'+ str(i), cv2.WINDOW_NORMAL)
		cv2.resizeWindow('Image'+ str(i), 640, 480)
		cv2.imshow("Image" + str(i), img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()



#img_path = "fotos2/4.jpeg"
#img_path = "botao_colado/6.jpg"
img_path = "botao_colado/1.jpg"


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
#cv2.imshow("Image2", blur)
#cv2.waitKey(0)


edged = cv2.Canny(blur, 50, 150)
#edged = cv2.Canny(blur, 60, 90)
#cv2.imshow("Image2", edged)
#cv2.waitKey(0)

edged = cv2.dilate(edged, None, iterations=1)
#cv2.imshow("Image2", edged)
#cv2.waitKey(0)

edged = cv2.erode(edged, None, iterations=1)
#cv2.imshow("Image2", edged)
#cv2.waitKey(0)


#show_images([blur, edged])

# Find contours
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print(cnts)
# Sort contours from left to right as leftmost contour is reference object
(cnts, _) = contours.sort_contours(cnts)

# Remove contours which are not large enough
cnts = [x for x in cnts if cv2.contourArea(x) > 100]

#cv2.drawContours(image, cnts, -1, (0,255,0), 3)

#show_images([image, edged])
#print(len(cnts))

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



# Draw remaining contours
for cnt in cnts:
	box = cv2.minAreaRect(cnt)
	box = cv2.boxPoints(box)
	box = np.array(box, dtype="int")
	box = perspective.order_points(box)
	(tl, tr, br, bl) = box
	cv2.drawContours(image, [box.astype("int")], -1, (0, 0, 255), 2)
	mid_pt_horizontal = (tl[0] + int(abs(tr[0] - tl[0])/2), tl[1] + int(abs(tr[1] - tl[1])/2))
	mid_pt_verticle = (tr[0] + int(abs(tr[0] - br[0])/2), tr[1] + int(abs(tr[1] - br[1])/2))
	wid = euclidean(tl, tr)/pixel_per_cm
	ht = euclidean(tr, br)/pixel_per_cm
	cv2.putText(image, "{:.1f}cm".format(wid), (int(mid_pt_horizontal[0] - 15), int(mid_pt_horizontal[1] - 10)), 
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
	cv2.putText(image, "{:.1f}cm".format(ht), (int(mid_pt_verticle[0] + 10), int(mid_pt_verticle[1])), 
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

show_images([image])