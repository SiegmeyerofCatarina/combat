# main program call combat module with scene and entities
from typing import Set, List
import logger
from entity import Entity
import time
from generator import generate_team, generate_entity, generate_scene
import random

def main() -> None:

    scene = generate_scene()
    teams = {*map(generate_team, range(2))}

    for team in teams:
        count_members = random.randint(1, 5)
        persons = [generate_entity(id, team) for id in range(count_members)]
        team.update(persons)
    combat = Combat(scene, teams)
    combat.do()


class Combat:
    def __init__(self, scene: 'Scene', teams: Set['Entity.Team']) -> None:
        """
        Make war not love!

        :param scene:
        :param persons:
        """
        self.scene = scene
        self.teams = teams

    def do(self) -> None:
        """
        lets fight!
        :return: winner
        """
        logger.log.strart_combat(self.scene, self.teams)
        winner = False

        while not winner:  # main loop
            for team in self.teams:
                enemies_teams = self.teams - {team}
                enemies_alive = set.union(*[team.alive_members for team in enemies_teams])
                ally_alive = team.alive_members
                for person in ally_alive:
                    person.do_action(ally_alive, enemies_alive)

                    # logger.log.death(person)

            winner = self.search_winner()


    def search_winner(self) -> bool:

        teams = [team for team in self.teams if team.alive_members]
        if len(teams) <= 1:
            logger.log.end_combat(teams)
            return True
        else:
            return False


if __name__ == '__main__':
    main()
