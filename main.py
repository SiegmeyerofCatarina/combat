# main program call combat module with scene and entities
from combat import Combat
import generator
import random
import teams as tms

MAX_TEAMS = 2
MAX_MEMBERS_IN_TEAM = 1


def main() -> None:

    scene = generator.generate_scene()
    count_teams = random.randint(2, MAX_TEAMS)
    teams = tms.Teams(*map(generator.generate_team, range(count_teams)))

    for team in teams:
        count_members = random.randint(1, MAX_MEMBERS_IN_TEAM)
        persons = [generator.generate_entity(id, team) for id in range(count_members)]
        team.update(persons)
    combat = Combat(scene, teams)
    combat.do()


if __name__ == '__main__':
    main()
