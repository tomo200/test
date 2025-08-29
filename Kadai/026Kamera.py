# -*- coding: utf-8 --* 
import cv2
import os

cascadeName = "haarcascade_frontalface_alt.xml" # 分類器ファイル名
cascade_path = os.path.join(cv2.data.haarcascades, cascadeName)
cascade = cv2.CascadeClassifier(cascade_path) # 分類器の読み込み

# VideoCapture オブジェクト
cap = cv2.VideoCapture(0) 

while True:
    # フレームの読み取り
    ret, frame = cap.read()

    # グレースケール変換
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 顔の学習データ精査
    front_face_list = cascade.detectMultiScale(img_gray,scaleFactor=1.1, minNeighbors=3, flags=0, minSize=(20, 20))
    #print('検出数', len(front_face_list))
    print(front_face_list)

    # 認識しない場合はコマンドラインに"Failed"と出力
    if len(front_face_list) ==0:
        print("Failed")
        cv2.waitKey(10)

    else:
        # 顔を四角で囲む
        for (x,y,w,h) in front_face_list:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),thickness=3)
            cv2.waitKey(10)

    # フレームを表示
    cv2.imshow("Frame", frame)

    # ESCキーが押されたら途中終了
    key = cv2.waitKey(10)
    if key == 27: #ESC
        break


cap.release()
cv2.destroyAllWindows()

