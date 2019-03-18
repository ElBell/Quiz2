class Animal:
    def __init__(self, move: str, color: str, speed: int):
        self.move: str = move
        self.color: str = color
        self.speed: int = speed


class Horse(Animal):
    def __init__(self):
        super().__init__("gallop", "brown", 40)


class Bird(Animal):
    def __init__(self, color: str, speed: int):
        super().__init__("fly", color, speed)
        self.migration_month = ""


class BlueJay(Bird):
    def __init__(self):
        super().__init__("blue", 13)


class RedRobin(Bird):
    def __init__(self):
        super().__init__("red", 10)
