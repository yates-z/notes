# -*-coding:utf-8-*-

"""
适配器模式
类型：结构型模型
意图：将一个接口转换成客户希望的另一个接口
优点：提高了类的复用
缺点：过多地使用适配器容易让系统变得混乱，例如A接口的内部实际上被适配成立B接口
"""


# 示例1： 我们有一个txt阅读器，现在想要扩展阅读pdf的功能，正好有另一款pdf阅读器产品，
# 但是它们的接口不一样
class TxtReader:

    def show(self, file_name):
        print("打开了txt文件：{}".format(file_name))


class PdfReader:

    def show_pdf(self, file_name):
        print("打开了pdf文件：{}".format(file_name))


class ReaderAdapter:
    pdf = PdfReader()

    def show(self, file_name):
        self.pdf.show_pdf(file_name)


class ComplexReader:

    reader = TxtReader

    def show(self, file_type, file_name):
        if file_type == "txt":
            pass
        elif file_type == "pdf":
            self.reader = ReaderAdapter
        else:
            raise TypeError("不支持此格式！")
        self._show(file_name)

    def _show(self, file_name):
        self.reader().show(file_name)


if __name__ == '__main__':
    reader = ComplexReader()
    reader.show("txt", "python程序设计.txt")
    reader.show("pdf", "python程序设计.pdf")
