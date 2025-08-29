# -*- coding: utf-8 -*-
import cv2
import numpy as np

file_src = "image/stuff.jpg"
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_dst = img_src.copy()
cv2.namedWindow('src')

img_gray = cv2.cvtColor(img_dst, cv2.COLOR_BGR2GRAY)

# ���͉摜�̕\��
cv2.imshow('src', img_src)


#�~���o�̊֐�00
circles = cv2.HoughCircles(img_gray,
                            cv2.HOUGH_GRADIENT, #�n�t�Ԋ҂̎�@
                            dp=1.5,   #�������̉𑜓x���x���@�Ⴂ�ƌ�����
                            minDist=150, #�ׂ荇���~���o���鋗��
                            param1=150,        #�G�b�W�ɂ��F�̌��o �����L����ΈႤ�Ɣ��f
                            param2=60,          #�M���x��臒l�@�~�Ȃ̂��𔻒f
                            minRadius=10,      #�~�Ɣ��f����ŏ����a
                            maxRadius=100)      #�~�Ɣ��f����ő唼�a
if circles is not None:
    print(circles.shape)
    circles = circles[0, :].astype(int)
    print(circles.shape)
    for (x, y, r) in circles:
        cv2.circle(img_dst, (x, y), r, (0, 255, 0),5)
else:
    print("nothing")
cv2.imshow('src', img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

