import numpy as np
import cv2 as cv

cap = cv.VideoCapture('소융 자기소개_2020105723 이우일.mp4')

while cap.isOpened():
    ret , frame = cap.read()

    #if frame is read correctly ret is True
    if not ret:
        print("Can`t receive fram (stream end?). Exiting...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #cvtColor : Converts an image from one color space to another

    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()