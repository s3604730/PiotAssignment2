
class book:
    def __init__(self,__bookName,__bookID,__authorName,__ISBN):
        self.__bookName = __bookName
        self.__bookID = __bookID
        self.__authorName = __authorName
        self.__ISBN = __ISBN

    def getBookName(self):
        """
        Return bookName
        """
        return self.bookName

    def getBookID(self):
        """
        Return bookID
        """
        return self.bookID

    def getAuthorName(self):
        """
        Return authorName
        """
        return self.authorName

    def getISBN(self):
        """
        Return ISBN
        """
        return self.ISBN