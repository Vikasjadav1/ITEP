class Library:
    total_books=0
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.status=True
        Library.total_books+=1

    def issue_book(self):
        if self.status==True:
            self.status=False
            print(self.title , "book issued successfully")
        else:
            print(self.title , "book is already issued")

    def return_book(self):
        if self.status==False:
            self.status=True
            print(self.title,"book return successfully")
        else:
            print(self.title,"book already available")

    def availability(self):
        print(f"Book id  : {self.book_id}")
        print(f"title : {self.title}")
        print(f"author : {self.author}")

        if self.status==True:
            print("status : Available.....")
        else:
            print("status : Issued.....")    

book1=Library(101,"abc","king2")
book2=Library(102,"abcd","king1")
book1.issue_book()
book2.issue_book()
book2.issue_book()
book2.return_book()
book2.return_book()
book1.availability()
book2.availability()

