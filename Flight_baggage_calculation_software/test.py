import unittest
from domesticFlight import domesticFlight
from internationalFlight import internationalFlight


class Test(unittest.TestCase):
    def setUp(self):
        print("test start running")

    def tearDown(self):
        print("test is finished")

    # weight[], A[], B[], C[], number, space, passenger, price result
    parameter1 = [[[20, 30, 40], [30, 20, 40], [30, 20, 40], [30, 20, 40], 3, 1, 1, 200, 0],  # 免费
                  [[51, 30, 40], [30, 20, 40], [30, 20, 40], [30, 20, 40], 3, 1, 1, 200, None],  # 超出最大重量
                  [[30], [40], [200], [10], 1, 2, 1, 200, None],  # 超尺寸
                  [[10], [40], [20], [10], 1, 2, 4, 200, 0],  # 婴儿免费
                  [[15], [40], [20], [10], 1, 2, 4, 200, 15],  # 婴儿收费
                  [[45], [40], [20], [10], 1, 2, 1, 200, 45],  # 超重收费
                  [[45], [40], [20], [10], 1, 1, 6, 200, 0],  # 会员免费
                  [[50], [1], [2], [1], 1, 3, 3, -1000, None]]  # 负数
    def testOne(self):
        # domesticFlight
        for i in range(len(self.parameter1)):
            a = domesticFlight(self.parameter1[i][0], self.parameter1[i][1], self.parameter1[i][2],
                               self.parameter1[i][3],
                               self.parameter1[i][4], self.parameter1[i][5], self.parameter1[i][6],
                               self.parameter1[i][7])
            self.assertTrue(a.calculate() == self.parameter1[i][8])

    # weight[], A[], B[], C[], number, space, passenger, region, privilege result
    parameter2 = [[[20, 30, 30], [30, 20, 40], [30, 20, 40], [30, 20, 40], 3, 1, 5, 1, False, 0],  # 免费
                  [[50, 30, 30], [30, 20, 40], [30, 20, 40], [30, 20, 40], 3, 1, 1, 1, True, None],  # 超出最大重量
                  [[20, 30, 30], [100, 20, 40], [100, 20, 40], [110, 20, 40], 3, 1, 1, 1, True, None],  # 超出300
                  [[40, 30, 30], [50, 20, 40], [50, 20, 40], [100, 20, 40], 3, 1, 6, 1, True, 1000],# 超出158,会员,计重制,重量没有超出
                  [[2, 3, 9], [30, 20, 40], [30, 20, 40], [30, 20, 40], 3, 1, 4, 1, True, 0],  # 婴儿免费
                  [[20, 30, 30], [30, 20, 40], [30, 20, 40], [30, 20, 40], 3, 1, 4, 1, True, None],  # 婴儿超重
                  [[20, 30, 40, 20, 20], [30, 20, 40, 20, 20], [30, 20, 40, 20, 20], [30, 20, 40, 20, 20], 5, 3, 7, 1,
                   True, 7000]]  # 留学生,超出一件，重量超出一层和两层

    def testtwo(self):
        # internationalFlight
        for i in range(len(self.parameter2)):
            a = internationalFlight(self.parameter2[i][0], self.parameter2[i][1], self.parameter2[i][2],
                                    self.parameter2[i][3],
                                    self.parameter2[i][4], self.parameter2[i][5], self.parameter2[i][6],
                                    self.parameter2[i][7], self.parameter2[i][8])
            self.assertTrue(a.calculate() == self.parameter2[i][9])


if __name__ == '__main__':
    unittest.main
