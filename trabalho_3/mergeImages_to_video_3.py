import cv2
import os

image_folder =  '/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/out_frames/'
video_name = '/home/luigy/analise_imagens/AI-UFF2019-2/trabalho_3/out_video/video.mp4'


images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()