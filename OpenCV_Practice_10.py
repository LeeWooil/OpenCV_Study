# Making Border for Images(Padding)

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img1 = cv.imread('opencv-logo.png')

# cv.copyMakeBorder() arguments
# src - input image
# top,bottom, left, right - border width in number of pixels in corresponding direction
# border type - cv.BORDER_CONSTANT : add constant colored border
#             - cv.BORDER_REFLECT : border will be mirror reflection of the border elements
#             - cv.BORDER_REFLECT_101(BORDER_DEFAULT) : same as above
#             - cv.BORDER_REPLICATE : last element is replicated throughout
#             - cv.BORDER_WRAP
# value - color of border if border type is cv.BORDER_CONSTANT

replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)

#.subplot : 그래프가 그려질 위치를 격자형으로 지정, subplot(nrow,ncol,pos)
plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()
