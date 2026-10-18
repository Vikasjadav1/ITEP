n=int(input("enter number : "))

for i in range(1,n+1):
    for j in range(1,n+1):
        
        if i==1 or j==1 or i==(n+1)//2:
            print("*",end="")
        else:
            print(" ",end="")
    print()