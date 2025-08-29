# -*- coding: utf-8 --* 
import cv2 
# 画像読込み（white.png） 
file_src = 'image/white.png' 
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR) 
cv2.namedWindow('src') 
# 関数定義：マウスが押されたら座標・ピクセル値を表示 
def onMouse(event, x, y, flags, params): 
    if event == cv2.EVENT_LBUTTONDOWN: 
        print(x, y) 
        print(img_src[y,x])
# 画像表示 
cv2.imshow('src', img_src) 
# ‘src’ウインドウにマウスイベント発生時、関数呼び出しをセット 
cv2.setMouseCallback('src', onMouse) 
# キーボード入力待ち※マウスイベント受け付け中 
cv2.waitKey(0) 
cv2.destroyAllWindows()