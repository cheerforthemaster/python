class flightType:
    # weight(重量) A（高） B（宽） C（长） number(件数) space(舱位) passenger(旅客类型)
    weight = []
    A = []
    B = []
    C = []
    number = 0
    space = 0  # 1：头等舱、2：公务舱、3：明珠经济舱、4：经济舱
    passenger = 0  # 1：成年人、2：儿童、3：占座婴儿、4：不占座婴儿、5：南航明珠金卡会员/天合联盟超级精英、6：南航明珠银卡会员/天合联盟精英、7：留学生/劳务/海员

    def __init__(self, weight, A, B, C, number, space, passenger):
        self.weight = weight
        self.A = A
        self.B = B
        self.C = C
        self.number = number
        self.space = space
        self.passenger = passenger
        if len(A) != number or len(B) != number or len(C) != number or len(weight) != number:
            return None
