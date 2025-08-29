# -*- coding: utf-8 -*-

import cv2
import os
import numpy as np

file_src = "image/street.jpg"
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_dst = img_src.copy()
cv2.namedWindow('src')

img_rgb = cv2.cvtColor(img_src, cv2.COLOR_BGR2RGB)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
boxes, weights = hog.detectMultiScale(img_rgb, winStride=(4, 4), padding=(8, 8), scale=1.05)
print('kensyutu', len(boxes))

for (x, y, w, h) in boxes:
    cv2.rectangle(img_dst, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow('src', img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
