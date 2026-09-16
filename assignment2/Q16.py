Physics=int(input("enter Physics marks : "))
chemistry=int(input("enter chemistry marks : "))
bio=int(input("enter bio marks : "))
math=int(input("enter math marks : "))
computer=int(input("enter computer marks : "))

percentage=(Physics+chemistry+math+bio+computer)/5

if percentage>=90:
    print("A")
elif percentage>=80:
    print("B")
elif percentage>=70:
    print("C")
elif percentage>=60:
    print("D")
elif percentage>=40:
    print("E")
else:
    print("F")