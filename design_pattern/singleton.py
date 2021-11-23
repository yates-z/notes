# -*-coding:utf-8-*-
"""
单例模式
类型：对象创建型
意图：一个类只有一个实例，且提供一个全局访问点
优点：
缺点：
"""


# 示例： 计数器
class Counter(object):
    instance = None
    n = 0

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Counter, cls).__new__(cls)
        return cls.instance

    def __call__(self):
        self.n += 1
        return self.n


if __name__ == '__main__':
    count = Counter()
    count()
    print(count.n)
    count2 = Counter()
    count2()
    print(count.n)
