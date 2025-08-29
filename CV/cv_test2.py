# -*- coding: utf-8 --*
import cv2
import numpy as np

#作成日: 2025/07/29
#作成者: 佐々木　智幸

file_bkg = 'image/road_haikei.png'  #背景画像
file_src= 'image/road_taisyo.png'   #人物の画像


#人物画像のグレースケール化
img_src = cv2.imread(file_src, cv2.IMREAD_GRAYSCALE)
# dstにコピー
img_dst = img_src.copy()
#背景画像をグレースケール化
img_bkg = cv2.imread(file_bkg, cv2.IMREAD_GRAYSCALE)
# 背景画像のサイズを対象画像に合わせる
img_bkg = cv2.resize(img_bkg, (img_src.shape[1], img_src.shape[0]))
cv2.namedWindow('src')
cv2.namedWindow('bkg')
cv2.namedWindow('dst')
#差分
img_div=cv2.absdiff(img_src, img_bkg)

#二値画像生成
thresh=60 #差が６０以上のものを白くする。
img_div2=cv2.threshold(img_div,thresh,255,cv2.THRESH_BINARY)[1]

#膨張収縮
# op=np.ones((1,1)).astype(np.uint8)
# img_md=cv2.erode(img_div2,op,iterations=4)
# img_md2=cv2.dilate(img_md,op,iterations=4)

#カーネルすべて０に定義している。
op = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], np.uint8)

img_md=cv2.dilate(img_div2,op,iterations=4)
#ノイズを減らす処理
img_md2=cv2.erode(img_md,op,iterations=4)


#論理積
img_result=cv2.bitwise_and(img_dst,img_md2)


cv2.imshow('src', img_src)
cv2.imshow('bkg', img_bkg)
cv2.imshow('dst', img_result)


cv2.waitKey(0)
cv2.destroyAllWindows()
