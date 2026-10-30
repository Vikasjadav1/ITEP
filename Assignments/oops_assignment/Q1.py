'''
Create a class Employee with private fields: id, name, and salary.
Use setter methods to assign values. Add a method to display employee details.
'''

class Employee:
    '''
    def __init__(self,id,name,salary):
        self.__id=id
        self.__name=name
        self.__salary=salary
    '''
    def set_id(self,id):
        self.__id=id

    def set_name(self,name):
        self.__name=name

    def set_salary(self,salary):
        self.__salary=salary

    def display(self):
        print(f"Employee id {self.__id}")
        print(f"Employee name {self.__name}")
        print(f"Employee salary {self.__salary}")

# obj=Employee(1,"Vikas",2000065)
obj=Employee()
obj.set_id(1)
obj.set_name("vikas")
obj.set_salary(200000)
obj.display()