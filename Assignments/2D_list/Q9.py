#swap min or max row sum

arr=[[1,2,3],[10,20,6],[7,8,9]]
max=0
min=0
m=0
n=0
for i in range(len(arr)):
    sum=0
    for j in range(len(arr[i])):
        sum+=arr[i][j]
    if sum>max:
        max=sum
        m=i
    if i==0:
        min=sum
        n=i
    elif min>sum:
        min=sum
        n=i

arr[n],arr[m]=arr[m],arr[n]
print(arr)