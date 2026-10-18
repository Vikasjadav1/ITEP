
'''21. Combine two dictionaries by adding the values of common keys.
    Example: {'a': 10, 'b': 20} and {'b': 5, 'c': 7}
    Expected: {'a': 10, 'b': 25, 'c': 7}
'''
a={'a': 10, 'b': 20}
b={'b': 5, 'c': 7}
'''
for key in b.keys():
    if key in a:
        a[key]+=b[key]
    else:
        a[key]=b[key]
'''

for key in b.keys():
    a[key]=a.get(key,0)+b[key]

print(a)