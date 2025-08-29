# -*- coding: utf-8 --*
import cv2

# 動画ファイルのパス
filepath = "image/Megamind/Megamind.avi"

# 動画のキャプチャ
cap = cv2.VideoCapture(filepath)
        
# 動画終了まで繰り返し
while (cap.isOpened()):
    # フレームを取得
    ret, frame = cap.read()

    # フレームを表示
    cv2.imshow("Frame", frame)

    # ESCキーが押されたら途中終了
    key = cv2.waitKey(30)

    if key == 27: #ESC
        break

cap.release()
cv2.destroyAllWindows()