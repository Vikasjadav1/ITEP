#Given a dictionary of student details, print each key and value on a separate line.

student={
    "name":"vikas",
    "age":20,
    "marks":60
}

for keys in student.keys():
    print(keys,":",student[keys])

'''
student={
    "name":["vikas","tushar"],
    "age":[50,60],
    "marks":[10,30]
}
print("name","age","marks")
for i in range(len(student["name"])):
    print(student["name"][i], student["age"][i], student["marks"][i])
    '''