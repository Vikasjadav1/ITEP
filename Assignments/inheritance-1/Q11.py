'''
11. Company Hierarchy
Person
Employee(Person)
Manager(Employee)

Display company hierarchy.

'''
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def person_details(self):
        print(f"Person name: {self.__name}")
        print(f"Person age: {self.__age}")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary

    def employee_details(self):
        print(f"Employee salary: {self.__salary}")


class Manager(Employee):
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.__team_size = team_size

    def manager_details(self):
        print(f"Manager team size: {self.__team_size}")


obj = Manager("Vikas", 22, 20000, 10)

obj.person_details()
obj.employee_details()
obj.manager_details()

print(f"hierarchy :{Manager.mro()}")