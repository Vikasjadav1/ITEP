arr=[2,7,11,15]

i=0
j=len(arr)-1
result=[]
sum=0
while(i<j):
    sum=arr[i]+arr[j]
    if sum==target:
        result