from typing import Set

import actions
import entity


class Timer:
    def __init__(self):
        self.turn = 0
        self.combat = None
        self.actions: Set['actions.Action'] = set()
        entities: Set['entity.Entity']

    def teak(self):
        for action in self.actions:
            action.do()
        self.turn += 1
        print(f'turn: {self.turn}')

    def add_action(self, action):
        self.actions.add(action)

    def get_time(self):
        return self.turn

    time = property(get_time)


timer = Timer()
