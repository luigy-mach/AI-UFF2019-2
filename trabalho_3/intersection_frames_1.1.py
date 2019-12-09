import cv2
import numpy as np 

from matplotlib import pyplot as plt

from imutils import grab_contours
from imutils import perspective
from imutils import contours as imutil_contours

from scipy.spatial.distance import euclidean

import glob
import os.path
	

def print_array_imgs(images,titles):
	for i in range(len(images)):
		# plt.subplot(2,4,i+1)
		plt.subplot(2,3,i+1)
		plt.imshow(images[i],'gray')
		# if titles is not None:
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.savefig('foo.png')
	plt.show()


# cv2.namedWindow("test1", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("test1", 640,480)


def analisis_person(frame1,frame2,name_imgSave): 

	img1 = cv2.imread(frame1)
	img2 = cv2.imread(frame2)
	test1 = img1.copy()
	# ret,test1 = cv2.threshold(test1,80,255,cv2.THRESH_BINARY_INV)

	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	cv2.imwrite("/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/imgs_paper/gray1.png",img1)
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
	cv2.imwrite("/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/imgs_paper/gray2.png",img2)


	_, bin1 = cv2.threshold(img1,80,255,cv2.THRESH_BINARY_INV)
	cv2.imwrite("/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/imgs_paper/bin1.png",bin1)

	_, bin2 = cv2.threshold(img2,80,255,cv2.THRESH_BINARY_INV)
	cv2.imwrite("/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/imgs_paper/bin2.png",bin2)

	gray1=bin1
	gray2=bin2

	# gray1 = cv2.cvtColor(bin1, cv2.COLOR_BGR2GRAY)
	# cv2.imwrite("/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/imgs_paper/gray1.png",gray1)
	# gray2 = cv2.cvtColor(bin2, cv2.COLOR_BGR2GRAY)
	# cv2.imwrite("/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/imgs_paper/gray2.png",gray2)


	kernel = np.ones((3,3), np.uint)

	# _, contours, _ = cv2.findContours(img1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	# findContours = cv2.drawContours(img1, contours, -1, (0,225,0), 3)# util para encontrar contornos de objectos de un solo color

	# img_bwa = cv2.bitwise_and(img1,img2)
	# # img_bwo = cv2.bitwise_or(img1,img2)
	img_bw_xor = cv2.bitwise_xor(gray1,gray2) # elegido
	cv2.imwrite("/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/imgs_paper/img_bw_xor.png",img_bw_xor)
	# edges = cv2.Canny(img_bw_xor,100,200)


	dilate1 = cv2.dilate(img_bw_xor, kernel, iterations=4)
	cv2.imwrite("/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/imgs_paper/dilate1.png",dilate1)
	# dilate2 = cv2.dilate(gray2, kernel, iterations=1)
	# cv2.imwrite("/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/imgs_paper/dilate2.png",dilate2)

	erode1 = cv2.erode(dilate1, kernel, iterations=3)
	cv2.imwrite("/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/imgs_paper/erode1.png",erode1)
	# erode2 = cv2.erode(dilate2, kernel, iterations=2)
	# cv2.imwrite("/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/imgs_paper/erode2.png",erode2)

	# img1_laplacian = cv2.Laplacian(img1, cv2.CV_64F)
	# img2_laplacian = cv2.Laplacian(img2, cv2.CV_64F)




	# Find contours
	cnts = cv2.findContours(erode1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = grab_contours(cnts)

	# Sort contours from left to right as leftmost contour is reference object
	(cnts, _) = imutil_contours.sort_contours(cnts)
	# print(cnts)

	# Remove contours which are not large enough
	# cnts = [x for x in cnts if cv2.contourArea(x) > 100]
	contours=dict()
	for i,x in enumerate(cnts):
		if cv2.contourArea(x)>100:
			contours[i]=x

	centroide=dict()
	for key,value in contours.items():
		M = cv2.moments(value)
		# calculate x,y coordinate of center
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
		centroide[key]=[cX,cY]


	ratio_max = 50
	ids=set(centroide.keys())

	temp_centroides = centroide.copy()
	
	final_ids=dict()
	for idx in ids:
		tmp = list()
		tmp_ids = set(temp_centroides.keys())
		if idx in tmp_ids:
			for key,v in temp_centroides.items():
				dis_eucli = euclidean(temp_centroides[idx],v)
				if ratio_max>dis_eucli and dis_eucli>0 :
					tmp.append(key)
			for d in tmp:
				del temp_centroides[d]
			if len(tmp)>0:
				final_ids[idx]=tmp


	final_contours=dict()
	for k,value in final_ids.items():
		tmp = contours[k]
		for i in value:	
			tmp=np.concatenate((tmp,contours[i]))
		final_contours[k]=tmp

	# Draw remaining contours
	for cnt in final_contours.values():
	# for cnt in contours.values():
		box = cv2.minAreaRect(cnt)
		box = cv2.boxPoints(box)
		box = np.array(box, dtype="int")
		box = perspective.order_points(box)
		cv2.drawContours(test1, [box.astype("int")], -1, (0, 0, 255), 10)


	# cv2.imshow("Bitwise AND of Image 1 and 2", img_bwa)
	# cv2.waitKey(0)
	# cv2.imshow("Bitwise OR of Image 1 and 2", img_bwo)
	# cv2.waitKey(0)
	# cv2.imshow("canny", edges)
	# cv2.imshow("Bitwise XOR of Image 1 and 2", img_bw_xor)
	# cv2.imshow("canny", canny)
	# cv2.imshow("img2", img2)

	# cv2.imshow("img1", img1)
	# cv2.imshow("test1", test1)
	cv2.imwrite(name_imgSave,test1)
	print(name_imgSave + ", salvado")
	# cv2.imshow("mg", mg)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()




# titles = ['1','2','3']
# images = [img1,test1,img_bw_xor]
# print_array_imgs(images,titles)


# Main testing 
if __name__ == "__main__":

	# base_name_in = '/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/in_frames/'
	base_name_in = '/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/new_split_video/'
	# base_name_out = '/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/out_frames_sort/'
	base_name_out = '/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/imgs_paper/'
	image_paths = sorted(glob.glob(os.path.join(base_name_in,'*.jpg')))
	# image_paths = image_paths[300:370]
	image_paths = image_paths[:2]

	print(len(image_paths))

	img1 = image_paths[0]
	for img2 in image_paths[1:]:
		_,file = os.path.split(img2)
		save = base_name_out + file
		analisis_person(img1,img2,save)
		img1=img2