# -*- coding: utf-8 --*
import cv2
import numpy as np

a=1.0   #画像１の重み
b=0.0  #画像２の重み
step=0.1  #重みに対して変更をかける値

file_src = 'image/airplane.jpg'
file_src2 = 'image/fruits_alp.jpg'
 
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_dst = img_src.copy()
img_src2 = cv2.imread(file_src2, cv2.IMREAD_COLOR)
cv2.namedWindow('src')
cv2.namedWindow('src2')
cv2.namedWindow('dst')


img_dst = cv2.addWeighted(img_src, a, img_src2, b, 0)

def updata():
    global img_dst
    img_dst = cv2.addWeighted(img_src, a, img_src2, b, 0)
    cv2.imshow('dst',img_dst)




def onMouse(event, x, y, flags, params):
    global a,b
    if event == cv2.EVENT_LBUTTONDOWN:  #左クリック押された場合
        if a>0.0:
            a=round(a-step , 1) 
            b=round(b+step , 1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        if b>0.0:
            a=round(a+step , 1) 
            b=round(b-step , 1)

    
    updata()


        

cv2.imshow('src', img_src)
cv2.imshow('src2', img_src2)
cv2.imshow('dst',img_dst)

cv2.setMouseCallback('dst', onMouse,img_src2)
 
cv2.waitKey(0)
cv2.destroyAllWindows()

