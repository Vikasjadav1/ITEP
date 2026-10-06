n=int(input("enter number : "))


for i in range(1,n+1):
   for j in range(1,n+1):
       if(j<=n-i):
           print(" ",end="")
       else:
           if (i==3 and j==4) or (i==4 and j==3) or (i==4 and j==4):
                 print("@",end="")
           else:
                 print("1",end="")
           
   print()