target=int(input("enter target :"))

l=[1,2,3,26,5,82,2,4,5]

result=[]

for i in range(len(l)):
     if target==l[i]:
         result.append(i)
        
if result!=0:
    s="element found"
    for element in result:
        s=s+" "+str(element)
    print(s)
else:
    print("element not found")
