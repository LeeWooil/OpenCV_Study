import cv2 as cv
import numpy as np

# Changing Color-space
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print(flags)

# For color conversion, we use the function cv.cvtColor(input_image,flag)
# For BGR -> Gray : cv.COLOR_BGR@GRAY, BGR -> HSV : cv.COLOR_BGR2HSV

#object Tracking

cap = cv.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()
    # 제대로 프레임 읽음 -> _: Ture, 아니면 False

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Checks if array elements lie between the elements of two other arrays

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask=mask)

    cv.imshow('hsv',hsv)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()