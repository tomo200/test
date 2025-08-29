# -*- coding: utf-8 --*

import cv2
import numpy as np


file_src ='image/animals.jpg'

img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_dst = img_src.copy()
cv2.namedWindow('src')
cv2.namedWindow('dst')


def onMouse(event, x, y, flags, params):
    global img_dst
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        img_dst = cv2.blur(img_dst, (11, 15)) #‰æ‘œ‚Ì•½ŠŠ‰»
        cv2.imshow('dst', img_dst)

    if event == cv2.EVENT_RBUTTONDOWN:
        k = 10
        op = np.array([[-k, -k,  -k],  
        [-k, 1+8*k, -k], 
        [-k, -k,    -k]])  
        img_tmp = cv2.filter2D(img_dst, -1, op) 
        img_dst = cv2.convertScaleAbs(img_tmp, alpha = 1, beta = 0) 
        cv2.imshow('dst', img_dst)



cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)

cv2.setMouseCallback('dst', onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()


