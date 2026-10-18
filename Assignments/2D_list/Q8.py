#multiplication

arr1=[[1,2,3],[1,2,3],[1,2,3]]
arr2=[[1,2,3],[1,2,3],[1,2,3]]
result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(arr1)):
    for j in range(len(arr2)):
        ans=0
        for k in range(len(arr2)):
            ans+=arr1[i][k]*arr2[k][j]
            result[i][j]=ans
        
              

print(result)