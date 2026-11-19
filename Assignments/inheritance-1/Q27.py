'''
27. Transport Fare System

Abstract:

Transport

Derived:

Train
Flight
Bus

Implement ticket pricing.
'''

from abc import ABC,abstractmethod
class Transport(ABC):
    @abstractmethod
    def ticket_pricing(self):
        pass

class Train(Transport):
    def ticket_pricing(self):
        distance=int(input("enter distance for train : "))
        print(f"distance : {distance} , rate_per_km : 0.5 , ticket price : {distance*0.5}")

class Flight(Transport):
    def ticket_pricing(self):
        distance=int(input("enter distance for flight: "))
        print(f"distance : {distance} , rate_per_km : 100 , fare : {distance*100}")

class Bus(Transport):
    def ticket_pricing(self):
        distance=int(input("enter distance for Bus : "))
        print(f"distance : {distance} , rate_per_km : 2 , fare : {distance*2}")

obj1=Train()
obj1.ticket_pricing()
print(".............................")
obj2=Flight()
obj2.ticket_pricing()
print(".............................")
obj3=Bus()
obj3.ticket_pricing()