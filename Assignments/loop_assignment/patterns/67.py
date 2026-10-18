n=int(input("enter number : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        if j==1:
            print("1 ",end="")
        elif j==i:
            if j%2!=0:
                print("1 ",end="")
            else:
                print("0 ",end="")
        elif i==n:
            if j%2!=0:
                print("1 ",end="")
            else:
                print("0 ",end="")
        else:
            print(" ",end="")
    print() 