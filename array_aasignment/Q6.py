#Q.6 Sort the array of 0s , 1s and 2s.

arr=[1,1,1,2,2,0,0,1,1]

cz=0
co=0
ct=0

for i in arr:
    if i==0:
        cz+=1
    elif i==1:
        co+=1
    else:
        ct+=1

for i in range(cz):
    arr[i]=0

for i in range(cz,cz+co):
    arr[i]=1

for i in range(cz+co,cz+co+ct):
    arr[i]=2

print(arr)