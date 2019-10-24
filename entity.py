from __future__ import annotations
from typing import List, Tuple, Set, Dict
import numpy as np


class Health:
    def __init__(self, max_hp: int, hp: int, alive: bool):
        """
        class for tracking hp
        :param max_hp:
        :param hp:
        :param alive:
        """
        self.max_hp = max_hp
        self.hp = hp
        self.alive = alive

    def update_hp(self, value_hp: int):
        """
        make damage to self or heal if it possible
        :param value_hp:
        :return:
        """
        if self.alive:
            self.hp += value_hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        elif self.hp <= 0:
            self.alive = False


class Effect:
    pass


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
            health: Health,
            team: str,
            parts: Dict[str, Part],
            actions: Set[Act],
            skills: Set[Skill],
            effects: Set[Effect],
    ):
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
        self.parts = parts
        self.actions = actions
        self.skills = skills
        self.effects = effects

    def do_action(self, target):
        """

        :return:
        """
        if target.team == self.team:
            ally_actions = [action for action in self.actions if action.target == 'ally']
            action = np.random.choice(ally_actions)
        elif target.team == self.team:
            enemy_actions = [action for action in self.actions if action.target == 'enemy']
            action = np.random.choice(enemy_actions)
        else:
            action = np.random.choice(list(self.actions))
        action.do(self, target)


class Act:
    def __init__(self,
                 name: str,
                 target: str,
                 max_range: int,
                 damage_deal: int,
                 pre_effects: Set[Effect],
                 post_effects: Set[Effect],
                 ):
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

    def do(self, actor: Entity, target: Entity):
        """
        do action in relation to the target
        :param actor:
        :param target:
        :return:
        """
        if self.max_range >= measure_distance(actor, target):
            target.health.update_hp(-self.damage_deal)
            if self.damage_deal > 0:
                print('{} attack {} with {} on {} hp, {} hp left'.format(
                    actor.name, target.name, self.name, self.damage_deal, target.health.hp))
            else:
                print('{} heal'.format(actor.name), end=' ')
                print('yourself' if target is actor else '{}'.format(target.name), end=' ')
                print('with {} on {} hp, and now have {} hp'.format(self.name, -self.damage_deal, target.health.hp))


def measure_distance(actor: Entity, target: Entity):
    """
    Measure distance between two entities
    :param actor:
    :param target:
    :return:
    """
    dst = int(actor is not target)
    return dst


def generate_entity(id: int) -> Entity:
    """
    Generate entity
    :param id:
    :return: new entity
    """
    team = np.random.choice(['pirates', 'british'])
    simple_attack = Act("pistol", 'enemy', 1, 6, set(), set())
    simple_heal = Act('drink potion', 'ally', 0, -2, set(), set())

    entity = Entity(
        id,
        (0, 0),
        '{} soldier {}'.format(team, id),
        Health(10, 10, True),
        team,
        dict(),
        {simple_attack, simple_heal},
        set(),
        set(),
    )
    return entity


def generate_scene():
    """
    Generate scene
    :return: new scene
    """
    return 2