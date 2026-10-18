n=int(input("enter  a number : "))
count=0
lastnumber=0
reverse=0
while n!=0:
    lastnumber=n%10
    count+=1
    n=n//10
    
print(f"count of digit : {count}")