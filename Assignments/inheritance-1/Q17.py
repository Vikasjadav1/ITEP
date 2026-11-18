'''
17. Online Course Platform
Course
ProgrammingCourse
PythonCourse

Add certification system.
'''


class Course:
    def __init__(self, name, duration):
        self.__name = name
        self.__duration = duration

    def course_details(self):
        print("Course Name:", self.__name)
        print("Duration:", self.__duration)


class ProgrammingCourse(Course):
    def __init__(self, name, duration, language):
        super().__init__(name, duration)
        self.__language = language

    def programming_details(self):
        print("Language:", self.__language)


class PythonCourse(ProgrammingCourse):
    def __init__(self, name, duration, language):
        super().__init__(name, duration, language)

    def certification(self, marks):
        if marks >= 60:
            print("Congratulations! Certificate Awarded.")
        else:
            print("Sorry! Certificate Not Awarded.")


obj = PythonCourse("Python", "3 Months", "Python")

obj.course_details()
obj.programming_details()


obj.certification(80)
