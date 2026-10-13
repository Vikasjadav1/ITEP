'''Reverse a dictionary so that values become keys and keys become values.
Assume all values are unique.
'''
student={
    "name":"vikas",
    "age":20,
    "marks":60
}
result={}
#result={value:key for key,value in student.items()}

for key,value in student.items():
    result[value]=key

print(result)