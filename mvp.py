import random
from Health import Health


class Boat:
    __health: Health

    def __init__(self):
        self.__health = Health(100)

    def __get_health(self):
        return self.__health

    def combat(self):
        print("бой")
        self.health.health -= 30

    def choice_battle(self):
        self.combat()

    def choice_run(self):
        result = random.randint(0, 1)
        if result == 0:
            print("не удалось убежать")
            self.combat()
        else:
            print("вы убежали")

    def tick(self):
        x = random.randint(0, 1)
        if x == 0:
            self.health.health += 10
            print("ничего не происходит вы плывете")
        elif x == 1:
            print("на вас напали пираты вступить в бой(0) или удрать(1)?")
            choice = int(input())
            if choice == 0:
                print("вы вступаете в бой")
                self.choice_battle()
            elif choice == 1:
                print("вы пытаетесь убежать")
                self.choice_run()
        print(f'boat health: {self.health.hp_bar} {self.health.health_in_percentage}%')

    health = property(__get_health)


if __name__ == '__main__':
    print("начало игры")
    boat = Boat()
    while boat.health.alive:
        boat.tick()
    else:
        print("конец")
