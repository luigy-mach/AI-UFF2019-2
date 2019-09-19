import cv2
import numpy as np
#from matplotlib import pyplot as plt

cv2.namedWindow('Image2', cv2.WINDOW_NORMAL)
#cv2.resizeWindow('Image2', 640, 480)
cv2.resizeWindow('Image2', 800, 600)


img = cv2.imread('botao_colado/6.jpg')


# Aplica os respectivos filtros
kernel = np.ones((9,9),np.float32)/15	
filter2D = cv2.filter2D(img,-1,kernel)
cv2.imwrite("image_test.png", filter2D)




ret,thresh1 = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
cv2.imshow('Image2', thresh1)
cv2.waitKey(0)

#ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('Image2', thresh2)
#cv2.waitKey(0)

#ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#ret,thresh3 = cv2.threshold(img,110,255,cv2.THRESH_TRUNC)
#cv2.imshow('Image2', thresh3)
#cv2.waitKey(0)

#ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
#cv2.imshow('Image2', thresh4)
#cv2.waitKey(0)

#ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
#cv2.imshow('Image2', thresh5)
#cv2.waitKey(0)



#titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
#images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
#
#for i in xrange(6):
#    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
#
#plt.show()