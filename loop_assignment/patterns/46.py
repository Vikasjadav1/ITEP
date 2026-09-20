n=int(input("enter number :"))

for i in range(1,n+1):
    a=1
    for j in range(1,n+1):
        if j<=n-i:
            print(" ",end="")
        else:
            print(a,end="")
            a+=1
    print()