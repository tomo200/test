# -*- coding: utf-8 --*�@�@
import cv2
import numpy as np

 
file_src = 'image/m_parts.jpg'
file_src2 = 'image/m_template.jpg'
 
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_tmp = cv2.imread(file_src2, cv2.IMREAD_COLOR)
#img_dst = img_src.copy()
cv2.namedWindow('src')
cv2.namedWindow('dst')
 
#�ގ��x�̍ő�̏ꏊ���擾�[�[�[�[�[�[�[�[�[�[�[�[�[�[�[�[�[�[�[�[�[�[�[�[�[�[�[
img_result = cv2.matchTemplate(img_src, img_tmp, cv2.TM_CCOEFF_NORMED) #�摜�����m�F�������̒l
_, maxVal, _, maxLoc = cv2.minMaxLoc(img_result)    #�ގ��x�̍����Ⴂ�l�Əꏊ���擾�@4�擾
topLeft = maxLoc   #�摜�̌��_���w���Ă�����W
bottomRight = (topLeft[0] + img_tmp.shape[1], topLeft[1] + img_tmp.shape[0]) #�E���̍��W�擾
cv2.rectangle(img_src, topLeft, bottomRight, (0, 0, 255), 1)
 

cv2.imshow('src', img_src)
cv2.imshow('dst', img_tmp)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
