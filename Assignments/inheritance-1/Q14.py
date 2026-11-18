'''
14. Multiple Inheritance Example

Classes:

Father
Mother
Child(Father, Mother)

Access methods from both.

'''

class Father:
    def respect(self):
        print("always repect your father")

class Mother:
    def love(self):
        print("always love with mother")

class Child(Father,Mother):
    pass

obj=Child()
obj.respect()
obj.love()