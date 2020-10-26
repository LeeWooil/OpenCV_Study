import numpy as np
import cv2 as cv

img = cv.imread('Son.jpg')

# access a pixel value by its row and column coordinates.
px = img[100,100]
print(px)

# accessing only blue pixel
blue = img[100,100,0]
print(blue)

# modify the pixel value
img[100,100] = [255,255,255]
print(img[100,100])

#accessing RED value
img.item(10,10,2)
# (10,10,2)인 픽셀의 2번째 값 출력
# Modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

#Accessing image properties
# return number of row, columns and channels
print(img.shape)
# Total number of pixels
print(img.size)
# image datatype
print(img.dtype)

# Image ROI(Region of Interest)
face = img[67:154, 177:258]
img[200:287, 50:131] = face

# Splitting and Merging Image Channels
b,g,r = cv.split(img)
img = cv.merge((b,g,r))


while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()