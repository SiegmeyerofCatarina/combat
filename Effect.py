from typing import Set
from CoolDown import CoolDown


class Effect:
    __name: str
    __cool_down: CoolDown

    def __init__(self, name: str, cool_down_timer: int = 0) -> None:
        self.__name = name
        self.__cool_down = CoolDown(cool_down_timer)

    def update(self):
        self.__cool_down.tick()

    def __get_name(self):
        return self.__name

    def __get_cool_down(self):
        return self.__cool_down

    def __get_is_done(self):
        return self.cool_down.is_cooled

    name = property(__get_name)
    cool_down = property(__get_cool_down)
    is_done = property(__get_is_done)


class Effects:
    __effects: set

    def __init__(self, effects: Set[Effect] = None) -> None:
        self.__effects = effects or set()

    def __get_effects(self) -> Set[Effect]:
        return self.__effects

    def __set_effects(self, effects: Set[Effect] = None):
        self.__effects = effects

    def update(self):
        for effect in self.effects:
            effect.update()
        self.effects -= {effect for effect in self.effects if effect.is_done}

    def add(self, effect: Effect):
        self.effects.add(effect)

    effects = property(__get_effects, __set_effects)
