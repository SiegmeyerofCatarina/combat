# main program call combat module with scene and entities
from logger import Logger
from entity import generate_entity, generate_scene


def main():
    logger = Logger()
    scene = generate_scene()
    persons = {*map(generate_entity, range(3))}
    combat = Combat(scene, persons, logger)
    combat.do()


class Combat:
    def __init__(self, scene, persons, logger):
        """
        Make war not love!
        :param scene:
        :param persons:
        """
        self.log = logger
        self.scene = scene
        self.persons = persons

    def do(self):
        """
        lets fight!
        :return: winner
        """
        self.log.strart_combat(self.scene, self.persons)
        mortuary = set()
        winner = False

        while not winner:  # main loop
            for person in self.persons:
                if person.health.alive:
                    targets = self.persons
                    person.do_action(targets)
                else:
                    mortuary.add(person)
                    self.log.death(person)

            self.persons -= mortuary
            winner = self.search_winner()
        else:
            self.log.end_combat(self.persons)

    def search_winner(self):
        teams = set([person.team for person in self.persons])
        if len(teams) <= 1:
            if len(teams) == 1:
                winner = teams.pop()
            else:
                winner = True
            return winner


if __name__ == '__main__':
    main()
