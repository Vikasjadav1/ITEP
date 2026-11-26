# 29. Insurance Premium Calculator
# Problem Statement

# Insurance premium varies.

# Create:

# HealthInsurance
# CarInsurance
# LifeInsurance


from abc import ABC, abstractmethod

class Insurance(ABC):

    def __init__(self, customer_name, amount):
        self.__customer_name = customer_name
        self.__amount = amount

    def get_name(self):
        return self.__customer_name

    def get_amount(self):
        return self.__amount

    @abstractmethod
    def calculate_premium(self):
        pass

    def display_details(self):
        print("Customer Name:", self.__customer_name)
        print("Insurance Amount:", self.__amount)


class HealthInsurance(Insurance):

    def calculate_premium(self):
        premium = self.get_amount() * 0.05
        print("Health Insurance Premium:", premium)


class CarInsurance(Insurance):

    def calculate_premium(self):
        premium = self.get_amount() * 0.03
        print("Car Insurance Premium:", premium)


class LifeInsurance(Insurance):

    def calculate_premium(self):
        premium = self.get_amount() * 0.02
        print("Life Insurance Premium:", premium)


h = HealthInsurance("Rahul", 500000)
c = CarInsurance("Amit", 500000)
l = LifeInsurance("Raj", 500000)

h.display_details()
h.calculate_premium()

c.display_details()
c.calculate_premium()

l.display_details()
l.calculate_premium()