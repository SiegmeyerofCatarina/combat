# main program call combat module with scene and entities
from __future__ import annotations
from collections import defaultdict
from logger import Logger
from entity import generate_entity, generate_scene


def main():
    logger = Logger()
    scene = generate_scene()
    persons = {*map(generate_entity, range(10))}
    combat = Combat(scene, persons, logger)
    combat.do()
    pass


class Combat:
    def __init__(self, scene, persons, logger):
        """
        Make war not love!
        :param scene:
        :param persons:
        """
        print("Make war not love!")
        self.logger = logger
        self.scene = scene
        self.persons = persons

    def do(self):
        """
        lets fight!
        :return: winner
        """
        self.logger.strart_combat(self.scene, self.persons)
        mortuary = set()
        winner = False
        persons_in_combat = self.persons
        while not winner:
            for person in persons_in_combat:
                if person.health.alive:

                    targets = persons_in_combat
                    person.do_action(targets)
                else:
                    mortuary.add(person)
                    print('{} died!'.format(person.name))

            persons_in_combat -= mortuary

            teams = set([person.team for person in persons_in_combat])
            if len(teams) <= 1:
                if len(teams) == 1:
                    winner = self.persons.pop()
                    print('{} win!'.format(winner.team))
                    print(*map('{} alive with {} hp'.format,
                               [person.name for person in persons_in_combat],
                               [person.health.hp for person in persons_in_combat]), sep=', ')
                else:
                    winner = True
                    print('all died!')
        return winner


if __name__ == '__main__':
    main()
