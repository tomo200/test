# -*- coding: utf-8 --*
import cv2
import numpy as np


file_src1 = 'image/vtest01.jpg'
file_src2 = 'image/vtest02.jpg'
file_src3 = 'image/vtest03.jpg'
 
img_src1 = cv2.imread(file_src1, cv2.IMREAD_GRAYSCALE)
img_src2 = cv2.imread(file_src2, cv2.IMREAD_GRAYSCALE)
img_src3 = cv2.imread(file_src3, cv2.IMREAD_GRAYSCALE)
img_dst = img_src1.copy()
cv2.namedWindow('src1')
cv2.namedWindow('src2')
cv2.namedWindow('src3')
cv2.namedWindow('dst')

#差分 1と2
img_m12=cv2.absdiff(img_src1,img_src2)
#差分　2と3
img_m23=cv2.absdiff(img_src2,img_src3)

#cv2.imshow('dst', img_m23)

#二値画像生成
thresh=25
img_div12=cv2.threshold(img_m12,thresh,255,cv2.THRESH_BINARY)[1]
img_div23=cv2.threshold(img_m23,thresh,255,cv2.THRESH_BINARY)[1]

#論理積
img_result=cv2.bitwise_and(img_div12,img_div23)
#cv2.imshow('dst', img_result)

#収縮・膨張
op=np.ones((1,1)).astype(np.uint8)
img_result=cv2.erode(img_result,op,iterations=4)
img_result=cv2.dilate(img_result,op,iterations=4)

img_dst=cv2.bitwise_and(img_result,img_src2)

cv2.imshow('src1', img_src1)
cv2.imshow('src2', img_src2)
cv2.imshow('src3', img_src3)
cv2.imshow('dst', img_dst)


cv2.waitKey(0)
cv2.destroyAllWindows()


