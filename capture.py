import cv2

# カメラの準備
cap = cv2.VideoCapture(0)

# 無限ループ
while(True):

    # カメラで撮った静止画像を frame に格納
    rv, frame = cap.read()

    # frame を表示
    cv2.imshow('hoge', frame)

    # キー入力を受け付け． q だったらループを抜ける
    if cv2.waitKey(1) == ord('q'):
        break
        
# 終了のための後始末
cap.release()
cv2.destroyAllWindows()
