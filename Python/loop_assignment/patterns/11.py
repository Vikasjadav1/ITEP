n=int(input("enter  a number : "))


for i in range(1,n+1):
    char=97
    for j in range(1,i+1):
        print(chr(char),end=" ")
        char += 1

    print()

    