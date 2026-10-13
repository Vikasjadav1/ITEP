'''Find the number of key-value pairs in a dictionary without using len().'''

student={
    "name":"vikas",
    "age":20,
    "marks":60
}
len=0
for key in student.keys():
    if key:
        len+=1
print(f"length of dictionary : {len}")