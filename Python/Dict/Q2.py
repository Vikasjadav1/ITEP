#merge two diffrent dict
student1={
    "name":"vikas",
    "age":25,
    "course":"ai/ml",
    "teacher":"yes"
}

student2={
    "name":"vikas",
    "age":25,
    "course":"ai/ml",
    "roll_no":1
}

result={}

for key,value in student1.items():
    if key not in student2:
        student2[key]=value

print(student2)