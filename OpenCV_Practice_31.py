import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Feature set containing (x,y) values of 25 known/training data
# 하나의 데이터당 (x,y) 좌표를 갖기 때문에 배열은 (25,2) 크기를 갖는다.
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
print(trainData)
# Label each one either Red or Blue with numbers 0 and 1
# 25개 데이터에 대해 0또는 1로 라벨을 붙임.
responses = np.random.randint(0,2,(25,1)).astype(np.float32)
print(responses)
# numpy.random.randint : Return random integers
# parameters : low, high, size, dtype
# astype : 모든 열의 데이터 타입 변경

# Take Red neighbours and plot them
red = trainData[responses.ravel()==0]
# .ravel() : 2차원 배열을 1차월 배열로
plt.scatter(red[:,0],red[:,1],80,'r','^')

# Take Blue neighbours and plot them
blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')
# plt.scatter : 산포 그래프 그리기
# parameter : x축과 y축을 리스트나 numpy 배열로 입력, s - 마커의 크기, c - 마커의 색상

newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

# KNN 알고리즘을 초기화
knn = cv.ml.KNearest_create()
# 좌표와 라벨을 전달하여 모델 훈련
knn.train(trainData, cv.ml.ROW_SAMPLE, responses)
# k=3로 해서 최근접 이웃들을 찾아서 새로 추가된 데이터가 어느쪽에 속하는 지 결정
ret, results, neighbours, dist = knn.findNearest(newcomer,3)

print("result : {}\n".format(results)) # 새로 추가된 데이터를 파란색인지 빨간색인지 판정
print("neighbours: {} \n".format(neighbours)) # 이웃에 파란색과 빨간색 사각형 구성을 알려줌
print("distance : {}\n".format(dist)) # 각각 데이터로부터의 거리

plt.show()