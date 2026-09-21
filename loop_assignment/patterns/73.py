n=int(input("enter number : "))


for i in range(n,0,-1):
    a=1
    for j in range(i,6):
        print(" ",end="")

    for j in range(1,i*2):
        if j==1 or j==i or i==n:
            print(a,end=" ")
            a+=1
        else:
            print(" ",end="")
            
    print()
     
