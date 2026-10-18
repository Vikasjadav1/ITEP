# …... -6	-3	0	3	6	9	……. n terms [where n is divisible by 3]	

n=int(input("enter number : "))

if n%3==0:
    for i in range(-n,n+1,+3):
        print(i)

