from typing import Set, List
from sty import fg
from emoji import emojize

import entity

class Logger:
    def __init__(self):
        self.turn = 1
        self.event_log = list()
        self.death_log = list()

    def strart_combat(self, scene: 'Scene', teams: Set['entity.Team']) -> None:
        """

        :param persons:
        :param args:
        :return:
        """
        print(f'generated {sum([len(team.alive_members) for team in teams])} persons:', end=' ')
        print(*map(lambda team: f'{len(team.alive_members)} in {team.name_color} team', teams), sep=', ')

    def death(self, person: 'entity.Entity') -> None:
        self.death_log.append(f'{person.name_color}')

    def end_combat(self, teams: List['entity.Team']) -> None:
        if teams:
            winner_team = teams[0]
            print(f'{emojize(":crown:")} {winner_team.name_color} win!')
            print(f'Alive {len(winner_team.alive_members)}:', end=' ')
            print(*map(lambda person: f'{person.name_color} ({person.health.hp_percent})',
                       [person for person in winner_team.alive_members]), sep=' ')
        else:
            print(f'{emojize(":skull:")} All dead!')

    def event(self, actor: 'entity.Entity', action: 'entity.Action', target: 'entity.Entity', damage: int) -> None:
        """

        :param actor:
        :param action:
        :param target:
        :param damage:
        :return:
        """
        if damage > 0:
            log_str = f'{emojize(":crossed_swords:")} {actor.name_color} {actor.health.hp_bar} ' \
                      f'attack {target.name_color} {target.health.hp_bar} with {action.name} on {fg.red}{damage} hp{fg.rs}'
        elif damage == 0:
            log_str = f'{actor.name_color}{actor.health.hp_bar}{actor.cooldowns} {action.name}'
        else:
            log_str = f'{emojize(":syringe:")} {actor.name_color} {actor.health.hp_bar} '
            log_str += 'healed' if target is actor else f' heal {target.name_color} {target.health.hp_bar} '
            log_str += f' with {action.name} on {fg.cyan}{-damage} hp{fg.rs}'

        self.event_log.append(log_str)

    def turn_log(self):
        print(f'turn {self.turn}:')
        for event in self.event_log:
            print(event)

        if self.death_log:
            print(f'{emojize(":skull:")} Died:', end=' ')
            print(*[death for death in self.death_log], sep=', ', end='.\n')

        self.update()

    def update(self):
        self.turn += 1
        self.death_log = list()
        self.event_log = list()


log = Logger()
