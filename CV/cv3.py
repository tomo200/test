# -*- coding: utf-8 -*-
import cv2
import numpy as np

# �t�@�C���p�X
file_src1 = 'image/img.jpg'
file_src2 = 'image/human.png'

# �摜�ǂݍ���
img1 = cv2.imread(file_src1, cv2.IMREAD_COLOR)
img2 = cv2.imread(file_src2, cv2.IMREAD_COLOR)

# �����T�C�Y�Ƀ��T�C�Y
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# �E�B���h�E�쐬
cv2.namedWindow('Blend')

# �g���b�N�o�[�p�̋�֐�
def nothing(x):
    pass

# �g���b�N�o�[�쐬�i0?100�j
cv2.createTrackbar('Alpha', 'Blend', 0, 100, nothing)

while True:
    # �g���b�N�o�[�̒l���擾
    alpha = cv2.getTrackbarPos('Alpha', 'Blend') / 100.0
    beta = 1.0 - alpha

    # ���d����
    blended = cv2.addWeighted(img1, beta, img2, alpha, 0)

    # �\��
    cv2.imshow('Blend', blended)

    # ESC�L�[�ŏI��
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
