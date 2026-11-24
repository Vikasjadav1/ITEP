'''
44. Online Examination System

Features:

Student
Exam
Result

Use abstract classes for exams.
'''

from abc import ABC, abstractmethod

class Exam(ABC):
    def __init__(self, subject, total_marks):
        self.subject = subject
        self.total_marks = total_marks

    @abstractmethod
    def conduct_exam(self):
        pass


class MCQExam(Exam):
    def __init__(self, subject, total_marks, marks_obtained):
        super().__init__(subject, total_marks)
        self.marks_obtained = marks_obtained

    def conduct_exam(self):
        print("Exam Subject:", self.subject)
        print("Total Marks:", self.total_marks)
        print("Exam completed...")


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display_student(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)


class Result:
    def __init__(self, student, exam):
        self.student = student
        self.exam = exam

    def display_result(self):
        print("\n----- EXAM RESULT -----")
        self.student.display_student()
        print("Subject:", self.exam.subject)
        print("Total Marks:", self.exam.total_marks)
        print("Obtained Marks:", self.exam.marks_obtained)

        if self.exam.marks_obtained >= self.exam.total_marks / 2:
            print("Status: PASS")
        else:
            print("Status: FAIL")


student = Student(101, "Vikas")

exam = MCQExam("Python", 100, 85)

exam.conduct_exam()

result = Result(student, exam)
result.display_result()
