import cv2
import numpy as np

import glob
import os.path

 
img_array = []
basename_in_images = "/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/in_frames/"


image_paths = sorted(glob.glob(os.path.join(basename_in_images,'*.jpg')))
image_paths = image_paths[:300]

print(image_paths)
i = 0
for filename in image_paths:
	print("arrumando " +str(i))
	img = cv2.imread(filename)
	height, width, layers = img.shape
	size = (width,height)
	img_array.append(img)
	i+=1
 

basename_outvideo = "/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/out_video/"
out = cv2.VideoWriter(basename_outvideo+'out.avi',cv2.VideoWriter_fourcc(*'XVID'), 0.5, size)
# out = cv2.VideoWriter(basename_outvideo+'out.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.5, size)
 
j=0
for i in range(len(img_array)):
	print("saving..." + str(j))
	out.write(img_array[i])
	j+=1
out.release()
