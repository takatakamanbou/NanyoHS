import cv2
import fd

# カメラの準備
cap = cv2.VideoCapture(0)

# 顔検出器の準備
detector = fd.FaceDetector()

# 無限ループ
while(True):

    # カメラで撮った静止画像を frame に格納
    rv, frame = cap.read()

    # 顔を検出
    posList = detector.detect(frame)
    for i, pos in enumerate(posList):
        # px: 顔領域の左上のX座標， py: Y座標， w: 幅， h: 高さ
        px, py, w, h = pos
        print(f'{i+1}人目: (顔領域の左上のX座標, Y座標, 幅, 高さ) =  ({px}, {py}, {w}, {h})')

    # frame を表示
    cv2.imshow('hoge', frame)

    # キー入力を受け付け． q だったらループを抜ける
    if cv2.waitKey(1) == ord('q'):
        break
        
# 終了のための後始末
cap.release()
cv2.destroyAllWindows()
