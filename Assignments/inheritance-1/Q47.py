'''
47. School ERP System

Features:

attendance
exams
student records
teacher management
'''



class School:
    def __init__(self):
        self.students = {}
        self.teachers = {}
        self.attendance = {}
        self.marks = {}


    def add_student(self, student_id, name):
        self.students[student_id] = name
        print("Student added successfully!")

    def add_teacher(self, teacher_id, name, subject):
        self.teachers[teacher_id] = {
            "name": name,
            "subject": subject
        }
        print("Teacher added successfully!")

    def mark_attendance(self, student_id, status):
        if student_id in self.students:
            self.attendance[student_id] = status
            print("Attendance marked!")
        else:
            print("Student not found!")

    def add_marks(self, student_id, subject, marks):
        if student_id in self.students:
            self.marks[student_id] = {
                "subject": subject,
                "marks": marks
            }
            print("Marks added successfully!")
        else:
            print("Student not found!")

    def show_students(self):
        print("\nStudent Records:")
        for student_id, name in self.students.items():
            print(student_id, name)

    def show_teachers(self):
        print("\nTeacher Records:")
        for teacher_id, details in self.teachers.items():
            print(teacher_id, details["name"], details["subject"])


school = School()

school.add_student(101, "Vikas")
school.add_student(102, "Rahul")

school.add_teacher(1, "Amit", "Python")
school.add_teacher(2, "Neha", "Java")

school.mark_attendance(101, "Present")
school.mark_attendance(102, "Absent")

school.add_marks(101, "Python", 85)
school.add_marks(102, "Java", 90)

school.show_students()
school.show_teachers()

print("\nAttendance:", school.attendance)
print("Exam Marks:", school.marks)
