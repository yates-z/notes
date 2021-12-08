# -*-coding:utf-8-*-
"""
模板方法模式
类型： 对象行为模式
意图： 定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以不改变一个算法的结构
        即可重定义该算法的某些特定步骤。
优点： 封装不变部分，扩展可变部分，行为由父类控制，子类实现
缺点： 每一个不同的实现都需要一个子类来实现
"""


# 示例
class Message:

    def foramt_message(self):
        pass

    def choose_receiver(self):
        pass

    def send(self):
        pass

    def run(self):
        self.choose_receiver()
        self.foramt_message()
        self.send()


class Mail(Message):

    def choose_receiver(self):
        print("选择收件人")

    def foramt_message(self):
        print("整理格式")

    def send(self):
        print("发送邮件\n")


class WxMessage(Message):

    def choose_receiver(self):
        print("选择好友")

    def foramt_message(self):
        print("整理格式")

    def send(self):
        print("发送微信消息\n")


if __name__ == "__main__":
    # 假设某个对象向我们传递了一个消息集合
    messages = [Mail(), WxMessage()]
    # 我们不需要区分消息的类型，直接调用run方法就可以了
    for message in messages:
        if isinstance(message, Message):
            message.run()
