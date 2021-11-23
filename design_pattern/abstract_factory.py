# -*-coding:utf-8-*-

"""
抽象工厂模式
类型：对象创建型
意图：提供一个创建一系列相关或互相依赖对象的接口，无需指定具体的类
优点：分离了具体的类、产品易于交换
缺点：难以增加新的产品,增加新产品需要修改工厂类和抽象工厂类
"""

import abc

"""
示例：换肤系统
"""


class Window(metaclass=abc.ABCMeta):
    """一号产品： 窗口"""

    def __init__(self):
        self.createEvent()
        self.paintEvent()

    @abc.abstractmethod
    def createEvent(self):
        pass

    @abc.abstractmethod
    def paintEvent(self):
        pass


class NormalWindow(Window):
    """正常风格"""

    def createEvent(self):
        print("创建正常窗口")

    def paintEvent(self):
        print("绘制正常窗口")


class DarkStyleWindow(Window):
    """暗黑风格"""

    def createEvent(self):
        print("创建黑暗风格窗口")

    def paintEvent(self):
        print("绘制黑暗风格窗口")


class ScrollBar:
    """二号产品：滚动条"""
    def __init__(self):
        self.createEvent()
        self.scrollEvent()

    @abc.abstractmethod
    def createEvent(self):
        pass

    @abc.abstractmethod
    def scrollEvent(self):
        pass


class NormalScrollBar(ScrollBar):
    """正常风格"""

    def createEvent(self):
        print("创建正常风格滚动条")

    def scrollEvent(self):
        print("正常风格滚动条滚动事件")


class DarkStyleScrollBar(ScrollBar):
    """暗黑风格"""
    def createEvent(self):
        print("创建黑暗风格滚动条")

    def scrollEvent(self):
        print("黑暗风格滚动条滚动事件")


class WidgetFactory:
    """client通过这个类的接口创建窗口组件"""
    def produce(self):
        pass

    def createWindow(self):
        pass

    def createScrollBar(self):
        pass


"""
静态语言需要指明变量类型，所以工厂类都需要继承自抽象工厂
在python中可以不用继承抽象工厂类，也可以利用抽象工厂类实现factory_producer的
功能，这样的好处是可以动态扩展工厂种类而不用修改factory_producer的逻辑
"""


class NormalFactory(WidgetFactory):
    """正常模式的工厂"""
    def produce(self):
        self.createWindow()
        self.createScrollBar()

    def createWindow(self):
        return NormalWindow()

    def createScrollBar(self):
        return NormalScrollBar()


class DarkStyleFactory(WidgetFactory):
    """黑暗模式的工厂"""
    def produce(self):
        self.createWindow()
        self.createScrollBar()

    def createWindow(self):
        return DarkStyleWindow()

    def createScrollBar(self):
        return DarkStyleScrollBar()


def factory_producer(choice):
    if choice == "normal":
        return NormalFactory()
    elif choice == 'dark':
        return DarkStyleFactory()
    else:
        return None


if __name__ == "__main__":
    # 可以很方便切换normal和dark
    factory = factory_producer("normal")
    factory.produce()
