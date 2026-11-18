'''
9. Library Management

Parent:

LibraryItem

Derived:

Book
Magazine
Newspaper

Implement borrowing system.
'''

from abc import ABC,abstractmethod
class LibraryItem(ABC):
    @abstractmethod
    def borrowing(self):
        pass


class Book(LibraryItem):
    def borrowing(self):
        print("Book borrowed...........")

class Magazine(LibraryItem):
    def borrowing(self):
        print("Magazine borrowed...........")

class Newspaper(LibraryItem):
    def borrowing(self):
        print("Newspaper borrowed...........")
        

obj=Book()
obj.borrowing()

print("-------------------------------------------")


obj=Magazine()
obj.borrowing()

print("-------------------------------------------")


obj=Newspaper()
obj.borrowing()

print("-------------------------------------------")