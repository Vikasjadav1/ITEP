n=int(input("enter number : "))

for i in range(1,n+1):
   ans=1
   for j in range(1,n+1):
       if(j<=n-i):
           print(" ",end="")
       else:
           print(ans,end="")
           ans+=1
   print()