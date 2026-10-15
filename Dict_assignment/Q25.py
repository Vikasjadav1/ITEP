'''
Given a nested dictionary of students and their subject marks, calculate
    each student's total marks and find the topper.
'''

students={
    "student1":{"subject1":50,"subject2":65,"subject3":54},
    "student2":{"subject1":80,"subject2":95,"subject3":95},
    "student3":{"subject1":10,"subject2":45,"subject3":34},
}


max=0
ans=""
for key1 in students.keys():
    total_marks=0
    for value2 in students[key1].values():
        total_marks+=value2
    if total_marks>max:
        max=total_marks
        ans=key1
    

print(f"{ans} has max marks")
