print("at the start")

try:
    a=int(input("enter 1st value"))
    b=int(input("enter 2nd value"))
    c=a/b
    print(f"result {c}")

except ZeroDivisionError as e:
    print("ZeroDivisionError Caught...")

except ArithmeticError as e:
    print("ArithmeticError Caught...")
    
except ValueError as e:
    print("ValueError Caught...")   


print("At the end....")