'''
7. Password Strength Checker
Intermediate
Concepts: Conditions, loops, functions, strings
Requirements
•	Accept a password from the user.
•	Check its length.
•	Check for uppercase and lowercase letters.
•	Check for digits and special characters.
•	Classify it as weak, medium, or strong according to your defined rules.
Bonus: Display suggestions to improve a weak password.

'''

password=input("Enter Password :- ")

upper = False
lower = False
digit = False
special = False

for char in password:
    if char.isalpha() and char==char.lower():
        lower=True
    elif char.isalpha() and char==char.upper():
        upper=True
    elif char.isdigit():
        digit=True
    else:
        special=True

def easy():
    print("\nweak Password........(minimum 8 charater is required........)")
    print("\nSuggestions to make your password stronger:")
    print("- Add an uppercase letter (A-Z).")
    print("- Add a lowercase letter (a-z).")
    print("- Include a number (0-9).")
    print("- Add a special character (@, #, !, etc.).")

def medium(lower,upper,digit,special):
    print("medium password.........")
    print("\nSuggestions to make your password stronger:")
    if not upper:
        print("- Add an uppercase letter (A-Z).")
    if not lower:
        print("- Add a lowercase letter (a-z).")
    if not digit:
        print("- Include a number (0-9).")
    if not special:
        print("- Add a special character (@, #, !, etc.).")

def hard():
    print("Strong Password............")



if len(password)<8:
    easy()
elif upper and lower and digit and special:
    hard()
else:
    medium(lower,upper,digit,special)
    



        




