# main program call combat module with scene and entities
from typing import Set, List
import logger
from entity import Entity
import time
from generator import generate_team, generate_entity, generate_scene
import random

MAX_TEAMS = 3
MAX_MEMBERS_IN_TEAM = 2


def main() -> None:

    scene = generate_scene()
    count_teams = random.randint(2, MAX_TEAMS)
    teams = {*map(generate_team, range(count_teams))}

    for team in teams:
        count_members = random.randint(1, MAX_MEMBERS_IN_TEAM)
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
            alive_members = dict()
            for team in self.teams:
                ally_alive = team.alive_members
                alive_members[team] = ally_alive

            for team in self.teams:
                ally_alive = set(alive_members[team])
                enemies_teams = self.teams - {team}
                enemies_alive = set.union(*[alive_members[team] for team in enemies_teams])

                for person in ally_alive:
                    person.do_action(ally_alive, enemies_alive)

            logger.log.turn_log()
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
