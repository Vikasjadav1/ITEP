#Write a java progrtam to implement insertion sort algorithm 

arr=[4,1,5,2,3]

for i in range(1,len(arr)):
    cur=arr[i]
    prev=i-1
    
    while(prev>=0 and arr[prev]>cur):
        arr[prev+1]=arr[prev]
        prev-=1
    
    arr[prev+1]=cur


print(arr) 