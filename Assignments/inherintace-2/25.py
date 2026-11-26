'''
25. Employee Work Report System
Problem Statement

Different employees submit reports differently.

Create:

abstract class WorkReport

Child:

DeveloperReport
TesterReport
ManagerReport
'''
from abc import ABC, abstractmethod

class WorkReport(ABC):
    def __init__(self, employee_name):
        self.employee_name = employee_name

    @abstractmethod
    def submit_report(self):
        pass


class DeveloperReport(WorkReport):
    def submit_report(self):
        tasks = input("Enter completed development tasks: ")
        print("Developer Work Report")
        print("Employee:", self.employee_name)
        print("Completed Tasks:", tasks)


class TesterReport(WorkReport):
    def submit_report(self):
        bugs = int(input("Enter number of bugs found: "))
        print("Tester Work Report")
        print("Employee:", self.employee_name)
        print("Bugs Found:", bugs)


class ManagerReport(WorkReport):
    def submit_report(self):
        team_size = int(input("Enter team size: "))
        progress = input("Enter project progress: ")
        print("Manager Work Report")
        print("Employee:", self.employee_name)
        print("Team Size:", team_size)
        print("Project Progress:", progress)


print("1. Developer")
print("2. Tester")
print("3. Manager")

choice = int(input("Enter your choice: "))
name = input("Enter employee name: ")

if choice == 1:
    employee = DeveloperReport(name)
elif choice == 2:
    employee = TesterReport(name)
elif choice == 3:
    employee = ManagerReport(name)
else:
    print("Invalid choice")
    employee = None

if employee:
    employee.submit_report()
