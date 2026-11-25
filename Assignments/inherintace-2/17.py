
'''
17. Smart Appliance Controller
Problem Statement

Different appliances behave differently.

Create:

abstract class Appliance

Child:

Fan
AC
WashingMachine
'''
from abc import ABC, abstractmethod

class Appliance(ABC):

    @abstractmethod
    def operate(self):
        pass


class Fan(Appliance):

    def operate(self):
        speed = int(input("Enter fan speed (1-5): "))
        print("Fan is running at speed:", speed)


class AC(Appliance):

    def operate(self):
        temperature = int(input("Enter AC temperature: "))
        print("AC is running at", temperature, "degree Celsius")


class WashingMachine(Appliance):

    def operate(self):
        mode = input("Enter washing mode (Quick/Normal/Heavy): ")
        print("Washing machine is running in", mode, "mode")


print("----- Smart Appliance Controller -----")
print("1. Fan")
print("2. AC")
print("3. Washing Machine")

choice = int(input("Enter your choice: "))

if choice == 1:
    obj = Fan()

elif choice == 2:
    obj = AC()

elif choice == 3:
    obj = WashingMachine()

else:
    print("Invalid choice")
    obj = None

if obj:
    obj.operate()