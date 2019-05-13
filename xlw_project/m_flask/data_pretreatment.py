import pickle
from .getFeaturePoints import *

clf = None


def dp_init():
    global clf
    f = open('m_flask/dataReslut.dat', 'rb')
    clf = pickle.loads(f.read())  # 使用loads反序列化
    f.close()


def getDataPretreatment(f):
    width, height, X, Y, originalX, originalY = getFeaturePoints(f)
    if X == None or Y == None:
        return "图片不符合要求"

    testX = []
    temX = []
    for i in range(len(X)):
        # if (X[j] + 50) + (Y[j] + 50) * 300 < 0:
        #     print(X[j], Y[j])
        temX.append((X[i] + (Y[i] + 200) * 300) / 1000)
    testX.append(temX)
    testX = np.array(testX)
    result = clf.predict(testX)
    result = result.tolist()
    match = 0
    data = "error"
    if result[0] == 0:
        data = "中性"
    elif result[0] == 1:
        data = "高兴"
    elif result[0] == 2:
        data = "沮丧"
    elif result[0] == 3:
        data = "惊讶"
    elif result[0] == 4:
        data = "恐惧"
    elif result[0] == 5:
        data = "厌恶"
    elif result[0] == 6:
        data = "愤怒"
    elif result[0] == 7:
        data = "蔑视"
    return data


# 0 对应中性表情  5500张
# 1 对应高兴表情   5500张
# 2 对应沮丧表情   5500张
# 3 对应惊喜表情  5500张
# 4 对应恐惧表情  4000张
# 5 对应厌恶表情  4000张
# 6 对应愤怒表情  5500张
# 7 对应蔑视表情  4000张
