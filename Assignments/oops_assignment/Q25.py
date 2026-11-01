'''
 Write a Java program to create a class called "School" with attributes for students, teachers, 
 and classes, and methods to add and remove students and teachers, and to create classes.
'''

class School:
    students=[]
    teachers=[]
    classes=[]

    def add_student(self,student):
        if student not in School.students:
            School.students.append(student)
            print(f"student {student} added..........")
        else:
            print(f"student {student} already enrolled.....")

    def remove_student(self,student):
        if student in School.students:
            School.students.remove(student)
            print(f"student {student} removed......")
        else:
            print(f"student {student} not exist.....")

    
    def add_teacher(self,teacher):
        if teacher not in School.teachers:
            School.teachers.append(teacher)
            print(f"teacher {teacher} added..........")
        else:
            print(f"teacher {teacher} already exist.....")

    def remove_teacher(self,teacher):
        if teacher in School.teachers:
            School.teachers.remove(teacher)
            print(f"teacher {teacher} removed..........")
        else:
            print(f"teacher {teacher} not exist........")

    def create_class(self,classs):
        if classs not in School.classes:
            School.classes.append(classs)
            print(f"class {classs} created...........")
        else:
            print(f"class {classs} already exist..........")

obj=School()
# obj.add_student("vikas")
# obj.add_student("jayant")
# obj.add_student("mohit")

# obj.remove_student("mohit") 

# obj.add_teacher("teacher1")
# obj.add_teacher("teacher2")
# obj.add_teacher("teacher3")

# obj.remove_teacher("teacher2")
# print(School.students)
# print(School.teachers)

# obj.create_class("python")
# obj.create_class("java")
# obj.create_class("c++")
# obj.create_class("c++")

print(School.classes)