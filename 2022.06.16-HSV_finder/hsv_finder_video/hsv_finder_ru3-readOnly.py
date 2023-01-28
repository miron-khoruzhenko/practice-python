import cv2
import numpy as np
from lib import video

if __name__ == '__main__':
    def nothing(*arg):
        pass

def red_control(img):
    #Проверка открытия
    # if(type(img) is NoneType):
    #     print("\n\n###############\n\nОшибка открытия\n\n###############\n\n")
    #     exit()

    #Конверт в HSV 
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #Создание масок для контроля красного
    red_low1 = np.array([0, 140, 130])
    red_high1 = np.array([7, 255, 255])

    red_low2 = np.array([170, 140, 130])
    red_high2 = np.array([180, 255, 255])

    #Изменение изображения и создания двух других изображений с помощью масок  
    mask1 = cv2.inRange(hsv_img, red_low1, red_high1)
    mask2 = cv2.inRange(hsv_img, red_low2, red_high2)

    #Объединение двух изображений
    return mask1 | mask2

image = cv2.imread('C:\\Users\\Miron\\Desktop\\VS_Code_Projects\\Python\\ImgProcess\\realtime_process\\colorpanel_red.jpeg')

cv2.namedWindow( "result" ) # создаем главное окно
cv2.namedWindow('color table', cv2.WINDOW_NORMAL)
cv2.namedWindow( "settings" ) # создаем окно настроек

(img_height, img_width) = image.shape[:2]
image2 = cv2.resize(image, (int( img_width * 0.75), int( img_height * 0.75)))

cap = video.create_capture(0)
# создаем 6 бегунков для настройки начального и конечного цвета фильтра

crange = [0,0,0, 0,0,0]

while True:
    flag, img = cap.read()

    blurred = cv2.GaussianBlur(img, (11, 11), 0)
 
    mask = red_control(blurred)
    mask2 = red_control(image2)
    # формируем начальный и конечный цвет фильтра

    # накладываем фильтр на кадр в модели HSV

    result = cv2.bitwise_and(image2, image2, mask=mask2)

    cv2.imshow('result', mask) 
    cv2.imshow('color table', result) 
 
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
