from typing import Tuple, Set, Dict
from numpy.random import choice

from ai import Ai


class Health:
    __alive: bool
    __health: int
    __max_health: int
    __death_callback: callable

    def __init__(
            self,
            health: [int],
            max_health: int = -1,
            alive: bool = True,
            death_callback: callable = None,
    ) -> None:
        """
        class for tracking hp
        :param max_health:
        :param health:
        :param alive:
        """
        self.__health = health
        self.__max_health = max_health if max_health >= 0 else self.__health
        self.__alive = alive
        self.__death_callback = death_callback

    def get_alive(self):
        return self.__alive

    def set_alive(self, state):
        self.__alive = state
        if not self.alive and self.__death_callback:
            self.__death_callback()

    def get_health(self):
        return self.__health

    def set_health(self, value):
        self.__health = min(max(value, 0), self.max_health)
        self.check_alive()

    def get_health_in_percentage(self):
        return round(self.health * 100 / self.max_health, 2)

    def get_max_health(self):
        return self.__max_health

    def set_max_health(self, value):
        self.__max_health = value
        self.health += self.max_health - value

    def check_alive(self):
        self.alive = self.health > 0

    alive = property(get_alive, set_alive)
    health = property(get_health, set_health)
    max_health = property(get_max_health, set_max_health)
    health_in_percentage = property(get_health_in_percentage)


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

        action.do(self, target)

    def get_actions(self, targets: Set['Entity']) -> Tuple[Set['Action'], Set['Entity']]:
        """
        get list of available actions

        :param targets:
        :return:
        """

        return self.actions, targets


class Action:
    def __init__(self,
                 name: str,
                 target: str,
                 max_range: int,
                 damage_deal: int,
                 pre_effects: Set[Effect],
                 post_effects: Set[Effect],
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

    def do(self, actor: Entity, target: Entity) -> None:
        """
        do action in relation to the target
        :param actor:
        :param target:
        :return:
        """
        if self.max_range >= measure_distance(actor, target):
            damage = self.damage_deal  # some modifier
            target.health.health -= damage
            # TODO: logging
            # log.event(actor, self, target, damage)


def measure_distance(actor: Entity, target: Entity) -> int:
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
    default_ai = Ai()
    team = choice(['pirates', 'british'])
    simple_attack = Action('pistol', 'enemy', 1, 6, set(), set())
    simple_heal = Action('drink potion', 'ally', 0, -2, set(), set())

    entity = Entity(
        id,
        (0, 0),
        f'{team} soldier {id}',
        Health(10),
        team,
        default_ai,
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
