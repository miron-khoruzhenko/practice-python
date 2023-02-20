import cv2
import numpy as np
import os
from datetime import datetime
import time 


def calculate_fps(start_time):
    edit_time = time.time()-start_time

    show_time_milliseconds = 1
    fps = 1.0 / (edit_time + show_time_milliseconds/1000)
    return fps


def process_frame(frame, start_time):
    mean = cv2.mean(frame)[0:3]

    # create average color image
    average = np.full_like(frame, (mean))

    # create opposite (inverted) average color
    opposite = 255 - average

    # convert both images to HSV
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    opposite_hsv = cv2.cvtColor(opposite, cv2.COLOR_BGR2HSV)

    # copy the opposite hue and saturation channels to img_hsv
    img_hsv[:,:,0] = opposite_hsv[:,:,0]
    img_hsv[:,:,1] = opposite_hsv[:,:,1]

    # convert img_hsv back to BGR
    img2 = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    # blend 50-50 with original img
    result = cv2.addWeighted(img2, 0.5, frame, 0.5, 0)

    fps = calculate_fps(start_time)
    cv2.putText(result, "FPS: {:.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    return result

cap = cv2.VideoCapture('deep.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)
size = (1920, 1080)
frames_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(frames_count)
# fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
# video_writer = cv2.VideoWriter('26m_below_water_1_minute_result.mp4', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)


index = 1
while True:
    start_time = time.time()
    ret, frame = cap.read()
    if not ret:
        break

    processed_frame = process_frame(frame, start_time)

    #if you want to save the frames uncomment the following code
    # video_writer.write(processed_frame)


    #if you want to preview the live video while being processed, uncomment the following 3 lines
    cv2.imshow('Result', processed_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    # print(f'Frame {index} out of {frames_count}')
    # index = index + 1

cv2.waitKey(0)
cv2.destroyAllWindows()

