# -*- coding: utf-8 --*
import cv2
import numpy as np


file_src = 'image/tigers.jpg' 

img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_dst = img_src.copy()
cv2.namedWindow('src')
cv2.namedWindow('Lap')
# BGR -> GRAY
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)


#img_dst = img_gray


#img_gray = cv2.blur(img_gray, (1, 5)) 
#img_dst = cv2.Canny(img_gray, 50, 200) #Canny–@‚ðŽd—l

img_Lap = cv2.Laplacian(img_gray, cv2.CV_64F,ksize=3,scale=0.005) 



cv2.imshow('src', img_src)
cv2.imshow('Lap',img_Lap)

cv2.waitKey(0)
cv2.destroyAllWindows()
