try:
    a=int(input("enter integer number...."))
    print(f"a : {a}")
except ValueError as e:
    print("only interger value is allowed....")
