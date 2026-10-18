n=int(input("enter  a number : "))

A=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(A,end=" ")
        A += 1

    print()

    