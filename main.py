# main program call combat module with scene and entities
from __future__ import annotations
from collections import defaultdict
import numpy as np

from entity import generate_entity, generate_scene


def main():
    scene = generate_scene()
    persons = {*map(generate_entity, range(10))}
    print('generated {} persons'.format(len(persons)))
    teams = defaultdict(int)
    for person in persons:
        teams[person.team] += 1
    print(*map('{} in {} team'.format, teams.values(), teams.keys()), sep=', ')
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
