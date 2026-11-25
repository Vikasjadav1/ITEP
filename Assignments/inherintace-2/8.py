'''
8. Salary Tax Calculator
Problem Statement

Tax calculation differs by employee category.

Create:

abstract class TaxPayer

Child:

GovernmentEmployee
PrivateEmployee
Freelancer
'''

from abc import ABC, abstractmethod

class TaxPayer(ABC):
    @abstractmethod
    def calculate_tax(self):
        pass


class GovernmentEmployee(TaxPayer):
    def calculate_tax(self):
        salary = 600000
        tax = salary * 0.05
        return tax


class PrivateEmployee(TaxPayer):
    def calculate_tax(self):
        salary = 800000
        tax = salary * 0.10
        return tax


class Freelancer(TaxPayer):
    def calculate_tax(self):
        income = 500000
        tax = income * 0.15
        return tax


gov = GovernmentEmployee()
private = PrivateEmployee()
freelancer = Freelancer()

print("Government Employee Tax:", gov.calculate_tax())
print("Private Employee Tax:", private.calculate_tax())
print("Freelancer Tax:", freelancer.calculate_tax())
