# -*- coding: utf-8 -*-
import cv2

# �O���[�o���ϐ�
img_src = cv2.imread('image/t_insect.jpg')  # �����摜��ǂݍ���
img_disp = img_src.copy()             # �\���p�摜�i�s�x���Z�b�g�����j
drawing = False                       # �}�E�X���쒆���ǂ���
clk1 = (-1, -1)                       # �n�_
clk2 = (-1, -1)                       # �I�_
cnt = 0                               # �E�B���h�E�J�E���g�p

# �}�E�X�R�[���o�b�N�֐�
def draw_rectangle(event, x, y, flags, param):
    global clk1, clk2, drawing, img_disp, cnt

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        clk1 = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_disp = img_src.copy()
            cv2.rectangle(img_disp, clk1, (x, y), (0, 255, 0), 2)  # ���o�[�o���h

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        clk2 = (x, y)

        # ���W�̐���i�h���b�O�����Ɋւ�炸���と�E���j
        x1, y1 = min(clk1[0], clk2[0]), min(clk1[1], clk2[1])
        x2, y2 = max(clk1[0], clk2[0]), max(clk1[1], clk2[1])

        # ROI �؂�o���Ɗg��
        s_roi = img_src[y1:y2, x1:x2]
        if s_roi.size == 0:
            return  # ������ROI�i�͈�0�j�̏ꍇ�͖���

        s_roi_resize = cv2.resize(s_roi, None, fx=3.0, fy=3.0)

        # �V�����E�B���h�E�ɕ\��
        winname = 'dst' + str(cnt)
        cv2.namedWindow(winname)
        cv2.imshow(winname, s_roi_resize)
        cnt += 1

# �E�B���h�E�\���ƃ}�E�X�C�x���g�ݒ�
cv2.namedWindow('src')
cv2.setMouseCallback('src', draw_rectangle)

while True:
    cv2.imshow('src', img_disp)
    if cv2.waitKey(1) & 0xFF == 27:  # Esc�L�[�ŏI��
        break

cv2.destroyAllWindows()

