'''Calculate the sum of all numeric values in a dictionary.'''

student={
    "name":"vikas",
    "age":20,
    "marks":60
}
sum=0
for value in student.values():
    if str(value).isdigit():
        sum+=value
print(f"sum of all numeric values in a dictionary :{sum}")
