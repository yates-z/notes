# -*-coding:utf-8-*-
"""
策略模式
类型： 对象行为模式
意图： 定义一系列的算法,把它们一个个封装起来, 并且使它们可相互替换。
优点： 算法可以自由切换、扩展性良好
缺点： 策略类会增多
"""


# 解决if-else过多的问题
# 假设小明要从A城市到B城市
class Strategy:
    def move(self):
        pass


class CarStrategy(Strategy):
    def move(self):
        print("乘坐了汽车。")


class PlaneStrategy(Strategy):
    def move(self):
        print("乘坐了飞机。")


class TrainStrategy(Strategy):
    def move(self):
        print("乘坐了火车。")


class Person:

    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self):
        self.strategy.move()


# 一般写法
def move(strategy):
    if strategy == "car":
        print("乘坐了汽车")
    elif strategy == "plane":
        print("乘坐了飞机")
    elif strategy == "train":
        print("乘坐了火车")


"""
一般写法需要向函数传递一个类型参数，具体的分支判断与执行逻辑都在
函数中，不易扩展。
策略模式只需要向Person中传递一个Strategy对象，而Strategy对象是可以
自己创建的，方便扩展。
"""
if __name__ == "__main__":
    xiaoming = Person(CarStrategy())
    xiaoming.execute()

    xiaoming = Person(PlaneStrategy())
    xiaoming.execute()

    xiaoming = Person(TrainStrategy())
    xiaoming.execute()
