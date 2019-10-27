from typing import Set, List
from sty import fg
from emoji import emojize

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
    name_with_hp_str = f'{person.team.color}{person.name}{fg.rs}({fg.red}{person.health.health} hp{fg.rs})'
    return name_with_hp_str


class Logger:
    def __init__(self):
        self.log = list()

    def strart_combat(self, scene: 'Scene', teams: Set['entity.Team']) -> None:
        """

        :param persons:
        :param args:
        :return:
        """
        print(f'generated {sum([len(team.alive_members) for team in teams])} persons:', end=' ')
        print(*map(lambda team: f'{len(team.alive_members)} in {team.color}{team.name}{fg.rs} team', teams), sep=', ')

    def death(self, person: 'entity.Entity') -> None:
        print(f'{person.name} died! {emojize(":skull:")}')

    def end_combat(self, teams: List['entity.Team']) -> None:
        if teams:
            winner_team = teams[0]
            print(f'{winner_team.name} win! {emojize(":crown:")}')
            print(f'Alive {len(winner_team.alive_members)}:', end=' ')
            print(*map(name_with_hp, [person for person in winner_team.alive_members]), sep=' ')
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
            print(f'{name_with_hp(actor)} attack {name_with_hp(target)} with {action.name} on {fg.red}{damage} hp{fg.rs}')
        elif damage == 0:
            print(f'{name_with_hp_and_cooldowns(actor)} {action.name}')
        else:
            print(f'{actor.name}', end=' ')
            print('healed' if target is actor else 'heal {target.name}', end=' ')
            print(f'with {name_with_hp(actor)} on {fg.red}{-damage} hp{fg.rs}')

log = Logger()
