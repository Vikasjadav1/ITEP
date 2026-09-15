num=int(input("enter a number : "))

reverse=0


lastnumber1=num%10
reverse = reverse * 10 + lastnumber1
num=num//10

lastnumber2=num%10
reverse = reverse * 10 + lastnumber2
num=num//10
 
lastnumber3=num%10
reverse = reverse * 10 + lastnumber3
num=num//10

lastnumber4=num%10
reverse = reverse * 10 + lastnumber4
num=num//10



print(reverse)