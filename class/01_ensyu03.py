# -*- coding: utf-8 --*

import cv2

import numpy as np
img =np.zeros((480, 640)).astype(np.uint8)


cv2.namedWindow('src')

file_src = 'image/lena.jpg'

img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
                                        
cv2.imshow('src', img_src)





#�A�N�V�������s����܂Ń��[�v
while True: 

     #�L�[���������܂ő҂ikey�ɓ��͂����L�[�́u���l�v������j
    key=cv2.waitKey(0)

    kye=ord('q') #ord�֐��E�E�E�L�[�́u���l�v���擾�iq�L�[�̒l���m�F�j

    if key == ord('q'): #�L�[�������ꂽ��I��


        break   


cv2.destroyAllWindows()


