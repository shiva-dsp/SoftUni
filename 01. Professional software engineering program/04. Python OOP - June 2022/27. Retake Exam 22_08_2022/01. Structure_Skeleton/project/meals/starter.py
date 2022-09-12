from project.meals.meal import Meal


class Starter(Meal):
    DEFAULT_QUANTITY = 60

    def __init__(self, name: str, price: float, quantity=DEFAULT_QUANTITY):
        super().__init__(name, price, quantity)

    def details(self):
        # price_per_piece = self.price / self.quantity
        price_per_piece = self.price
        return f'Starter {self.name}: {price_per_piece:.2f}lv/piece'