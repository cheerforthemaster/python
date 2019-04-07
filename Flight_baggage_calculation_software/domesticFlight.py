from flightType import flightType


class domesticFlight(flightType):
    price = 0  # 经济舱普通票价
    weightMax = 50  # 最大上限
    spaceFlight = [0, 40, 30, 20, 20]
    passengerFlight = [0, 0, 0, 0, 10, 20, 10, 0]

    def __init__(self, weight, A, B, C, number, space, passenger, price):
        flightType.__init__(self, weight, A, B, C, number, space, passenger)
        self.price = price

    def calculate(self):
        sum = 0
        if True in list(map(lambda x: x > self.weightMax, self.weight)):  # 单件行李的重量是否超出最大的上限
            return None
        if True in list(map(lambda x: x > 100, self.A)) + list(map(lambda x: x > 60, self.B)) + list(
                map(lambda x: x > 40, self.C)):  # 行李尺寸
            return None
        if self.passenger == 4:  # 婴儿游客
            if True in list(map(lambda x: x <= self.passengerFlight[self.passenger], self.weight)):
                return sum
            else:
                for i in self.weight:
                    if i > self.passengerFlight[self.passenger]:
                        sum += (i - self.passengerFlight[self.passenger]) * 0.015 * self.price
                return sum
        if not (False in list(map(lambda x: x <= self.spaceFlight[self.space], self.weight))):  # 所有行李都没超重
            return sum
        else:
            exceeding = 0
            for i in self.weight:  # 部分行李超重
                if i > self.spaceFlight[self.space]:
                    exceeding += i - self.spaceFlight[self.space]
            if exceeding <= self.passengerFlight[self.passenger]:  # 超重部分小于会员部分
                return 0
            else:
                sum += (exceeding - self.passengerFlight[self.passenger]) * 0.015 * self.price
                if sum < 0:
                    return None
                return round(sum, 2)
