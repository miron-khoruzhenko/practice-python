import cv2
gstreamer_str = "sudo gst-launch-1.0 rtspsrc location=rtsp://192.168.1.5:8080/h264_ulaw.sdp latency=100 ! queue ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! videoscale ! video/x-raw,width=640,height=480,format=BGR ! appsink drop=1"
gstreamer_str1 = "gst-launch-1.0 udpsrc port=5600 ! application/x-rtp, encoding-name=H264,payload=96 ! rtph264depay ! avdec_h264 "
gstreamer_str2 = "sudo gst-launch-1.0 -v videotestsrc pattern=snow ! video/x-raw,width=1280,height=720 ! autovideosink"
print('Trying to connect')
# cap = cv2.VideoCapture(gstreamer_str2, cv2.CAP_GSTREAMER)
cap = cv2.VideoCapture('videotestsrc ! video/x-raw,framerate=20/1 ! videoscale ! videoconvert ! appsink', cv2.CAP_GSTREAMER)


# while not cap.isOpened():
# 	continue

# print('connected')

while(1):
	ret, frame = cap.read()
	if ret:
		cv2.imshow("Input via Gstreamer", frame)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break        
	else:            
		break

cap.release()
cv2.destroyAllWindows()