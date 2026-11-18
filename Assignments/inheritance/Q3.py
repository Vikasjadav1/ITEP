'''
3. Employee Management

Base class Employee.

Derived:

Developer
Tester
HR

Calculate salaries differently.
'''

from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass

class Developer(Employee):
    def salary(self):
        monthly_salary=int(input("enter developer monthly salary : "))
        bonus_salary = monthly_salary + (monthly_salary * 30 / 100)
        print(f"Developer salary : {monthly_salary}")
        print(f"Developer salary after 30% bonus : {bonus_salary}")

class Tester(Employee):
    def salary(self):
        monthly_salary=int(input("enter Tester monthly salary : "))
        bonus_salary = monthly_salary + (monthly_salary * 20 / 100)
        print(f"Tester salary : {monthly_salary}")
        print(f"Developer salary after 30% bonus : {bonus_salary}")

class Hr(Employee):
    def salary(self):
        monthly_salary=int(input("enter tester monthly salary : "))
        bonus_salary = monthly_salary + (monthly_salary * 10 / 100)
        print(f"Hr salary : {monthly_salary}")
        print(f"Developer salary after 30% bonus : {bonus_salary}")

obj=Developer()
obj.salary()

obj=Tester()
obj.salary()

obj=Hr()
obj.salary()