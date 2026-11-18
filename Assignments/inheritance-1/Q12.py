'''
12. University System
Person
Student(Person)
GraduateStudent(Student)
'''
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def person_details(self):
        print(f"person name : {self.__name}")
        print(f"person age : {self.__age}")

class Student(Person):
    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.__id=id

    def student_details(self):
        print(f"student id : {self.__id}")

class GraduateStudent(Student):
    def __init__(self,name,age,id,degree):
        super().__init__(name,age,id)
        self.__degree=degree

    def display(self):
        print(f"student degree : {self.__degree}")

obj=GraduateStudent("vikas",22,201,"B-Tech")
obj.person_details()
obj.student_details()
obj.display()