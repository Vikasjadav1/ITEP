'''Find the key associated with the largest value in a dictionary.'''

marks={
    "maths":60,
    "bio":90,
    "chemistry":40
}
max=0
ans=""
for key,value in marks.items():
    if value>max:
        max=value
        ans=key

print(ans)
