import cv2 as cv
import numpy as np

# Load two images
img1 = cv.imread('son.jpg')
img2 = cv.imread('opencv-logo.png')

# Put logo on top-left corner
# Create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Create a mask of logo and create its inverse mark also
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
# cv2.threshold() : 기준이 되는 임계값보다 작으면 흑, 크면 백이 되도록 만들때 이용하는 함수
# Parameters : src - input image
#              thresh - 임계값
#              maxval - 임계값을 넘었을 때 적용할 value
#              type - thresholding type
#              type 종류   - BINARY, BINARY_INV, TRUNC, TOZERO, TOZERO_INV
mask_inv = cv.bitwise_not(mask)
# bitwise_and,bitwise_or,bitwise_not,bitwise_xor
# parameters : src1 - 이미지 파일, src2 - 이미지 파일
#              dst - 결과파일, mask - 적용 영역 지정
# and 연산 : 모두 흰색(1)인 부분만 흰색
# or 연산 : 모두 검은색(0)인 부분만 검정색
# not 연산 : B 그림 색이 반대로
# xor 연산 : 값이 같으면 검은색, 다르면 흰색


#Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi, mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2, img2, mask = mask)

# Put logo in ROI and modify the main image
dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst


cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()
