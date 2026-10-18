n=int(input("enter a number :"))

temp=n
last=temp%10

first=0
temp=n
divisor=1
while(temp>10):
    temp=temp//10
    divisor*=10

first=temp

middle=(n%divisor)//10

result=(last*divisor)+(middle*10)+first

   
print(result)




