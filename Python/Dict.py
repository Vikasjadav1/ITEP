'''
d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d1)
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)

student = {
    "name": "Ajay",
    "age": 25,
    "city": "Bhopal"
}

print(student)

student = {
    "name": "Ajay",
    "age": 25,
    "name": "amit"
}

print(student)

student = {"name": "Ajay", "age": 25, "city": "Bhopal"}
print(student["name"])  # Ajay
print(student.get("age"))

student = {"name": "Ajay", "age": 25, "city": "Bhopal"}
print(student["country"]) 


student = {"name": "Ajay", "age": 25, "city": "Bhopal"}
#print(student["country"]) 
print(student.get("country"))



d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 22
# Updating an existing value
d[1] = "Python dict"
print(d)

student = {"name": "Ajay", "age": 25, "city": "Bhopal"}

print(student.pop("city"))
print(student)

student = {
    "name": "Ajay",
    "age": 25,
    "city": "Bhopal"
}

removed_item = student.popitem()

print("Removed:", removed_item)
print("Remaining Dictionary:", student)


data = {
    "A": 10,
    "B": 20,
    "C": 30
}

while data:
    print(data.popitem())

print(data)


student = {
    "name": "Ajay",
    "age": 25,
    "city": "Bhopal"
}

del student["age"]

print(student)

student = {
    "name": "Ajay",
    "age": 25
}

del student

print(student)


student = {"name": "Ajay"}

student.clear()
print(student)

student = {
    "name": "Ajay",
    "age": 25,
    "city": "Bhopal"
}

print(student.keys())


student = {
    "name": "Ajay",
    "age": 25,
    "city": "Bhopal"
}

print(student.values())
print(list(student.values()))

student = {
    "name": "Ajay",
    "age": 25,
    "city": "Bhopal"
}

print(student.items())

student = {"name":"Ajay"}

student.update({"age":25})

print(student)

student = {'name':'Ajay','age':30}

student.update({"age":25})

print(student)

student = {'name':'Ajay','age':30}

student.update({"city":"Bhopal","phone":"99999"})

print(student)

student = {"name":"Ajay","age":25}

new_student = student.copy()

print(new_student)


student = {"name":"Ajay","age":25}

new_student = student.copy()

student.update({"address":"indore"})
print(new_student)
print(student)

square_dict = {}
for i in range(1, 6):
    square_dict[i] = i * i

print(square_dict)

square_dict = {i: i*i for i in range(1, 6)}
print(square_dict)

even_square = {i: i*i for i in range(1, 11) if i % 2 == 0}
print(even_square)

words = ["apple", "banana", "mango"]
length_dict = {word: len(word) for word in words}
print(length_dict)

numbers = [1, 2, 3, 4, 5]

result = {x: "Even" if x % 2 == 0 else "Odd" for x in numbers}
print(result)

keys = ["name", "age", "city"]
values = ["Ajay", 25, "Bhopal"]

my_dict = {keys[i]: values[i] for i in range(len(keys))}
print(my_dict)


text = "programming"

freq = {char: text.count(char) for char in text}
print(freq)

students = {
    101: {"name": "Ajay", "age": 25},
    102: {"name": "Rahul", "age": 23},
    103: {"name": "Priya", "age": 24}
}
print(students[101])

print(students[101]["name"])
print(students[101])
students[101]["age"] = 26
print(students[101])

print(students[101])
students[101]["city"] = "Bhopal"
print(students[101])

students = {
    101: {"name": "Ajay", "age": 25},
    102: {"name": "Rahul", "age": 23},
    103: {"name": "Priya", "age": 24}
}

print(students)
students[104] = {"name": "Karan", "age": 22}
print(students)


students = {
    101: {"name": "Ajay", "age": 25},
    102: {"name": "Rahul", "age": 23},
    103: {"name": "Priya", "age": 24}
}

for student_id, details in students.items():
    print("ID:", student_id)
    for key, value in details.items():
        print(key, ":", value)

students = {
    101: {"name": "Ajay", "age": 25},
    102: {"name": "Rahul", "age": 23},
    103: {"name": "Priya", "age": 24}
}
del students[101]["age"]
print(students[101])

logins = ["Ajay", "Ravi", "Ajay", "Aman", "Ajay", "Ravi"]

counter = {}

for user in logins:
    counter[user] = counter.get(user, 0) + 1

print(counter)

words = ["cat", "dog", "lion", "tiger", "ant"]

grouped = {}

for word in words:
    length = len(word)                  # Step 1: Find length of current word
    if length not in grouped:           # Step 2: Check if this length is already a key
        grouped[length] = []            # If not, create a new list for this length
    grouped[length].append(word)        # Step 3: Add word to the list for this length

print(grouped)


nums = [1, 2, 3, 1, 4, 5]

seen = {}

for num in nums:
    if num in seen:
        print(True)
        break
    seen[num] = True
else:
    print(False)

print(seen)

store1 = {'apple': 10, 'banana': 5, 'orange': 8}
store2 = {'banana': 7, 'orange': 2, 'grapes': 4}

# Solution
merged = store1.copy()  # start with first dict
for key, value in store2.items():
    merged[key] = merged.get(key, 0) + value

print(merged)
'''
for 