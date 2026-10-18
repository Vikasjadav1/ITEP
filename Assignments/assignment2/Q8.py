classes_held=int(input("classes held : "))
classes_attended=int(input("classes attended : "))
medical_cause=input("medical cause (y/n) : ").lower()

percentage=(classes_attended/classes_held)*100

if percentage>75:
    print("allowed")
elif medical_cause=="y":
    print("allowed")
else:
    print("not allowed")