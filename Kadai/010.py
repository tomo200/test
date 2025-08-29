# -*- coding: utf-8 -*-
import cv2
import numpy as np

# トラックバー用の空関数（コールバック用）
def nothing(x):
    pass

# 関数：画像の指定チャネルのピクセル値を一括で変更する
# 引数：
# img : 対象の画像
# n : BGRのチャネル番号（0: Blue, 1: Green, 2: Red）
# value : 設定する値（0?255）
def modifyPixel2(img, n, value): 
    global height, width 
    for yy in range(0, height): 
        for xx in range(0, width): 
            if 0 <= value <= 255: 
                img[yy, xx][n] = value

# 画像の読み込み（カラー）
file_src = 'image/fruits.jpg'
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)


# ウィンドウの作成
cv2.namedWindow('src')
cv2.namedWindow('dst')

# 画像サイズとチャンネル数を取得
height, width, channels = img_src.shape[:3]

# コピーとHSV変換（今後の処理に備えて）
img_dst = img_src
img_hsv = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)

# 最初に画像を表示
cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)
cv2.createTrackbar('S', 'dst', 127, 255, nothing)   #ｓ左上名前　　127初期値　255マックス値　

# 無限ループでトラックバーの値を取得・表示
while True:
    # トラックバーの値を取得
    v = cv2.getTrackbarPos('S', 'dst')

    modifyPixel2(img_hsv,1,v)

    img_dst= cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR) 

    # 表示更新
    cv2.imshow('dst', img_dst)

    img_hsv_mod = img_hsv.copy()
    img_hsv_mod[:, :,1 ] = v  # Sチャンネルに値vを設定  彩度　　黒くなれば明度
    img_dst = cv2.cvtColor(img_hsv_mod, cv2.COLOR_HSV2BGR)
    # 'q'またはESCで終了
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q') or key == 27:
        break

# ウィンドウを閉じる
cv2.destroyAllWindows()