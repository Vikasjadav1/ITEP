class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Department:
    def __init__(self,dept_name):
        self.dept_name=dept_name
        self.employee=[]

    def add_employee(self,emp):
        self.employee.append(emp)
        print(f"{emp.name} added to {self.dept_name}")
    
    def display(self):
        print(f"Department : {self.dept_name}")
        print("employee details..")
        for emp in self.employee:
            print(f"Name : {emp.name}")
            print(f"Salary : {emp.salary}")

    def total_salary(self):
        total=0
        for emp in self.employee:
            total+=emp.salary
        return total

e1=Employee("vikas",2500000)
e2=Employee("jp",56545)
e3=Employee("kp",265959)

d1=Department("IT")
d2=Department("HR")

d1.add_employee(e1)
d1.add_employee(e2)
d2.add_employee(e3)

d1.display()
d2.display()

print(f"IT department salary : {d1.total_salary()}")
print(f"HR department salary : {d2.total_salary()}")
