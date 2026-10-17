s="a3b2c4d1"
result=""
word=""
for char in s:
    if char.isdigit():
        result+=word*int(char)
        word=""
    else:
        word+=char
print(result)
    
     
