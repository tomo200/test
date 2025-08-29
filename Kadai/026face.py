# -*- coding: utf-8 --* 
import cv2
import os
import numpy as np

file_src = "image/soccer.png"
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)
img_dst = img_src.copy()
cv2.namedWindow('src')

cascadeName = "haarcascade_frontalface_alt.xml" # ���ފ�t�@�C����
cascade_path = os.path.join(cv2.data.haarcascades, cascadeName)
cascade = cv2.CascadeClassifier(cascade_path) # ���ފ�̓ǂݍ���


img_gray = cv2.cvtColor(img_dst, cv2.COLOR_BGR2GRAY)

# ���͉摜�̕\��
#cv2.imshow('src', img_src)

# �X�P�[��
scale = 1.2

# �������ԒZ�k�̂��߂ɉ摜���k���A�q�X�g�O�������ψꉻ
img_small = cv2.resize(img_gray, (int(img_src.shape[1] / scale), int(img_src.shape[0] / scale)))
img_small = cv2.equalizeHist(img_small)

# �}���`�X�P�[���i��j�T��
# ���͉摜�C�k���X�P�[���C�Œ��`���C�i�t���O�j�C�ŏ���`
searches = cascade.detectMultiScale(img_small, scaleFactor=1.1, minNeighbors=1, flags=0, minSize=(30,30))
print('KNWSYUTU',len(searches))


# ���ʂ̕`��
for (x, y, w, h) in searches:
    center = (int((x + w//2) * scale), int((y + h//2) * scale))
    radius = int(((w + h) // 4) * scale)
    cv2.circle(img_dst, center, radius, (0, 0, 255), 3, cv2.LINE_8, 0)


cv2.imshow('src', img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

