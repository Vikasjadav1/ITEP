'''
#Remove a key from a dictionary using pop(). Handle the case where the key does not exist.
'''
student={
    "name":"vikas",
    "age":20,
    "marks":60
}

for key in student.keys():
    if key == "age":
        student.pop(key)
        print(student)
        break
else:
    print("key does not exist")