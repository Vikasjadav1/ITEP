'''
4. Vehicle Parking Fee System
Problem Statement

Parking fees vary by vehicle type.

Create:

abstract class Vehicle

Child classes:

Bike
Car
Bus

Rules:

Bike → ₹10/hour
Car → ₹30/hour
Bus → ₹50/hour
'''
from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def price(self):
        pass

class Bike(Vehicle):
    def price(self):
        hours=float(input("enter hours :"))
        print(f"total price : {hours*10}")


class Car(Vehicle):
    def price(self):
        hours=float(input("enter hours :"))
        print(f"total price : {hours*30}")

class Bus(Vehicle):
    def price(self):
        hours=float(input("enter hours :"))
        print(f"total price : {hours*50}")

obj=None
print("1 Book Bike ")
print("2 Book Car")
print("3 Book Bus")
choice = int(input("enter choice : "))
if choice==1:
    obj=Bike()
elif choice==2:
    obj=Car()
elif choice==3:
    obj=Bus()
else:
    print("invalid choice..........")

obj.price()

