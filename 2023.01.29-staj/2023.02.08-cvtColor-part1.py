import cv2
import numpy as np

frame_time = 1

if __name__ == '__main__':
    def nothing(*arg):
        pass

    def stop(*arg):
        global frame_time

        if frame_time:
            frame_time = 0
            print('Stopped')
        else:
            frame_time = 1
            print('Continue')



cap = cv2.VideoCapture('deep.mp4')
if not cap.isOpened():
    print('\033[93mSomething went wrong. Control your working directory and path\033[0m')
    quit()

# img = cv2.imread('./test.png')
ret, img = cap.read()
height, width, = img.shape[:2]

blank_image = np.zeros((70,250,3), np.uint8)
blank_image.fill(255)

# Текст примерно 25 в высоту и 125 в ширину
blank_image = cv2.putText(
                blank_image, 
                'Settings', 
                (60, 45), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0, 0, 0), 2, cv2.LINE_AA)

cv2.imshow('settings', blank_image)

cv2.namedWindow( "settings", cv2.WINDOW_AUTOSIZE) # создаем окно настроек
cv2.namedWindow( "result", cv2.WINDOW_AUTOSIZE) # создаем главное окно

cv2.createButton('STOP', stop, None, buttonType=cv2.QT_PUSH_BUTTON)
# cv2.createButton('STOP', stop, None, buttonType=cv2.QT_NEW_BUTTONBAR)

cv2.resizeWindow('settings', 500, 350)

cv2.moveWindow('settings', 0, 0)
cv2.moveWindow('result', 400, 0)

hsv_h1, hsv_s1, hsv_v1 = (0, 0, 0)
bgr_r1, bgr_g1, bgr_b1 = (0, 0, 0)
lab_l1, lab_a1, lab_b1 = (0, 0, 0)

cv2.createTrackbar('hsv_h', 'settings', hsv_h1, 255, nothing)
cv2.createTrackbar('hsv_s', 'settings', hsv_s1, 255, nothing)
cv2.createTrackbar('hsv_v', 'settings', hsv_v1, 255, nothing)

# cv2.createTrackbar('bgr_r', 'settings', bgr_r1, 255, nothing)
# cv2.createTrackbar('bgr_g', 'settings', bgr_g1, 255, nothing)
# cv2.createTrackbar('bgr_b', 'settings', bgr_b1, 255, nothing)

cv2.createTrackbar('lab_l', 'settings', lab_l1, 255, nothing)
cv2.createTrackbar('lab_a', 'settings', lab_a1, 255, nothing)
cv2.createTrackbar('lab_b', 'settings', lab_b1, 255, nothing)

x =0

while True:
    x += 1
    ret, img = cap.read()

    print(cap.get(cv2.CAP_PROP_FRAME_COUNT) - x)

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break


    img = cv2.resize(img, (int(width/4), int(height/4)))
    # bgr_b, bgr_g, bgr_r = cv2.split(img)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv_h, hsv_s, hsv_v = cv2.split(hsv)

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    lab_l, lab_a, lab_b = cv2.split(lab)
    
    hsv_h1 = cv2.getTrackbarPos('hsv_h', 'settings')
    hsv_s1 = cv2.getTrackbarPos('hsv_s', 'settings')
    hsv_v1 = cv2.getTrackbarPos('hsv_v', 'settings')

    # bgr_r1 = cv2.getTrackbarPos('bgr_r', 'settings')
    # bgr_g1 = cv2.getTrackbarPos('bgr_g', 'settings')
    # bgr_b1 = cv2.getTrackbarPos('bgr_b', 'settings')
    
    lab_l1 = cv2.getTrackbarPos('lab_l', 'settings')
    lab_a1 = cv2.getTrackbarPos('lab_a', 'settings')
    lab_b1 = cv2.getTrackbarPos('lab_b', 'settings')


    hsv_new = cv2.merge([
        (hsv_h + hsv_h1), 
        (hsv_s + hsv_s1), 
        (hsv_v + hsv_v1)])

    lab_new = cv2.merge([
        (lab_l + lab_l1), 
        (lab_a + lab_a1), 
        (lab_b + lab_b1)])

    # rgb_new = cv2.merge([
    #     (bgr_b + bgr_b1),
    #     (bgr_g + bgr_g1), 
    #     (bgr_r + bgr_r1)])


    kernel = np.array([[0, -1, 0],
                    [-1, 5,-1],
                    [0, -1, 0]])
    rgb_new = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)


    kernel = np.array([[0, -1, 0],
                    [-1, 5,-1],
                    [0, -1, 0]])
    hsv_new = cv2.filter2D(src=hsv_new, ddepth=-1, kernel=kernel)

    hsv_new = cv2.cvtColor(hsv_new, cv2.COLOR_HSV2BGR)
    lab_new = cv2.cvtColor(lab_new, cv2.COLOR_LAB2BGR)

    vis1 = np.concatenate((img, hsv_new), axis=1)
    vis2 = np.concatenate((rgb_new, lab_new), axis=1)
    vis3 = np.concatenate((vis1, vis2), axis=0)

    cv2.imshow('result', vis3)

    if cv2.waitKey(frame_time) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()