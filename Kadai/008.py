# -*- coding: utf-8 --* 
import cv2

# �O���[�o���ϐ��̏�����
click_count = 0
x1 = y1 = x2 = y2 = 0
color = [0, 255, 0]  # �΁iBGR�`���j

# ���摜�ƍ�Ɨp�摜��p��
original_img = cv2.imread('image/fruits.jpg', cv2.IMREAD_COLOR)

img = original_img.copy()

# �h��Ԃ��֐�
def fill_area(img, x1, x2, y1, y2, color):
    start_x = min(x1, x2)
    end_x = max(x1, x2)
    start_y = min(y1, y2)
    end_y = max(y1, y2)

    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            img[y, x] = color

# �}�E�X�N���b�N�̃R�[���o�b�N�֐�
def mouse_event(event, x, y, flags, param):
    global click_count, x1, y1, x2, y2, img

    # ���N���b�N���ꂽ�Ƃ�
    if event == cv2.EVENT_LBUTTONDOWN:
        if click_count % 2 == 0:
            # 1��ڂ̃N���b�N �� �J�n�_
            x1, y1 = x, y
            print(f": ({x1}, {y1})")
        else:
            # 2��ڂ̃N���b�N �� �I���_ + �h��Ԃ����s
            x2, y2 = x, y
            print(f"end: ({x2}, {y2})")
            fill_area(img, x1, x2, y1, y2, color)
            cv2.imshow('Image', img)
        click_count += 1

    # �E�N���b�N���ꂽ�Ƃ� �� �摜�����Z�b�g
    elif event == cv2.EVENT_RBUTTONDOWN:
        img = original_img.copy()
        click_count = 0
       
        cv2.imshow('Image', img)

# �E�B���h�E�ƃ}�E�X�C�x���g�̐ݒ�
cv2.imshow('Image', img)
cv2.setMouseCallback('Image', mouse_event)

# �L�[���������܂ő҂�
cv2.waitKey(0)
cv2.destroyAllWindows()