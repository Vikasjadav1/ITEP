
from abc import ABC, abstractmethod

class FoodItem(ABC):
    @abstractmethod
    def tax(self):
        pass


class VegFood(FoodItem):
    def tax(self):
        bill = int(input("Enter veg food bill: "))
        tax = bill * 5 / 100
        print(f"5% tax on veg food: {tax}")
        print(f"Total bill: {bill + tax}")


class NonVegFood(FoodItem):
    def tax(self):
        bill = int(input("Enter non-veg food bill: "))
        tax = bill * 12 / 100
        print(f"12% tax on non-veg food: {tax}")
        print(f"Total bill: {bill + tax}")


class Beverage(FoodItem):
    def tax(self):
        bill = int(input("Enter beverage bill: "))
        tax = bill * 18 / 100
        print(f"18% tax on beverage: {tax}")
        print(f"Total bill: {bill + tax}")


veg = VegFood()
nonveg = NonVegFood()
beverage = Beverage()

veg.tax()
nonveg.tax()
beverage.tax()
