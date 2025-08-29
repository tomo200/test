# -*- coding: utf-8 --* 
import cv2

# グローバル変数の初期化
click_count = 0
x1 = y1 = x2 = y2 = 0
color = [0, 255, 0]  # 緑（BGR形式）

# 元画像と作業用画像を用意
original_img = cv2.imread('image/fruits.jpg', cv2.IMREAD_COLOR)

img = original_img.copy()

# 塗りつぶし関数
def fill_area(img, x1, x2, y1, y2, color):
    start_x = min(x1, x2)
    end_x = max(x1, x2)
    start_y = min(y1, y2)
    end_y = max(y1, y2)

    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            img[y, x] = color

# マウスクリックのコールバック関数
def mouse_event(event, x, y, flags, param):
    global click_count, x1, y1, x2, y2, img

    # 左クリックされたとき
    if event == cv2.EVENT_LBUTTONDOWN:
        if click_count % 2 == 0:
            # 1回目のクリック → 開始点
            x1, y1 = x, y
            print(f": ({x1}, {y1})")
        else:
            # 2回目のクリック → 終了点 + 塗りつぶし実行
            x2, y2 = x, y
            print(f"end: ({x2}, {y2})")
            fill_area(img, x1, x2, y1, y2, color)
            cv2.imshow('Image', img)
        click_count += 1

    # 右クリックされたとき → 画像をリセット
    elif event == cv2.EVENT_RBUTTONDOWN:
        img = original_img.copy()
        click_count = 0
       
        cv2.imshow('Image', img)

# ウィンドウとマウスイベントの設定
cv2.imshow('Image', img)
cv2.setMouseCallback('Image', mouse_event)

# キーが押されるまで待つ
cv2.waitKey(0)
cv2.destroyAllWindows()