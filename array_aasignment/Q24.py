# 24. Write a Java program to swap first and last element of an integer 1-d array.

arr=[1,2,3,4,5,6,7,8,9]

first=0
last=len(arr)-1

arr[first],arr[last]=arr[last],arr[first]

print(arr)