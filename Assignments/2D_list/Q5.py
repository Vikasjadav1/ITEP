#return row of miximum sum

arr=[[1,2,3],[10,20,6],[7,8,9]]
maxsum=0
ans=0
for i in range(len(arr)):
    sum=0
    for j in range(len(arr[i])):
        sum+=arr[i][j]
    if sum>maxsum:
        maxsum=sum
        ans=i

print(f"maximum sum row : {arr[ans]} , sum = {maxsum}")
        