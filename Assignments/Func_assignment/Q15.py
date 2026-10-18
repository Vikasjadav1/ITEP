# Find the ASCII/Unicode value of each character using ord().

s="infobeans"

def func(s):
    result={}

    for char in s:
        result[char]=ord(char)

    print(result)

func(s)