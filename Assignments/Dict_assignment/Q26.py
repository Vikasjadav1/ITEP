#26. Find the second-largest distinct value in a dictionary.

numbers={
    "one":1,
    "two":7,
    "three":3,
    "four":8
}

max=0
ans=0
for key,value in numbers.items():
    if value>max:
        max=value

diffrence=0 
mindiff=max    
for value in numbers.values():
    diffrence=max-value
    if value!=max and mindiff>diffrence:
        mindiff=diffrence
        ans=value

print(ans)
