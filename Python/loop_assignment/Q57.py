#57) WAP to print all the prime numbers between two entered numbers

a=int(input("enter a : "))
b=int(input("enter b : "))

for i in range(a,b+1):  
  if i > 1 :
    for j in range(2,(i//2)+1):
        if(i%j==0):
            break
    else:
        print(i)
    