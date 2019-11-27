import cv2
import numpy as  np
import glob

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image', 640, 480)
#list_images = glob.iglob("letters/*")
img_path = "botao_colado/1.jpg"

#for image_title in list_images:
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
#f = np.fft.fft2(img)
#fshift = np.fft.fftshift(f)
#magnitude_spectrum = 20*np.log(np.abs(fshift))
#magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)
#img_and_magnitude = np.concatenate((img, magnitude_spectrum), axis=1)

f = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
f_shift = np.fft.fftshift(f)
f_complex = f_shift[:,:,0] + 1j*f_shift[:,:,1]
f_abs = np.abs(f_complex) + 1 # lie between 1 and 1e6
f_bounded = 20 * np.log(f_abs)
f_img = 255 * f_bounded / np.max(f_bounded)
f_img = f_img.astype(np.uint8)



height, width = img.shape 
radius=200
h=height
w=width
y=int(h/2-radius/2)
x=int(w/2-radius/2)
#crop_img = f_img[y:y+h, x:x+w]
crop_img = f_img[y:y+radius, x:x+radius]
cv2.imshow('Image', f_img)
cv2.waitKey(0)
cv2.imshow("Image", crop_img)
    
cv2.waitKey(0)
cv2.destroyAllWindows()