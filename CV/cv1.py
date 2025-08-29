# -*- coding: utf-8 -*-
#作成者　佐々木智幸
#作成日   2025/07/24

import cv2
import numpy as np

cnt = 0  # 表示する画像のインデックス

cv2.namedWindow('src')  # ウィンドウを先に作成しておく

def onMouse(event, x, y, flags, param):
    global cnt
    if event == cv2.EVENT_LBUTTONDOWN:  #左クリックした際にifの中を処理
        cnt = (cnt + 1) % 6  # 画像は n0.png ～ n5.pngのループ

cv2.setMouseCallback('src', onMouse)

#cntの値ごとに出力したい画像を出力するループ文
while True:
    file_src = f'image/n{cnt}.jpg'
    img_r = cv2.imread(file_src)

    if img_r is None:
        print('Image not found:', file_src)
        break

    cv2.imshow('src', img_r)

    key = cv2.waitKey(1) 

    if key == ord('q'): #ｑのボタンでループ終了
        break

cv2.destroyAllWindows()
