import numpy as np
import cv2 as cv

img = cv.imread('son.jpg',0)
rows, cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))
# cv.wrapAffine : applies an affine transformation to an image
# Parameters : src- input image, dst - output image, M - 2X3 transformation matrix
#              dsize - size of output image, flags - combination of interpolation method
#              borderMode, borderValue

cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()