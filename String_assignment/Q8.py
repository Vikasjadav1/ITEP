#8. Remove all spaces from a string.

s="vik k a s"
s=list(s)
result=""
for char in s:
    if char==" ":
        continue
    else:
        result+=char

print(result)
