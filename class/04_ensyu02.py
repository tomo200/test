# -*- coding: utf-8 --*
import cv2

# ����t�@�C���̃p�X
filepath = "image/Megamind/Megamind.avi"

# ����̃L���v�`��
cap = cv2.VideoCapture(filepath)
        
# ����I���܂ŌJ��Ԃ�
while (cap.isOpened()):
    # �t���[�����擾
    ret, frame = cap.read()

    # �t���[����\��
    cv2.imshow("Frame", frame)

    # ESC�L�[�������ꂽ��r���I��
    key = cv2.waitKey(30)

    if key == 27: #ESC
        break

cap.release()
cv2.destroyAllWindows()