n=int(input("enter number : "))

a=5
for i in range(1,n+1):
   for j in range(1,n+1):
       if(j<=n-i):
           print(" ",end="")
       else:
           print(a,end="")
   a-=1
   print()