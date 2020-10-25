import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Drawing Circle
# parameters : img, center, radius, color, thickness,linetype,shift
cv.circle(img, (447, 63), 63, (0,0,255), -1)

# Drawing Ellipse
# parameters : center location(x,y), axes length(major axis length, minor axis length)
# angle(angle of rotation of ellipse in anti-clockwise direction), startAngle, endAngle
# color, thickness, line Type, shift
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Drawing Polygon
# 꼭짓점의 좌표를 정수형의 행렬로 정리
# parameters : img, pts, isClosed, color, thickness, line type, shift
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

# Adding Text to images
# parameters : img, text, org, fontFace, fontScale, color, thickness, ilne Type, bottomLeftOrigin
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV',(10,500),font,4,(255,255,255),2,cv.LINE_AA)

cv.imshow('img', img)
k = cv.waitKey(0)