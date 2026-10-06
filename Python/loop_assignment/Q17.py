#  1 	2	 4	 7	 11	 16 	…… n terms

n=int(input("enter number : "))

term = 1
i=1
diffrence=1

while(i<=n):
    print(term)
    term=term+diffrence
    diffrence=diffrence+1
    i=i+1
    
