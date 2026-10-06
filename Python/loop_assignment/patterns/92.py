for i in range(1,8):
    for j in range(1,7):
        if ((j==5 and i%2!=0) or (i==j) or (i==2 and j==6) or (i==7 and j==1) or ((i>4 and i<7) and (i+j==9))):
            print("*",end="")
        else:
            print(" ",end="")
    print()