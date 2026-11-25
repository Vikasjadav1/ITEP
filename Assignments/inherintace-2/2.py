'''
2. Delivery Charge Calculator
Problem Statement

A delivery company calculates delivery charges differently.

Create:

abstract class Delivery

Child classes:

BikeDelivery
TruckDelivery
DroneDelivery

Rules:

Bike → ₹5/km
Truck → ₹15/km
Drone → ₹20/km
Input Example

Distance = 10 km

Expected Output
Bike Delivery Charge = 50
Truck Delivery Charge = 150
'''

from abc import ABC,abstractmethod
class Delivery(ABC):
    @abstractmethod
    def charge(self):
        pass

class BikeDelivery(Delivery):
    def charge(self):
        distance=int(input("enter distance : "))
        print(f"Bike delivery charge  : {5*distance}")

class TruckDelivery(Delivery):
    def charge(self):
        distance=int(input("enter distance : "))
        print(f"Truck delivery charge  : {15*distance}")


class DroneDelivery(Delivery):
    def charge(self):
        distance=int(input("enter distance : "))
        print(f"Drone delivery charge  : {20*distance}")

obj=None
print("1 Truck delivery")
print("2 Bike delivery")
print("3 Drone delivery")
choice = int(input("enter delivery choice : "))
if choice==1:
    obj=TruckDelivery()
elif choice==2:
    obj=BikeDelivery
elif choice==3:
    obj=DroneDelivery()
else:
    print("invalid choice..........")

obj.charge()
