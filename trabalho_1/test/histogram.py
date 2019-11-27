
#import cv2
#import numpy as np
#from matplotlib import pyplot as plt
#
##img = cv2.imread('/home/luigy/AI-UFF2019-2/calibration/1/normal1.jpeg')
#img = cv2.imread('/home/luigy/AI-UFF2019-2/1000.jpg')
#color = ('b','g','r')
#for i,col in enumerate(color):
#    histr = cv2.calcHist([img],[i],None,[256],[0,256])
#    plt.plot(histr,color = col)
#    plt.xlim([0,256])
#plt.show()





#import cv2
#import numpy as np
#from matplotlib import pyplot as plt
#img = cv2.imread('/home/luigy/analise_imagens/calibration/1/normal1.jpeg')
#
#plt.hist(img.ravel(),256,[0,256])
#plt.show()


import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('test_azul1.jpg')
#img = cv2.imread('/home/luigy/AI-UFF2019-2/calibration/1/normal1.jpeg')
#img = cv2.imread('home.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()