'''
1. Employee Bonus Calculator
Problem Statement

A company gives bonuses differently based on employee type.

Create:

abstract class Employee
child classes:
Developer
Manager
Intern

Rules:

Developer → 20% bonus
Manager → 35% bonus
Intern → fixed ₹5000 bonus
Requirements

Methods:

calculate_bonus()
display_details()
Concepts
Abstract class
Method overriding
Business logic
'''
from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def display_details():
        pass

    @abstractmethod
    def calculate_bonus():
        pass

class Developer(Employee):
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def display_details(self):
        print(f"Developer name : {self.name}")
        print(f"Developer id : {self.id}")
        print(f"Developer salary : {self.salary}")

    def calculate_bonus(self):
        bonus=self.salary*20/100
        self.salary=self.salary+bonus
        print(f"Developer bonus : {bonus}")
        print(f"Developer salary after bonus : {self.salary}")


class Manager(Employee):
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def display_details(self):
        print(f"Manager name : {self.name}")
        print(f"Manager id : {self.id}")
        print(f"Manager salary : {self.salary}")

    def calculate_bonus(self):
        bonus=self.salary*35/100
        self.salary=self.salary+bonus
        print(f"Manager bonus : {bonus}")
        print(f"Manager salary after bonus : {self.salary}")

class Intern(Employee):
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def display_details(self):
        print(f"Intern name : {self.name}")
        print(f"Intern id : {self.id}")
        print(f"Intern salary : {self.salary}")

    def calculate_bonus(self):
        bonus=5000
        self.salary=self.salary+bonus
        print(f"Intern bonus : {bonus}")
        print(f"Intern salary after bonus : {self.salary}")

obj=Developer("vikas",101,25000)
obj.display_details()
obj.calculate_bonus()
print(".................................................")
obj1=Manager("rohit",102,30000)
obj1.display_details()
obj1.calculate_bonus()
print(".................................................")
obj2=Intern("jayant",103,10000)
obj2.display_details()
obj2.calculate_bonus()