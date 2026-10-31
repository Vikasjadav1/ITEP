'''
Write a Java program to create a class called "Person" with a name and age attribute. Create two instances of the "Person" class, set their attributes using the constructor, and print their name and age.
'''
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def display(self):
        print(f"name {self.__name}")
        print(f"age {self.__age}")

obj1=Person("vikas",20)
obj2=Person("Ram",26)
obj1.display()
obj2.display()
