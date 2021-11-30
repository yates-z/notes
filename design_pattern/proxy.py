# -*-coding:utf-8-*-
"""
代理模式
类型：对象结构型模型
意图： 为其他对象提供一种代理以控制这个对象的访问
优点：
缺点：
"""
# 例如，有些图形对象的创建开销很大，因此打开文档时应避免一次性创建所有开销很大的对象。
# 解决方案是使用Proxy图像代替真正的图像，并在有需要时实例化真正的图像

class Image:

    def display(self):
        pass


# RealImage 每次创建时都需要从磁盘中加载
class RealImage(Image):

    def __init__(self, file_name):
        self.file_name = file_name
        self.load(file_name)

    def display(self):
        print("Displaying " + self.file_name)

    def load(self, file_name):
        print("Loading from disk: {}".format(file_name))


class ProxyImage(Image):

    realImage = None

    def __init__(self, file_name):
        self.file_name = file_name

    def display(self):
        if not self.realImage:
            self.realImage = RealImage(self.file_name)
        self.realImage.display()


if __name__ == "__main__":
    image = ProxyImage("test.jpg")
    image.display()
    print(" ")
    image.display()
