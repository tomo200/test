# -*- coding: utf-8 -*-
import cv2
import numpy as np

file_src = "image/rnd_circle0.png"
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_dst = img_src.copy()
cv2.namedWindow('src')

img_gray = cv2.cvtColor(img_dst, cv2.COLOR_BGR2GRAY)

# ì¸óÕâÊëúÇÃï\é¶
cv2.imshow('src', img_src)


#â~åüèoÇÃä÷êî
circles = cv2.HoughCircles(img_gray,
                            cv2.HOUGH_GRADIENT,
                           dp=1.2,
                           minDist=21,
                           param1=50,
                           param2=18,
                           minRadius=10,
                           maxRadius=60)
if circles is not None:
    print(circles.shape)
    circles = circles[0, :].astype(int)
    print(circles.shape)
    for (x, y, r) in circles:
        cv2.circle(img_dst, (x, y), r, (255, 255, 255),5)
else:
    print("nothing")
cv2.imshow('src', img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

