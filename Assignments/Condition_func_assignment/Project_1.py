'''
Concepts: if-elif-else, while, functions
Requirements
•	Display a menu for addition, subtraction, multiplication, division, and modulus.
•	Take two numbers from the user.
•	Use separate functions for each operation.
•	Handle division by zero.
•	Repeat until the user selects Exit.
Bonus: Add power and floor division operations.
'''

print("===========Smart Calculator===========")
print("1. Addition (+)")
print("2. Substraction (+)")
print("3. Multiplication (+)")
print("4. Divition (+)")
print("5. Modulus (+)")
print("6. Power (^)")
print("7. Floor Division (//)")
print("8. Exit (+)")

def add(a,b):
    return a+b

def substraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def modulus(a,b):
    return a%b

def power(a,b):
    return a**b

def floor_division(a,b):
    return a//b


while(True):
    choice=input("Enter your choice : ")
    if(choice=="1"):
        a=int(input("enter first number : "))
        b=int(input("enter second number : "))
        result=add(a,b)
        print(f"Addition : {result}")
    elif(choice=="2"):
        a=int(input("enter first number : "))
        b=int(input("enter second number : "))
        result=substraction(a,b)
        print(f"substraction : {result}")
    elif(choice=="3"):
        a=int(input("enter first number : "))
        b=int(input("enter second number : "))
        result=multiplication(a,b)
        print(f"multiplication : {result}")
    elif(choice=="4"):
        a=int(input("enter first number : "))
        b=int(input("enter second number : "))
        if(b==0):
            print("Division by zero is not allowed.")
        result=division(a,b)
        print(f"division : {result}")
    elif(choice=="5"):
        a=int(input("enter first number : "))
        b=int(input("enter second number : "))
        result=modulus(a,b)
        print(f"modulus : {result}")
    elif(choice=="6"):
        a=int(input("enter first number : "))
        b=int(input("enter second number : "))
        result=power(a,b)
        print(f"power : {result}")
    elif(choice=="7"):
        a=int(input("enter first number : "))
        b=int(input("enter second number : "))
        result=floor_division(a,b)
        print(f"floor_division : {result}")
    elif(choice=="8"):
        break
    else:
        print("Enter valid operation...........")
