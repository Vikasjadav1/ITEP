try:
    student = {"name": "Vikas", "age": 22}
    print(student["city"])
except KeyError:
    print("Key not found!")