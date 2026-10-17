#Remove all digits from a string.
s="st8ri5ng99"
result=""

for char in s:
    if not char.isdigit():
        result+=char

print(result)
