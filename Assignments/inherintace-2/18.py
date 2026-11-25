'''
18. Report Card Generator
Problem Statement

Different grading systems exist.

Create:

abstract class Student

Child:

SchoolStudent
CollegeStudent

Each generates grades differently.
'''

from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    @abstractmethod
    def grade(self):
        pass


class SchoolStudent(Student):

    def grade(self):
        print(f"Student name: {self.get_name()}")
        print(f"Marks: {self.get_marks()}")

        if self.get_marks() >= 90:
            print("Grade A")
        elif self.get_marks() >= 75:
            print("Grade B")
        elif self.get_marks() >= 50:
            print("Grade C")
        else:
            print("Grade D")


class CollegeStudent(Student):

    def grade(self):
        print(f"Student name: {self.get_name()}")
        print(f"Marks: {self.get_marks()}")

        if self.get_marks() >= 85:
            print("Grade A+")
        elif self.get_marks() >= 70:
            print("Grade A")
        elif self.get_marks() >= 60:
            print("Grade B")
        elif self.get_marks() >= 40:
            print("Grade C")
        else:
            print("Fail")


print("----- Report Card Generator -----")
print("1. School Student")
print("2. College Student")

choice = int(input("Enter your choice: "))

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

if choice == 1:
    obj = SchoolStudent(name, marks)

elif choice == 2:
    obj = CollegeStudent(name, marks)

else:
    print("Invalid choice")
    obj = None

if obj:
    print("\n----- Report Card -----")
    obj.grade()
    