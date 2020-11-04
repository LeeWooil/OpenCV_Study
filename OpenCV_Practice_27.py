import numpy as np
import  cv2 as cv

im = cv.imread('Test.jpg')
imgray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray,127,255,0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# cv.findContours : argumnets - source image, contour retrieval mode, contour approximation method
# Contour : Python list of all the contours in the image, Numpy array of (x,y) coordinates of boundary points of the object

# Draw contours
cv.drawContours(im,contours,-1,(0,255,0),3)
"""
cv.drawContours(im,contours,3,(0,255,0),3)
# To draw an individual contour
#cnt = contours[4]
#cv.drawContours(im,[cnt],0,(0,255,0),3)
"""
# cv.drawContours : arguments - source image, contours which should be passed as a Python list, index of contours, color, thickness
cv.imshow('img',im)
cv.waitKey(0)