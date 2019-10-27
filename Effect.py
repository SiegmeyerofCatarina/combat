class Effect:
    def __init__(self, name: str, timer: int = 0) -> None:
        self.name = name
        self.timer = timer

    def set_timer(self, timer: int):
        self.timer = timer

    def update(self):
        if self.timer:
            self.timer -= 1