import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('Output.avi', fourcc, 20.0, (640, 480))
# VideoWriter : output 파일명 명시, frame per second, frame size도 명시, 마지막은 isColor flag임.
# isColor flag가 True 이면 color frame, 아니면 grayscale

# FourCC는 4바이트로 된 데이터 형식 구분, avi 영상 코덱 구분할 때 사용

while cap.isOpened():
    ret, frame = cap.read()
    if not ret :
        print("Can`t receive frame (stream end?). Exiting...")
        break
    frame = cv.flip(frame, 1)
    # flip : 영상 뒤집기, 수평으로는 양수, 수직으로는 0, 모두 뒤집기는 음수
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()