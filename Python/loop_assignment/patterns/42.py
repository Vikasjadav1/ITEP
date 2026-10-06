n=int(input("enter number : "))


for i in range(n,0,-1):
   char=ord("A")
   for j in range(1,n+1):
       if(j<=n-i):
           print(" ",end="")
       else:
           if(i==4 and j==3) or (i==4 and j==4) or (i==3 and j==4):
               print("_",end="")
           else:
               print(chr(char),end="")
           char+=1  
   print()