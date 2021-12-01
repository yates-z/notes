# -*-coding:utf-8-*-
"""
观察者模式
类型：对象行为型模型
意图： 定义对象间一对多的依赖关系，当一个对象的状态发生改变时，所有依赖它的对象都会得到通知并更新
优点：目标与观察者耦合度最小、广播
缺点：产生意外的更新
"""


# 示例：
class Observer:
    def update(self):
        pass


class ObserverA(Observer):
    def update(self):
        pass


class ObserverB(Observer):
    def update(self):
        pass


class Subjects:
    # 存储多个观察者
    observers = []

    def notify(self):
        for observer in self.observers:
            observer.update()
