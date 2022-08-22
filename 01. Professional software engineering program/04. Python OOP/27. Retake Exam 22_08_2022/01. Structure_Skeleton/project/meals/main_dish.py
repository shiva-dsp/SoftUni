from project.meals.meal import Meal


class MainDish(Meal):
    DEFAULT_QUANTITY = 50

    def __init__(self, name: str, price: float, quantity=DEFAULT_QUANTITY):
        super().__init__(name, price, quantity)

    def details(self):
        # price_per_piece = self.price / self.quantity
        price_per_piece = self.price
        return f'Main Dish {self.name}: {price_per_piece:.2f}lv/piece'