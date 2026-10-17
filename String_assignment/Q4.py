4. #Count uppercase letters, lowercase letters, digits, and special characters.

s="vikasJadav@#$123"
uc=0
lc=0
dc=0
sc=0

for char in s:
    ascii=ord(char)
    if ascii>=65 and ascii<=90:
        uc+=1
    elif ascii>=97 and ascii<=122:
        lc+=1
    elif ascii>=480 and ascii<=57:
        dc+=1
    else:
        sc+=1

print(f"Upper count :{uc}")
print(f"Lower count : {lc}")
print(f"Digit count : {dc}")
print(f"Special count : {sc}")    