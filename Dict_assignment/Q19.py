'''
Find all duplicate elements in a list and their frequencies.
'''
l=[1,2,2,2,3,4,5,5,6,7,7,7,7]
result={}
for elem in l:
    if elem in result:
        result[elem]=result[elem]+1
    else:
        result[elem]=1

for key in list(result.keys()):
    if result[key]==1:
        del result[key]
print(result)

#RuntimeError: dictionary changed size during iteration
