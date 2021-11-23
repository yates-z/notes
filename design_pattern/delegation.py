# -*-coding:utf-8-*-

"""
委托
优点：如果窗口需要变为圆形，只需简单的使用圆形对象替换矩形对象
缺点：动态、参数化导致难以理解
"""


class Rectangle:

    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Window:

    def __init__(self):
        self.rectangle = Rectangle()

    def area(self):
        return self.rectangle.area()
