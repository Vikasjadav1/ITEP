print("at the start......")

a = int(input("Enter 1st value.."))
b = int(input("Enter 2nd value.."))

try:
    c=a/b
    print(f"result : {c}")
except ZeroDivisionError as e:
    print(e)

print("at the end...")