#33. Write a java program to impelment binary search algorithm

arr=[-1,0,3,4,5,9,12]
target=int(input("enter target : "))

st=0
end=len(arr)-1

while(st<=end):
    mid=(st+end)//2
    if(target>arr[mid]):
        st=mid+1
    elif(target<arr[mid]):
        end=mid-1
    else:
        print(f"element found at index : {mid}")    
        break
else:
    print("element not found")