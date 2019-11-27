import cv2
vidcap = cv2.VideoCapture('video/TownCentreXVID.avi')
success,image = vidcap.read()
count = 0
while success:
	num = str(count).zfill(6)
	cv2.imwrite("frames/frame%s.jpg" % num, image)     # save frame as JPEG file      
	success,image = vidcap.read()
	print('Read a new frame: ', success)
	count += 1