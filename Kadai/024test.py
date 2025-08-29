# -*- coding: utf-8 -*-
import cv2

# グローバル変数
img_src = cv2.imread('image/t_insect.jpg')  # 昆虫画像を読み込む
img_disp = img_src.copy()             # 表示用画像（都度リセットされる）
drawing = False                       # マウス操作中かどうか
clk1 = (-1, -1)                       # 始点
clk2 = (-1, -1)                       # 終点
cnt = 0                               # ウィンドウカウント用

# マウスコールバック関数
def draw_rectangle(event, x, y, flags, param):
    global clk1, clk2, drawing, img_disp, cnt

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        clk1 = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_disp = img_src.copy()
            cv2.rectangle(img_disp, clk1, (x, y), (0, 255, 0), 2)  # ラバーバンド

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        clk2 = (x, y)

        # 座標の整列（ドラッグ方向に関わらず左上→右下）
        x1, y1 = min(clk1[0], clk2[0]), min(clk1[1], clk2[1])
        x2, y2 = max(clk1[0], clk2[0]), max(clk1[1], clk2[1])

        # ROI 切り出しと拡大
        s_roi = img_src[y1:y2, x1:x2]
        if s_roi.size == 0:
            return  # 無効なROI（範囲0）の場合は無視

        s_roi_resize = cv2.resize(s_roi, None, fx=3.0, fy=3.0)

        # 新しいウィンドウに表示
        winname = 'dst' + str(cnt)
        cv2.namedWindow(winname)
        cv2.imshow(winname, s_roi_resize)
        cnt += 1

# ウィンドウ表示とマウスイベント設定
cv2.namedWindow('src')
cv2.setMouseCallback('src', draw_rectangle)

while True:
    cv2.imshow('src', img_disp)
    if cv2.waitKey(1) & 0xFF == 27:  # Escキーで終了
        break

cv2.destroyAllWindows()

