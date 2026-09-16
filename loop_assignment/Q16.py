# …... -6	-3	0	3	6	9	……. n terms [where n is even]	

n=int(input("enter number : "))

i=1
term=-6

while(i<=n):
    print(term, end=" ")
    term=term+3
    i=i+1