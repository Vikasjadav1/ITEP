'''
3. Electricity Bill Generator
Problem Statement

Electricity bills are calculated differently for:

Residential users
Commercial users
Industrial users

Create abstract class ElectricityBill.

Rules

Residential:

Bill=Units×5

Commercial:

Bill=Units×8

Industrial:

Bill=Units×12
'''
from abc import ABC,abstractmethod

class ElectricityBill(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

class ResidentialUsers(ElectricityBill):
    def calculate_bill(self):
        unit=int(input("enter unit : "))
        print(f"Bill : {unit*5}")

class CommercialUsers(ElectricityBill):
    def calculate_bill(self):
        unit=int(input("enter unit : "))
        print(f"Bill : {unit*8}")

class IndustrialUsers(ElectricityBill):
    def calculate_bill(self):
        unit=int(input("enter unit : "))
        print(f"Bill : {unit*12}")

obj=None
print("1 Residential Users")
print("2 Commercial Users")
print("3 Industrial Users")
choice = int(input("enter choice : "))
if choice==1:
    obj=ResidentialUsers()
elif choice==2:
    obj=CommercialUsers()
elif choice==3:
    obj=IndustrialUsers()
else:
    print("invalid choice..........")

obj.calculate_bill()
