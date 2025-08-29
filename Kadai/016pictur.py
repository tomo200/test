import cv2
import numpy as np

img=np.zeros((480,640)).astype(np.uint8)

img_str=np.full((480,640,3),255,dtype=np.uint8)

cv2.line(img_str, (100,100), (100, 300), (0, 0, 0), 10)
cv2.line(img_str, (100,100), (400,100), (0, 0, 0), 10)
cv2.line(img_str, (400,300), (100, 300), (0, 0, 0), 10)
cv2.line(img_str, (400,100), (500,300), (0, 0, 0), 10)

cv2.imshow('src',img_str)
cv2.waitKey(0)
cv2.destroyAllWindows()