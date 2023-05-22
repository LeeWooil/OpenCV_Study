import cv2
"""
image1 = cv2.VideoCapture(0)
image1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
image1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while cv2.waitKey(33) < 0 :
    ret, frame = image1.read()
    cv2.imshow("VideoFrame", frame)
    
cv2.imshow(image1,'image11')
"""
"""
image_color = cv2.imread('C:\Hyper\picture1.png',cv2.IMREAD_COLOR)
image_gray = cv2.imread('C:\Hyper\picture1.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('color',image_color)
cv2.imshow('gray',image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('picture_gray.png',image_gray)
"""
"""
image_color=cv2.imread('C:\Hyper\lenna.png',cv2.IMREAD_COLOR)

cv2.imshow('color',image_color)
image_color_rgb = cv2.cvtColor(image_color,cv2.COLOR_BGR2RGB)
cv2.imshow('RGB2',image_color_rgb)
image_color_gray = cv2.cvtColor(image_color,cv2.COLOR_BGR2GRAY)
cv2.imshow('GRAY',image_color_gray)
cv2.waitKey(0)
"""
"""
image1 = cv2.VideoCapture(0)
image1.set(cv2.CAP_PROP_FRAME_WIDTH,640)
image1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while cv2.waitKey(33) <0:
    ret,frame = image1.read()
    cv2.imshow("videoFrame",frame)
    image1_RGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow("RGB2",image1_RGB)
    image1_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("GRAY",image1_gray)
"""
"""
image_color=cv2.imread('C:\Hyper\lenna.png',cv2.IMREAD_COLOR)
row = image_color.shape[0]
col = image_color.shape[1]
image_color_gray = cv2.cvtColor(image_color,cv2.COLOR_BGR2GRAY)
for i in range(row):
    for j  in range(col):
        if image_color_gray[i][j] < 128:
            image_color_gray[i][j] = 64
        else :
            image_color_gray[i][j] = 192
cv2.imshow('GRAY2',image_color_gray)
cv2.waitKey(0)
"""
image_color=cv2.imread('C:\Hyper\lenna.png',cv2.IMREAD_COLOR)
row = image_color.shape[0]
col = image_color.shape[1]
image_color_gray = cv2.cvtColor(image_color,cv2.COLOR_BGR2GRAY)
image_color_reverse = cv2.cvtColor(image_color,cv2.COLOR_BGR2GRAY)

for i in range(row):
    for j  in range(col):
        image_color_reverse[i][j] = image_color_gray[i][col-j-1]

cv2.imshow('REVERSE',image_color_reverse)
cv2.waitKey(0)
