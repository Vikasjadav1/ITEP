people1=int(input("enter age of people 1 : "))
people2=int(input("enter age of people 2 : "))
people3=int(input("enter age of people 3 : "))

if(people1 > people2 and people1>people3):
    print("elder: people1")
elif(people2 > people1 and people2>people2):
    print("elder: people2")
else:
    print("elder: peolpe3")

if(people1 < people2 and people1<people3):
    print("younger: people1")
elif(people2 < people1 and people2<people2):
    print("younger: people2")
else:
    print("younger: peolpe3")
