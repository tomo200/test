# -*- coding: utf-8 --*
import cv2
import numpy as np

file_bkg = 'image/road_haikei.png'
file_src= 'image/road_taisyo.png'



img_src = cv2.imread(file_src, cv2.IMREAD_GRAYSCALE)
img_dst = img_src.copy()
img_bkg = cv2.imread(file_bkg, cv2.IMREAD_GRAYSCALE)
img_bkg = cv2.resize(img_bkg, (img_src.shape[1], img_src.shape[0]))
cv2.namedWindow('src')
cv2.namedWindow('bkg')
cv2.namedWindow('dst')
#·•ª
img_div=cv2.absdiff(img_src, img_bkg)

#“ñ’l‰æ‘œ¶¬
thresh=60
img_div2=cv2.threshold(img_div,thresh,255,cv2.THRESH_BINARY)[1]

#–c’£ûk
# op=np.ones((1,1)).astype(np.uint8)
# img_md=cv2.erode(img_div2,op,iterations=4)
# img_md2=cv2.dilate(img_md,op,iterations=4)

op = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], np.uint8)
img_md=cv2.dilate(img_div2,op,iterations=4)
img_md2=cv2.erode(img_md,op,iterations=4)


#˜_—Ï
img_result=cv2.bitwise_and(img_dst,img_md2)


cv2.imshow('src', img_src)
cv2.imshow('bkg', img_bkg)
cv2.imshow('dst', img_result)


cv2.waitKey(0)
cv2.destroyAllWindows()
