# -*- coding: utf-8 -*-
import cv2

# 元画像ファイルのパスを設定し、カラー画像として読み込む
file_src = 'image/fruits.jpg'
img_src = cv2.imread(file_src, cv2.IMREAD_COLOR)

# 表示ウィンドウを2つ作成
cv2.namedWindow('src')
cv2.namedWindow('dst')

# 画像サイズとチャネル数の取得
height, width, channels = img_src.shape[:3]

# 元画像をコピーして出力用画像を作成
img_dst = img_src.copy()

# BGR画像をHSV画像に変換（色相・彩度・明度に分解）
img_hsv = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)

# 関数：ピクセルの数値を変える 
# 引数： 
#    img：画像データ 
#    yy：ピクセル縦方向位置    
#    xx：ピクセル横方向位置 
#    n：ピクセル値配列の添字（０～２） 
#    incre：増分値 

def modifyPixel(img, yy, xx, n, incre): 
    global height, width 
    for yy in range(0, height): 
        for xx in range(0, width): 
                
            value = int(img[yy,xx][n]) + incre 
            if value >= 0 and value <= 255: 
                img[yy,xx][n] = value 



# マウスイベント用の関数（クリックで処理を分岐）
def onMouse(event, x, y, flags, params):
    global img_src, img_dst, img_hsv

    modifyPixel(img_dst,y,x,)

    # 左クリックが押されたときの処理
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)




        # クリックされた画素のHSVの色相を変更
        h, s, v = img_hsv[y, x]
        h = (h + 60) % 180  # HSV色空間で色相を変える（180が最大）
        img_hsv[y, x] = (h, s, v)

        #画像変換して表示する
        img_dst = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('dst', img_dst)

    # 右クリックが押されたときの処理
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x, y)
        # HSV画像全体の色相を変更
        img_hsv[:, :, 0] = (img_hsv[:, :, 0] + 30) % 180

        # HSV画像をBGR画像に変換して表示する
        img_dst = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('dst', img_dst)

# 画像を表示（元画像と変換結果）
cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)

# マウスイベント関数を設定（dstウィンドウ上でクリック処理を行う）
cv2.setMouseCallback('dst', onMouse)

# キーが押されるまで待機
cv2.waitKey(0)

# すべてのウィンドウを閉じる
cv2.destroyAllWindows()