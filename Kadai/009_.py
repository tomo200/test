# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 画像ファイルをカラーで読み込む
file_src = 'image/fruits.jpg'
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)

# 2つのウィンドウを作成（オリジナルと加工画像）
cv2.namedWindow('src')
cv2.namedWindow('dst')

# 画像サイズを取得
height, width, channels = img_src.shape[:3]

# 編集用画像の初期化
img_dst = img_src.copy()
img_hsv = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)

# ピクセルを変更する関数
# 引数:
#   img: HSV画像
#   channel: 0=H, 1=S, 2=V
#   incre: 増減値（±5など）
def modifyPixel(img, channel, incre):
    global height, width
    for yy in range(height):
        for xx in range(width):
            value = int(img[yy, xx][channel]) + incre

            # H（色相）は0?179でループさせる
            if channel == 0:
                img[yy, xx][channel] = (value + 180) % 180
            else:
                # S/Vは0?255に制限
                img[yy, xx][channel] = np.clip(value, 0, 255)

# マウスイベントの処理
def onMouse(event, x, y, flags, param):
    global img_src, img_dst, img_hsv

    # 左クリック: +5
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left click at:", x, y)

        # H（色相）を+5する処理
        modifyPixel(img_hsv, 0, 5)

        # S（彩度）を+5する処理（コメントアウト）
        # modifyPixel(img_hsv, 1, 5)

        # V（明度）を+5する処理（コメントアウト）
        # modifyPixel(img_hsv, 2, 5)

        img_dst = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('dst', img_dst)

    # 右クリック: -5
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("Right click at:", x, y)

        # H（色相）を-5する処理
        modifyPixel(img_hsv, 0, -5)

        # S（彩度）を-5する処理（コメントアウト）
        # modifyPixel(img_hsv, 1, -5)

        # V（明度）を-5する処理（コメントアウト）
        # modifyPixel(img_hsv, 2, -5)

        img_dst = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('dst', img_dst)

# 画像をウィンドウに表示
cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)

# マウスコールバックを設定
cv2.setMouseCallback('dst', onMouse)

# キー入力を待って終了
cv2.waitKey(0)
cv2.destroyAllWindows()