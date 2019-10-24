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
            coordinates:  Tuple[int, int],
            name: str,
            health: Health,
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
        self.parts = parts
        self.actions = actions
        self.skills = skills
        self.effects = effects

        print('created person ', name)

    def do_action(self, target):
        """

        :return:
        """
        action = np.random.choice(list(self.actions))
        action.do(self, target)


class Act:
    def __init__(self,
                 name: str,
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
        self.name = name
        self.max_range = max_range
        self.damage_deal = damage_deal

    def do(self, actor: Entity, target: Entity):
        """
        do action in relation to the target
        :param actor:
        :param target:
        :return:
        """
        if self.max_range >= measure_distance(actor, target):
            target.health.update_hp(-self.damage_deal)
            print('{} {} {} on {} hp'.format(actor.name, self.name, target.name, self.damage_deal))


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
    simple_attack = Act("Hit!", 1, 6, [], [])
    simple_heal = Act('Heal!', 0, 2, [], [])

    entity = Entity(
        id,
        (0, 0),
        'soldier{}'.format(id),
        Health(10, 10, True),
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