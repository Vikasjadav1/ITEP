'''
t=(1,2,3)
t = 1, 2, 3
print(t)

t =()
print(t)

t =([1, 2, 3])
print(t)
print(type(t))

t = (10,)
print(t)
print(type(t))

t = (10, 20, 30)

print(t[0])    # 10
print(t[-1])  # 30

t = (10, 20, 30, 40)

print(t[1:3])


t = ([1, 2], 3)

t[0].append(4)

print(t)


t = 10, 20, 30

print(t)

a, b, c = (10, 20, 30)

print(a)
print(b)
print(c)

a, *b = (1, 2, 3, 4)

print(a)   # 1
print(b)   # [2, 3, 4]

a, *b, c = (1,2,3,4,5)

print(a)
print(b)
print(c)


t = (1, 2, 2, 3)

print(t.count(2))
print(t.index(3))
print(len(t))
print(max(t))
print(min(t))
print(sum(t))

t = (10, 20, 30)

for i in t:
    print(i)

t = (10, 20, 30)
for i in range(len(t)):
    print(t[i])


t1 = (1, 2)
t2 = (3, 4)

print(t1 + t2)
t = (1, 2)

print(t * 3)


t = ((1, 2), (3, 4))
print(t[0])
print(t[1][1])


emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
dept = input("Enter Department: ")
salary = float(input("Enter Salary: "))

employee = (emp_id, name, dept, salary)
print("\nEmployee Details")
print("Employee ID:", employee[0])
print("Name:", employee[1])
print("Department:", employee[2])
print("Salary:", employee[3])


pname = input("Enter Product Name: ")
price = float(input("Enter Product Price: "))
qty = int(input("Enter Quantity: "))

bill = (pname, price, qty)
total = bill[1] * bill[2]

print("\nBill Details")
print("Product:", bill[0])
print("Total Amount:", total)

username = input("Enter Username: ")
password = input("Enter Password: ")

credentials = (username, password)
print("Stored Successfully")
print(credentials)


t = (10, 20, 30)

print(20 in t)
print(50 not in t)

t1 = (1, 2, 3)
t2 = (1, 2, 4)

print(t1 < t2)


t1 = (1, 2, 8)
t2 = (1, 2, 4,9)

print(t1 < t2)


t = (10, 20, 30)

del t
print(t)

t = (1, 2, 3)

l = list(t)

print(l)

l = [4, 5, 6]

t = tuple(l)

print(t)

t = (5, 2, 8, 1)

print(sorted(t))

t = ()
print(all(t))
print(any(t))


import sys
a = ('Learn', 'Python', 'with', 'GFG')
print("Memory size of tuple:", sys.getsizeof(a)) 


import sys

# Creating a list with same elements
a = ['Learn', 'Python', 'with', 'GFG']

# Checking memory usage of the list
print("Memory size of list:", sys.getsizeof(a))


from collections import namedtuple
student=namedtuple("student",['name','age','DOB'])
s1=student('Nandini','19','2541999')
print(s1.name)

from collections import namedtuple
Student = namedtuple("Student", ["roll", "name", "marks"])
n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print(f"\nEnter details for student {i+1}")
    roll = int(input("Roll Number: "))
    name = input("Name: ")
    marks = float(input("Marks: "))

    students.append(Student(roll, name, marks))

print("\nStudent Records")
for s in students:
    print(s)


from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "city"])

s1 = Student("Ajay", 25, "Bhopal")

print(Student._fields)

from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "city"])

s1 = Student("Ajay", 25, "Bhopal")

print(s1._asdict())

from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "city"])

s1 = Student("Ajay", 25, "Bhopal")

print(s1)

s2 = s1._replace(age=26)  # change age
print("After replacing age:", s2)

from collections import namedtuple

# Create namedtuple class
Student = namedtuple("Student", ["name", "age", "city"])

# Data in a list
data = ["Ajay", 25, "Bhopal"]

# Create namedtuple object using _make()
s1 = Student._make(data)

# Access fields
print(s1.name)  # Ajay
print(s1.age)   # 25
print(s1.city)  # Bhopal

from collections import namedtuple

# Create namedtuple class
Student = namedtuple("Student", ["name", "age", "city"])
info = ("Ravi", 22, "Delhi")
s2 = Student._make(info)
print(s2)

'''