from typing import Set
from sty import fg
import entity


class Teams(set):
    def __get_alive(self):
        alive = set()
        for team in self:
            alive.update(team.alive_members)
        return alive

    alive = property(__get_alive)



class Team:
    def __init__(self, name: str, color: 'str', members: Set['entity.Entity'] = None) -> None:
        self.name = name
        self.color = color
        self.members = members or set()

    def add(self, member: 'entity.Entity') -> None:
        self.members.add(member)

    def remove(self, member: 'entity.Entity') -> None:
        self.members.remove(member)

    def update(self, members: Set['entity.Entity']) -> None:
        self.members.update(members)

    def __get_alive(self) -> Set['entity.Entity']:
        return {member for member in self.members if member.health.alive}

    def __get_name_in_color(self) -> str:
        return f'{self.color}{self.name}{fg.rs}'

    alive_members = property(__get_alive)
    name_color = property(__get_name_in_color)