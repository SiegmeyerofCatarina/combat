from typing import Set, Tuple
from numpy.random import choice

import entity


class Ai:
    def ___init___(self) -> None:
        pass

    def choose_action(
            self,
            actor: 'entity.Entity',
            actions: Set['entity.Action'],
            targets: Set['entity.Entity']
    ) -> Tuple['entity.Action', 'entity.Entity']:
        """

        :param actor:
        :param actions:
        :param targets:
        :return:
        """

        target = choice(list(targets))
        if target.team == actor.team:
            ally_actions = [action for action in actions if action.target == 'ally']
            action = choice(ally_actions)
        elif target.team == actor.team:
            enemy_actions = [action for action in actions if action.target == 'enemy']
            action = choice(enemy_actions)
        else:
            action = choice(list(actions))

        return action, target
