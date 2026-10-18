a=int(input("enter number a : "))
b=int(input("enter number b : "))
choice=input("enter a choice (+,>,==)")

if choice=="+":
    print(f"addtion :{a+b}")
elif choice==">":
    if a>b:
        print(f"greater : {a}")
    else:
        print(f"greater : {b}")
elif choice=="=":
    if a==b:
        print("equal")
    else:
        print("not equal")
else:
    print("invalid choice")

