class Box():
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def __init__(self, length, width, height):
        self.lenght = length
        self.width = width
        self.height = height

    def voluem(self):
        return self.lenght * self.width * self.height

    def __voluem(self):  # 私有化函数 加__ 使方法私有化
        return self.lenght * self.width * self.height


class Box1(Box):  # 类的继承 Box1继承自Box
    def __init__(self, length1, width1, height1):
        super().__init__(length1, width1, height1)  # super实现父类与子类的关联
        self.color = 'white'  # 增加颜色属性
        self.type = 'fish'  # 增加类型属性

    def area(self):
        re = self.lenght * self.width + self.lenght * self.height + self.width * self.height
        return re * 2


class Ts():
    def __init__(self):
        self.lenght = 0
        self.width = 0
        self.height = 0


if __name__ == '__main__':
    box1 = Box1(10, 10, 10)
    box = Box(10, 10, 10)
    print(box1.area(), box.voluem())
    ts = Ts()
    # 修改下列属性值
    ts.lenght = input()
    ts.width = input()
    ts.height = input()
    print(ts.lenght, ts.width, ts.height)
    print('{0},{1},{2:.2f}'.format(1, 2, 1.0))
