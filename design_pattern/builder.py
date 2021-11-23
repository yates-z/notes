# -*-coding:utf-8-*-

"""
生成器模式
类型：对象创建型
意图：将复杂对象的构建与表示分离，使得不同的构建可以有不同的表示(将变与不变分离)
优点：对产品的构造过程进行更精细的控制
缺点：链式调用用一个类实例化另一个类，性能损耗
"""
import abc

# 示例：订购电脑
# 设计一个根据输入的参数（cpu、内存等）返回电脑的程序


# product
class Computer:

    def __init__(self, cpu, ram, disk):
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
        self.usb_count = 0
        self.display = ""
        self.keyboard = ""

    def setUSBCount(self, usb_count):
        self.usb_count = usb_count

    def setDisplay(self, display):
        self.display = display

    def __str__(self):
        return "处理器 %d 核， 内存 %d G，磁盘 %d G，usb接口数量 %d， 显示器品牌：%s" % (self.cpu, self.ram, self.disk, self.usb_count, self.display)


# director
class ComputerDirector:

    def orderComputer(self, builder):
        builder.setUsbCount()
        builder.setDisplay()


# builder python中可以不用写这个类
class ComputerBuilder(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def setUsbCount(self):
        pass

    @abc.abstractmethod
    def setDisplay(self):
        pass

    @abc.abstractmethod
    def getComputer(self):
        pass


# concrete builder
class LenovoComputerBuilder(ComputerBuilder):
    def __init__(self, cpu, ram, disk):
        self.computer = Computer(cpu, ram, disk)

    def setUsbCount(self):
        self.computer.setUSBCount(4)

    def setDisplay(self):
        self.computer.setDisplay("联想显示器")

    def getComputer(self):
        return self.computer


class AppleComputerBuilder(ComputerBuilder):
    def __init__(self, cpu, ram, disk):
        self.computer = Computer(cpu, ram, disk)

    def setUsbCount(self):
        self.computer.setUSBCount(2)

    def setDisplay(self):
        self.computer.setDisplay("苹果显示器")

    def getComputer(self):
        return self.computer


# 示例2：词法分析器
# 设计一个可以显示不同语言的阅读器

# product
class Word:
    def __init__(self, word):
        self.word = word

    def set_color(self, color):
        self.word = color.format(self.word)

    def set_background(self, color):
        self.word = color.format(self.word)

    def __str__(self):
        return self.word


class Text:
    def __init__(self, origin_text):
        self.text = []
        for word in origin_text.split(" "):
            self.text.append(Word(word))
            self.text.append(Word(" "))

    def set_indent(self, pos, size):
        self.text = self.text[:pos] + [" "]*size + self.text[pos:]

    def get_text(self):
        text = ""
        for word in self.text:
            text += str(word)
        return text


# builder
class TextConvert:

    def color_keyword(self):
        pass

    def highlight_error(self):
        pass

    def indent(self):
        pass

    def get_text(self):
        pass


class PythonTextConvert(TextConvert):
    def __init__(self, text):
        self._text = Text(text)
        self.text = self._text.text
        self.keywords = ["class", "def", "return", "if"]
        self.errors = ["error", "错误"]

    def color_keywords(self):
        for word in self.text:
            if str(word) in self.keywords:
                word.set_color("\033[33;1m{}\033[0m")

    def highlight_error(self):
        for word in self.text:
            if str(word) in self.errors:
                word.set_background("\033[41;1m{}\033[0m")

    def indent(self):
        for word in self.text:
            if str(word).endswith(":\n"):
                self._text.set_indent(self.text.index(word) + 1, 4)

    def get_text(self):
        return self._text.get_text()


class CppTextConvert(TextConvert):
    def __init__(self, text):
        self._text = Text(text)
        self.text = self._text.text
        self.keywords = ["class", "struct", "template", "virtual"]
        self.errors = ["error", "错误"]

    def color_keywords(self):
        for word in self.text:
            if str(word) in self.keywords:
                word.set_color("\033[33;1m{}\033[0m")

    def highlight_error(self):
        for word in self.text:
            if str(word) in self.errors:
                word.set_background("\033[41;1m{}\033[0m")

    def indent(self):
        for word in self.text:
            if str(word).endswith(":\n"):
                self._text.set_indent(self.text.index(word) + 1, 4)

    def get_text(self):
        return self._text.get_text()


# director
class TextReader:
    def parse_text(self, builder):
        builder.color_keywords()
        builder.highlight_error()
        builder.indent()


# 示例3 链式调用
class Person:
    def __init__(self, builder):
        self.__name = builder.name
        self.__gender = builder.gender
        self.__age = builder._age
        self.__height = builder._height
        self.__weight = builder._weight
        self.__career = builder._career
        self.__tel = builder._tel
        self.__address = builder._address
        self.__email = builder._email

    class Builder:
        def __init__(self, name, gender):
            self.name = name
            self.gender = gender
            self._age = None
            self._height = None
            self._weight = None
            self._career = None
            self._tel = None
            self._address = None
            self._email = None

        def age(self, age):
            self._age = age
            return self

        def height(self, height):
            self._height = height
            return self

        def weight(self, weight):
            self._weight = weight
            return self

        def career(self, career):
            self._career = career
            return self

        def tel(self, tel):
            self._tel = tel
            return self

        def address(self, address):
            self._address = address
            return self

        def email(self, email):
            self._email = email
            return self

        def build(self):
            return Person(self)


if __name__ == "__main__":
    # 示例1
    director = ComputerDirector()
    builder = AppleComputerBuilder(2, 16, 500)
    director.orderComputer(builder)
    computer = builder.getComputer()
    print(computer)

    director = ComputerDirector()
    builder = LenovoComputerBuilder(4, 8, 1000)
    director.orderComputer(builder)
    computer = builder.getComputer()
    print(computer)

    # 示例2
    # text = "def test:\n return error"
    # director = TextReader()
    # builder = PythonTextConvert(text)
    # director.parse_text(builder)
    # text = builder.get_text()
    # print(text)

    # 示例3
    # person = Person.Builder("张三", "male").age(18).tel(13123456789).build()
    # print(person.__dict__)
