from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAXIMUM_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.name = name
        self.speed = speed
        self.is_taken = False

    def train(self):
        new_speed = self.__speed + 3
        if new_speed > self.MAXIMUM_SPEED:
            new_speed = self.MAXIMUM_SPEED
        return new_speed