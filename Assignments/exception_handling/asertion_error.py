try:
    age = 15
    assert age >= 18
except AssertionError:
    print("Age must be 18 or above!")