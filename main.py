import cv2
import numpy as np
#�摜���쐬�i8�r�b�g(0�`255)�̓񎟌��R�[�h�z���0�������@�O���[�X�P�[��

img =np.zeros((480, 640)).astype(np.uint8)

#�摜���E�B���h�E�ɕ\��

cv2.imshow('src', img)

#�L�[���͂��ێ��i0�j�͖����ɑҋ@�A�C�ӂ̃L�[�ŕ���

cv2.waitKey(0)

#���ׂẴE�B���h�E�����

cv2.destroyAllWindows()
