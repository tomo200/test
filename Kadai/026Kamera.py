# -*- coding: utf-8 --* 
import cv2
import os

cascadeName = "haarcascade_frontalface_alt.xml" # ���ފ�t�@�C����
cascade_path = os.path.join(cv2.data.haarcascades, cascadeName)
cascade = cv2.CascadeClassifier(cascade_path) # ���ފ�̓ǂݍ���

# VideoCapture �I�u�W�F�N�g
cap = cv2.VideoCapture(0) 

while True:
    # �t���[���̓ǂݎ��
    ret, frame = cap.read()

    # �O���[�X�P�[���ϊ�
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ��̊w�K�f�[�^����
    front_face_list = cascade.detectMultiScale(img_gray,scaleFactor=1.1, minNeighbors=3, flags=0, minSize=(20, 20))
    #print('���o��', len(front_face_list))
    print(front_face_list)

    # �F�����Ȃ��ꍇ�̓R�}���h���C����"Failed"�Əo��
    if len(front_face_list) ==0:
        print("Failed")
        cv2.waitKey(10)

    else:
        # ����l�p�ň͂�
        for (x,y,w,h) in front_face_list:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),thickness=3)
            cv2.waitKey(10)

    # �t���[����\��
    cv2.imshow("Frame", frame)

    # ESC�L�[�������ꂽ��r���I��
    key = cv2.waitKey(10)
    if key == 27: #ESC
        break


cap.release()
cv2.destroyAllWindows()

