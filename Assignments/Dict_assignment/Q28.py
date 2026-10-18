'''
28. Create a new dictionary containing only entries whose values are greater
    than or equal to a given threshold. Do not modify the dictionary while
    iterating over it.
    '''

d = {'a': 10, 'b': 25, 'c': 5, 'd': 30}
threshold = 20
result={}
for key in d.keys():
    if d[key]>=threshold:
        result[key]=d[key]

print(result)