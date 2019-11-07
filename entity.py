from typing import Tuple, Set, Dict

from sty import fg

import actions
import synchronizer as sc
import logger
import teams
from effects import Effects

from health import Health
from ai import Ai
import neuter


class Entity:
    def __init__(
            self,
            id: int,
            coordinates: Tuple[int, int],
            name: str,
            health: 'Health',
            ai: 'Ai',
            parts: Dict[str, 'neuter.Part'],
            abilities: Set['actions.Ability'],
            skills: Set['neuter.Skill'] = None,
            effects: Effects = None,
            team: 'teams.Team' = None,
    ) -> None:
        """
        construct any person or destroyable object
        :param id:
        :param coordinates: (x,y) - position
        :param name:
        :param health:
        :param parts: {'slot_name' : part, ...}
        :param abilities:
        :param skills:
        :param effects:
        """

        self.id = id
        self.position = coordinates
        self.name = name
        self.health = health
        self.ai = ai
        self.parts = parts
        self.abilities = abilities
        self.skills = skills or set()
        self.effects = effects or Effects()
        self.team = team

    def do_action(self, ally: Set['Entity'], enemy: Set['Entity']) -> None:
        """
        choose targets and abilities
        :return:
        """
        # self.effects.teak(self)
        available_actions, available_ally_targets, available_enemy_targets = self.get_abilities(ally, enemy)
        capability, target = self.ai.choose_action(self, available_actions, available_ally_targets, available_enemy_targets)
        if not capability:
            capability = actions.pass_action
            target = self
        action = actions.Action(capability, self, target)
        sc.timer.add_action(action)
        # capability.do(self, target)

    def get_abilities(self, ally: Set['Entity'], enemy: Set['Entity']) \
            -> Tuple[Set['actions.Ability'], Set['Entity'], Set['Entity']]:
        """
        get list of available abilities

        :param ally:
        :param enemy:
        :return:
        """
        available_actions = set()
        for ability in self.abilities:
            if ability.cool_down.name not in [effect.name for effect in self.effects.effects]:
                available_actions.add(ability)
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





