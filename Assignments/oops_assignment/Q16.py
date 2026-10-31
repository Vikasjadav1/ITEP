'''
Write a Java program to create a class called "Employee" with a name, job title, and salary attributes, and methods to calculate and update salary.
'''
class Employee:
    def __init__(self,job_title,salary):
        self.__job_title=job_title
        self.__salary=salary
        

    def update_salary(self,salary):
        self.__salary=salary

    def salary_cal(self):
        print(f"per day salary {self.__salary/30}")
        print(f"yearly salary {12*self.__salary}")
        print(f"hourly salary {self.__salary/(26*8)}")


obj=Employee("software_enginner",20000)
obj.update_salary(20858)
obj.salary_cal()

    