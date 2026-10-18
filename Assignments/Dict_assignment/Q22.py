#22. Find the common keys between two dictionaries.

a={'a': 10, 'b': 20}
b={'b': 5, 'c': 7}

l=[]

for key in b.keys():
    if key in a:
        l.append(key)

print(l)