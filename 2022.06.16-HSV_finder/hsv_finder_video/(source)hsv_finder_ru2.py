import cv2
import numpy as np
from lib import video

#? INFO ==========
#? ===============
#? Меняет HSV кадров с камеры и показывает результат в соседнем окне

if __name__ == '__main__':
    def nothing(*arg):
        pass

# image = cv2.imread('C:\\Users\\Miron\\Desktop\\VS_Code_Projects\\Python\\ImgProcess\\realtime_process\\colorpanel_red.jpeg')

cv2.namedWindow( "result" ) # создаем главное окно
# cv2.namedWindow('color table', cv2.WINDOW_NORMAL)
cv2.namedWindow( "settings" ) # создаем окно настроек

# (img_height, img_width) = image.shape[:2]
# image2 = cv2.resize(image, (int( img_width * 0.75), int( img_height * 0.75)))

cap = video.create_capture(0)
# создаем 6 бегунков для настройки начального и конечного цвета фильтра
cv2.createTrackbar('h1', 'settings', 0, 255, nothing)
cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
cv2.createTrackbar('v2', 'settings', 255, 255, nothing)
crange = [0,0,0, 0,0,0]

while True:
    flag, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    # hsv2 = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV )
 
    # считываем значения бегунков
    h1 = cv2.getTrackbarPos('h1', 'settings')
    s1 = cv2.getTrackbarPos('s1', 'settings')
    v1 = cv2.getTrackbarPos('v1', 'settings')
    h2 = cv2.getTrackbarPos('h2', 'settings')
    s2 = cv2.getTrackbarPos('s2', 'settings')
    v2 = cv2.getTrackbarPos('v2', 'settings')

    # формируем начальный и конечный цвет фильтра
    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)

    # накладываем фильтр на кадр в модели HSV
    thresh = cv2.inRange(hsv, h_min, h_max)
    # thresh2 = cv2.inRange(hsv2, h_min, h_max)

    # result = cv2.bitwise_and(image2, image2, mask=thresh2)
    result = cv2.bitwise_and(img, img, mask=thresh)

    cv2.imshow('result', thresh) 
    # cv2.imshow('color table', result) 
 
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
