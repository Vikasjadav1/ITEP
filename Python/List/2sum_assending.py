arr=[2,7,11,15]
target=9
i=0
j=len(arr)-1
result=[]
sum=0

while(i<j):
    sum=arr[i]+arr[j]
    if sum==target:
        result.extend([i,j])
        break
    elif sum>target:
        j-=1
    else:
        i+=1

print(result)