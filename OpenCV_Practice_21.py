import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('opencv-logo.png')
blur = cv.blur(img,(5,5))
# Gaussian Blurring : cv.GaussianBlur(img,(5,5))
# Median Blur : cv.medianBlur(img,5)
# Bilateral Filtering : cv.bilateralFilter,img,9,75,75)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()