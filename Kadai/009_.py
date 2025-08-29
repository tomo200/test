# -*- coding: utf-8 -*-
import cv2
import numpy as np

# �摜�t�@�C�����J���[�œǂݍ���
file_src = 'image/fruits.jpg'
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)

# 2�̃E�B���h�E���쐬�i�I���W�i���Ɖ��H�摜�j
cv2.namedWindow('src')
cv2.namedWindow('dst')

# �摜�T�C�Y���擾
height, width, channels = img_src.shape[:3]

# �ҏW�p�摜�̏�����
img_dst = img_src.copy()
img_hsv = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)

# �s�N�Z����ύX����֐�
# ����:
#   img: HSV�摜
#   channel: 0=H, 1=S, 2=V
#   incre: �����l�i�}5�Ȃǁj
def modifyPixel(img, channel, incre):
    global height, width
    for yy in range(height):
        for xx in range(width):
            value = int(img[yy, xx][channel]) + incre

            # H�i�F���j��0?179�Ń��[�v������
            if channel == 0:
                img[yy, xx][channel] = (value + 180) % 180
            else:
                # S/V��0?255�ɐ���
                img[yy, xx][channel] = np.clip(value, 0, 255)

# �}�E�X�C�x���g�̏���
def onMouse(event, x, y, flags, param):
    global img_src, img_dst, img_hsv

    # ���N���b�N: +5
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left click at:", x, y)

        # H�i�F���j��+5���鏈��
        modifyPixel(img_hsv, 0, 5)

        # S�i�ʓx�j��+5���鏈���i�R�����g�A�E�g�j
        # modifyPixel(img_hsv, 1, 5)

        # V�i���x�j��+5���鏈���i�R�����g�A�E�g�j
        # modifyPixel(img_hsv, 2, 5)

        img_dst = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('dst', img_dst)

    # �E�N���b�N: -5
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("Right click at:", x, y)

        # H�i�F���j��-5���鏈��
        modifyPixel(img_hsv, 0, -5)

        # S�i�ʓx�j��-5���鏈���i�R�����g�A�E�g�j
        # modifyPixel(img_hsv, 1, -5)

        # V�i���x�j��-5���鏈���i�R�����g�A�E�g�j
        # modifyPixel(img_hsv, 2, -5)

        img_dst = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('dst', img_dst)

# �摜���E�B���h�E�ɕ\��
cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)

# �}�E�X�R�[���o�b�N��ݒ�
cv2.setMouseCallback('dst', onMouse)

# �L�[���͂�҂��ďI��
cv2.waitKey(0)
cv2.destroyAllWindows()