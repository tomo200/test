# -*- coding: utf-8 -*-
#�쐬�ҁ@���X�ؒq�K
#�쐬��   2025/07/24

import cv2
import numpy as np

cnt = 0  # �\������摜�̃C���f�b�N�X

cv2.namedWindow('src')  # �E�B���h�E���ɍ쐬���Ă���

def onMouse(event, x, y, flags, param):
    global cnt
    if event == cv2.EVENT_LBUTTONDOWN:  #���N���b�N�����ۂ�if�̒�������
        cnt = (cnt + 1) % 6  # �摜�� n0.png �` n5.png�̃��[�v

cv2.setMouseCallback('src', onMouse)

#cnt�̒l���Ƃɏo�͂������摜���o�͂��郋�[�v��
while True:
    file_src = f'image/n{cnt}.jpg'
    img_r = cv2.imread(file_src)

    if img_r is None:
        print('Image not found:', file_src)
        break

    cv2.imshow('src', img_r)

    key = cv2.waitKey(1) 

    if key == ord('q'): #���̃{�^���Ń��[�v�I��
        break

cv2.destroyAllWindows()
