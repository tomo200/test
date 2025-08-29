# -*- coding: utf-8 --* 
import cv2
import numpy as np

#�u���[�o���ϐ�
x1=0
y1=0
x2=0
y2=0
click = 0 # �N���b�N��
color=[0,255,0] #�J���[

#�o�X�̎w��
file_src='image/fruits.jpg'
img_src=cv2.imread(file_src,cv2.IMREAD_COLOR)



def rectPixel(img,y1,x1,y2,x2,color):
    if x1>x2:
        x_s=x2
        x_e=x1
    else:
        x_s=x1
        x_e=x2
    if y1>y2:
        y_s=y2
        y_e=y1
    else:
        y_s=y1
        y_e=y2


    for i in range(y_s,y_e):
        for j in range(x_s,x_e):
            img[i][j]=color



def onMouse(event,x,y,flags,params):
    if event ==cv2.EVENT_LBUTTONDOWN:
        global x1,y1,x2,y2,click,file_src
        
        if click == 0:
            x1=x
            y1=y
            click+=1
        else :
            x2=x
            y2=y
            rectPixel(img_src,y1,x1,y2,x2,color)
            click=0
            cv2.imshow('src', img_src)










#�摜�̕\��
cv2.imshow('src',img_src)
cv2.setMouseCallback('src',onMouse)


while True: 

     #�L�[���������܂ő҂ikey�ɓ��͂����L�[�́u���l�v������j
    key=cv2.waitKey(0)

    kye=ord('q') #ord�֐��E�E�E�L�[�́u���l�v���擾�iq�L�[�̒l���m�F�j

    if key == ord('q'): #�L�[�������ꂽ��I��

        break   

cv2.destroyAllindows()

