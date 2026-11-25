'''
16. Hospital Billing System
Problem Statement

Hospital charges differ by patient type.

Create:

abstract class Patient

Child:

GeneralPatient
ICUPatient
EmergencyPatient
'''

from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self,name,mobile_num,city,age,charge):
        self.__name=name
        self.__mobile_num=mobile_num
        self.__city=city
        self.__age=age
        self.__charge=charge



    def get_name(self):
        return self.__name

    def get_mobile_num(self):
        return self.__mobile_num

    def get_city(self):
        return self.__city

    def get_age(self):
        return self.__charge

    def get_charge(self):
        return self.__charge

    @abstractmethod
    def display_details(self):
        pass

class GeneralPatient(Patient):
    def __init__(self,name,mobile_num,city,age,charge,bed_charge):
        super().__init__(name,mobile_num,city,age,charge)
        self.__bed_charge=bed_charge

    def display_details(self):
        total_bill=self.get_charge()+self.__bed_charge
        print(f"patient name : {self.get_name()}")
        print(f"patient age : {self.get_age()}")
        print(f"patient city : {self.get_city()}")
        print(f"patient mobile number : {self.get_mobile_num()}")
        print(f"hospital charge : {self.get_charge()}")
        print(f"hospital bed charge  : {self.__bed_charge}")
        print(f"total bill : {total_bill}")

class ICUPatient(Patient):
    def __init__(self,name,mobile_num,city,age,charge,bed_charge):
        super().__init__(name,mobile_num,city,age,charge)
        self.__bed_charge=bed_charge

    def display_details(self):
        total_bill=self.get_charge()+self.__bed_charge
        print(f"patient name : {self.get_name()}")
        print(f"patient age : {self.get_age()}")
        print(f"patient city : {self.get_city()}")
        print(f"patient mobile number : {self.get_mobile_num()}")
        print(f"hospital charge : {self.get_charge()}")
        print(f"hospital bed charge  : {self.__bed_charge}")
        print(f"total bill : {total_bill}")

class EmergencyPatient(Patient):
    def __init__(self,name,mobile_num,city,age,charge,bed_charge):
        super().__init__(name,mobile_num,city,age,charge)
        self.__bed_charge=bed_charge

    def display_details(self):
        total_bill=self.get_charge()+self.__bed_charge
        print(f"patient name : {self.get_name()}")
        print(f"patient age : {self.get_age()}")
        print(f"patient city : {self.get_city()}")
        print(f"patient mobile number : {self.get_mobile_num()}")
        print(f"hospital charge : {self.get_charge()}")
        print(f"hospital bed charge  : {self.__bed_charge}")
        print(f"total bill : {total_bill}")

print("----- Patient Management System -----")
print("1. General Patient")
print("2. ICU Patient")
print("3. Emergency Patient")

choice = int(input("Enter your choice: "))

name = input("Enter patient name: ")
mobile_num = int(input("Enter mobile number: "))
city = input("Enter city: ")
age = int(input("Enter age: "))
charge = int(input("Enter hospital charge: "))
bed_charge = int(input("Enter bed charge: "))

if choice == 1:
    obj = GeneralPatient(name, mobile_num, city, age, charge, bed_charge)

elif choice == 2:
    obj = ICUPatient(name, mobile_num, city, age, charge, bed_charge)

elif choice == 3:
    obj = EmergencyPatient(name, mobile_num, city, age, charge, bed_charge)

else:
    print("Invalid choice")
    obj = None

if obj:
    print("\n----- Patient Details -----")
    obj.display_details()

