import cv2
vidcap = cv2.VideoCapture('video/TownCentreXVID_half.avi')
success,image = vidcap.read()
count = 0


base_name="/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/in_frames/"
while success:
	num = str(count).zfill(6)
	cv2.imwrite(base_name+"frame%s.jpg" % num, image)     # save frame as JPEG file      
	success,image = vidcap.read()
	print('Read a new frame: ', success)
	count += 1