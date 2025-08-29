# -*- coding: utf-8 --*
import cv2
import numpy as np

# ��`�\����ON/OFF
DRAW_OFF = 0
DRAW_ON = 1

file_src = 'image/t_insect.jpg' 

img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_dst = img_src.copy()
#cv2.namedWindow('src')
cv2.namedWindow('dst')

draw = DRAW_OFF

s_roi=None

# �N���b�N���W�P�ƂQ
clk1 = (0, 0)
clk2 = (0, 0)

cnt = 0

def onMouse(event, x, y, flags, params):
    global img_src, img_dst, draw, clk1, clk2, cnt
    if event == cv2.EVENT_LBUTTONDOWN:  # ���}�E�X�_�E��
        draw = DRAW_ON
        print(x, y)
        clk1 = (x, y)

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
            #resized = cv2.resize(img_dst, (320,240))
            resiz = cv2.resize(s_roi, None, fx=3.0, fy=3.0)
            
            # �ʃE�C���h�E���쐬 
            winname = 'dst' + str(cnt) 
            
            cv2.namedWindow(winname) 
            cv2.imshow(winname, resiz)
            # �����͈͂�ʃE�C���h�E�ɕ\�� 
            #cv2.imshow(winname,s_roi) 
       

            # �E�C���h�E�̃J�E���g
            cnt = cnt + 1
 
    elif event == cv2.EVENT_MOUSEMOVE:   # �}�E�X�ړ�
        if draw == DRAW_ON:
            img_dst = img_src.copy()
            # ��`�`��
            cv2.rectangle(img_dst, clk1, (x - 1, y - 1), (0, 255, 0), 3)
            cv2.imshow('dst', img_dst)


#cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)
 
cv2.setMouseCallback('dst', onMouse)
cv2.waitKey(0)
cv2.imwrite("roi_result.jpg", img_dst)
cv2.destroyAllWindows()
