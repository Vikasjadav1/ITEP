n=int(input("enter number : "))


char=ord("a")
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i==3 and j==2) or (i==4 and j==2) or (i==4 and j==3):
             print("@",end="")
        else:
            print("*",end="")
    print()