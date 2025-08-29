# -*- coding: utf-8 --*
import cv2
import numpy as np

 
file_src = 'image/horse.jpg '
file_src2 = 'image/sougen.jpg'
 
 
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_dst = img_src.copy()
img_src2 = cv2.imread(file_src2, cv2.IMREAD_COLOR)
cv2.namedWindow('src')
cv2.namedWindow('src2')
cv2.namedWindow('dst')



# = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
img_gray=cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)
thresh = 200
img_data=cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)[1]
#�O���[�X�P�[���摜��3�̃J���[�摜�̍���
img_mask=cv2.merge((img_data, img_data, img_data))
img_mask=cv2.bitwise_not(img_mask)
#cv2.imshow('dst',img_mask)#-------B�摜



haikei=img_src2  #-----���摜

img_mask2 = cv2.bitwise_not(img_mask)#���摜

img_result=cv2.bitwise_and(img_src,img_mask) #---e�̖��@�@a,b�̘_����



img_result2=cv2.bitwise_and(img_mask2, haikei)#----f�̖��


img_result3=cv2.bitwise_or(img_result2, img_result)#�@e��f�̘_�����Z


#-----�o��---------------
cv2.imshow('src', img_src)
cv2.imshow('src2', img_src2)
cv2.imshow('dst',img_result3) 


cv2.waitKey(0)
cv2.destroyAllWindows()

