#Suppose a one-dimensional array AR containing integers is arranged in ascending order. Write a java program to search for an integer from AR with the help of Binary search method,

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