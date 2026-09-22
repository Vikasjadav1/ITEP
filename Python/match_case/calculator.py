while(True):
    print("press 1 for addition")
    print("press 2 for substraction")
    print("press 3 for multiplication")
    print("press E/e for end")

    choice=input("enter choice :")

    match choice:
        case "1":
            a=int(input("enter a : "))
            b=int(input("enter b : "))
            print(f"addition : {a+b}")

        case "2":
            a=int(input("enter a : "))
            b=int(input("enter b : "))
            print(f"substraction : {a-b}")

        case "3":
            a=int(input("enter a : "))
            b=int(input("enter b : "))
            print(f"multiplication : {a*b}")

        case "E"|"e": 
            break  

        case _:
            print("invalid choice")

    