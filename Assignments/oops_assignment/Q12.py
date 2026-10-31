'''
 Write a Java program to create a class called "Dog" with a name and breed attribute. 
 Create two instances of the "Dog" class, set their attributes using the constructor 
 and modify the attributes using the setter methods and print the updated values.'''

class Dog:
    def __init__(self,name,breed):
        self.__name=name
        self.__breed=breed

    def set_name(self,name):
        self.__name=name
    
    def set_breed(self,breed):
        self.__breed=breed
    

    def display(self):
        print(f"Name {self.__name}")
        print(f"Breed {self.__breed}")   

obj1=Dog("puppy","vodaphone") 
obj1.display() 
obj1.set_name("jogi") 
print("after obj1 change") 
obj1.display()

obj2=Dog("hacker","pitbad")
obj2.display()
obj2.set_name("Hitter") 
print("after obj2 change") 
obj2.display()


