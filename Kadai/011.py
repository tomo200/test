# -*- coding: utf-8 --*
import cv2
import numpy as np
 

#�p�X���Ƃ�
file_src = 'image/mountain.png' 

#�J���[�œǂݍ���
#img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
#img_dst = img_src.copy()

#�O���[�X�P�[��
img_src = cv2.imread(file_src, cv2.IMREAD_GRAYSCALE)
img_dst = img_src.copy()



#�I���W�i���ƕҏW�p�ɖ��O�Â�
cv2.namedWindow('src')
cv2.namedWindow('dst')



# ���b�N�A�b�v�e�[�u���ɂ���f�l�̕ϊ�

table = np.arange(256, dtype = np.uint8)

for i in range(0, 256):

    table[i] = 127+i/2
    
   
   # if i <128:
    #    table[i] = 127
    #else:
        #table[i] = 255

for i in range(0, 256):
    print('table[', i, '] =', table[i])

img_dst = cv2.LUT(img_src, table)



cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()





