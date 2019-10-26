from typing import Tuple, Set, Dict
from logger import logger

from Health import Health
from ai import Ai


class Effect:
    def __init__(self, name: str, timer: int = 0) -> None:
        self.name = name
        self.timer = timer

    def set_timer(self, timer: int):
        self.timer = timer

    def update(self):
        if self.timer:
            self.timer -= 1


class Part:
    pass


class Skill:
    pass


class Entity:
    def __init__(
            self,
            id: int,
            coordinates: Tuple[int, int],
            name: str,
            health: 'Health',
            team: str,
            ai: 'Ai',
            parts: Dict[str, 'Part'],
            actions: Set['Action'],
            skills: Set['Skill'],
            effects: Set['Effect'],
    ) -> None:
        """
        construct any person or destroyable object
        :param id:
        :param coordinates: (x,y) - position
        :param name:
        :param health:
        :param parts: {'slot_name' : part, ...}
        :param actions:
        :param skills:
        :param effects:
        """

        self.id = id
        self.position = coordinates
        self.name = name
        self.health = health
        self.team = team
        self.ai = ai
        self.parts = parts
        self.actions = actions
        self.skills = skills
        self.effects = effects

    def do_action(self, targets: Set['Entity']) -> None:
        """
        choose targets and actions
        :return:
        """
        available_actions, available_targets = self.get_actions(targets)
        action, target = self.ai.choose_action(self, available_actions, available_targets)
        if not action:
            action = pass_action
        action.do(self, target)

    def get_actions(self, targets: Set['Entity']) -> Tuple[Set['Action'], Set['Entity']]:
        """
        get list of available actions

        :param targets:
        :return:
        """
        available_actions = [action for action in self.actions if not action.cooldown.timer]
        available_targets = targets

        return available_actions, available_targets


class Action:
    def __init__(self,
                 name: str,
                 target: str,
                 max_range: int,
                 damage_deal: int,
                 cooldown: Effect,
                 cooldown_time: int = 0,
                 pre_effects: Set[Effect] = set(),
                 post_effects: Set[Effect] = set(),

                 ) -> None:
        """
        action
        :param name:
        :param max_range:
        :param damage_deal:
        :param pre_effects:
        :param post_effects:
        """
        self.target = target
        self.name = name
        self.max_range = max_range
        self.damage_deal = damage_deal
        self.pre_effects = pre_effects
        self.post_effects = post_effects
        self.cooldown = cooldown
        self.cooldown_time = cooldown_time

    def do(self, actor: Entity, target: Entity) -> None:
        """
        do action in relation to the target

        :param actor:
        :param target:
        :return:
        """
        expired_events = set()
        for effect in actor.effects:
            effect.update()
            if not effect.timer:
                expired_events.add(effect)

        actor.effects -= expired_events

        for effect in self.pre_effects:
            actor.effects.add(effect)

        if not self.cooldown.timer:

            if self.max_range >= measure_distance(actor, target):
                damage = self.damage_deal  # some modifier
                target.health.health -= damage
                self.cooldown.timer = self.cooldown_time

                logger.event(actor, self, target, damage)

                actor.effects.add(self.cooldown)

                for effect in self.post_effects:
                    actor.effects.add(effect)


def measure_distance(actor: Entity, target: Entity) -> int:
    """
    Measure distance between two entities
    :param actor:
    :param target:
    :return:
    """
    dst = int(actor is not target)
    return dst


no_cooldown = Effect('')
pass_action = Action('pass', 'ally', 1, 0, no_cooldown)
