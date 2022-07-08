class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity: int):
        pass

    def increase(self, quantity: int):
        pass

    def __repr__(self):
        return self.name