# -*- coding: utf-8 -*-
import cv2
import numpy as np

file_src = "image/n1300503479.jpg"
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_dst = img_src.copy()
cv2.namedWindow('src')

img_gray = cv2.cvtColor(img_dst, cv2.COLOR_BGR2GRAY)

# 入力画像の表示
cv2.imshow('src', img_src)


#円検出の関数
circles = cv2.HoughCircles(img_gray,
                            cv2.HOUGH_GRADIENT, #ハフ返還の手法
                            dp=1.6, #処理時の解像度レベル　低いと厳しい
                            minDist=300, #隣り合う円検出する距離
                            param1=130,        #エッジによる色の検出 差が広がれば違うと判断
                            param2=100,           #信頼度の閾値　円なのかを判断
                            minRadius=50,      #円と判断する最小半径
                            maxRadius=250)      #円と判断する最大半径
if circles is not None:
    print(circles.shape)
    circles = circles[0, :].astype(int)
    print(circles.shape)
    for (x, y, r) in circles:
        cv2.circle(img_dst, (x, y), r, (100, 255, 100),10)
else:
    print("nothing")
cv2.imshow('src', img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

