'''
Create a class Book with fields: title, author, and price.
Use setters to assign values and a method to print book details.'''

class Book:
    def set_title(self,title):
        self.__title=title

    def set_author(self,author):
        self.__author=author
    
    def set_price(self,price):
        self.__price=price

    def display(self):
        print(f"title {self.__title}")
        print(f"author {self.__author}")
        print(f"pricev {self.__price}")

obj=Book()
obj.set_title("slack wars")
obj.set_author("djn ckf")
obj.set_price("548")
obj.display()
