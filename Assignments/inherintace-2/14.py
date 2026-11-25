'''
14. Employee Attendance Tracker
Problem Statement

Attendance calculation differs.

Create:

abstract class Employee

Child:

FullTimeEmployee
PartTimeEmployee
ContractEmployee
'''
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_attendance(self):
        pass


class FullTimeEmployee(Employee):

    def calculate_attendance(self):
        days = int(input("Enter working days: "))
        present = int(input("Enter present days: "))

        print("Full Time Attendance:", (present / days) * 100, "%")


class PartTimeEmployee(Employee):

    def calculate_attendance(self):
        total_hours = int(input("Enter total working hours: "))
        worked_hours = int(input("Enter worked hours: "))

        print("Part Time Attendance:", (worked_hours / total_hours) * 100, "%")


class ContractEmployee(Employee):

    def calculate_attendance(self):
        total_days = int(input("Enter contract working days: "))
        present_days = int(input("Enter present days: "))

        print("Contract Employee Attendance:", (present_days / total_days) * 100, "%")

print("1. Full Time Employee")
print("2. Part Time Employee")
print("3. Contract Employee")

choice = int(input("Enter your choice: "))

if choice == 1:
    emp = FullTimeEmployee()

elif choice == 2:
    emp = PartTimeEmployee()

elif choice == 3:
    emp = ContractEmployee()

else:
    print("Invalid choice")
    emp = None

if emp:
    emp.calculate_attendance()