from flightType import flightType


class internationalFlight(flightType):
    region = 0  # 区域编号
    weightMax = 45
    privilege = False  # True 为计重制 False 为计件制
    spaceFlight = [[], [32, 32, 23, 23], [32, 32, 32, 32], [32, 32, 23, 23], [32, 23, 23, 23],
                   [32, 32, 23, 23]]  # 每个舱位的免费重量
    numberFlight = [[], [0, 3, 2, 2, 2], [0, 3, 2, 1, 1], [0, 3, 2, 2, 1], [0, 3, 3, 2, 1],
                    [0, 3, 2, 1, 1]]  # 每个舱位的免费行李数量
    premium = [[], [[], [1000, 2000, 1000, 3000], [1000, 2000, 1000, 3000], [1000, 2000, 1000, 1000, 3000],
                    [1000, 2000, 1000, 1000, 3000]],
               [[], [450, 1300, 1000, 3000], [450, 1300, 1000, 3000], [450, 1300, 1000, 3000],
                [450, 1300, 1000, 3000]],
               [[], [1000, 2000, 1000, 3000], [1000, 2000, 1000, 3000], [1000, 2000, 1000, 2000, 3000],
                [1000, 2000, 1000, 2000, 3000]],
               [[], [450, 1300, 1000, 3000], [450, 1300, 1000, 1000, 3000], [450, 1300, 1000, 1000, 3000],
                [450, 1300, 1000, 1000, 3000]],
               [[], [450, 1300, 1000, 3000], [450, 1300, 1000, 1000, 3000], [450, 1300, 1000, 1000, 3000],
                [450, 1300, 1000, 1000, 3000]]]
    passengerFlight = [0, 0, 0, 0, 10, 20, 10, 0]  # 特殊乘客额外重量

    def __init__(self, weight, A, B, C, number, space, passenger, region, privilege):
        flightType.__init__(self, weight, A, B, C, number, space, passenger)
        self.region = region
        self.privilege = privilege

    def calculate(self):
        sum = 0
        if True in list(map(lambda x: x > self.weightMax, self.weight)):  # 单件行李的重量是否超出最大的上限
            return None
        for i in range(self.number):
            if self.A[i] + self.B[i] + self.C[i] > 158:
                if self.A[i] + self.B[i] + self.C[i] > 300:
                    return None
                else:
                    sum += self.premium[self.region][self.space][2]  # 超尺寸
        if self.passenger == 4:  # 婴儿游客
            if True in list(map(lambda x: x <= self.passengerFlight[self.passenger], self.weight)):
                return sum
            else:
                return None
        if self.passenger == 7 or ((self.passenger == 5 or self.passenger == 6) and not self.privilege):  # 留学生
            self.numberFlight[self.region][self.space] = self.numberFlight[self.region][self.space] + 1
        if self.number <= self.numberFlight[self.region][self.space] and not (False in list(  # 数量、重量都没超出免费额度
                map(lambda x: x <= self.spaceFlight[self.region][self.space], self.weight))):
            return 0
        if self.number > self.numberFlight[self.region][self.space]:  # 数量超出
            sum += self.premium[self.region][self.space][0] + self.premium[self.region][self.space][1] * (
                    self.number - self.numberFlight[self.region][self.space] - 1)
        self.weight.sort(reverse=False)
        if False in list(map(lambda x: x <= self.spaceFlight[self.region][self.space], self.weight)):  # 重量超出
            for i in range(self.number):
                if self.weight[i] > self.spaceFlight[self.region][self.space]:
                    if self.privilege and self.weight[i]- self.spaceFlight[self.region][self.space] <= \
                            self.passengerFlight[self.passenger]:  # 会员计重制额度足够
                        self.passengerFlight[self.passenger] -= self.weight[i]
                        continue
                    if self.weight[i] < self.spaceFlight[self.region][1]:  # 一层超重
                        sum += self.premium[self.region][self.space][3]
                    else:
                        sum += self.premium[self.region][self.space][-1]  # 二层超重
        return sum
