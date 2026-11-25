'''
20. Ticket Booking System
Problem Statement

Ticket prices differ by seat category.

Create:

abstract class Ticket

Child:

SilverTicket
GoldTicket
PlatinumTicket
'''

from abc import ABC, abstractmethod

class Ticket(ABC):
    def __init__(self, quantity):
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    @abstractmethod
    def calculate_price(self):
        pass


class SilverTicket(Ticket):
    def calculate_price(self):
        price = self.get_quantity() * 150
        print("Silver Ticket Price:", price)


class GoldTicket(Ticket):
    def calculate_price(self):
        price = self.get_quantity() * 250
        print("Gold Ticket Price:", price)


class PlatinumTicket(Ticket):
    def calculate_price(self):
        price = self.get_quantity() * 400
        print("Platinum Ticket Price:", price)


print("----- Ticket Booking System -----")
print("1. Silver Ticket")
print("2. Gold Ticket")
print("3. Platinum Ticket")

choice = int(input("Enter your choice: "))

quantity = int(input("Enter number of tickets: "))

if choice == 1:
    obj = SilverTicket(quantity)

elif choice == 2:
    obj = GoldTicket(quantity)

elif choice == 3:
    obj = PlatinumTicket(quantity)

else:
    print("Invalid choice")
    obj = None

if obj:
    obj.calculate_price()