from typing import Set
from collections import defaultdict

import entity


def name_with_hp_and_cooldowns(person: 'Entiy') -> str:
    name_with_hp_str = name_with_hp(person)
    cooldown_str = f'{[(action.name, action.cooldown.timer) for action in person.actions]}'
    return name_with_hp_str + cooldown_str


def name_with_hp(person: 'Entiy') -> str:
    """
    make colorful output

    :param person:
    :return:
    """
    name_with_hp_str = f'{person.name}(\033[91m{person.health.health} hp\033[0m)'
    return name_with_hp_str


class Logger:
    def __init__(self):
        self.log = list()

    def strart_combat(self, scene: 'Scene', persons: Set['entity.Entity']) -> None:
        """

        :param persons:
        :param args:
        :return:
        """
        print(f'generated {len(persons)} persons:', end=' ')
        teams = defaultdict(int)
        for person in persons:
            teams[person.team] += 1
        print(*map(lambda count, name: f'{count} in {name}\033[0m team', teams.values(), teams.keys()), sep=', ')

    def death(self, person: 'entity.Entity') -> None:
        print(f'{person.name} died! ☠️')

    def end_combat(self, alive: Set['entity.Entity']) -> None:
        if alive:
            print(f'{list(alive)[0].team}\033[0m win! \U0001F451  \nAlive {len(alive)}:', end=' ')
            print(*map(name_with_hp, alive), sep=', ')
        else:
            print('All dead!')

    def event(self, actor: 'entity.Entity', action: 'entity.Action', target: 'entity.Entity', damage: int) -> None:
        """

        :param actor:
        :param action:
        :param target:
        :param damage:
        :return:
        """
        if damage > 0:
            print(f'{name_with_hp(actor)} attack  {name_with_hp(target)} with {action.name} on \033[91m{damage} hp\033[0m')
        elif damage == 0:
            print(f'{name_with_hp_and_cooldowns(actor)} {action.name}')
        else:
            print(f'{actor.name}', end=' ')
            print('healed' if target is actor else 'heal {target.name}', end=' ')
            print(f'with {name_with_hp(actor)} on \033[91m{-damage} hp\033[0m')


logger = Logger()
