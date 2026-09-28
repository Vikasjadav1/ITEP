#25. Write a Java program to reverse the element of an integer 1-D array. 


arr=[1,2,3,4,5,6,7,8,9]

low=0
high=len(arr)-1

while(low<high):
    arr[low],arr[high]=arr[high],arr[low]
    low+=1
    high-=1

print(arr)