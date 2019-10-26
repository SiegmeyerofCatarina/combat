class Health:
    __alive: bool
    __health: int
    __max_health: int
    __death_callback: callable

    def __init__(
            self,
            health: [int],
            max_health: int = -1,
            alive: bool = True,
            death_callback: callable = None,
    ) -> None:
        """
        Class for create health

        :param health: Current health
        :param max_health: Max health
        :param alive: Alive state
        :param death_callback: Function called at dead
        """
        self.__health = health
        self.__max_health = max_health if max_health >= 0 else self.__health
        self.__alive = alive
        self.__death_callback = death_callback

    def get_alive(self) -> bool:
        return self.__alive

    def set_alive(self, state) -> None:
        self.__alive = state
        if not self.alive and self.__death_callback:
            self.__death_callback()

    def get_health(self) -> int:
        return self.__health

    def set_health(self, value) -> None:
        self.__health = min(max(value, 0), self.max_health)
        self.check_alive()

    def get_health_in_percentage(self) -> float:
        return round(self.health * 100 / self.max_health, 2)

    def get_max_health(self) -> int:
        return self.__max_health

    def set_max_health(self, value) -> None:
        self.__max_health = value
        self.health += self.max_health - value

    def check_alive(self) -> None:
        self.alive = self.health > 0

    alive = property(get_alive, set_alive)
    health = property(get_health, set_health)
    max_health = property(get_max_health, set_max_health)
    health_in_percentage = property(get_health_in_percentage)
