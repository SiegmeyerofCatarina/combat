from typing import Set
import neuter
import logger
import synchronizer as sc


class Combat:
    def __init__(self, scene: 'neuter.Scene', teams: 'teams.Teams') -> None:
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
            for person in self.teams.alive:
                person.do_action()



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

            for team in self.teams:
                for person in team.alive_members:
                    person.effects.update(person)

            sc.timer.teak()

            logger.log.turn_log()
            winner = self.search_winner()

    def search_winner(self) -> bool:
        teams = [team for team in self.teams if team.alive_members]
        if len(teams) <= 1:
            logger.log.end_combat(teams)
            return True
        else:
            return False
