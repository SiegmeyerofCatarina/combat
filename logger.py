from typing import Set
from collections import defaultdict

import entity


class Logger:
    def __init__(self):
        self.log = list()

    def strart_combat(self, scene: 'Scene', persons: Set['entity.Entity']) -> None:
        """

        :param persons:
        :param args:
        :return:
        """
        print(f'generated {len(persons)} persons')
        teams = defaultdict(int)
        for person in persons:
            teams[person.team] += 1
        print(*map(lambda count, name: f'{count} in {name}\033[0m team', teams.values(), teams.keys()), sep=', ')

    def death(self, person: 'entity.Entity') -> None:
        print(f'{person.name} died! ☠️')

    def end_combat(self, alive: Set['entity.Entity']) -> None:
        if alive:
            print(f'{list(alive)[0].team} win! Alive {len(alive)}:')
            print(*map(lambda person: f'{person.name} (\033[91m{person.health.health} hp\033[0m)', alive), sep=', ')
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
            print(f'{actor.name} attack \U0001F52B {target.name} with {action.name} on \033[91m{damage} hp\033[0m, \033[91m{target.health.health} hp\033[0m left')
        else:
            print(f'{actor.name} heal', end=' ')
            print(f'yourself' if target is actor else '{target.name}', end=' ')
            print(f'with {action.name} on \033[91m{-damage} hp\033[0m, and now have \033[91m{target.health.health} hp\033[0m')

log = Logger()
