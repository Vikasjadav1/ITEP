class InvalidVoterError(Exception):
    pass

age=int(input("enter age : "))

try:
    if age<18:
        raise InvalidVoterError()
    else:
        print("thank you for voting")

except InvalidVoterError as e:
    print("age must be greater than 18")

finally:
    print("thank you ..")