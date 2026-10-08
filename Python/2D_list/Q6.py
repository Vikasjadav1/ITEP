#reverse every row element

arr=[[1,2,3],[10,20,6],[7,8,9]]

for row in range(len(arr)):
    i=0
    j=len(arr[row])-1
    while(i<j):
        arr[row][i], arr[row][j] = arr[row][j], arr[row][i]
        i+=1
        j-=1

print(arr)