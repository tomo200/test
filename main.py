import cv2
import numpy as np
#画像を作成（8ビット(0～255)の二次元コード配列に0初期化　グレースケール

img =np.zeros((480, 640)).astype(np.uint8)

#画像をウィンドウに表示

cv2.imshow('src', img)

#キー入力を維持（0）は無限に待機、任意のキーで閉じる

cv2.waitKey(0)

#すべてのウィンドウを閉じる

cv2.destroyAllWindows()
