# -*-coding:utf-8-*-
"""
原型模式
类型：对象创建型
意图：原型实例指定创建对象的种类，并通过拷贝这些原型创建新的对象
优点：
缺点：
"""


# 动态语言的基类如何预知未来的扩展类，并实现对它的操作
class BaseClass:

    def __init__(self):
        # 设计字典，用来存储子类实例
        self.children = {}

    # 设计一个注册类，将子类注册进来，动态语言类也是对象，可以直接存放类
    def register(self, class_name, child_class):
        self.children[class_name] = child_class

    def clone(self, class_name):
        return self.children[class_name]()

    # 如果子类比较复杂，需要在运行时复制经过处理的对象
    def register2(self, class_name, child):
        # child就是原型
        self.children[class_name] = child

    # 在子类中实现clone逻辑
    def clone2(self, class_name):
        return self.children[class_name].clone()


# 静态语言例如C++，类不是对象，不能被传递，只能注册实例对象
# 到父类实现克隆

