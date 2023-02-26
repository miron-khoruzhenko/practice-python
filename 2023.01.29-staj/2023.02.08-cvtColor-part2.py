import cv2
import numpy as np

if __name__ == '__main__':
    def nothing(*arg):
        pass


def fastPutText(img, str, coord=(0, 15), color=(0, 0, 0)):
    return cv2.putText(
                img, 
                str, 
                coord, 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.5, color, 1, cv2.LINE_AA)

cap = cv2.VideoCapture('./deep.mp4')

if not cap.isOpened():
    print('\033[93mSomething went wrong. Control your path and cwd\033[0m')
    quit()

ret, img = cap.read()
height, width, = img.shape[:2]

cv2.namedWindow( "result", cv2.WINDOW_AUTOSIZE) # создаем главное окно
cv2.moveWindow('result', 0, 0)

kernel_sharpen = np.array([
                [0, -1, 0],
                [-1, 5,-1],
                [0, -1, 0]])
kernel_edge1 = np.array([
                [-1, -1, -1],
                [-1, 8, -1],
                [-1, -1, -1]])
kernel_edge2 = np.array([
                [+1, +2, +1],
                [0, 0, 0],
                [-1, -2, -1]])
# kernel_edge1 = np.array([
#                 [-1/4, 0, 1/4],
#                 [0, 0, 0],
#                 [1/4, 0, -1/4]])
# kernel_edge1 = np.array([
#                 [-1, -1, 8, -1, -1],
#                 [-1, -1, -1, -1, -1],
#                 [-1, -1, -1, -1, 8],
#                 [-1, -1, -1, -1, -1],
#                 [-1, -1, 8, -1, -1]])


# kernel_edge3 = np.array([
#                 [1, 0, -1],
#                 [0, 0, 0],
#                 [-1, 0, 1]])

old_hsv = 0

while True:
    ret, img = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break


    img = cv2.resize(img, (int(width/4), int(height/4)))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv[:, :, 2] += 145
    hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    sharped_bgr = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_sharpen)
    hsv         = cv2.filter2D(src=hsv, ddepth=-1, kernel=kernel_sharpen)
    contured1   = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_edge1)
    contured2   = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_edge2)
    # contured3   = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_edge3)

    img         = fastPutText(img, "Original")
    hsv         = fastPutText(hsv, "HSV + Sharped")
    sharped_bgr = fastPutText(sharped_bgr, "Sharped")
    contured1   = fastPutText(contured1, "Edge v1", color=(255, 255, 255))
    contured2   = fastPutText(contured2, "Edge v2", color=(255, 255, 255))
    # contured3   = fastPutText(contured3, "Edge v3", color=(255, 255, 255))

    # vis1 = np.concatenate((img, contured3), axis=0)
    vis1 = np.concatenate((img, img), axis=0)
    vis2 = np.concatenate((hsv, sharped_bgr), axis=0)
    vis3 = np.concatenate((contured1, contured2), axis=0)
    vis4 = np.concatenate((vis1, vis2), axis=1)
    vis4 = np.concatenate((vis3, vis4), axis=1)

    cv2.imshow('result', vis4)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()