n=int(input("enter number : "))

for i in range(1,n+1):
    for j in range(1,4):
        if j==1 or j==3 or (j == 2 and (i + j)%3  == 0) :
            print("*",end="  ")
        else:
            print(" ",end="  ")
    print()
