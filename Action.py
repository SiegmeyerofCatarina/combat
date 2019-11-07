import logger
from Effect import Effect, Effects
from entity import Entity, measure_distance


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

    def do(self, actor: 'Entity', target: 'Entity') -> None:
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