print("At the start..")

try:
  a = int(input("Enter 1st value.."))
  b = int(input("Enter 2nd value..")) # ValueError

  c = a / b   # ZeroDivisionError
  print(f"Result : {c}")

except ValueError as e:
    print(f"type {type(e)}")
    print(f"class : {e.__class__}")
    print(f"message : {e.__class__.__name__}")

except ZeroDivisionError as e:
  print(e)  
  
print("At the end...")

