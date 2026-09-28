#26. Write a Java program to find the largest and smallest element of an array.

arr=[5,2,-3,6,4]

min=arr[0]
max=arr[0]
for i in arr:
    if i<min:
       min=i
    if i>max:
       max=i

print(min)
print(max)