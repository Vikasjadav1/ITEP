s1={1,2,3,}
s2={1,2,3,4}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
# print(s1.difference(s2))

s1.symmetric_difference_update(s2)
print(s1)


