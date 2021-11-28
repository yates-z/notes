# -*-coding:utf-8-*-

"""
享元模式
类型：对象结构型模型
意图： 运用共享技术有效地支持大量细粒度的对象
优点： 当一个程序使用了大量对象，造成了很大的内存开销，应该使用享元模式进行优化
缺点：
"""


class CharacterA:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = None

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setColor(self, color):
        self.color = color

    def paint(self):
        print("绘出字符 A， 位于屏幕({}, {}), 颜色为 {}".format(self.x, self.y, self.color))


class CharacterB:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = None

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setColor(self, color):
        self.color = color

    def paint(self):
        print("绘出字符 B， 位于屏幕({}, {}), 颜色为 {}".format(self.x, self.y, self.color))

"""
... ...
"""


class CharacterFactory:

    char_map = {}

    def get_char(self, name):
        char = self.char_map.get(name)
        if not char:
            print("没有查询到字符{}， 执行创建逻辑".format(name))
            char = eval("Character" + name.upper())()
            self.char_map[name] = char
        return char


if __name__ == "__main__":
    factory = CharacterFactory()
    string = "aaaabbbbb"
    for name in string:
        char = factory.get_char(name)
        char.setX(string.index(name))
        char.setY(1)
        char.setColor("black")
        char.paint()
