# 20. Remove duplicate characters while preserving their original order.
# Example: "programming" → "progamin"

s="programming"
result=""

for char in s:
    if char not in result:
        result+=char
print(result)

