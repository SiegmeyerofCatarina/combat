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