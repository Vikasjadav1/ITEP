#Write a java program to implement selection sort algoritm
arr=[4,1,5,2,3]
size=len(arr)

for i in range(size):
    smallest=i
    for j in range(i+1,size):
        if arr[j]<arr[smallest]:
            smallest=j
    arr[i],arr[smallest]=arr[smallest],arr[i]


print(arr)