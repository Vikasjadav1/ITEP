'''
29. Employee Attendance

Abstract:

Employee

Derived:

FullTimeEmployee
PartTimeEmployee

Calculate working hours.
'''
from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def working_hours(self):
        pass

class FullTimeEmployee(Employee):
    def working_hours(self):
        print("full time employee works 8 hours........")

class PartTimeEmployee(Employee):
    def working_hours(self):
        print("full time employee works 4 hours........")

obj=FullTimeEmployee()
obj.working_hours()
print(".............................")
obj=PartTimeEmployee()
obj.working_hours()