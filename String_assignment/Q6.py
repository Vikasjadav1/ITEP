#6. Find the length of a string without using len()

s="infobeans"
length=0

for char in s:
    if char:
        length+=1

print(length)