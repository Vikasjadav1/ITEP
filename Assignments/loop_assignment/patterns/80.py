n=int(input("enter number :"))

for i in range(1,n+1):
    for j in range(1,2*n):
        if j<=n-i or j>=n+i:
            print(" ",end="")
        else:
            if j==n-i+1 or j==n+i-1:
                print("*",end="")
            else:
                print("_",end="")
            
    print()   


for i in range(n-1,0,-1):
    for j in range(1,2*n):
        if j<=n-i or j>=n+i:
            print(" ",end="")
        else:
            if j==n-i+1 or j==n+i-1:
                print("*",end="")
            else:
                print("_",end="")
    print()             


