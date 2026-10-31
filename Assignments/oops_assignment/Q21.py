'''
 Write a Java program to create a class called "Student" with a name, grade, and 
 courses attributes, and methods to add and remove courses.'''

class Student:
    students=[]

    def add_student(self,name,grade,course):
        self.__name=name
        self.__grade=grade
        self.__course=course

        Student.students.append({
            "name":name,
            "grade":grade,
            "course":course
        })

    def remove(self,name):
        for student in Student.students:
            if student["name"]==name:
                Student.students.remove(student)
                print("remove successfull")
            else:
                print("student does not exist")

std1=Student()
std1.add_student("vikas","A","cse")
std2=Student()
std2.add_student("jp","c","civil")
print(Student.students)
std2.remove("jp")
print(Student.students)
