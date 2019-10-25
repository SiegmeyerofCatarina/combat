from typing import Set
from collections import defaultdict


class Logger:
    def __init__(self):
        self.log = list()

    def strart_combat(self, scene: 'Scene', persons: Set['Entity']) -> None:
        """

        :param args:
        :return:
        """
        print('generated {} persons'.format(len(persons)))
        teams = defaultdict(int)
        for person in persons:
            teams[person.team] += 1
        print(*map('{} in {} team'.format, teams.values(), teams.keys()), sep=', ')

    def death(self, person: 'Entity') -> None:
        print('{} died!'.format(person.name))

    def end_combat(self, alive: Set['Entity']) -> None:
        if alive:
            print('{} win! Alive {}:'.format(list(alive)[0].team, len(alive)), end=' ')
            print(*map('{} ({} hp)'.format,
                       [person.name for person in alive],
                       [person.health.hp for person in alive]), sep=', ')
        else:
            print('All dead!')

    def event(self, actor: 'Entity', action: 'Act', target: 'Entity', damage: int) -> None:
        """

        :param actor:
        :param action:
        :param target:
        :param damage:
        :return:
        """
        if damage > 0:
            print('{} attack {} with {} on {} hp, {} hp left'.format(
                actor.name, target.name, action.name, damage, target.health.hp))
        else:
            print('{} heal'.format(actor.name), end=' ')
            print('yourself' if target is actor else '{}'.format(target.name), end=' ')
            print('with {} on {} hp, and now have {} hp'.format(action.name, -damage, target.health.hp))
