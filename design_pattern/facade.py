# -*-coding:utf-8-*-

"""
外观模式
类型：对象结构型模型
意图： 为子系统中的一组接口提供一致的界面
优点： 当子系统过于复杂时，大多数用户并不需要知道如何使用底层功能，也不需要去封装底层的工能。facade可以提供
        一个缺省视图，满足大多数用户的使用
缺点：
"""


class Task:

    def start(self):
        pass


class TaskA(Task):

    def pre_start(self):
        print("执行A任务前的环境检查")

    def start(self):
        self.pre_start()
        print("执行了任务A")


class TaskB(Task):

    def start(self):
        print("执行了任务B")
        self.finished()

    def finished(self):
        print('发送了B任务结束的信号')


class TaskC(Task):

    def start(self):
        a_task = TaskA()
        a_task.start()
        # C任务逻辑
        print("执行了任务C")
        b_task = TaskB()
        b_task.start()


class TaskMaker:

    a_task = TaskA()
    b_task = TaskB()
    c_task = TaskC()

    def start_task_a(self):
        self.a_task.start()

    def start_task_b(self):
        self.b_task.start()

    def start_task_c(self):
        self.c_task.start()


if __name__ == '__main__':
    # 对于普通用户，使用TaskMaker快速执行任务
    task_maker = TaskMaker()
    task_maker.start_task_b()

    # 对于高级用户，可以继承任务类以控制执行细节
