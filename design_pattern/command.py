# -*-coding:utf-8-*-
"""
命令模式
类型： 对象行为型模型
意图： 将一个请求封装为一个对象，从而可以适用不同的请求对客户进行参数化、记录请求日志以及支持撤销操作
优点： 1、降低了系统耦合度。 2、新的命令可以很容易添加到系统中去。
缺点： 使用命令模式可能会导致某些系统有过多的具体命令类。
"""

# 有时必须向对象提交请求，但是并不知道被请求对象的信息
# 为了解耦合，不能将请求对象绑定到请求中
# 请求者和执行对象之间通过command进行联系

# 示例： 在一系列操作中如何实现撤销/事务


# 接收者，假设有一个画布对象
class Canvas:

    color = "white"

    def add_module(self):
        print("添加了内置模型")

    def remove_module(self):
        print("删除了内置模型")

    def set_background(self, color):
        self.color = color
        print("设置了背景颜色为：%s" % color)

    def get_background(self):
        return self.color


# 命令
class Command:

    # 执行命令
    def execute(self):
        pass

    # 撤销
    def undo(self):
        pass


# 具体的命令
class AddModuleCommand(Command):

    def __init__(self, canvas):
        self.canvas = canvas

    def execute(self):
        self.canvas.add_module()

    def undo(self):
        self.canvas.remove_module()


class RemoveModuleCommand(Command):

    def __init__(self, canvas):
        self.canvas = canvas

    def execute(self):
        self.canvas.remove_module()

    def undo(self):
        self.canvas.add_module()


class SetBackgroundCommand(Command):

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.origin_color = canvas.get_background()
        self.color = color

    def execute(self):
        self.canvas.set_background(self.color)

    def undo(self):
        self.canvas.set_background(self.origin_color)


# 请求类
class Invoke:

    def __init__(self):
        self.add_module_command = None
        self.remove_module_command = None
        self.set_background_command = None
        self.undo_command = None

    def set_command(self, add_module_command, remove_module_command, set_background_command):
        self.add_module_command = add_module_command
        self.remove_module_command = remove_module_command
        self.set_background_command = set_background_command

    def add_module(self):
        self.add_module_command.execute()
        self.undo_command = self.add_module_command

    def remove_module(self):
        self.remove_module_command.execute()
        self.undo_command = self.remove_module_command

    def set_background(self):
        self.set_background_command.execute()
        self.undo_command = self.set_background_command

    def undo(self):
        self.undo_command.undo()


# 客户端
if __name__ == "__main__":
    canvas = Canvas()
    add_module_command = AddModuleCommand(canvas)
    remove_module_command = RemoveModuleCommand(canvas)
    set_background_command = SetBackgroundCommand(canvas, "blue")

    invoke = Invoke()
    invoke.set_command(add_module_command, remove_module_command, set_background_command)
    invoke.add_module()
    invoke.remove_module()
    invoke.undo()
    invoke.set_background()
    invoke.undo()
