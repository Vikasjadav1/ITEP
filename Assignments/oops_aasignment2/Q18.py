class Class:
    class_strength=0
    def __init__(self):
        self.student=[]
        self.teacher=[]
        Class.class_strength+=1

    def add_student(self,student):
        if student not in self.student:
            self.student.append(student)
            print("student added successfully.........")
        else:
            print("student already exist.....")

    def remove(self,student):
        if student in self.student:
            self.student.remove(student)
            print("removed.........")
        else:
            print("student not exists.........")


    @classmethod
    def strength(cls):
        return cls.class_strength

std1=Class()
std2=Class()
std3=Class()
std1.add_student("vikas")
std2.add_student("kp")
std3.add_student("ram")
std1.remove("ramd")
print(f"class strength : {Class.strength()}")

