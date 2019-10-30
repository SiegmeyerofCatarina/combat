from typing import Tuple, Set, Dict

from sty import fg

import logger
from Effect import Effect, Effects

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

    def __get_alive(self) -> Set['Entity']:
        return {member for member in self.members if member.health.alive}

    def __get_name_in_color(self) -> str:
        return f'{self.color}{self.name}{fg.rs}'

    alive_members = property(__get_alive)
    name_color = property(__get_name_in_color)


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
            skills: Set['Skill'] = None,
            effects: Effects = None,
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
        self.skills = skills or set()
        self.effects = effects or Effects()
        self.team = team

    def do_action(self, ally: Set['Entity'], enemy: Set['Entity']) -> None:
        """
        choose targets and actions
        :return:
        """
        self.effects.update()
        available_actions, available_ally_targets, available_enemy_targets = self.get_actions(ally, enemy)
        action, target = self.ai.choose_action(self, available_actions, available_ally_targets, available_enemy_targets)
        if not action:
            action = pass_action
            target = self
        action.do(self, target)

    def get_actions(self, ally: Set['Entity'], enemy: Set['Entity']) -> Tuple[
        Set['Action'], Set['Entity'], Set['Entity']]:
        """
        get list of available actions

        :param targets:
        :return:
        """
        available_actions = set()
        for action in self.actions:
            if action.cool_down.name not in [effect.name for effect in self.effects.effects]:
                available_actions.add(action)
        # print(f'{self.name_color} has {[action.name for action in available_actions]}')
        return available_actions, ally, enemy

    def take_damage(self, damage_value):
        self.health.health -= damage_value
        if not self.health.alive:
            logger.log.death(self)

    def __get_name_with_color(self):
        return f'{self.team.color}{self.name}{fg.rs}'

    def __get_person_cooldowns(self) -> str:
        cooldown_str = f'{[(effect.name, effect.cool_down.time) for effect in self.effects.effects]}'
        return cooldown_str

    name_color = property(__get_name_with_color)
    cooldowns = property(__get_person_cooldowns)


class Action:
    def __init__(
            self,
            name: str,
            target: str,
            max_range: int,
            damage_deal: int,
            cool_down: Effect,
            pre_effects: Effects = None,
            post_effects: Effects = None,
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
        self.cool_down = cool_down
        self.pre_effects = pre_effects or Effects()
        self.post_effects = post_effects or Effects()

    def do(self, actor: Entity, target: Entity) -> None:
        """
        do action in relation to the target

        :param actor:
        :param target:
        :return:
        """

        # TODO проверить расчет кулдауна. Возможно не правильная последовательность сброса кулдауна

        if self.max_range >= measure_distance(actor, target):
               # for effect in self.pre_effects:
            #     actor.effects.add(effect)

            damage = self.damage_deal  # some modifier
            target.take_damage(damage)
            actor.effects.add(self.cool_down)

            # for effect in self.post_effects:
            #     actor.effects.add(effect)
            logger.log.event(actor, self, target, damage)


def measure_distance(actor: Entity, target: Entity) -> int:
    """
    Measure distance between two entities
    :param actor:
    :param target:
    :return:
    """
    dst = int(actor is not target)
    return dst


pass_action = Action('pass', 'ally', 1, 0, Effect('pass', 0))
