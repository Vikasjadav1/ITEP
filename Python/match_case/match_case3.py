per=float(input("enter student percentage : "))

match per:
    case per if per>90: print("A grade")
    case per if per>=80 and per<90: print("B grade")
    case per if per>=60 and per<80: print("C grade")
    case _:print("D grade")