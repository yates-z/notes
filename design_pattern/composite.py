# -*-coding:utf-8-*-

"""
组合模式
类型：对象结构型模型
意图： 将对象组合成树型结构表示“部分-整体”层次结构，使得用户对单个对象和组合对象的使用具有一致性。
优点： 可以忽略组合单个对象和整体的不同
缺点：
"""


# 示例： 文件系统
class FileSystem:

    def __init__(self, name):
        self.children = []
        self.name = name

    def create(self, component):
        pass

    def delete(self):
        pass

    def rename(self):
        pass

    def print(self):
        pass


class File(FileSystem):

    def delete(self):
        pass

    def rename(self):
        pass


class Folder(FileSystem):

    def create(self, component):
        self.children.append(component)

    def delete(self):
        pass

    def rename(self):
        pass

    def print(self, count=1):
        print("|" + "-" * count + "{}".format(self.name))
        for component in self.children:
            if component.children:
                component.print(count + 2)
            else:
                print("|" + "-" * (count + 2) + "{}".format(component.name))


if __name__ == '__main__':
    f = Folder("/")
    f2 = Folder("data")
    f2.create(File("文件3"))

    f.create(File("文件1"))
    f.create(File("文件2"))

    f.create(f2)

    f.print()



