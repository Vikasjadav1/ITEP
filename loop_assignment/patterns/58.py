n=int(input("enter number : "))

for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    
    for j in range(1,(2*n)-(2*i)+1,+1):
        print(" ",end="")

    for j in range(1,i+1):
        print("*",end="")
    print()
