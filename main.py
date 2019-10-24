# main program call combat module with scene and entities
from argparse import Action
from typing import List
import numpy as np


def main():
    scene = generate_scene()
    persons = [*map(generate_entity, range(5))]
    combat = Combat(scene, persons)
    combat.do()
    pass


class Combat:
    def __init__(self, scene, persons):
        """
        Make war not love!
        :param scene:
        :param persons:
        """
        print("Make war not love!")
        self.scene = scene
        self.persons = persons

    def do(self):
        """
        lets fight!
        :return: winner
        """
        winner = np.random.choice(self.persons)
        print('{} win!'.format(winner.name))
        return winner


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
            coordinates: (int, int),
            name: str,
            health: Health,
            parts: List[Part],
            actions: list,  # List[Act],
            skills: List[Skill],
            effects: List[Effect],
    ):
        """
        construct any person or destroyable object
        :param id:
        :param coordinates: (x,y) - position
        :param name: 
        :param health: 
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


class Act:
    def __init__(self,
                 name: str,
                 max_range: int,
                 damage_deal: int,
                 pre_effects: List[Effect],
                 post_effects: List[Effect],
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
            print("person {} take damage from person {}, he has {} and almost alive {}".format(
                target.name, actor.name, target.health.hp, target.health.alive))


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

    entity = Entity(
        id,
        (0, 0),
        'soldier{}'.format(id),
        Health(10, 10, True),
        [],
        [simple_attack],
        [],
        [],
    )
    return entity


def generate_scene():
    """
    Generate scene
    :return: new scene
    """
    return 2


if __name__ == '__main__':
    main()
