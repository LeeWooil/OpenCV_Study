import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('nike-logo.jpg',0)
kernel = np.ones((5,5), np.uint8)
erosion = cv.erode(img, kernel, iterations = 2)
dilation = cv.dilate(img,kernel, iterations = 2)

plt.subplot(131), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(erosion), plt.title('erosion')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(dilation), plt.title('dilation')
plt.xticks([]), plt.yticks([])
plt.show()

