l=[1,2,3,4,5]

even=0
odd=0

for element in l:
    if element%2==0:
        even+=element
    else:
        odd+=element

print(f"sum of even numbers : {even}")
print(f"sum of odd numbers : {odd}")