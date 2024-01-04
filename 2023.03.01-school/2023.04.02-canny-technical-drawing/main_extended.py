
#=======================================================================================#
#                                                                 0000000000000         #  
#     File: main_extended.py                                    00000000000000000       #
#     Size: 3.8KiB                                            000000000000000000000     #
#                                                            00000 00000000000 00000    #
#                                                           00000   000000000   00000   #
#     By: Miron Khoruzhenko                                 000000 00000000000 000000   #
#     <mironkhoruzhenko@gmail.com>                          0000000000000000000000000   #
#                                                           00000 0000000000000 00000   #
#                                                            00000             00000    #
#     Created: 2023/04/03 07:05:56                            000000         000000     #
#     Updated: 2023/04/03 07:05:56                              00000000000000000       #
#                                                                 0000000000000         #
#=======================================================================================#

from datetime import datetime
import numpy as np
import glob
import cv2
import math

def takeCoords(height, width, x, y):
    coords = (0,0)
    x = int(x)
    y = int(y)
    if (0.5*width - x == abs(0.5*width - x) and 
        0.5*height - y == abs(0.5*height - y)):
        coords=(x - 30,y - 30)
    elif (0.5*width - x != abs(0.5*width - x) and 
        0.5*height - y == abs(0.5*height - y)):
        coords=(x + 30,y - 30)
    elif (0.5*width - x == abs(0.5*width - x) and 
        0.5*height - y != abs(0.5*height - y)):
        coords=(x - 30,y + 30)
    elif (0.5*width - x != abs(0.5*width - x) and 
        0.5*height - y != abs(0.5*height - y)):
        coords=(x + 30, y + 30)

    return coords

images = []
for filename in glob.glob('./img/input/*.jpeg'):
    images.append(cv2.imread(filename))

if len(images) == 0:
    print('Something wrong. Check path or current working directory (CWD).')

for index, img in enumerate(images):
    # img = cv2.imread('./1.jpeg')
    height, width, = img.shape[:2]
    scale = 1.25
    img = cv2.resize(img, (int(width/scale), int(height/scale)))

    img.resize()
    img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blank = np.ones_like(img, np.uint8) 
    blank.fill(255)

    cv2.namedWindow( "settings", cv2.WINDOW_AUTOSIZE) # создаем окно настроек
    cv2.namedWindow( "result", cv2.WINDOW_AUTOSIZE) # создаем окно настроек

    cv2.moveWindow('result', 0, 0)

    lower, higher = (22, 79)
    iterations = 0
    circle = 1
    blur = 2

    def nothing(*arg):
        pass

    cv2.createTrackbar('lower', 'settings', lower, 255, nothing)
    cv2.createTrackbar('higher', 'settings', higher, 255, nothing)
    cv2.createTrackbar('iterations', 'settings', iterations, 15, nothing)
    cv2.createTrackbar('circle', 'settings', circle, 100, nothing)
    cv2.createTrackbar('blur', 'settings', blur, 15, nothing)

    clone = img.copy()
    blank_clone = blank.copy()

    while True:
        cv2.moveWindow('result', 0, 0)

        clone = img.copy()
        blank_clone = blank.copy()

        clone = cv2.erode(clone, None, iterations=iterations) #1
        clone = cv2.dilate(clone, None, iterations=iterations)
        clone = cv2.GaussianBlur(clone, (blur*2 + 1, blur*2 + 1), 0) 

        lower       = cv2.getTrackbarPos('lower', 'settings')
        higher      = cv2.getTrackbarPos('higher', 'settings')
        iterations  = cv2.getTrackbarPos('iterations', 'settings')
        circle      = cv2.getTrackbarPos('circle', 'settings')
        blur        = cv2.getTrackbarPos('blur', 'settings')

        # thresh=cv2.Canny(img,60,125)
        thresh=cv2.Canny(clone, lower, higher)
        contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


        for cnt in contours:
            epsilon = circle/1000*cv2.arcLength(cnt, True)
            approx  = cv2.approxPolyDP(cnt, epsilon, True)

            cv2.drawContours(clone, [approx], -1, (0, 0, 0), 1, lineType=cv2.LINE_4)
            cv2.drawContours(blank_clone, [approx], -1, (0, 0, 0), 1, lineType=cv2.LINE_4)


            if len(approx) > 100:
                (x, y), radius = cv2.minEnclosingCircle(cnt)
                coords = takeCoords(height, width, x, y)

                cv2.putText(blank_clone, "r={:.2f}".format(radius), coords, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 0, 0), 1)
                cv2.line(blank_clone, (int(x), int(y)), coords, (0,0,0), 1)

            else:
                x, y, w, h = cv2.boundingRect(cnt)
                coords = takeCoords(height, width, x, y)

                cv2.putText(blank_clone, f"x={int(math.sqrt(h**2 + w**2))}cm", 
                            coords, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
                cv2.line(blank_clone, (x, y), coords, (0,0,0), 1)


        cv2.imshow('result', clone)
        cv2.imshow('result', blank_clone)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

