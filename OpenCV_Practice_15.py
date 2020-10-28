import numpy as np
import cv2 as cv

img = cv.imread('son.jpg')

res = cv.resize(img, None,fx=2,fy=2, interpolation = cv.INTER_CUBIC)
# cv.resize : resize an image
# Parameters : src - input image, dst - output image, dsize - output image size
#              fx - scale factor along the horizontal axis,
#              fy - scale factor along the vertical axis,
#              interpolation - Interpolation flag

# OR

height ,width = img.shape[:2]
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)

cv.imshow('img',img)
cv.imshow('res',res)
cv.waitKey(0)
cv.destroyAllWindows()
