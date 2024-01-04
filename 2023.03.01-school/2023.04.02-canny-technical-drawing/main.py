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


def getContoursOf(img):
    lower, higher   = (22, 79)
    blur        = 2

    img      = cv2.GaussianBlur(img, (blur*2 + 1, blur*2 + 1), 0) 
    thresh   = cv2.Canny(img, lower, higher)
    contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0]

    return contours



def drawContours(img):
    height, width, = img.shape[:2]

    blank = np.ones_like(img, np.uint8) 
    blank.fill(255)

    circle      = 1
    font_style  = cv2.FONT_HERSHEY_SIMPLEX
    black       = (0,0,0)
    grey        = (200, 200, 200)

    contours = getContoursOf(img)


    for cnt in contours:
        epsilon = circle/1000*cv2.arcLength(cnt, True)
        approx  = cv2.approxPolyDP(cnt, epsilon, True)

        cv2.drawContours(blank, [approx], -1, black, 1, lineType=cv2.LINE_4)

        if len(approx) > 100:
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            coords = takeCoords(height, width, x, y)

            cv2.putText(blank, "r={:.2f}".format(radius), coords, 
                        font_style, 0.5, (100, 0, 0), 1)
            cv2.line(blank, (int(x), int(y)), coords, grey, 1)

        else:
            x, y, w, h  = cv2.boundingRect(cnt)
            coords      = takeCoords(height, width, x, y)

            cv2.line(blank, (x, y), coords, grey, 1)
            cv2.putText(blank, f"x={int(math.sqrt(h**2 + w**2))}", 
                        coords, font_style, 0.5, black, 1)

    return blank

images = []
for filename in glob.glob('./images/*.jpeg'):
    images.append(cv2.imread(filename))

if len(images) == 0:
    print('Something wrong. Check path or current working directory (CWD).')

if __name__ == '__main__':
    for index, img in enumerate(images):
        blank = drawContours(img)

        cv2.imwrite(datetime.today().strftime(f"%Y.%m.%d-{index+1}")+'.jpg', blank)