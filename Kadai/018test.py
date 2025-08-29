# -*- coding: utf-8 --*
import cv2
import numpy as np

alpha = 1.0  
beta = 0.0   
step = 0.1   



file_src = 'image/airplane.jpg'
file_src2 = 'image/fruits_alp.jpg'
img1 = cv2.imread(file_src, cv2.IMREAD_COLOR)
img2 = cv2.imread(file_src2, cv2.IMREAD_COLOR)


img_dst = cv2.addWeighted(img1, alpha, img2, beta, 0)


cv2.namedWindow('Image1')
cv2.namedWindow('Image2')
cv2.namedWindow('Blended')


def update_blend():
    global img_dst
    img_dst = cv2.addWeighted(img1, alpha, img2, beta, 0)
    cv2.imshow('Blended', img_dst)

def onMouse(event, x, y, flags, param):
    global alpha, beta
    if event == cv2.EVENT_LBUTTONDOWN:
        if alpha > 0.0:
            alpha = round(alpha - step, 1)
            beta = round(beta + step, 1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        if beta > 0.0:
            alpha = round(alpha + step, 1)
            beta = round(beta - step, 1)
    
    
    #alpha = min(max(alpha, 0.0), 1.0)
    #beta = min(max(beta, 0.0), 1.0)

    print(f" x={alpha:.1f}, : y={beta:.1f}")
    update_blend()


cv2.imshow('Image1', img1)
cv2.imshow('Image2', img2)
cv2.imshow('Blended', img_dst)

cv2.setMouseCallback('Blended', onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()
