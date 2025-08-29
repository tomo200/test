# -*- coding: utf-8 -*-
import cv2
import numpy as np

file_src = 'image/Brasil1.jpg'

img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
height, width, channels = img_src.shape[:3]

# ���摜�i�\���p�j
img_dst = np.full((height, width, channels), 255, dtype=np.uint8)

# �}�X�N�摜�i0�������\�����Ȃ��A255���\������j
img_mask = np.zeros((height, width), dtype=np.uint8)

cv2.namedWindow('src')
cv2.namedWindow('dst')

def onMouse(event, x, y, flags, params):
    global img_dst, img_mask

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)

        #2 �}�X�N�摜�ɍ��~�i���Sx,y, ���a10, ���F255, �h��Ԃ��j
        cv2.circle(img_mask, center=(x, y), radius=100, color=255, thickness=-1)

        #3 �}�X�N�����������摜����\���ibitwise�j
        img_fg = cv2.bitwise_and(img_src, img_src, mask=img_mask)
        img_bg = cv2.bitwise_and(img_dst, img_dst, mask=cv2.bitwise_not(img_mask))
        img_dst = cv2.bitwise_or(img_fg, img_bg)

        cv2.imshow('dst', img_dst)

cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)

cv2.setMouseCallback('dst', onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()
