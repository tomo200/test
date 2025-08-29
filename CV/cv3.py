# -*- coding: utf-8 -*-
import cv2
import numpy as np

# ファイルパス
file_src1 = 'image/img.jpg'
file_src2 = 'image/human.png'

# 画像読み込み
img1 = cv2.imread(file_src1, cv2.IMREAD_COLOR)
img2 = cv2.imread(file_src2, cv2.IMREAD_COLOR)

# 同じサイズにリサイズ
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# ウィンドウ作成
cv2.namedWindow('Blend')

# トラックバー用の空関数
def nothing(x):
    pass

# トラックバー作成（0?100）
cv2.createTrackbar('Alpha', 'Blend', 0, 100, nothing)

while True:
    # トラックバーの値を取得
    alpha = cv2.getTrackbarPos('Alpha', 'Blend') / 100.0
    beta = 1.0 - alpha

    # 加重合成
    blended = cv2.addWeighted(img1, beta, img2, alpha, 0)

    # 表示
    cv2.imshow('Blend', blended)

    # ESCキーで終了
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
