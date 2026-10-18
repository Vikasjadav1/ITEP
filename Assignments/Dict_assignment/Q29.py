'''29. Given two dictionaries, return the keys whose values are equal in both.'''

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'a': 10, 'b': 50, 'c': 30}

l1=len(d1)
l2=len(d2)
ans=[]
if l1>=l2:
    for key in d2.keys():
        if key in d1 and d1[key]==d2[key]:
            ans.append(key)
else:
    for key in d1.keys():
        if key in d2 and d1[key]==d2[key]:
            ans.append(key)

print(ans)


