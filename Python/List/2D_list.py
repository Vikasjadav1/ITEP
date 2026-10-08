x=[[1,2,3],[4,5,6],[7,8,9]]
'''
for r in range(len(x)):
    for c in range(len(x[r])):
        print(x[r][c],end=" ")
    print()
'''
for row in x:
    for element in row:
        print(element,end=" ")
    print()
