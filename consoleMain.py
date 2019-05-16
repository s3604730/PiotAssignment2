from Database import Database
from Calendar import Calendar
from datetime import datetime

# stays idle if no message is sent from Reception Pi


class consoleMP:
    def __init__(self):
        with Database() as db:
            db.createTables()
        self.initialise()

    def initialise(self):
        print("1: Search a book")
        print("2: Borrow a book")
        print("3: Return a book")
        print("4: Logout")

        choice = int(input("Enter your choice"))
        print()
        if choice == "1":
            bookTitle = str(input("Input Book TItle"))
            self.searchBook(bookTitle)
        elif choice == "2":
            self.borrowBook()
        elif choice == "3":
            self.returnBook()
        elif choice == "4":
            self.logout()
        else:
            print("Invalid Input!")

    # searches the table for the specified book
    def searchBook(self, bookTitle):
        with Database() as db:
            db.searchBook(bookTitle)

    # takes the id of a book and returns a borrowing id if it's available
    def borrowBook(self):
        exit = False
        print("--- Borrow a book ---")
        bookID = input("Enter the ID of the book: ")
        with Database() as db:
            db.searchBook(bookID)
            choice = input("Do you want to borrow this book? \n Y/N")
            if choice == 'Y':
                while (exit != True):
                    borrowDate = datetime.date(datetime.now())
                    returnDate = borrowDate - datetime.timedelta(days=7)
                    LmsUserID = input("Please enter your user ID")
                    db.insertBorrowedBook(
                        bookID, LmsUserID.bookID, "borrowed", borrowDate, returnDate)
                    # creates an event for the return date
                    e = Calendar()
                    e.addEvent(borrowDate, returnDate, bookID)
                    if input("Do you want to borrow another book? \n Y/N") == "N":
                        exit = True
            else:
                self.borrowBook()

    # takes a borrowing id and returns the book
    def returnBook(self):
        print("--- Return a book ---")
        print("1. List your books")
        print("2. Return your book")
        print("3. Exit")
        choice = int(input("Enter your choice"))
        with Database() as db:
            if choice == "1":
                db.getBorrowedBook(self.returnUserID())
            if choice == "2":
                borrowedBookID = input("Enter your Borrowed Book ID")
                db.searchBorrowedBook(borrowedBookID)
                # should remove from table and add back to Books table
                e = Calendar()
                e.removeEvent()
            if choice == "3":
                self.initialise()

    def logout(self):
        # TODO
        '''sends logout message from MP to RP'''

    # get user name from reception pi through sockets
    def returnUserID(self, userName):
        with Database() as db:
            return db.getUserID(userName)
