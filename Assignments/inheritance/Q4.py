
class Person:
    pass

class Student(Person):
    def student_details(self):
        std_name=input("enter name : ")
        std_id=input("enter id : ")
        std_course=input("enter course : ")
        
        print("................................................................................")
        print(f"student name : {std_name}")
        print(f"student id : {std_id}")
        print(f"student course : {std_course}")

class Teacher(Person):
    def teacher_details(self):
        teacher_name=input("enter teacher name : ")
        teacher_id=input("enter teacher id : ")
        teacher_subject=input("enter teacher subjet : ")
        
        print("................................................................................")
        print(f"teacher name : {teacher_name}")
        print(f"teacher id : {teacher_id}")
        print(f"teacher subject : {teacher_subject}")

obj=Student()
obj.student_details()
print("................................................................................")
obj=Teacher()
obj.teacher_details()
