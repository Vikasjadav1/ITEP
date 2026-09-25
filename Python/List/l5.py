l = [10,20,30,40,50,60,5,8,8,548]

l.append([500,600])
print(l)

l.extend([500,600])
print(l)


l[2:8:2] = ["A","B","C"]
print(l)