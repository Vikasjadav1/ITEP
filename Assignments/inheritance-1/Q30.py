'''
30. Restaurant Management

Abstract:

Restaurant

Derived:

PizzaRestaurant
BurgerRestaurant

Prepare food differently.
'''
from abc import ABC, abstractmethod

class Restaurant(ABC):

    @abstractmethod
    def prepare_food(self):
        pass


class PizzaRestaurant(Restaurant):

    def prepare_food(self):
        print("Preparing Pizza...")
        print("Adding cheese, toppings and baking pizza.")


class BurgerRestaurant(Restaurant):

    def prepare_food(self):
        print("Preparing Burger...")
        print("Adding patty, vegetables and sauces.")


obj = PizzaRestaurant()
obj.prepare_food()

print("/*-+-*/*+-*++//-+-/+-/*+/-+/*+/-")

obj = BurgerRestaurant()
obj.prepare_food()