l=["apple","ant","banana","cat","chery"]

result={}

for str in l:
    key=str[0]
    if key in result:
        result[key].append(str)
    else:
        result[key]=[]
        result[key].append(str)

print(result)