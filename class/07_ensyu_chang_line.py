# -*- coding: utf-8 --*

import cv2
import numpy as np

# グレースケールで画像を読み込み
gray_image = cv2.imread('image/fruits.jpg', cv2.IMREAD_GRAYSCALE)

# 読み込み確認
if gray_image is None:
    print("e")
    exit()

# 画像のコピーを用意（元画像を保持したい場合）
modified_image = gray_image.copy()

# マウスイベント処理関数
def on_mouse_click(event, x, y, flags, param):
    global modified_image

    if event == cv2.EVENT_LBUTTONDOWN:
        height, width = modified_image.shape  # 画像のサイズを取得

        print(x,y)
        
        for i in range(width):  # 横方向すべての画素に対して
            pixel_value = modified_image[y, i]
            new_value = min(pixel_value + 50, 255)  # 255を超えないように
            modified_image[y, i] = new_value  # 値を更新

        cv2.imshow('Gray Image', modified_image)  # 画像を再表示

# ウィンドウとコールバック設定
cv2.imshow('Gray Image', modified_image)
cv2.setMouseCallback('Gray Image', on_mouse_click)

# 無限ループで待機（Escキーで終了）
while True:
    if cv2.waitKey(1) & 0xFF == 27:  # 27はEscキーのキーコード
        break

cv2.destroyAllWindows()