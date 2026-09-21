n=int(input("enter number :"))

for i in range(n,0,-1):
    a=1
    for j in range(1,2*n):
        if j<=n-i or j>=n+i:
            print(" ",end="")
        else:
            print(a,end="")
            a+=1
    print()            


