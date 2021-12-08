# -*-coding:utf-8-*-

"""
状态模式
类型： 对象行为模式
意图： 允许对象在内部状态发生改变时改变它的行为，对象看起来好像修改了它的类。
优点：
缺点：
"""


# 对象的行为依赖于它的状态（属性），并且可以根据它的状态改变而改变它的相关行为
# 示例，设计一款游戏的状态系统，并根据状态控制游戏行为
class State:

    def start(self, game):
        pass

    def pause(self, game):
        pass

    def stop(self, game):
        pass


class PendingState(State):
    name = "等待开始"

    def start(self, game):
        print("游戏开始！")
        game.set_state(game.running_state)

    def pause(self, game):
        print("游戏还未开始，不能暂停！")
        game.set_state(self)

    def stop(self, game):
        print("游戏还未开始，不能结束！")
        game.set_state(self)


class RunningState(State):
    name = "运行中"

    def start(self, game):
        print("游戏已经开始，不能再次开始！")
        game.set_state(self)

    def pause(self, game):
        print("游戏暂停！")
        game.set_state(game.pause_state)

    def stop(self, game):
        print("游戏结束！")
        game.set_state(game.pending_state)


class PauseState(State):
    name = "暂停"

    def start(self, game):
        print("游戏再次开始！")
        game.set_state(game.running_state)

    def pause(self, game):
        print("游戏已经暂停！")
        game.set_state(self)

    def stop(self, game):
        print("游戏结束！")
        game.set_state(game.pending_state)


# context
class Game:

    def __init__(self):
        self.pending_state = PendingState()
        self.running_state = RunningState()
        self.pause_state = PauseState()

        self.state = self.pending_state

    # 在类的不同状态下的同一动作显示出不同结果
    def start_game(self):
        self.state.start(self)

    def pause_game(self):
        self.state.pause(self)

    def stop_game(self):
        self.state.stop(self)

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state


"""
状态模式和策略模式的类图完全一样！
状态模式和策略模式的区别在于状态的转换是自动的、无意识的
"""
if __name__ == "__main__":
    game = Game()
    print("当前状态: {}".format(game.get_state().name))
    game.pause_game()
    print("当前状态: {}".format(game.get_state().name))
    game.start_game()
    print("当前状态: {}".format(game.get_state().name))
    game.pause_game()
    print("当前状态: {}".format(game.get_state().name))
    game.start_game()
    print("当前状态: {}".format(game.get_state().name))
    game.stop_game()
    print("当前状态: {}".format(game.get_state().name))
