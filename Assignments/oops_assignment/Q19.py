'''
 Write a Java program to create a class called "Employee" with a name, salary, and hire date attributes, 
 and a method to calculate years of service.
 '''

class Employee:
    employees=[]

    def set_employee_details(self,name,salary,hire_date):
        self.name = name
        self.salary = salary
        self.hire_date = hire_date
        Employee.employees.append({
            "name":name,
            "salary":salary,
            "hire_date":hire_date
        })

    def cal_year(self):
        year = 2026 - self.hire_date
        print(f"{self.name} years of service: {year}")



emp1=Employee()
emp2=Employee()
emp1.set_employee_details("vikas",51505,2000)
emp2.set_employee_details("jayant",25522,2022)
print(Employee.employees)
emp2.cal_year()
emp1.cal_year()
