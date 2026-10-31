'''
Write a Java program to create a class called "Book" with attributes for title, author, and ISBN, and methods to add and remove books from a collection.
'''


class Book:
    books=[]
    def add_book(self,title,author,ISBN):
        self.__title=title
        self.__author=author
        self.__ISBN=ISBN
        
        Book.books.append(self)
        print("Book added successfull................")

    def remove(self):
        if self in Book.books:
            del self
        else:
            print("book not exist...")

    def display(self):
        if len(Book.books) == 0:
            print("No books available...")
        else:
            print("\n------ Books Collection ------")

            for book in Book.books:
                print(f"Title: {book.__title}")
                print(f"Author: {book.__author}")
                print(f"ISBN: {book.__ISBN}")
                print("-----------------------------")

obj1=Book()
obj2=Book()
obj1.add_book("vikas","vikas",200)
obj2.add_book("vikadfddfvs","vfgfikas",2005)
obj1.remove()
obj1.display()








