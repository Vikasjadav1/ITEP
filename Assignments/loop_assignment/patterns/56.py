for i in range(1,10):
    for j in range(1,10): 
        if (i==5 or j==5) or (i<=5 and j==1) or (j>=5 and i==1) or (j<=5 and i==9) or (j==9 and i>=5) :
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()