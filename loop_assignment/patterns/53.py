n=int(input("enter number :"))

for i in range(1,n+1):
    for j in range(1,2*n):
        if j<=n-i or j>=n+i:
            print(" ",end="")
        else:
            if(j==5):
                print("#",end="")
            else:
                print("*",end="")
    print()            


