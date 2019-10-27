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
        print(*map(lambda team: f'{len(team.alive_members)} in {team.color}{team.name}{fg.rs} team', teams), sep=', ')

    def death(self, person: 'entity.Entity') -> None:
        self.death_log.append(f'{name_with_hp(person)}')

    def end_combat(self, teams: List['entity.Team']) -> None:
        if teams:
            winner_team = teams[0]
            print(f'{emojize(":crown:")} {winner_team.color}{winner_team.name}{fg.rs} win!')
            print(f'Alive {len(winner_team.alive_members)}:', end=' ')
            print(*map(name_with_hp, [person for person in winner_team.alive_members]), sep=' ')
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
            log_str = f'{emojize(":crossed_swords:")} {name_with_hp(actor)} attack {name_with_hp(target)} with {action.name} on {fg.red}{damage} hp{fg.rs}'
        elif damage == 0:
            log_str = f'{name_with_hp_and_cooldowns(actor)} {action.name}'
        else:
            log_str = f'{emojize(":syringe:")} {name_with_hp(actor)}' + ' healed' if target is actor else ' heal {target.name}' + f'with {action.name} on {fg.red}{-damage} hp{fg.rs}'

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
