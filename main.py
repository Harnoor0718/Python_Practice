class Library:
    def __init__(self, noBooks=0):
        self.noBooks = noBooks
        self.books = []
    
    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books) 
    
    def showInfo(self):
        print(f"The library has {self.noBooks} books")  
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook("Harry Potter")
l1.showInfo()
l1.addBook("Harry Potter 2")
l1.showInfo()
