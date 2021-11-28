# -*-coding:utf-8-*-

"""
桥接模式
类型：对象结构型模型
意图：将抽象部分与它的实现部分分离，使它们都可以独立变化
优点： 类的实现部分可以在程序运行时被替换、类的抽象和实现都可以通过子类加以扩充
缺点：
"""
import abc


# 接口类
class ReportApi:

    def gen_report(self, name):
        pass


# 实现类
class XlsxReport(ReportApi):

    def gen_report(self, name):
        print("生成了xlsx格式的报告：%s" % name)


# 实现类
class PdfReport(ReportApi):

    def gen_report(self, name):
        print("生成了pdf格式的报告：%s" % name)


# 抽象类
class Report(metaclass=abc.ABCMeta):

    def __init__(self, api):
        self.api = api

    @abc.abstractmethod
    def generate(self):
        pass


class NormalReport(Report):

    def __init__(self, name, api):
        self.name = name
        super().__init__(api)

    def generate(self):
        self.api().gen_report(self.name)


# 桥接
if __name__ == '__main__':
    pdf = NormalReport("20211101-checkReport.pdf", PdfReport)
    pdf.generate()
