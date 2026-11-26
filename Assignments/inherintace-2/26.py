'''
26. Water Bill Calculator
Problem Statement

Water charges vary by usage type.

Create:

Residential
Commercial
Agricultural
'''

class WaterBill:
    def __init__(self, units):
        self.units = units

    def calculate_bill(self):
        pass

class Residential(WaterBill):
    def calculate_bill(self):
        return self.units * 5

class Commercial(WaterBill):
    def calculate_bill(self):
        return self.units * 10

class Agricultural(WaterBill):
    def calculate_bill(self):
        return self.units * 2

print("1. Residential")
print("2. Commercial")
print("3. Agricultural")

choice = int(input("Enter your choice: "))
units = int(input("Enter water units consumed: "))

if choice == 1:
    obj = Residential(units)

elif choice == 2:
    obj = Commercial(units)

elif choice == 3:
    obj = Agricultural(units)

else:
    print("Invalid choice")
    obj = None

if obj:
    print("Total Water Bill:", obj.calculate_bill())