from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle, ABC):
    AIR_CONDITIONER_FUEL_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: int):
        fuel_needed = distance * (self.fuel_consumption + self.AIR_CONDITIONER_FUEL_CONSUMPTION)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER_FUEL_CONSUMPTION = 1.6
    COEFFICIENT_OF_POSSIBLE_FUEL_QUANTITY = 0.95

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: int):
        fuel_needed = distance * (self.fuel_consumption + self.AIR_CONDITIONER_FUEL_CONSUMPTION)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel: int):
        self.fuel_quantity += self.COEFFICIENT_OF_POSSIBLE_FUEL_QUANTITY * fuel