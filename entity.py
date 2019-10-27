from typing import Tuple, Set, Dict

from sty import fg

import logger
from Effect import Effect

from Health import Health
from ai import Ai


class Part:
    pass


class Skill:
    pass


class Team:
    def __init__(self, name: str, color: 'str', members: Set['Entity'] = None) -> None:
        self.name = name
        self.color = color
        self.members = members or set()

    def add(self, member: 'Entity') -> None:
        self.members.add(member)

    def remove(self, member: 'Entity') -> None:
        self.members.remove(member)

    def update(self, members: Set['Entity']) -> None:
        self.members.update(members)

    def get_alive(self) -> Set['Entity']:
        return {member for member in self.members if member.health.alive}

    alive_members = property(get_alive)


class Entity:
    def __init__(
            self,
            id: int,
            coordinates: Tuple[int, int],
            name: str,
            health: 'Health',
            ai: 'Ai',
            parts: Dict[str, 'Part'],
            actions: Set['Action'],
            skills: Set['Skill'] = set(),
            effects: Set['Effect'] = set(),
            team: 'Team' = None,
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
        self.ai = ai
        self.parts = parts
        self.actions = actions
        self.skills = skills
        self.effects = effects
        self.team = team

    def do_action(self, ally: Set['Entity'], enemy: Set['Entity']) -> None:
        """
        choose targets and actions
        :return:
        """
        available_actions, available_ally_targets, available_enemy_targets = self.get_actions(ally, enemy)
        action, target = self.ai.choose_action(self, available_actions, available_ally_targets, available_enemy_targets)
        if not action:
            action = pass_action
        action.do(self, target)

    def get_actions(self, ally: Set['Entity'], enemy: Set['Entity']) -> Tuple[Set['Action'], Set['Entity'], Set['Entity']]:
        """
        get list of available actions

        :param targets:
        :return:
        """
        available_actions = {action for action in self.actions if not action.cooldown.timer}

        return available_actions, ally, enemy

    def take_damage(self, damage_value):
        self.health.health -= damage_value


class Action:
    def __init__(
            self,
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

        if not self.cooldown.timer:
            if self.max_range >= measure_distance(actor, target):

                for effect in self.pre_effects:
                    actor.effects.add(effect)

                damage = self.damage_deal  # some modifier
                target.take_damage(damage)
                self.cooldown.timer = self.cooldown_time
                actor.effects.add(self.cooldown)

                for effect in self.post_effects:
                    actor.effects.add(effect)

                logger.log.event(actor, self, target, damage)
        else:
            raise Exception('called action in cooldown')


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
