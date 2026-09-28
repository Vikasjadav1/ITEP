#23. Write a Java program to find the sum and average of one dimensional integer array.


arr=[1,2,3,4,5,6,7,8,9]
sum=0
avg=0
for i in arr:
    sum+=i
    avg=sum/len(arr) 

print(f"sum : {sum}")
print(f"average : {avg}")