# 19. Count the frequency of every character using a dictionary.
# Example: "hello" → {'h': 1, 'e': 1, 'l': 2, 'o': 1}

s="hello"
result={}
for char in s:
    if char in result:
        result[char]=result[char]+1
    else:
        result[char]=1

print(result)