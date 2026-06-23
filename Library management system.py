class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True

    def issue_book(self):
        if self.available:
            self.available = False
            print("Book Issued")
        else:
            print("Book Not Available")

book1 = Book(101, "Python Basics")
book1.issue_book()