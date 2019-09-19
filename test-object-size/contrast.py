import cv2


def show_image(name,img):
	cv2.namedWindow(name, cv2.WINDOW_NORMAL)
	cv2.resizeWindow(name, 800, 600)
	cv2.imshow(name,img)
	#cv2.waitKey(0)


#-----Reading the image-----------------------------------------------------
img = cv2.imread('botao_colado/1.jpg', 1)
show_image("img",img) 

#-----Converting image to LAB Color model----------------------------------- 
lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
show_image("lab",lab)

#-----Splitting the LAB image to different channels-------------------------
l, a, b = cv2.split(lab)
show_image('l_channel', l)
cv2.imwrite('botao_colado/chanel_l.jpg',l) 

show_image('a_channel', a)
show_image('b_channel', b)

#-----Applying CLAHE to L-channel-------------------------------------------
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
cl = clahe.apply(l)
show_image('CLAHE output', cl)

#-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
limg = cv2.merge((cl,a,b))
show_image('limg', limg)

#-----Converting image from LAB Color model to RGB model--------------------
final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
show_image('final', final)
cv2.imwrite('botao_colado/final.jpg',final) 


cv2.waitKey(0)

#_____END_____#