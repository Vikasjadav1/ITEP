#Check whether the key "age" exists in a dictionary.

student={
    "name":"vikas",
    "age":20,
    "marks":60
}

found=False
for key in student.keys():
    if key=="age":
       found=True
       break
if found:
    print("exists in a dictionary")
else:
    print("not exists in a dictionary")
    