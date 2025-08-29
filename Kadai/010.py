# -*- coding: utf-8 -*-
import cv2
import numpy as np

# �g���b�N�o�[�p�̋�֐��i�R�[���o�b�N�p�j
def nothing(x):
    pass

# �֐��F�摜�̎w��`���l���̃s�N�Z���l���ꊇ�ŕύX����
# �����F
# img : �Ώۂ̉摜
# n : BGR�̃`���l���ԍ��i0: Blue, 1: Green, 2: Red�j
# value : �ݒ肷��l�i0?255�j
def modifyPixel2(img, n, value): 
    global height, width 
    for yy in range(0, height): 
        for xx in range(0, width): 
            if 0 <= value <= 255: 
                img[yy, xx][n] = value

# �摜�̓ǂݍ��݁i�J���[�j
file_src = 'image/fruits.jpg'
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)


# �E�B���h�E�̍쐬
cv2.namedWindow('src')
cv2.namedWindow('dst')

# �摜�T�C�Y�ƃ`�����l�������擾
height, width, channels = img_src.shape[:3]

# �R�s�[��HSV�ϊ��i����̏����ɔ����āj
img_dst = img_src
img_hsv = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)

# �ŏ��ɉ摜��\��
cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)
cv2.createTrackbar('S', 'dst', 127, 255, nothing)   #�����㖼�O�@�@127�����l�@255�}�b�N�X�l�@

# �������[�v�Ńg���b�N�o�[�̒l���擾�E�\��
while True:
    # �g���b�N�o�[�̒l���擾
    v = cv2.getTrackbarPos('S', 'dst')

    modifyPixel2(img_hsv,1,v)

    img_dst= cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR) 

    # �\���X�V
    cv2.imshow('dst', img_dst)

    img_hsv_mod = img_hsv.copy()
    img_hsv_mod[:, :,1 ] = v  # S�`�����l���ɒlv��ݒ�  �ʓx�@�@�����Ȃ�Ζ��x
    img_dst = cv2.cvtColor(img_hsv_mod, cv2.COLOR_HSV2BGR)
    # 'q'�܂���ESC�ŏI��
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q') or key == 27:
        break

# �E�B���h�E�����
cv2.destroyAllWindows()