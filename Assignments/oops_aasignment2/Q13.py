class Exam:
    exam_conducted=0
    def __init__(self,exam_name,total_marks,passing_marks):
        self.exam_name=exam_name
        self.total_marks=total_marks
        self.passing_marks=passing_marks
        Exam.exam_conducted+=1

    def result(self):
        if self.passing_marks<=self.total_marks:
            print("Passed...........")
        else:
            print("Failed.............")

    def grade(self):
        if self.total_marks>90:
            print("grade A")
        elif self.total_marks>60 and self._total_marks<=90:
            print("grade B")
        else:
            print("grade C")

    @classmethod
    def exams(cls):
        return cls.exam_conducted

exam1=Exam("jee",60,75)
exam2=Exam("mp police",80,60)
exam1.result()
exam2.result()
exam1.grade()
print(f"exam conducted : {Exam.exams()}")
    