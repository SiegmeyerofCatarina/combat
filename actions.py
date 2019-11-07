import logger
from effects import Effect, Effects
import entity


class Action:
    """
    Some action that was committed

    """

    def __init__(self, capability: 'Ability', actor: 'entity.Entity', target: 'entity.Entity') -> None:
        assert isinstance(capability, Ability)
        self.capability = capability
        self.actor = actor
        self.target = target

    def do(self) -> None:
        damage = self.capability.damage_deal  # some modifier
        self.target.take_damage(damage)
        # self.target.effects.add(self.capability.damage_effect)
        self.actor.effects.add(self.capability.cool_down)

        logger.log.event(self.actor, self.capability, self.target, damage)


class Ability:
    """
    Ability to do some action

    """

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
        self.damage_effect = Effect('damage', 0, damage_deal)

    def do(self, actor: 'entity.Entity', target: 'entity.Entity') -> None:
        """
        do action in relation to the target

        :param actor:
        :param target:
        :return:
        """

        if self.max_range >= measure_distance(actor, target):
            damage = self.damage_deal  # some modifier
            # target.take_damage(damage)
            target.effects.add(self.damage_effect)
            actor.effects.add(self.cool_down)

            logger.log.event(actor, self, target, damage)

        else:
            print(f'\nWarning!: {actor.name_color} can\'t do action {self.name}, target {target.name_color}')


def measure_distance(actor: 'entity.Entity', target: 'entity.Entity') -> int:
    """
    Measure distance between two entities
    :param actor:
    :param target:
    :return:
    """
    dst = int(actor is not target)
    return dst


pass_action = Ability('pass', 'ally', 1, 0, Effect('pass', 0))