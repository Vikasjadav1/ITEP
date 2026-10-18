#Sort a dictionary by its values in ascending order.

d = {'a': 30, 'b': 10, 'c': 20}
items=list(d.items())

for i in range(len(items)):
    for j in range(i+1,len(items)):
        if items[i][1]>items[j][1]:
            items[i],items[j]=items[j],items[i]

result={}
for key,value in items:
    result[key]=value
print(result)