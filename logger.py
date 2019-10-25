from collections import defaultdict

class Logger:
    def __init__(self):
        self.log = list()

    def strart_combat(self, scene, persons):
        """

        :param args:
        :return:
        """
        print('generated {} persons'.format(len(persons)))
        teams = defaultdict(int)
        for person in persons:
            teams[person.team] += 1
        print(*map('{} in {} team'.format, teams.values(), teams.keys()), sep=', ')

    def death(self, person: 'Entity'):
        print('{} died!'.format(person.name))

    def end_combat(self, alive: set()):
        if alive:
            # print('{} win!'.format(alive.winner))
            print(*map('{} alive with {} hp'.format,
                       [person.name for person in alive],
                       [person.health.hp for person in alive]), sep=', ')
        else:
            print('All dead!')
