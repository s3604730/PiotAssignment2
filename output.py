class Output:
    def __init__(self):
        pass

    def displayBook(self, row):
        print("Book ID: ", row[0])
        print("Title ", row[1])
        print("Author: ", row[2])
        print("Published Date: ", row[3])

    def displayBorrowedBook(self, row):
        print("Book Borrowed ID: ", row[0])
        print("User ID: ", row[1])
        print("Book ID: ", row[2])
        print("Borrowed Date: ", row[4])
        print("Returned Date: ", row[5])
