# 28) 1	2	3	4	 Hello	6	7	8	9	Hello	11	12 ….

n=int(input("enter a number : "))

for i in range(1,n+1):
    if i%5==0:
        print("Hello" , end=" ")
    else:
        print(i , end=" ")