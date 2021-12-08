# -*-coding:utf-8-*-

"""
访问者模式
类型：对象行为型模型
意图： 主要将数据结构与数据操作分离。
优点： 1、符合单一职责原则。 2、优秀的扩展性。 3、灵活性。
缺点： 1、具体元素对访问者公布细节，违反了迪米特原则。
        2、具体元素变更比较困难。
        3、违反了依赖倒置原则，依赖了具体类，没有依赖抽象。
"""


# 主要解决稳定的数据结构和易变的操作耦合问题
class ComputerPart:

    # 违反了迪米特原则
    def accept(self, visitor):
        pass


class Keyboard(ComputerPart):
    name = "Keyboard"

    def accept(self, visitor):
        visitor.visit(self)


class Monitor(ComputerPart):
    name = "Monitor"

    def accept(self, visitor):
        visitor.visit(self)


class Mouse(ComputerPart):
    name = "Mouse"

    def accept(self, visitor):
        visitor.visit(self)


class Computer(ComputerPart):
    name = "Computer"

    def __init__(self):
        # 违反了依赖倒置原则
        self.parts = [Mouse(), Keyboard(), Monitor()]

    def accept(self, visitor):
        for part in self.parts:
            part.accept(visitor)
        visitor.visit(self)


class ComputerPartDisplayVisitor:
    """观察者"""

    def visit(self, part):
        print("Displaying {}".format(part.name))


if __name__ == "__main__":
    computer = Computer()
    computer.accept(ComputerPartDisplayVisitor())
