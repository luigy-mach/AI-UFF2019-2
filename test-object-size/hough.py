import sys
import cv2 
import numpy as np
import math  



def main(argv):
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Image', 640, 480)

    #default_file =  "test1.png"
    #default_file =  "/home/luigy/analise_imagens/data/data2/1000.jpg"
    #default_file =  "/home/luigy/analise_imagens/data/data2/1500.jpg"
    #default_file =  "/home/luigy/analise_imagens/data/data2/2500.jpg"
    #default_file =  "circle1.jpeg"
    default_file = "fotos2/4.jpeg"

    #filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    #src = cv.imread(filename)
    src = cv2.imread(default_file)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1
    

    #cv2.imshow("Image", src)
    #cv2.waitKey(0)
    
    #x=200
    #w=1200
    #y=200
    #h=600
    #src=src[y:y+h,x:x+w]

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    
    
    gray = cv2.medianBlur(gray, 9)
    
    
    rows = gray.shape[0]
    #circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 4,
                                param1=100, param2=30,
                                minRadius=0, maxRadius=50000)
                                #minRadius=0, maxRadius=300)
    
    print(circles)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(src, center, radius, (255, 0, 255), 3)
    
    if circles is not None:
        if len(circles[0])==2:
            circles = np.uint16(np.around(circles)) 
            distance = math.sqrt((circles[0][0][0]-circles[0][1][0])^2 + (circles[0][0][1]-circles[0][1][1])^2)
            print(distance)
    
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(src, str(distance), (230, 50), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
    
    cv2.imshow("Image", src)
    cv2.waitKey(0)
    




    return 0
if __name__ == "__main__":
    #main(sys.argv[1:])#
    main(sys.argv[1:])#