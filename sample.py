import cv2
import numpy as np

# blackuni3.png というファイル名の画像を読み込んで，変数 cat0 にその画素値を格納
cat0 = cv2.imread('blackuni3.png')

# cat0 の一部を切り取ったものを cat1 とする
cat1 = cat0[15:55, 80:120, :]

# cat1 の上下を反転したものを cat0 の元の範囲に代入する
cat0[15:55, 80:120, :] = cv2.flip(cat1, 0)

# cv2.imshow は画像を画面に表示する関数
cv2.imshow('hoge', cat0)

# 何かキー入力されるまで待つ
cv2.waitKey()

# ウィンドウを閉じる
cv2.destroyAllWindows()