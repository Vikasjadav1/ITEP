age=int(input("enter age : "))
emp=input("enter age sex ( M or F ) : ").lower()
marital_status=input("marital status(y/n)").lower()

if emp=="f":
    print("she will work only in urban areas")
elif (emp=="m" and (age>20 and age<40)):
    print("he may work in anywhere")
elif (emp=="m" and (age>40 and age<60)):
    print("he will work in urban areas only")
else:
    print("ERROR")

