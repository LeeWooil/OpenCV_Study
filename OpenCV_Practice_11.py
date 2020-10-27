import cv2 as cv
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

print(cv.add(x,y))
# saturated operation : all operations are limited to a fixed range between min and max value
# 이 경우 더한값이 255보다 크면 255로 값이 정해짐
print(x+y)
# modulo operation : returns the remainder or signed remainder of a division
# 이 경우 더한 값이 255보다 크면 256으로 나눈 나머지가 됨 (250+10)%256 = 4

# Image Blending
# 블렌딩이나 투명감 주기 위해 이미지에 다른 가중치 부여
# ex) g(X) = (1-a)f0(x) + af1(x)
# 두 사진의 크기 동일해야함.

img1 = cv.imread('Kyungheeuniv.jpg')
img2 = cv.imread('son1.jpg')

dst = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destoyAllWindows()