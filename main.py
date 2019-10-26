# main program call combat module with scene and entities
from typing import Set
from logger import logger
from entity import Entity
from generator import generate_entity, generate_scene


def main() -> None:

    scene = generate_scene()
    persons = {*map(generate_entity, range(5))}
    combat = Combat(scene, persons)
    combat.do()


class Combat:
    def __init__(self, scene: 'Scene', persons: Set['Entity']) -> None:
        """
        Make war not love!

        :param scene:
        :param persons:
        """
        self.scene = scene
        self.persons = persons

    def do(self) -> None:
        """
        lets fight!
        :return: winner
        """
        logger.strart_combat(self.scene, self.persons)
        mortuary = set()
        winner = False

        while not winner:  # main loop
            for person in self.persons:
                if person.health.alive:
                    targets = self.persons
                    person.do_action(targets)
                else:
                    mortuary.add(person)
                    logger.death(person)

            self.persons -= mortuary
            winner = self.search_winner()
        else:
            logger.end_combat(self.persons)

    def search_winner(self) -> bool:
        teams = set([person.team for person in self.persons])
        if len(teams) <= 1:
            return True
        else:
            return False


if __name__ == '__main__':
    main()
