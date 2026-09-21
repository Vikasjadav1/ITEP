A=int(input("enter A marks : "))
B=int(input("enter B marks : "))
C=int(input("enter C marks : "))
D=int(input("enter D marks : "))
E=int(input("enter E marks : "))

per=(A+B+C+D+E)/5

if(per>90):
    print("merit")
elif(per>=60 and per<=90):
    print("A")
elif(per>=59 and per<=60):
    print("B")
elif(per>=40 and per<50):
    print("c")
else:
    print("D")