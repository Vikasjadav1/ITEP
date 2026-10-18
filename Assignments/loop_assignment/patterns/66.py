n=int(input("enter number : "))


for i in range(1,n+1):
    char=97
    for j in range(1,i+1):
        if i==n or j==1 or j==i:
            print(chr(char),end=" ")
        else:
            print(" ",end="")
        char+=1
    print()