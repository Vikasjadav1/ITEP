'''
s={1,2,3}
for i in s:
    print(i)
'''
s1={1,2,3,4}
s2={1,2,3,4,5}
print(s1|s2)#union
print(s1.union(s2))#union
print(s1&s2)#intersection
print(s1.intersection(s2))#intersection
print(s1-s2)#diffrence
print(s1^s2)#symantic diffrence
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.update(s2))
print(s1.intersection_update(s2))



