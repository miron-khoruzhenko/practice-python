from types import NoneType
import cv2
import numpy as np

def nothing(x):
    pass

height      = 400
width       = 400
channels    = 3

blank_image = np.zeros((height, width, channels), dtype=np.uint8)
hsv_blank_image = cv2.cvtColor(blank_image, cv2.COLOR_BGR2HSV)

# Load image
# image = cv2.imread('/home/strewen/Desktop/VS_Code_Projects/Python/ImgProcess/imgs/rgb_spectrum_resized.jpg')
# image = cv2.imread('/home/strewen/Desktop/VS_Code_Projects/Python/ImgProcess/imgs/rgbspectrum1.jpg')
# image1 = cv2.imread('/home/strewen/Desktop/VS_Code_Projects/Python/ImgProcess/imgs/red.png')
# image2 = cv2.imread('C:/Users/Miron/Desktop/VS_Code_Projects/2022.06.16-sortedAutonomousPlane/HSV_finder/hsv_finder/colorpanel_red.jpeg')
image2 = cv2.imread('./colorpanel_red.jpeg')

def hsv_process(image):
    if(type(image) is NoneType):
        print("\n\n###############\n\nОшибка открытия\n\n###############\n\n")
        exit()


    # Create a window
    name = 'Press q to quit'
    name2= 'DYNAMIC'
    cv2.namedWindow(name)
    cv2.namedWindow(name2)

    # Create trackbars for color change
    # Hue is from 0-179 for Opencv
    cv2.createTrackbar('HMin', name, 0, 179, nothing)
    cv2.createTrackbar('HMax', name, 0, 179, nothing)
    cv2.createTrackbar('SMin', name, 0, 255, nothing)
    cv2.createTrackbar('SMax', name, 0, 255, nothing)
    cv2.createTrackbar('VMin', name, 0, 255, nothing)
    cv2.createTrackbar('VMax', name, 0, 255, nothing)

    # Set default value for Max HSV trackbars
    cv2.setTrackbarPos('HMax', name, 179)
    cv2.setTrackbarPos('SMax', name, 255)
    cv2.setTrackbarPos('VMax', name, 255)

    # Initialize HSV min/max values
    hMin = sMin = vMin = hMax = sMax = vMax = 0
    phMin = psMin = pvMin = phMax = psMax = pvMax = 0

    while(1):
        # Get current positions of all trackbars
        hMin = cv2.getTrackbarPos('HMin', name)
        sMin = cv2.getTrackbarPos('SMin', name)
        vMin = cv2.getTrackbarPos('VMin', name)
        hMax = cv2.getTrackbarPos('HMax', name)
        sMax = cv2.getTrackbarPos('SMax', name)
        vMax = cv2.getTrackbarPos('VMax', name)

        # Set minimum and maximum HSV values to display
        lower = np.array([hMin, sMin, vMin])
        upper = np.array([hMax, sMax, vMax])

        hsv_blank_image[:,:] = (hMin,sMin,vMin)

        # Convert to HSV format and color threshold
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(image, image, mask=mask)

        # Print if there is a change in HSV value
        if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
            print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
            phMin = hMin
            psMin = sMin
            pvMin = vMin
            phMax = hMax
            psMax = sMax
            pvMax = vMax

        rgb_image = cv2.cvtColor(hsv_blank_image, cv2.COLOR_BGR2HSV)

        # Display result image
        cv2.imshow(name, result)
        cv2.imshow(name2, rgb_image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

hsv_process(image2)