'''
19. Courier Service Pricing
Problem Statement

Pricing depends on package type.

Create:

abstract class Courier

Child:

NormalCourier
ExpressCourier
SameDayCourier
'''

from abc import ABC, abstractmethod

class Courier(ABC):
    def __init__(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    @abstractmethod
    def calculate_price(self):
        pass


class NormalCourier(Courier):
    def calculate_price(self):
        price = self.get_weight() * 40
        print("Normal Courier Charge:", price)


class ExpressCourier(Courier):
    def calculate_price(self):
        price = self.get_weight() * 70
        print("Express Courier Charge:", price)


class SameDayCourier(Courier):
    def calculate_price(self):
        price = self.get_weight() * 100
        print("Same Day Courier Charge:", price)

print("----- Courier Service -----")
print("1. Normal Courier")
print("2. Express Courier")
print("3. Same Day Courier")

choice = int(input("Enter your choice: "))

weight = float(input("Enter package weight (kg): "))

if choice == 1:
    obj = NormalCourier(weight)

elif choice == 2:
    obj = ExpressCourier(weight)

elif choice == 3:
    obj = SameDayCourier(weight)

else:
    print("Invalid choice")
    obj = None

if obj:
    obj.calculate_price()
