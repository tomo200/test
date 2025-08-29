# -*- coding: utf-8 -*-
import cv2

# ���摜�t�@�C���̃p�X��ݒ肵�A�J���[�摜�Ƃ��ēǂݍ���
file_src = 'image/fruits.jpg'
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)

# �\���E�B���h�E��2�쐬
cv2.namedWindow('src')
cv2.namedWindow('dst')

# �摜�T�C�Y�ƃ`���l�����̎擾
height, width, channels = img_src.shape[:3]

# ���摜���R�s�[���ďo�͗p�摜���쐬
img_dst = img_src.copy()

# BGR�摜��HSV�摜�ɕϊ��i�F���E�ʓx�E���x�ɕ����j
img_hsv = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)

# �֐��F�s�N�Z���̐��l��ς��� 
# �����F 
#    img�F�摜�f�[�^ 
#    yy�F�s�N�Z���c�����ʒu    
#    xx�F�s�N�Z���������ʒu 
#    n�F�s�N�Z���l�z��̓Y���i�O�`�Q�j 
#    incre�F�����l 

def modifyPixel(img, yy, xx, n, incre): 
    global height, width 
    for yy in range(0, height): 
        for xx in range(0, width): 
                
            value = int(img[yy,xx][n]) + incre 
            if value >= 0 and value <= 255: 
                img[yy,xx][n] = value 



# �}�E�X�C�x���g�p�̊֐��i�N���b�N�ŏ����𕪊�j
def onMouse(event, x, y, flags, params):
    global img_src, img_dst, img_hsv

    modifyPixel(img_dst,y,x,)

    # ���N���b�N�������ꂽ�Ƃ��̏���
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)




        # �N���b�N���ꂽ��f��HSV�̐F����ύX
        h, s, v = img_hsv[y, x]
        h = (h + 60) % 180  # HSV�F��ԂŐF����ς���i180���ő�j
        img_hsv[y, x] = (h, s, v)

        #�摜�ϊ����ĕ\������
        img_dst = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('dst', img_dst)

    # �E�N���b�N�������ꂽ�Ƃ��̏���
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x, y)
        # HSV�摜�S�̂̐F����ύX
        img_hsv[:, :, 0] = (img_hsv[:, :, 0] + 30) % 180

        # HSV�摜��BGR�摜�ɕϊ����ĕ\������
        img_dst = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('dst', img_dst)

# �摜��\���i���摜�ƕϊ����ʁj
cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)

# �}�E�X�C�x���g�֐���ݒ�idst�E�B���h�E��ŃN���b�N�������s���j
cv2.setMouseCallback('dst', onMouse)

# �L�[���������܂őҋ@
cv2.waitKey(0)

# ���ׂẴE�B���h�E�����
cv2.destroyAllWindows()