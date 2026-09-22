n=int(input("enter a number : "))

match n:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("invalid")