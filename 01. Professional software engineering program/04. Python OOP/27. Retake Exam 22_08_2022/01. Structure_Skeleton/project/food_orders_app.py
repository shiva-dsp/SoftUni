from project.meals.meal import Meal
from project.client import Client


class FoodOrdersApp:
    added_meals = []



    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception('The client has already been registered!')
        self.clients_list.append(Client(client_phone_number))
        return f'Client {client_phone_number} registered successfully.'

    def add_meals_to_menu(self, *meals: Meal):
        possible_meals = ['Starter', 'MainDish', 'Dessert']
        for meal in meals:
            if meal.__class__.__name__ not in possible_meals:
                continue
            self.menu.append(meal)
            self.added_meals.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')
        return '\n'.join(meal.details() for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        possible_meals = ['Starter', 'MainDish', 'Dessert']
        shopping_cart = []
        menu_names = []
        abble_meals = dict()
        clients_bill = 0

        if len(self.menu) < 5:
            raise Exception('The menu is not ready!')

        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                continue
            else:
                self.clients_list.append(Client(client_phone_number))

        for meal in self.menu:
            menu_names.append(meal)

        for meal_name, quantity in meal_names_and_quantities.items():
            if meal_name not in menu_names:
                raise Exception(f'{meal_name} is not on the menu!')

        for meal in self.menu:
            if meal.__class__.__name__ in possible_meals:
                if meal.quantity < meal_names_and_quantities[meal.name]:
                    raise Exception(f'Not enough quantity of {meal.__class__.__name__}: {meal.name}!')

                shopping_cart.append(meal)


    def cancel_order(self, client_phone_number: str):
        pass

    def finish_order(self, client_phone_number: str):
        pass

    def __str__(self):
        return f'Food Orders App has {len(self.added_meals)} meals on the menu and {len(self.clients_list)} clients.'