# -*- coding: utf-8 --* 
import cv2
import numpy as np

#ブローバル変数
x1=0
y1=0
x2=0
y2=0
click = 0 # クリック回数
color=[0,255,0] #カラー

#バスの指定
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










#画像の表示
cv2.imshow('src',img_src)
cv2.setMouseCallback('src',onMouse)


while True: 

     #キーが押されるまで待つ（keyに入力したキーの「数値」が入る）
    key=cv2.waitKey(0)

    kye=ord('q') #ord関数・・・キーの「数値」を取得（qキーの値を確認）

    if key == ord('q'): #キーが押されたら終了

        break   

cv2.destroyAllindows()

