'''
2. Student Result Management System
Beginner
Concepts: Conditions, loops, functions
Requirements
•	Input marks for five subjects.
•	Calculate total, percentage, and grade.
•	Check whether the student passed or failed.
•	Validate that each mark is between 0 and 100.
•	Create functions such as calculate_total(), calculate_percentage(), and calculate_grade().
Bonus: Accept results for multiple students and calculate the class average

'''

students=int(input("enter number of students :-"))
class_total = 0


def calculate_total(python,java,c,sql,node):
    return python+java+c+sql+node

def calculate_percentage(python,java,c,sql,node):
    return (python+java+c+sql+node)/5

def calculate_grade(python,java,c,sql,node):
    per=(python+java+c+sql+node)/5
    if per>=90:
        print("pass with A grade......")
    elif per>=70 and per<90:
        print("pass with B grade......")
    elif per>=50 and per<70:
        print("pass with C grade......")
    elif per>=40 and per<50:
        print("pass with D grade......")
    else:
        print("Fail")

def input_marks(subject):
        while True:
            marks = int(input(f"Enter {subject} marks: "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Enter marks between 0 and 100.")

for i in range(students):
    python = input_marks("Python")
    java = input_marks("Java")
    c = input_marks("C")
    sql = input_marks("SQL")
    node = input_marks("Node")


    result=calculate_total(python,java,c,sql,node)
    print(result)
    result=calculate_percentage(python,java,c,sql,node)
    print(result)
    class_total+=result
    calculate_grade(python,java,c,sql,node)
    

if students>0:
    class_average = class_total / students
    print("Class average:", class_average)


        







        





