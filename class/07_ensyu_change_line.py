# -*- coding: utf-8 --* 
import cv2 
# �摜�Ǎ��݁iwhite.png�j 
file_src = 'image/white.png' 
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR) 
cv2.namedWindow('src') 
# �֐���`�F�}�E�X�������ꂽ����W�E�s�N�Z���l��\�� 
def onMouse(event, x, y, flags, params): 
    if event == cv2.EVENT_LBUTTONDOWN: 
        print(x, y) 
        print(img_src[y,x])
# �摜�\�� 
cv2.imshow('src', img_src) 
# �esrc�f�E�C���h�E�Ƀ}�E�X�C�x���g�������A�֐��Ăяo�����Z�b�g 
cv2.setMouseCallback('src', onMouse) 
# �L�[�{�[�h���͑҂����}�E�X�C�x���g�󂯕t���� 
cv2.waitKey(0) 
cv2.destroyAllWindows()