n=int(input("enter number : "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==j and i<=(n//2)+1) or (j==(n//2)+1 and i>n//2) or (i<=n//2 and (i+j)%8==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()