

class book:
    def __init__(self,__bookName,__bookID,__authorName,__ISBN):
        self.__bookName = __bookName
        self.__bookID = __bookID
        self.__authorName = __authorName
        self.__ISBN = __ISBN

    def getBookName(self):
        return self.bookName

    def getBookID(self):
        return self.bookID

    def getAuthorName(self):
        return self.authorName

    def getISBN(self):
        return self.ISBN