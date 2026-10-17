'''
Convert lowercase characters to uppercase without using upper().
  s = "inDor434e"  => "INDOR434E"
  '''

s = "inDor434e"
result=''
for char in s:
    if char.islower():
        result+=chr(ord(char)-32)
    else:
        result+=char

print(result)

