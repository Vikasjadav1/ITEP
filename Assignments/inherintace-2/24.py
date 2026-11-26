'''
24. Ride Sharing App Surge Pricing
Problem Statement

Surge pricing differs.

Create:

abstract class RidePricing

Child:

NormalTime
PeakTime
RainTime
'''

from abc import ABC, abstractmethod

class RidePricing(ABC):
    def __init__(self, base_fare):
        self.base_fare = base_fare

    @abstractmethod
    def calculate_fare(self):
        pass


class NormalTime(RidePricing):
    def calculate_fare(self):
        return self.base_fare


class PeakTime(RidePricing):
    def calculate_fare(self):
        return self.base_fare * 1.5


class RainTime(RidePricing):
    def calculate_fare(self):
        return self.base_fare * 2

print("1. Normal Time")
print("2. Peak Time")
print("3. Rain Time")

choice = int(input("Enter your choice: "))
base_fare = float(input("Enter base fare: "))

if choice == 1:
    ride = NormalTime(base_fare)
elif choice == 2:
    ride = PeakTime(base_fare)
elif choice == 3:
    ride = RainTime(base_fare)
else:
    print("Invalid choice")
    ride = None

if ride:
    print("Total Ride Fare:", ride.calculate_fare())
