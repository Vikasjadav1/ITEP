student={
    "name":"vikas",
    "age":25,
    "course":"ai/ml"
}
student1={
    "name":"vikas",
    "age":25,
    "course":"ai/ml"
}
print(student==student1)
print(len(student))
for key in student.keys():
    print(student[key])

for key,value in student.items():
    print(key,value)