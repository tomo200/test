
# -*- coding: utf-8 -*-
import cv2
import numpy as np

# グローバル変数
x1 = y1 = x2 = y2 = 0
click = 0
color = [0, 255, 0]

# 画像パス
file_src = 'image/fruits.jpg'
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)

def rectPixel(img, y1, x1, y2, x2, color):
    x_s, x_e = sorted([x1, x2])
    y_s, y_e = sorted([y1, y2])

    for i in range(y_s, y_e):
        for j in range(x_s, x_e):
            img[i][j] = color

def onMouse(event, x, y, flags, params):
    global x1, y1, x2, y2, click

    if event == cv2.EVENT_LBUTTONDOWN:
        if click == 0:
            x1, y1 = x, y
            click = 1
        else:
            x2, y2 = x, y
            rectPixel(img_src, y1, x1, y2, x2, color)
            click = 0
            cv2.imshow('src', img_src)  # 再描画

# 画像の表示とマウスイベント設定
cv2.imshow('src', img_src)
cv2.setMouseCallback('src', onMouse)

# qキーで終了
while True:
    key = cv2.waitKey(0)
    if key == ord('q'):
        break

cv2.destroyAllWindows()