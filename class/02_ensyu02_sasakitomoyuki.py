# -*- coding: utf-8 --*

import cv2
import numpy as np


img = np.zeros((480, 640), dtype=np.uint8)

cnt = 0

cv2.namedWindow('src')

while True:
    file_src = 'images/n' + str(cnt) + '.png'  # Å© èCê≥Ç±Ç±ÅI

    img_r = cv2.imread(file_src)

    if img_r is None:
        print('Image not found', file_src)
        break

    cv2.imshow('src', img_r)

    key = cv2.waitKey(0)

    if key == ord('q'):
        break
    elif key == ord('n'):
        cnt = (cnt + 1) % 7
    elif key == ord('p'):
        cnt = (cnt - 1) % 7

    cv2.destroyAllWindows()