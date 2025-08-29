# -*- coding: utf-8 --*

import cv2

import numpy as np
img =np.zeros((480, 640)).astype(np.uint8)


cv2.namedWindow('src')

file_src = 'image/lena.jpg'

img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
                                        
cv2.imshow('src', img_src)

cv2.waitKey(0)

cv2.destroyAllWindows()
