'''
25. Ride Booking App

Abstract:

Ride

Derived:

BikeRide
CabRide
AutoRide

Calculate fare.

\[
\text{Fare} = \text{Distance} \times \text{Rate per km}
\]
'''
from abc import ABC,abstractmethod
class Ride(ABC):
    @abstractmethod
    def fare(self):
        pass

class BikeRide(Ride):
    def fare(self):
        distance=int(input("enter distance for BikeRide : "))
        print(f"distance : {distance} , rate_per_km : 5 , fare : {distance*5}")

class CabRide(Ride):
    def fare(self):
        distance=int(input("enter distance for CabRide: "))
        print(f"distance : {distance} , rate_per_km : 10 , fare : {distance*10}")

class AutoRide(Ride):
    def fare(self):
        distance=int(input("enter distance for AutoRide : "))
        print(f"distance : {distance} , rate_per_km : 15 , fare : {distance*15}")


obj=BikeRide()
obj.fare()
print("........................................")
obj=CabRide()
obj.fare()
print("........................................")
obj=AutoRide()
obj.fare()