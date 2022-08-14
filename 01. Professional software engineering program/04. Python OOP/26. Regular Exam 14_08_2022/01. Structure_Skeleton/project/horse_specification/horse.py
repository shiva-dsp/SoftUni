from abc import ABC


class Horse(ABC):
    MAXIMUM_SPEED = 0

    def __init__(self, name: str, speed: int, is_taken=False):
        self.name = name
        self.speed = speed
        self.is_taken = is_taken

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f'Horse name {value} is less than 4 symbols!')
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if self.__class__.__name__ == 'Appaloosa':
            self.MAXIMUM_SPEED = 120

        if self.__class__.__name__ == 'Thoroughbred':
            self.MAXIMUM_SPEED = 140

        if value > self.MAXIMUM_SPEED:
            raise ValueError(f'Horse speed is too high!')
        self.__speed = value

    def train(self):
        pass