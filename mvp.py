import random


def combat(try_escape=False):
    if not try_escape:
        print("вы умерли")
    else:
        print("вы пытались")

    return False


def choice_battle():
    return combat()


def choice_run():
    result = random.randint(0, 1)
    if result == 0:
        return combat(True)
    print("вы убежали")
    return True


def get_event():
    x = random.randint(0, 1)
    if x == 0:
        print("ничего не происходит вы плывете")
        return True

    print("на вас напали пираты вступить в бой(0) или удрать(1)?")
    choice = int(input())
    if choice == 0:
        return choice_battle()
    if choice == 1:
        return choice_run()


if __name__ == '__main__':
    print("начало игры")
    alive = True
    while alive:
        alive = get_event()
    else:
        print("конец")
