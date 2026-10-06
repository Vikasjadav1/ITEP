n=int(input("enter number : "))


for i in range(n,0,-1):
    char=ord("A")
    for j in range(1,i+1):
            print(chr(char),end="")
            char+=1
    print()