# -*- coding: utf-8 --*
import cv2
import numpy as np
 

#パスをとる
file_src = 'image/mountain.png' 

#カラーで読み込む
#img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
#img_dst = img_src.copy()

#グレースケール
img_src = cv2.imread(file_src, cv2.IMREAD_GRAYSCALE)
img_dst = img_src.copy()



#オリジナルと編集用に名前づけ
cv2.namedWindow('src')
cv2.namedWindow('dst')



# ルックアップテーブルによる画素値の変換

table = np.arange(256, dtype = np.uint8)

for i in range(0, 256):

    table[i] = 127+i/2
    
   
   # if i <128:
    #    table[i] = 127
    #else:
        #table[i] = 255

for i in range(0, 256):
    print('table[', i, '] =', table[i])

img_dst = cv2.LUT(img_src, table)



cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()





