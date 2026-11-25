'''
7. Cab Fare Calculator
Problem Statement

Cab fares differ based on ride type.

Create:

abstract class Ride

Child:

MiniRide
SedanRide
SUVRide

Rules:

Mini → ₹10/km
Sedan → ₹15/km
SUV → ₹20/km
'''
from abc import ABC,abstractmethod

class Ride(ABC):
    @abstractmethod
    def price(self):
        pass

class MiniRide(Ride):
    def price(self):
        distance=float(input("enter hours :"))
        print(f"total price : {distance*10}")


class SedanRide(Ride):
    def price(self):
        distance=float(input("enter hours :"))
        print(f"total price : {distance*15}")

class SUVRide(Ride):
    def price(self):
        distance=float(input("enter hours :"))
        print(f"total price : {distance*20}")

obj=None
print("1 mini ride ")
print("2 sedan ride ")
print("3 SUV ride ")
choice = int(input("enter choice : "))
if choice==1:
    obj=MiniRide()
elif choice==2:
    obj=SedanRide()
elif choice==3:
    obj=SUVRide()
else:
    print("invalid choice..........")

obj.price()


