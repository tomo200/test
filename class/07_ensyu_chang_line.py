# -*- coding: utf-8 --*

import cv2
import numpy as np

# �O���[�X�P�[���ŉ摜��ǂݍ���
gray_image = cv2.imread('image/fruits.jpg', cv2.IMREAD_GRAYSCALE)

# �ǂݍ��݊m�F
if gray_image is None:
    print("e")
    exit()

# �摜�̃R�s�[��p�Ӂi���摜��ێ��������ꍇ�j
modified_image = gray_image.copy()

# �}�E�X�C�x���g�����֐�
def on_mouse_click(event, x, y, flags, param):
    global modified_image

    if event == cv2.EVENT_LBUTTONDOWN:
        height, width = modified_image.shape  # �摜�̃T�C�Y���擾

        print(x,y)
        
        for i in range(width):  # ���������ׂẲ�f�ɑ΂���
            pixel_value = modified_image[y, i]
            new_value = min(pixel_value + 50, 255)  # 255�𒴂��Ȃ��悤��
            modified_image[y, i] = new_value  # �l���X�V

        cv2.imshow('Gray Image', modified_image)  # �摜���ĕ\��

# �E�B���h�E�ƃR�[���o�b�N�ݒ�
cv2.imshow('Gray Image', modified_image)
cv2.setMouseCallback('Gray Image', on_mouse_click)

# �������[�v�őҋ@�iEsc�L�[�ŏI���j
while True:
    if cv2.waitKey(1) & 0xFF == 27:  # 27��Esc�L�[�̃L�[�R�[�h
        break

cv2.destroyAllWindows()