from .product import Product


class ProductRepository:
    def __init__(self, name: str, quantity: int):
        super().__init__(name, quantity)
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        pass

    def remove(self, product_name: str):
        pass

    def __repr__(self):
        return