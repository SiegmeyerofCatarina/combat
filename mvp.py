import random

from Health import Health

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.clock import Clock



class GameLayout(BoxLayout):

    label_hp = ObjectProperty()
    label_event = ObjectProperty()
    button1 = ObjectProperty()
    button2 = ObjectProperty()
    boat = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_game()

    def next_teak(self, *args):

        if self.get_event():

            self.clock_stop()
            self.label_event.text = 'На вас напали пираты'


            self.button1.text = 'Сражаться'
            self.action_one = self.combat

            self.button2.text = 'Удирать'
            self.action_two = self.escape

        else:
            self.boat.health.health += 10
            self.update_hp()

    def update_hp(self):
        self.label_hp.text = f'Current hp {self.boat.health.health_in_percentage}'


    def combat(self):
        self.boat.health.health -= 30
        self.update_hp()
        if self.boat.health.alive:
            self.label_event.text = 'Вы отбились'
            self.reset_buttons()
        else:
            self.label_event.text = 'Вы погибли. Начать новую игру?'
            self.reset_buttons()
            self.button1.text = 'Новая игра'
            self.action_one = self.start_game
        pass

    def escape(self):
        if self.get_event():
            self.combat()

        else:
            self.label_event.text = 'Вам удалось удрать'
            self.reset_buttons()


    def reset_buttons(self):
        self.button1.text = 'Плыть'
        self.action_one = self.move

        self.button2.text = ''
        self.action_two = None



    def get_event(self):
        return random.randint(0, 1)


    def start_game(self):
        self.boat = Boat()
        self.update_hp()
        self.label_event.text = 'Что бы начать нажмите плыть'

        self.reset_buttons()


    def move(self):
        self.clock_start()
        self.label_event.text = 'Вы плывёте, всё хорошо'

        self.button1.text = 'Остановиться'
        self.action_one = self.stop

        self.button2.text = ''
        self.action_two = None

    def clock_start(self):
        Clock.schedule_interval(self.next_teak, .1)

    def clock_stop(self):
        Clock.unschedule(self.next_teak)

    def stop(self):
        self.clock_stop()
        self.label_event.text = 'Вы остановились. Что бы плыть нажмите плыть'
        self.reset_buttons()

    def action_one(self):
        pass

    def action_two(self):
        pass

    pass


class GameApp(App):
    def on_start(self):
        pass

    def build(self):
        return GameLayout()



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


def main():
    print("начало игры")
    boat = Boat()
    while boat.health.alive:
        boat.tick()
    else:
        print("конец")

if __name__ == '__main__':

    # main()
    GameApp().run()
