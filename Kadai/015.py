# -*- coding: utf-8 --*

import cv2
import numpy as np

 
file_src = 'image/kasure.jpg'
 
img_src = cv2.imread(file_src, cv2.IMREAD_GRAYSCALE)
img_dst = img_src.copy()
cv2.namedWindow('src')
cv2.namedWindow('dst')

thresh = 246
ret, img_dst = cv2.threshold(img_src, thresh, 255, cv2.THRESH_BINARY)

element4 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.uint8)

img_dst = cv2.erode(img_dst, element4, iterations = 1) 

img_dst = cv2.morphologyEx(img_dst, cv2.MORPH_OPEN, element4, iterations=1) 


cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)
 
cv2.waitKey(0)
cv2.destroyAllWindows()