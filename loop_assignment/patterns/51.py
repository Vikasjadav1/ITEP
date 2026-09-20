n=int(input("enter number :"))

for i in range(1,n+1):
    char=65
    for j in range(1,2*n):
        if j<=n-i or j>=n+i:
            print(" ",end="")
        else:
            print(chr(char),end="")
            char+=1
    print()            