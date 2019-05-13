# import numpy
# import cv2
#
# sift = None
#
#
# def s_init():
#     global sift
#     sift = cv2.xfeatures2d.SIFT_create()
#
#
# def getSift(f):
#     img = cv2.imread(f)
#     img = cv2.resize(img, (300, 300), interpolation=cv2.INTER_CUBIC)
#     kp, des = sift.detectAndCompute(img, None)
#
#     # cv2.imshow('gray', gray)
#     # cv2.waitKey(0)
#
#     img = cv2.drawKeypoints(img, kp, img, color=(255, 0, 255))
#     cv2.imwrite("m_flask/views/2.jpg", img)
#
#
# # if __name__ == '__main__':
# #     s_init()
# #     getSift("views/1.jpg")
