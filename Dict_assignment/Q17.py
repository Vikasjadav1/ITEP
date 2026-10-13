'''
Count the frequency of each number in a list.
    Example: [1, 2, 2, 3, 1, 2] -> {1: 2, 2: 3, 3: 1}
'''
l=[1, 2, 2, 3, 1, 2]
result={}
for elem in l:
    if elem in result:
        result[elem]=result[elem]+1
    else:
        result[elem]=1

print(result)