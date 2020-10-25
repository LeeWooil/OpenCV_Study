import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("starry_night.jpg"))
#imread : 사진 불러오기 위한 함수, 첫번째 argument는 파일의 경로, 두번째 argument는 이미지의 포멧 설정

if img is None:
    sys.exit("Could not read the image.")
# 이미지가 정확히 불러졌는지 확인

cv.imshow("Display window", img)
#imshow : 이미지 보여주기 위한 함수, 첫번째 argument는 창의 이름, 두번째 argument는 보여질 cv::Mat object

k = cv.waitKey(0)
#waitKey 함수의 parameter는 사용자의 input을 얼마나 기다릴지 결정. 0은 계속해서 기다린다는 뜻

if k == ord("s"):
    cv.imwrite("starry_night.png", img)
# s키를 누르게 되면, 이미지를 파일로 저장. 이를 위해 imwrite 함수를 호출함. imwrite의 argument는 파일경로와 cv::Mat object