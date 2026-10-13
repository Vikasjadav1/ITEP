'''
Merge two dictionaries. If a key exists in both dictionaries, use the
    value from the second dictionary.
    '''
student1={
    "name":"jayant",
    "class":"A",
    "leader":"yes"
}
student2={
    "name":"vikas",
    "age":20,
    "marks":60
}

for key,value in student2.items():
    student1[key]=value

print(student1)   