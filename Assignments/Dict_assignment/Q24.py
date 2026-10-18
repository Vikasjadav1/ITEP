'''
Group a list of words according to their length.
    Example: ["cat", "apple", "dog", "mango"]
    Expected groups: 3 -> ["cat", "dog"], 5 -> ["apple", "mango"]
    '''

l=["cat", "apple", "dog", "mango"]
result={}

for i in l:
    result[len(i)]=[]

for elem in l:
    result[len(elem)].append(elem)

for key,value in result.items():
    print(f"{key} -> {value}")

