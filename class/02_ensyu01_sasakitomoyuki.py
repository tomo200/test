# -*- coding: utf-8 --*

import cv2
import numpy as np


cnt = 0

cv2.namedWindow('src')

while True:
    file_src = 'image/n' + str(cnt) + '.jpg'  # Å© èCê≥Ç±Ç±ÅI

    img_r = cv2.imread(file_src)

    if img_r is None:
        print('Image not found', file_src)
        break

    cv2.imshow('src', img_r)

    key = cv2.waitKey(0)

    if key == ord('q'):
        break
    elif key == ord('n'):
        cnt = (cnt + 1) % 10
    elif key == ord('p'):
        cnt = (cnt - 1) % 10


cv2.destroyAllWindows()