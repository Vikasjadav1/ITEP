'''
5. Number Guessing Game
Beginner
Concepts: while, if-else, functions
Requirements
•	Generate a random number from 1 to 100.
•	Ask the player to guess the number.
•	Display “Too high” or “Too low.”
•	Limit the player to seven attempts.
•	Display the final result.
Bonus: Add easy, medium, and hard difficulty levels with different attempt limits.
'''
import random
ran=random.randint(1, 100)

def easy(ran):
    attempt=10
    while(attempt>0):
        num=int(input("enter number : "))
        if num==ran:
            print("Win...................................")
            break
        elif num>ran:
            attempt-=1
            print(f"Too high ....... {attempt} reamaining")
        else:
            attempt-=1
            print(f"To low ....... {attempt} reamaining")

def meduim(ran):
    attempt=7
    while(attempt>0):
        num=int(input("enter number : "))
        if num==ran:
            print("Win...................................")
            break
        elif num>ran:
            attempt-=1
            print(f"Too high ....... {attempt} reamaining")
        else:
            attempt-=1
            print(f"To low ....... {attempt} reamaining")

def hard(ran):
    attempt=5
    while(attempt>0):
        num=int(input("enter number : "))
        if num==ran:
            print("Win...................................")
            break
        elif num>ran:
            attempt-=1
            print(f"Too high ....... {attempt} reamaining")
        else:
            attempt-=1
            print(f"To low ....... {attempt} reamaining")

print("Number Guessing Game")
print("=====================Levels=====================")
print("1.Easy (10-chance)")
print("2.Medium (7-chance)")
print("3.Hard (5-chance)")
level=int(input("choose level : "))


while(True):
    if level==1:
        easy(ran)
        choice=input("Do you want to play again : (y/n)")
        if(choice=='y'):
            easy(ran)
        else:
            break
    elif level==2:
        medium(ran)
        choice=input("Do you want to play again : (y/n)")
        if(choice=='y'):
            medium(ran)
        else:
            break
    elif level==3:
        hard(ran)
        choice=input("Do you want to play again : (y/n)")
        if(choice=='y'):
            hard(ran)
        else:
            break
    else:
        print("invalid")
    



