n=int(input("enter number : "))


for i in range(n,0,-1):
   for j in range(1,n+1):
       if(j<=n-i):
           print(" ",end="")
       else:
           print(j,end="")
               
   print()