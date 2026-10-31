'''
11. Write a Java program to create a class called "Library" 
with a collection of books and methods to add and remove books.
'''

class Library:
    books=[]

    def add_book(self,title,author):
        Library.books.append({
            "title":title,
            "author":author
        })

    def remove(self,title):
        for book in Library.books:
            if book["title"]==title:
                Library.books.remove(book)
                print("Book removed successfully")

    

obj1=Library()
obj2=Library()
obj1.add_book("pk1","vikarm1")
obj2.add_book("pk2","vikarm2")

obj1.remove("pk1")
print(Library.books)

