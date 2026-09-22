n=int(input("enter a number : "))
match n:
    case n if n>0: print("positive")
    case n if n<0: print("negative")
    case n if n==0: print("zero")