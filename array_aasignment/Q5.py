#Q.5 Find the kth largest and kth smallest element in array.


arr=[5,3,4,1,2,6]
k=int(input("enter kth position : "))

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            arr[i],arr[j]=arr[j],arr[i]
   


print(f"kth smallest element {arr[k-1]}")
print(f"kth largest element {arr[len(arr)-k]}")

    
    
        
