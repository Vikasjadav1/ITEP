n=int(input("enter number : "))

char=ord("E")
for i in range(n,0,-1):
   if i%2==0:
       for j in range(1,i+1):
           print(j,end="")
       print()
   else:
        for j in range(i, 0, -1):
            print(j, end="")
        print()