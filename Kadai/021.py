# -*- coding: utf-8 --*
import cv2
import numpy as np

file_src = 'image/clock.jpg'

img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)

img_dst=img_src.copy()

cv2.namedWindow('img_src')
cv2.namedWindow('img_dst')

#img_dst = cv2.resize(img_src, None, fx=2, fy=0.5)
#img_dst = cv2.flip(img_src, 0)

#img_dst = cv2.rotate(img_src, cv2.ROTATE_90_CLOCKWISE)


# height, width = img_src.shape[:2]
# mat = np.array([[1, 0.3, 0], [0, 1, 0]], dtype=np.float32)
#  # アフィン変換
# img_dst = cv2.warpAffine(img_src, mat, (int(width + height*0.3), height))



angle = 10.0


while True:
    
    
    #回転
    height, width = img_src.shape[:2]
    center = (int(width/2), int(height/2))
    
    scale = 1.0

    trans = cv2.getRotationMatrix2D(center, angle, scale)
    #アフィン変換
    img_dst = cv2.warpAffine(img_src, trans, (width,height))

    angle-=10.0

    cv2.imshow('img_src',img_src)
    cv2.imshow('img_dst',img_dst)

    key = cv2.waitKey(100) 
    if key == 27  or  key == ord('q'):  #27=ESC 
        break 
    


cv2.destroyAllWindows











