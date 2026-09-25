for i in range(1,6):
    for j in range(1,8):
        if(i==1 and j<7) or (j==1 and i<5) or (j==6 and i<5) or (i==4 and j<7) or (i==3 and j==5) or (i==5 and j==7):
            print("*",end="")
        else:
            print(" ",end="")
    print()