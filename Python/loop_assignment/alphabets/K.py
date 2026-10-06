n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or (j==2 and (i+j)%2==0) or (j==3 and (i+j)%4==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()