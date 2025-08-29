# -*- coding: utf-8 -*-
import cv2
import numpy as np
 
file_src = 'image/Brasil1.jpg'
 
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
height, width, channels = img_src.shape[:3]
img_dst = img_src.copy()

cv2.namedWindow('src')
cv2.namedWindow('dst')

#1  
#h,w,c=img_src.shape   #元画像の大きさ取得
#img_dst = np.ones((h, w, c), np.uint8) * 255#画像を白に変換
#img_dst = np.full((h, w, c), 255, np.uint8)
DRAW_ON = False

img_dst = np.full((height, width, channels), 255, dtype=np.uint8)

# マスク画像（0＝何も表示しない、255＝表示する）
img_mask = np.zeros((height, width), dtype=np.uint8)


def onMouse(event, x, y, flags, params):
    global img_dst,img_mask,DRAW_ON

    if event == cv2.EVENT_LBUTTONDOWN:
        DRAW_ON = True

    elif event == cv2.EVENT_MOUSEMOVE:

         if DRAW_ON:
            print(x, y)
            #2
            cv2.circle(img_mask,center=(x,y),radius=100,color=255,thickness=-1)

            #3
            img_fg = cv2.bitwise_and(img_src, img_src, mask=img_mask)
            img_bg = cv2.bitwise_and(img_dst, img_dst, mask=cv2.bitwise_not(img_mask))
            img_dst = cv2.bitwise_or(img_fg, img_bg)
            
            cv2.imshow('dst', img_dst)
    elif event == cv2.EVENT_LBUTTONUP:
        DRAW_ON = False
 
 
cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)
 
cv2.setMouseCallback('dst', onMouse)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
