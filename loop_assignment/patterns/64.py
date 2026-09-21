num=1
for i in range(1,6):
     for j in range(i,5):
        print(" ",end="")

     for j in range(0,i):
          if(j==0 or j==i ):
               print("1 ",end="")
               
          else:
               num=num* (i-j)//j
               print(f"{num} ",end="")
     print()