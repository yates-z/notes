"""
备忘录模式
类型：对象行为型模式
意图： 在不破坏封装性的前提下，捕获一个对象的内部状态，以便以后恢复到原先保存的状态
优点： 给用户提供了一种可以恢复状态的机制，可以使用户能够比较方便地回到某个历史的状态。
缺点： 消耗资源。如果类的成员变量过多，势必会占用比较大的资源，而且每一次保存都会消耗一定的内存。
"""

# 回滚、后退操作


# Memento 包含了要被恢复的对象的状态
class Memento:
    """要保存的对象"""

    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state


class Originator:
    """发起者"""

    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def saveStateToMemento(self):
        return Memento(self.state)

    def getStateFromMemento(self, memento):
        self.state = memento.get_state()


class CareTaker:

    def __init__(self):
        self.memento_list = []

    def add(self, state):
        self.memento_list.append(state)

    def get(self, index):
        return self.memento_list[index]


if __name__ == "__main__":
    originator = Originator()
    careTaker = CareTaker()
    originator.set_state("State #1")
    originator.set_state("State #2")
    careTaker.add(originator.saveStateToMemento())
    originator.set_state("State #3")
    careTaker.add(originator.saveStateToMemento())
    originator.set_state("State #4")
    print("Current State: " + originator.get_state())
    originator.getStateFromMemento(careTaker.get(0))
    print("First saved State: " + originator.get_state())
    originator.getStateFromMemento(careTaker.get(1))
    print("Second saved State: " + originator.get_state())
