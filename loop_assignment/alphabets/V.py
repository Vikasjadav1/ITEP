n=4

for i in range(1,n+1):
    for j in range(1,2*n):
        if i==j or (i+j)%8==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()