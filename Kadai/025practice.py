# -*- coding: utf-8 -*-
import cv2
import numpy as np

file_src = 'image/shape.png'
 
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_dst = img_src.copy()
cv2.namedWindow('src')


# コーナー検出用パラメータ
qualityLevel = 0.05 #制度
minDistance = 10  #隣り合う円との距離


def updateImage(val):
    global img_src, img_dst, qualityLevel, minDistance

    img_dst = img_src.copy()

    img_gray = cv2.cvtColor(img_dst, cv2.COLOR_BGR2GRAY)

    # コーナー検出
    
    thresh = 230
    ret, img_gray = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)

    corners = cv2.goodFeaturesToTrack(img_gray, 80, qualityLevel,minDistance) #flatで

    # 検出箇所に円を描画する
    if corners is not None:
	#
        print(corners.shape)
	#
        corners = corners.reshape(-1, 2)
	#
        for x, y in corners:
            cv2.circle(img_dst, (int(x), int(y)), 1, (0, 0, 255), -1)
            cv2.circle(img_dst, (int(x), int(y)), 8, (0, 0, 255))

    cv2.imshow('src', img_dst)


def onTrackbarQ(val):
    global qualityLevel
    if val == 0:
        qualityLevel = 1 * 0.01
    else:
        qualityLevel = float(val) * 0.01
    updateImage(val)


def onTrackbarM(val):
    global minDistance
    if val < 5:
        minDistance = 5.0
    else:
        minDistance = float(val)
    updateImage(val)


cv2.imshow('src', img_dst)
 
cv2.createTrackbar("QL", 'src', 5, 100, onTrackbarQ)
cv2.createTrackbar("MD", 'src', 10, 100, onTrackbarM)

cv2.waitKey(0)
cv2.destroyAllWindows()
