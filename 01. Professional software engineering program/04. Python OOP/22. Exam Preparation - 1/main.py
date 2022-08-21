# from project.supply.drink import Drink
# from project.supply.food import Food
#
# from project.controller import Controller
# from project.player import Player
# #
# # food_25 = Food('banana')
# # print(food_25.energy)
# #
# # food = Food('banana', 2)
# # print(food.energy)
# #
# # drink_15 = Drink('wine')
# # print(drink_15.energy)
# #
# # drink = Drink('wine', 3)  # No second argument is expected. Filed as default.
# # print(drink.energy)
#
# apple = Food("apple", 22)
# cheese = Food("cheese")
# juice = Drink("orange juice")
# water = Drink("water")
#
#
#
# player = Player('Pesho', 21, 100)
# print(player.name)
#
# # player_2 = Player('Pesho', 13, 62)
# # print(player_2.name)
#
# player_2 = Player('Gosho', 13, 62)
# print(player_2.name)
#
# print(player.need_sustenance)
# print(player_2.need_sustenance)
#
# controller = Controller()
# print(controller.add_player(player, player_2, player))
#
# print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
# print(controller.supplies)

from project.controller import Controller
from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food

controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player))
print(controller.duel("Peter", "Lilly"))
print(controller.add_player(first_player))
print(controller.sustain("Lilly", "Drink"))
first_player.stamina = 0
print(controller.duel("Peter", "Lilly"))
print(first_player)
print(second_player)
controller.next_day()
print(controller)