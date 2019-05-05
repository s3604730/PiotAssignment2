

class book:
    def __init__(self,bookName,bookID,authorName,ISBN):
        self.bookName = bookName
        self.bookID = bookID
        self.authorName = authorName
        self.ISBN = ISBN

    def getBookName(self):
        return self.bookName

    def getBookID(self):
        return self.bookID

    def getAuthorName(self):
        return self.authorName

    def getISBN(self):
        return self.ISBN