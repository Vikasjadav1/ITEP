s1=frozenset((1,2,3,4))
s2=frozenset((1,2,3,5))

print(s1|s2)
print(s1&s2)
print(s1-s2)
print(s1^s2)

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))

# s1.update(s2)   -----> we cant do it bcz frozenset is immutable
# print(s1)