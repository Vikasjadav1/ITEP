# 46) WAP to find out the sum of first and last digit of a user entered number 

n=int(input("enter  a number : "))

sum=0

last=n%10
first=n

while first>=10:
    first=first//10

sum=first+last
print(f"sum of first and last digit of a user entered number : {sum}")
    