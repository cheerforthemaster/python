import cv2
import dlib
import numpy as np

from .data_pretreatment import *

detector = None
predictor = None


def gFP_init():
    global detector
    global predictor

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('m_flask/shape_predictor_68_face_landmarks.dat')


def getFeaturePoints(file):
    # cv2读取图像
    img = cv2.imread(file)
    img = cv2.resize(img, (300, 300), interpolation=cv2.INTER_CUBIC)

    # 人脸数rects
    rects = detector(img, 1)
    if len(rects) != 1:
        # print(file)
        return None, None, None, None, None, None

    width = rects[0].right() - rects[0].left()
    height = rects[0].bottom() - rects[0].top()
    landmarks = np.matrix([[p.x, p.y] for p in predictor(img, rects[0]).parts()])
    X = []
    Y = []
    Xo = landmarks[0][0, 0]
    Yo = landmarks[0][0, 1]
    originalX = []
    originalY = []
    for idx, point in enumerate(landmarks):
        # 68点的坐标
        x = point[0, 0]
        y = point[0, 1]
        originalX.append(x)
        originalY.append(y)
        pos = (x + 3, y + 3)
        # 利用cv2.circle给每个特征点画一个圈，共68个
        cv2.circle(img, pos, 2, color=(43, 43, 43))
        # 利用cv2.putText输出1-68
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img, str(idx + 1), pos, font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

        x = (int)((x - Xo) * 300 / width)
        y = (int)((y - Yo) * 300 / height)
        X.append(x)
        Y.append(y)
    cv2.imwrite("m_flask/views/3.jpg", img)
    return width, height, X, Y, originalX, originalY
