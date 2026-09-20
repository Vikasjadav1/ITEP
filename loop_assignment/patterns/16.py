n=int(input("enter number : "))


char=ord("a")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(char), end="")
        char+=1
    print()   