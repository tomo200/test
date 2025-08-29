# -*- coding: utf-8 --*
import cv2
import numpy as np

#�쐬��: 2025/07/29
#�쐬��: ���X�؁@�q�K

file_bkg = 'image/road_haikei.png'  #�w�i�摜
file_src= 'image/road_taisyo.png'   #�l���̉摜


#�l���摜�̃O���[�X�P�[����
img_src = cv2.imread(file_src, cv2.IMREAD_GRAYSCALE)
# dst�ɃR�s�[
img_dst = img_src.copy()
#�w�i�摜���O���[�X�P�[����
img_bkg = cv2.imread(file_bkg, cv2.IMREAD_GRAYSCALE)
# �w�i�摜�̃T�C�Y��Ώۉ摜�ɍ��킹��
img_bkg = cv2.resize(img_bkg, (img_src.shape[1], img_src.shape[0]))
cv2.namedWindow('src')
cv2.namedWindow('bkg')
cv2.namedWindow('dst')
#����
img_div=cv2.absdiff(img_src, img_bkg)

#��l�摜����
thresh=60 #�����U�O�ȏ�̂��̂𔒂�����B
img_div2=cv2.threshold(img_div,thresh,255,cv2.THRESH_BINARY)[1]

#�c�����k
# op=np.ones((1,1)).astype(np.uint8)
# img_md=cv2.erode(img_div2,op,iterations=4)
# img_md2=cv2.dilate(img_md,op,iterations=4)

#�J�[�l�����ׂĂO�ɒ�`���Ă���B
op = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], np.uint8)

img_md=cv2.dilate(img_div2,op,iterations=4)
#�m�C�Y�����炷����
img_md2=cv2.erode(img_md,op,iterations=4)


#�_����
img_result=cv2.bitwise_and(img_dst,img_md2)


cv2.imshow('src', img_src)
cv2.imshow('bkg', img_bkg)
cv2.imshow('dst', img_result)


cv2.waitKey(0)
cv2.destroyAllWindows()
