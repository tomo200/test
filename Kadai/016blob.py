# -*- coding: utf-8 --*
import cv2
import numpy as np

file_src = 'image/rnd_circle0.png'

#黒の画像表示
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_dst = img_src.copy()

cv2.namedWindow('src')
cv2.namedWindow('dst')
cv2.namedWindow('black')

#サイズ取得
height, width, channels = img_src.shape[:3]
#黒画像の作成
img_z = np.zeros((height,width,1), np.uint8)



# BGR -> GRAY
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
# GRAY -> BINARY
thresh = 5
ret, img_dst = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)

label, img_lab = cv2.connectedComponents(img_dst)


for i in range(1,label):
    #ラベルの取得
    img_label = cv2.compare(img_lab, i, cv2.CMP_EQ)

    # ブロブの面積 
    m = cv2.moments(img_label) 
    area = m['m00'] 
    print(area)

    if area>500000:
        img_z = cv2.bitwise_or(img_z,img_label)
        
    

cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)
cv2.imshow('black',img_z)

cv2.waitKey(0)

cv2.destroyAllWindows()
