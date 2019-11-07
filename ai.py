from typing import Set, Tuple
from numpy.random import choice
import entity


class Ai:
    def ___init___(self) -> None:
        pass

    def choose_action(
            self,
            actor: 'entity.Entity',
            actions: Set['entity.Ability'],
            ally_targets: Set['entity.Entity'],
            enemy_targets: Set['entity.Entity'],
    ) -> Tuple['entity.Ability', 'entity.Entity']:
        """

        :param actor:
        :param actions:
        :param targets:
        :return:
        """
        action = None
        target = actor

        if actions:
            action = choice(list(actions))
            if action.target == 'enemy' and enemy_targets:
                target = choice(list(enemy_targets))
            if action.target == 'ally' and ally_targets:
                target = choice(list(ally_targets))

        return action, target
