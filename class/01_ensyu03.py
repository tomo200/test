# -*- coding: utf-8 --*

import cv2

import numpy as np
img =np.zeros((480, 640)).astype(np.uint8)


cv2.namedWindow('src')

file_src = 'image/lena.jpg'

img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
                                        
cv2.imshow('src', img_src)





#アクションが行われるまでループ
while True: 

     #キーが押されるまで待つ（keyに入力したキーの「数値」が入る）
    key=cv2.waitKey(0)

    kye=ord('q') #ord関数・・・キーの「数値」を取得（qキーの値を確認）

    if key == ord('q'): #キーが押されたら終了


        break   


cv2.destroyAllWindows()


