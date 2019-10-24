# main program call combat module with scene and entities
from __future__ import annotations
import numpy as np

from entity import generate_entity, generate_scene


def main():
    scene = generate_scene()
    persons = {*map(generate_entity, range(5))}
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
        mortuary = set()
        winner = False
        persons_in_combat = self.persons
        while not winner:
            for person in persons_in_combat:
                if person.health.alive:
                    target = np.random.choice(list(persons_in_combat))
                    person.do_action(target)
                else:
                    mortuary.add(person)

            if mortuary:
                print('{} died!'.format([person.name for person in mortuary]))
            persons_in_combat -= mortuary
            num_survivors = len(self.persons)
            if num_survivors <= 1:
                if num_survivors == 1:
                    winner = self.persons.pop()
                    print('{} win! {} hp left'.format(winner.name, winner.health.hp))
                else:
                    winner = True
                    print('all died!')
        return winner


if __name__ == '__main__':
    main()