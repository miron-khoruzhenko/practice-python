import cv2
import numpy as np
from tkinter import filedialog

# import videos

#? ====================== INFO ======================
#? Выводит исходное и обработанное с помощью трекеров видео.
#? Так же выводит два изображения цветной панели и показывает
#? их изменение в зависимости от трекеров.
#? ==================================================

if __name__ == '__main__':
    def nothing(*arg):
        pass

ftypes = [
    ("JPG", "*.jpg *.jpeg *.JPG *.JPEG"), 
    ("PNG", "*.png *.PNG"),
    # ("GIF", "*.gif *.GIF"),
    ("All files", "*.*")
]

cv2.namedWindow( "result", cv2.WINDOW_AUTOSIZE) # создаем главное окно
cv2.namedWindow( "settings", cv2.WINDOW_AUTOSIZE) # создаем окно настроек
cv2.namedWindow( "frame", cv2.WINDOW_AUTOSIZE) 
cv2.namedWindow( "color panel", cv2.WINDOW_AUTOSIZE) 
cv2.namedWindow( "color panel 2", cv2.WINDOW_AUTOSIZE)

cv2.resizeWindow('settings', 500, 350)

img1 = cv2.imread('/home/strewen/Desktop/vscode_projects/Python/2022.06.16-HSV_finder/hsv_finder_video/src/colorpanel_red.jpeg')
# img1 = cv2.imread(filedialog.askopenfilename(filetypes = ftypes))
img2 = cv2.imread('/home/strewen/Desktop/vscode_projects/Python/2022.06.16-HSV_finder/hsv_finder_video/src/index.png')

# cap = video.create_capture(0)
cap = cv2.VideoCapture(0)

# нижняя маска
h1, s1, v1 = (0, 140, 130)
h2, s2, v2 = (9, 255, 255)

# верхняя маска
# h1, s1, v1 = (170, 140, 130)
# h2, s2, v2 = (180, 255, 255)

# создаем 6 бегунков для настройки начального и конечного цвета фильтра
cv2.createTrackbar('h1', 'settings', h1, 180, nothing)
cv2.createTrackbar('s1', 'settings', s1, 255, nothing)
cv2.createTrackbar('v1', 'settings', v1, 255, nothing)
cv2.createTrackbar('h2', 'settings', h2, 180, nothing)
cv2.createTrackbar('s2', 'settings', s2, 255, nothing)
cv2.createTrackbar('v2', 'settings', v2, 255, nothing)
# crange = [0,0,0, 0,0,0]

# инициализация переменных для использования в цикле
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

flag, frame = cap.read()
height, width, = frame.shape[:2]
height2, = img1.shape[:1]

cv2.moveWindow('result', 0, 0)
cv2.moveWindow('frame', 0, int(height/2) + 100)
cv2.moveWindow('color panel', int(width/2) + 65, 0)
cv2.moveWindow('color panel 2', int(width/2) + 65, img1.shape[0] + 100)
cv2.moveWindow('settings', int(width/2) + 65 + img2.shape[1] + 150, img1.shape[0] + 100)

while True:
    #*
    flag, frame = cap.read()
    height, width, = frame.shape[:2]
    
    # cv2.moveWindow('result', 0, 0)
    # cv2.moveWindow('frame', 0, int(height/2) + 30)
    # cv2.moveWindow('color panel', int(width/2), 0)
    # cv2.moveWindow('color panel 2', int(width/2), height2 + 30)


    # img = cv2.resize(frame, (int(width/2), int(height/2)))
    frame2 = cv2.resize(frame, (int(width/2), int(height/2)))
    img = cv2.GaussianBlur(frame2, (11, 11), 0)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV )
    hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV )
    
    # считываем значения бегунков
    h1 = cv2.getTrackbarPos('h1', 'settings')
    s1 = cv2.getTrackbarPos('s1', 'settings')
    v1 = cv2.getTrackbarPos('v1', 'settings')
    h2 = cv2.getTrackbarPos('h2', 'settings')
    s2 = cv2.getTrackbarPos('s2', 'settings')
    v2 = cv2.getTrackbarPos('v2', 'settings')

    if((phMin != h1) | (psMin != s1) | (pvMin != v1) | 
    (phMax != h2) | (psMax != s2) | (pvMax != v2) ):
        print("\n\n(hMin = %d , sMin = %d, vMin = %d)\n(hMax = %d , sMax = %d, vMax = %d)\n\n" % (h1 , s1 , v1, h2, s2 , v2))
        phMin = h1
        psMin = s1
        pvMin = v1
        phMax = h2
        psMax = s2
        pvMax = v2

    # формируем начальный и конечный цвет фильтра
    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)

    # накладываем фильтр на кадр в модели HSV
    thresh = cv2.inRange(hsv, h_min, h_max)

    mask1 = cv2.inRange(hsv1, h_min, h_max)
    result1 = cv2.bitwise_and(img1, img1, mask=mask1)

    mask2 = cv2.inRange(hsv2, h_min, h_max)
    result2 = cv2.bitwise_and(img2, img2, mask=mask2)

    cv2.imshow('result', thresh) 
    cv2.imshow('frame', img) 
    cv2.imshow('color panel', result1) 
    cv2.imshow('color panel 2', result2) 

    ch = cv2.waitKey(5)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()
