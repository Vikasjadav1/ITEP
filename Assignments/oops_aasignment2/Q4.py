class Student:
    total_std=0
    def __init__(self,roll_num,name,marks):
        self.roll_num=roll_num
        self.name=name
        self.marks=marks
        Student.total_std+=1

    def total_marks(self):
        total_num=0
        for num in self.marks:
            total_num+=num
        return total_num

    def per(self,total_marks):
        total_marks=total_marks/3
        return total_marks

    def grade(self,per):
        if per>90:
            print("A grade......")
        elif per>75 and per<=90:
            print("B grade.......")
        elif per>50 and per<=75:
            print("C grade.........")
        else:
            print("Fail............")

    @classmethod
    def student_count(cls):
        return cls.total_std

std1=Student(101,"vikas",[50,60,80])
std2=Student(102,"jp",[5,8,9])
total_marks=std1.total_marks()
print(f"total marks : {total_marks}")
per=std1.per(total_marks)
print(f"percentage : {per}")
std1.grade(per)
print(Student.student_count())