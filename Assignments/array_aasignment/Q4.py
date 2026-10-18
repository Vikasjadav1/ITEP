#Q.4 Write a program to sort the array

arr=[5,3,4,1,2,6]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            arr[i],arr[j]=arr[j],arr[i]
        

print(arr)