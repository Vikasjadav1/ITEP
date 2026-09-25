for i in range(1,6):
    for j in range(1,10):
        if j==1 or j==9 or ((i+j)%6==0 and j<=5) or (i==2 and j==6) or (i==3 and j==7) or (i==4 and j==8):
            print("*",end="")
        else:
            print(" ",end="")
    print()