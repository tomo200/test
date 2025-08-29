# -*- coding: utf-8 --*

import cv2
import numpy as np

animal_bmp=cv2.imread('animal/n0.bmp')
animal_jpeg=cv2.imread('animal/n1.jpeg')
animal_png=cv2.imread('animal/n2.png')

if animal_bmp is not None:
     cv2.namedWindow('BMP', cv2.WINDOW_AUTOSIZE)
     cv2.imshow('BMP', animal_bmp)
if animal_jpeg is not None:
     cv2.namedWindow('JPEG', cv2.WINDOW_AUTOSIZE)
     cv2.imshow('JPEG',animal_jpeg)
if animal_png is not None:
     cv2.namedWindow('JPEG', cv2.WINDOW_AUTOSIZE)
     cv2.imshow('PNG',animal_png)

cv2.waitKey(0)


cv2.destroyAllWindows()
