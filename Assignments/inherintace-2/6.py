'''
6. Exam Evaluation System
Problem Statement

Marks are evaluated differently.

Create:

abstract class Exam

Child:

MCQExam
PracticalExam
VivaExam

Each calculates grades differently.
'''

from abc import ABC, abstractmethod

class Exam(ABC):
    @abstractmethod
    def calculate_grade(self):
        pass


class MCQExam(Exam):
    def calculate_grade(self):
        marks = 85

        if marks >= 80:
            return "A Grade"
        else:
            return "B Grade"


class PracticalExam(Exam):
    def calculate_grade(self):
        marks = 75

        if marks >= 70:
            return "A Grade"
        else:
            return "B Grade"


class VivaExam(Exam):
    def calculate_grade(self):
        marks = 60

        if marks >= 60:
            return "A Grade"
        else:
            return "B Grade"

mcq = MCQExam()
practical = PracticalExam()
viva = VivaExam()

print("MCQ:", mcq.calculate_grade())
print("Practical:", practical.calculate_grade())
print("Viva:", viva.calculate_grade())
