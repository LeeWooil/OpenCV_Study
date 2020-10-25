import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
#VideoCapture : 비디오 캡처하기 위한 object, argument는 카메라 번호나 비디오 파일의 이름
if not cap.isOpened():
    print("CAnnot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # cap.read()는 bool type을 반환. frame이 올바르게 읽어지면 True.
    # if frame is read correctly ret is true
    if not ret:
        print("Can`t receive fram (stream end?). Exiting...")
        break
    # Our operation on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()