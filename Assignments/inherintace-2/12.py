# 12. Authentication System
# Problem Statement

# Users can login using multiple methods.

# Create:

# abstract class Authentication

# Child:

# OTPAuth
# GoogleAuth
# FingerprintAuth


from abc import ABC, abstractmethod
import random

class Authentication(ABC):

    @abstractmethod
    def login(self):
        pass

class OTPAuth(Authentication):

    def login(self):
        otp = input("Enter OTP: ")

        if otp == "1234":
            print("OTP Login Successful!")
        else:
            print("Invalid OTP!")



class GoogleAuth(Authentication):

    def login(self):
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        if email == "user@gmail.com" and password == "12345":

            print("Email and Password Correct!")

            otp = random.randint(1000, 9999)

            print("Your OTP is:", otp)

            user_otp = int(input("Enter OTP: "))

            if user_otp == otp:
                print("Google Login Successful!")
            else:
                print("Invalid OTP!")

        else:
            print("Incorrect Email or Password!")



class FingerprintAuth(Authentication):

    def login(self):
            print("Fingerprint Login Successful!")


print("1. OTP Authentication")
print("2. Google Authentication")
print("3. Fingerprint Authentication")

choice = int(input("Enter your choice: "))

if choice == 1:
    auth = OTPAuth()

elif choice == 2:
    auth = GoogleAuth()

elif choice == 3:
    auth = FingerprintAuth()

else:
    print("Invalid Choice!")
    exit()

auth.login()