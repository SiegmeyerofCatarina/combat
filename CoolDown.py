from typing import Callable


class CoolDown:
    __cool_down_time: int
    __time: int
    __cooled_callback: Callable

    def __init__(self, cool_down_time: int, time: int = None, cooled_callback: Callable = None):
        self.__cool_down_time = cool_down_time
        self.__time = time if time is not None else cool_down_time
        self.__cooled_callback = cooled_callback

    def __get_time(self):
        return self.__time

    def __set_time(self, time):
        self.__time = max(time, 0)

    def __get_cool_down_time(self):
        return self.__cool_down_time

    def tick(self):
        self.time -= 1

    def heat_up(self):
        self.time = self.cool_down_time

    def __get_is_cooled(self):
        return self.time == 0

    cool_down_time = property(__get_cool_down_time)
    time = property(__get_time, __set_time)
    is_cooled = property(__get_is_cooled)
