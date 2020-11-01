import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('nike-logo.jpg',0)
kernel = np.ones((5,5), np.uint8)

closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img,cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img,cv.MORPH_BLACKHAT, kernel)

plt.subplot(231), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232), plt.imshow(closing), plt.title('closing')
plt.xticks([]), plt.yticks([])
plt.subplot(233), plt.imshow(gradient), plt.title('gradient')
plt.xticks([]), plt.yticks([])
plt.subplot(234), plt.imshow(tophat), plt.title('tophat')
plt.xticks([]), plt.yticks([])
plt.subplot(235), plt.imshow(blackhat), plt.title('blackhat')
plt.xticks([]), plt.yticks([])
plt.show()