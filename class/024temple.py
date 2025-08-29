# -*- coding: utf-8 --*　　
import cv2
import numpy as np

 
file_src = 'image/m_parts.jpg'
file_src2 = 'image/m_template.jpg'
 
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_tmp = cv2.imread(file_src2, cv2.IMREAD_COLOR)
#img_dst = img_src.copy()
cv2.namedWindow('src')
cv2.namedWindow('dst')
 
#類似度の最大の場所を取得ーーーーーーーーーーーーーーーーーーーーーーーーーーー
img_result = cv2.matchTemplate(img_src, img_tmp, cv2.TM_CCOEFF_NORMED) #画像を一つ一つ確認したもの値
_, maxVal, _, maxLoc = cv2.minMaxLoc(img_result)    #類似度の高い低い値と場所を取得　4つ取得
topLeft = maxLoc   #画像の原点を指している座標
bottomRight = (topLeft[0] + img_tmp.shape[1], topLeft[1] + img_tmp.shape[0]) #右下の座標取得
cv2.rectangle(img_src, topLeft, bottomRight, (0, 0, 255), 1)
 

cv2.imshow('src', img_src)
cv2.imshow('dst', img_tmp)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
