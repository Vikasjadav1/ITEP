#transpose the matrix
arr=[[1,2,3],[4,5,6],[7,8,9]]
for row in range(len(arr)):
    for col in range(len(arr[row])):
        print(arr[col][row],end=" ")
    print()

