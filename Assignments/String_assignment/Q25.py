#  Check whether a string contains only digits without using isdigit().

s="455544"
check=True
for char in s:
    ascii=ord(char)
    if ascii<48 or ascii>57:
        check=False
        break

if check:
    print("string contains only digits")
else:
    print("string not contains only digits")