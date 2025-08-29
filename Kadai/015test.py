# -*- coding: utf-8 --*
import cv2
import numpy as np

file_src = 'image/lena.jpg'

img_src = cv2.imread(file_src, cv2.IMREAD_GRAYSCALE)
img_dst = img_src.copy()
cv2.namedWindow('src')
cv2.namedWindow('dst')

thresh = 180
ret, img_dst = cv2.threshold(img_src, thresh, 255, cv2.THRESH_BINARY)

element4 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)


def onMouse(event, x, y, flags, params):
    global img_dst
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        img_dst = cv2.dilate(img_dst, element4, iterations = 1)  #dailate ”’‚ğ‘å‚«‚­•‚ğ¬‚³‚­
        cv2.imshow('dst', img_dst)
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x, y)
        img_dst = cv2.erode(img_dst, element4, iterations = 1) #erode •‚ğ‘å‚«‚­”’¬‚³‚­
        cv2.imshow('dst', img_dst)


cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)

cv2.setMouseCallback('dst', onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()



