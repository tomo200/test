# -*- coding: utf-8 --* 
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
boxes, weights = hog.detectMultiScale(img_rgb, winStride=(4,4), padding=(64, 64),scale=1.025)
print('Kensyutu', len(boxes))

#信頼度の数値によって短径のいろを変化させてる。
for (box,weight) in zip(boxes,weights):

    x,y,w,h=box

    if weight>1.0:      #信頼度が0.8よりおおきい
        color=(0, 0, 255)

    elif weight>0.7:    #信頼度が0.5よりおおきい
        color=(0, 100, 255)

    else:
        color=(0, 200, 255)

    

    cv2.rectangle(img_dst, (x, y), (x + w, y + h), color, 2) #数値の表示

    cv2.putText(img_dst, f"{weight:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)


cv2.imshow('src', img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()