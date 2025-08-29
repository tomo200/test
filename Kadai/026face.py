# -*- coding: utf-8 --* 
import cv2
import os
import numpy as np

file_src = "image/soccer.png"
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_dst = img_src.copy()
cv2.namedWindow('src')

cascadeName = "haarcascade_frontalface_alt.xml" # 分類器ファイル名
cascade_path = os.path.join(cv2.data.haarcascades, cascadeName)
cascade = cv2.CascadeClassifier(cascade_path) # 分類器の読み込み


img_gray = cv2.cvtColor(img_dst, cv2.COLOR_BGR2GRAY)

# 入力画像の表示
#cv2.imshow('src', img_src)

# スケール
scale = 1.2

# 処理時間短縮のために画像を縮小、ヒストグラムを均一化
img_small = cv2.resize(img_gray, (int(img_src.shape[1] / scale), int(img_src.shape[0] / scale)))
img_small = cv2.equalizeHist(img_small)

# マルチスケール（顔）探索
# 入力画像，縮小スケール，最低矩形数，（フラグ），最小矩形
searches = cascade.detectMultiScale(img_small, scaleFactor=1.1, minNeighbors=1, flags=0, minSize=(30,30))
print('KNWSYUTU',len(searches))


# 結果の描画
for (x, y, w, h) in searches:
    center = (int((x + w//2) * scale), int((y + h//2) * scale))
    radius = int(((w + h) // 4) * scale)
    cv2.circle(img_dst, center, radius, (0, 0, 255), 3, cv2.LINE_8, 0)


cv2.imshow('src', img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

