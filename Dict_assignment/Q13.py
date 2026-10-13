#Check whether a dictionary is empty.

marks={
    "maths":60,
    "bio":90,
    "chemistry":40
}
ans=False
for key in marks.keys():
    if key:
        ans=True

if ans:
    print("dictionary is not empty")
else:
    print("dictionary is empty")
        