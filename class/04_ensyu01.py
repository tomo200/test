import cv2
import math
import numpy as np

file_src = 'image/color.jpg'

img_src = cv2. imread(file_src, cv2. IMREAD_COLOR)
cv2. namedWindow ('src')

cv2. imshow ('src',img_src)

cv2. waitKey (0)



cv2. destroyAllWindow ()