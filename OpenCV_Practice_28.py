import numpy as np
import  cv2 as cv

img = cv.imread('Test.jpg',0)
ret, thresh = cv.threshold(img,127,255,0)
contours, hierarchy = cv.findContours(thresh,1,2)

cnt = contours[0]
M = cv.moments(cnt)
print(M)
# moments() : Calculates all of the moments up to the third order of a polygon or rasterized shape
area = cv.contourArea(cnt)
# contourArea() : Calculates a contour area
perimeter = cv.arcLength(cnt,True)
# arcLength() : Calculates a contour perimeter or a curve length
epsilon = 0.1*perimeter
approx = cv.approxPolyDP(cnt,epsilon,True)
# approxPolyDP : Approximates a polygonal curve with specified precision
# Convex Hull
hull = cv.convexHull(cnt)
# Checking Convexity
k = cv.isContourConvex(cnt)
# Bounding Rectangle
# straight bounding rectangle
x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# rotated rectangle
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img,[box],0,(0,0,255),2)
# Minimum Enclosing circle
(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv.circle(img,center,radius,(0,255,0),2)
# Fitting an Ellipse
ellipse = cv.fitEllipse(cnt)
cv.ellipse(img,ellipse,(0,255,0),2)
# Fitting a Line
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

cv.imshow('img',img)
cv.waitKey(0)