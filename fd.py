import cv2
from pathlib import Path

fnCascade = Path(cv2.data.haarcascades) / 'haarcascade_frontalface_alt2.xml'

class FaceDetector():

    def __init__(self):

        # 顔検出器の初期化
        self.classifier = cv2.CascadeClassifier(str(fnCascade))

        if self.classifier.empty():
            raise RuntimeError(f'顔検出器を読み込めませんでした: {fnCascade}')


    def detect(self, image):

        # グレイスケール画像を用意する
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # グレイスケール画像から顔を検出
        result = self.classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(32, 32))

        # [ [ 1人目の顔の左上の位置（X座標）, 左上の位置（Y座標）, 幅, 高さ ],
        #   [ 2人目の顔の左上の位置（X座標）, 左上の位置（Y座標）, 幅, 高さ ],..., ]
        # というリストを作って return する．1人しか検出しなくても，戻り値は
        # [ [ 100, 50, 30, 30] ]  のようにリストのリストになることに注意
        rv = []
        for v in result:
            rv.append(list(v))

        return rv


if __name__ == '__main__':

    fd = FaceDetector()

