# -*- coding: utf-8 --*

import cv2
import numpy as np

# ��`�\����ON/OFF
DRAW_OFF = 0
DRAW_ON = 1

file_src = 'image/roi_pic.jpg'

img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_dst = img_src.copy()



cv2.namedWindow('src')
cv2.namedWindow('dst')

draw = DRAW_OFF
udo_img=None

# �N���b�N���W�P�ƂQ
#�^�v���z��
clk1 = (0, 0)
clk2 = (0, 0)


def onMouse(event, x, y, flags, params):
    global img_src, img_dst, draw, clk1, clk2
    if event == cv2.EVENT_LBUTTONDOWN:  # ���}�E�X�_�E��
        draw = DRAW_ON
        print(x, y)
        clk1 = (x, y)
        undo_img = img_dst.copy() 

    elif event == cv2.EVENT_LBUTTONUP:  # ���}�E�X�A�b�v
        draw = DRAW_OFF
        print(x, y)
        clk2 = (x, y)
        width = clk2[0] - clk1[0]
        height = clk2[1] - clk1[1]
        if width > 1 and height > 1:
            #img_dst = img_src.copy()
            # �����͈͂��擾
            s_roi = img_dst[clk1[1]:clk2[1], clk1[0]:clk2[0]]
          
            # �����͈͂𑀍� 
            #  s_roi = 255 - s_roi 
            angle = -15.0 
            scale = 1.0 
            center = tuple(np.array([s_roi.shape[1] * 0.5, s_roi.shape[0] * 0.5])) 
            rot_mat = cv2.getRotationMatrix2D(center, angle, scale) #��]
            size = tuple(np.array([s_roi.shape[1], s_roi.shape[0]])) 
            s_roi = cv2.warpAffine(s_roi, rot_mat, size, flags = cv2.INTER_CUBIC, 
            borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255)) 

            img_dst[clk1[1]:clk2[1], clk1[0]:clk2[0]]=s_roi
            cv2.imshow('dst',img_dst)


            # �o�͉摜�ɖ��ߍ���
            img_dst[clk1[1]:clk2[1], clk1[0]:clk2[0]]=s_roi
            cv2.imshow('dst',img_dst)
           
 
    elif event == cv2.EVENT_MOUSEMOVE:   # �}�E�X�ړ�
        
        if draw == DRAW_ON:
            temp = img_dst.copy()  # �ύX�_�F���摜�ł͂Ȃ��ҏW�摜���ꎞ�R�s�[
            cv2.rectangle(temp, clk1, (x - 1, y - 1), (255, 0, 0), 1)
            cv2.imshow('dst', temp)
    
    elif event == cv2.EVENT_RBUTTONDOWN:

        if undo_img is not None:
            img_dst = undo_img.copy()
            cv2.imshow('dst', img_dst)               
    

cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)
cv2.setMouseCallback('dst', onMouse)
cv2.waitKey(0)
cv2.imwrite("roi_result.jpg", img_dst)
cv2.destroyAllWindows()