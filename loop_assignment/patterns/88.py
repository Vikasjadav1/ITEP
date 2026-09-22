n=5
for i in range(n,0,-1):
    for space in range(5,i,-1):
        print(" ",end="")
    for j in range(1,2*i):
        if(j==1 or j==(2*i)-1 or i==n):
            print(j,end="")
        else:
            print("+",end="")
    print()