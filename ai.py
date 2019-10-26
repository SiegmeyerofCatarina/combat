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
        action = None
        target = actor

        if actions:
            ally_targets = set()
            enemy_targets = set()

            for target in targets:
                if target.team == actor.team:
                    ally_targets.add(target)
                else:
                    enemy_targets.add(target)

            action = choice(actions)
            if action.target == 'enemy' and enemy_targets:
                target = choice(list(enemy_targets))
            if action.target == 'ally' and ally_targets:
                target = choice(list(ally_targets))

        return action, target
