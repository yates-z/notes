# -*-coding:utf-8-*-
"""
工厂方法模式
类型：对象创建型
意图：提定义一个创建对象的接口，让子类决定实例化哪个类
优点：大大降低对象之间的耦合度，扩展性好，易于组装
缺点：每次增加产品都会增加相应的工厂
"""


class ApiV1:

    def search_inst(self):
        pass

    def delete_inst(self):
        pass


class ApiV2(ApiV1):

    def search_inst(self):
        pass


class SimpleFactory:

    def create_api(self, version):
        if version == "v1":
            return ApiV1()
        if version == "v2":
            return ApiV2()


# factory method
class ApiFactory:
    # factory method
    def create_api(self):
        pass


class ApiV1Factory:
    def create_api(self):
        return ApiV1()


class ApiV2Factory:
    def create_api(self):
        return ApiV2()
