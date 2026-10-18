n=5

for i in range(1,n+1):
    for j in range(1,2*n):
        if j==1 or j==2*n-1 or i==j or (i+j)%10==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()