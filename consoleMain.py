#!/usr/bin/env python3
from database import Database
from Calendar import Calendar
from datetime import datetime, timedelta
from output import Output
from SocketPi.MasterPiSocket import MasterPiSocket
import os
from SocketPi.ReceptionPiSocket import ReceptionPiSocket
path = os.path.abspath(os.path.dirname(__file__))
os.chdir(path)
import time

class consoleMP:
    """
    This class acts as the Master Pi console controller
    The console includes the functions.
        - Main menu
        - Search book
        - Borrow book
        - Return book
        - Log out
    """

    def __init__(self):
        self.db = Database()
        self.output = Output()
        self.initialise()

    def initialise(self):
        """
        This main menu function is automatically called after a user login 
        then receive the current username from the socket 
        and return userID from LMSuserID table
        if the user does not exist, register the user into the database
        print the menu to access the other functions. 
                ("1: Search a book")
                ("2: Borrow a book")
                ("3: Return a book")
                ("4: Logout")
        """
        while(True):
            # receiving username
            #user_name = "Fdsfads"
            # This is for sockets
            user_name = MasterPiSocket.receiveMessageLoginSocket(self)
            # self.db.insertUser("harryle")

            # check if the username is already in the masterpi.
            # if not then add it
            if self.returnUserID(user_name) == "None":
                print("Registering User into Masterpi")
                self.db.insertUser(user_name)
            else:
                print("Logged in")

            # print(self.db.getAllUsers())

            while(True):
                print("1: Search a book")
                print("2: Borrow a book")
                print("3: Return a book")
                print("4: Logout")

                choice = input("Enter your choice: ")
                if choice == "1":
                    bookTitle = str(input("Input Book Title: "))
                    self.searchBook(bookTitle)
                elif choice == "2":
                    self.borrowBook(user_name)
                elif choice == "3":
                    self.returnBook(user_name)
                elif choice == "4":
                    self.logout()
                    break
                else:
                    print("Invalid Input!")

    # searches the table for the specified book

    def searchBook(self, input):
        """
        Search books in the library database that contains of the 'input' and display them.
            param1: 'input' is used to search books 
        """
        res = self.db.searchBooks(input)
        for row in res:
            self.output.displayBook(row)

        return
    # takes the id of a book and returns a borrowing id if it's available

    def borrowBook(self, user_name):
        """
        Prints the menu console for borrowing a book from the library. 
            ("--- Borrow a book ---")
            ("Enter the ID of the book: ")
        The user borrows a book by entering a bookID. 
        If the bookID is not found, returns to BorrowBook menu.  
        Upon success it checks if the book is available and if so 
        it inserts userID of the current user, bookID of the book to the database
        and add the event to the Google Calendar of the library account. 
        After borrowing a book completed, the function will ask if the user may borrow another book. 
            ("Do you want to borrow another book?  Y/N: ")
            param1: 'user_name' is the username that receives from the socket and used to return userID
        """
        # exit = False
        print("--- Borrow a book ---")
        bookID = input("Enter the ID of the book: ")
        book = self.db.getBookByBookID(bookID)
        # no book found, return menu
        if book == None:
            print("Book Not Found!")
            # self.initialise()
            return
        # if found, display book
        self.output.displayBook(book)
        choice = input("Do you want to borrow this book? \n Y/N: ")
        if choice == 'Y' or choice == 'y':
            bookBorrowed = self.db.getBorrowedBookByBookID(bookID)
            if bookBorrowed != None:
                print("Sorry! This book is currently not available.")
            else:
                borrowDate = datetime.date(datetime.now())
                returnDate = borrowDate + timedelta(days=7)
                # user should not be asked about user ID after login
                # LmsUserID = input("Please enter your user ID")
                # will get userID later
                self.db.insertBorrowedBook(
                    self.db.getUserIDByUserName(user_name), bookID, borrowDate, returnDate)
            # creates an event for the return date
            # e = Calendar()
            # e.addEvent(borrowDate, returnDate, bookID)
            choice2 = input("Do you want to borrow another book? \n Y/N: ")
            if choice2 == "Y" or choice2 == 'y':
                self.borrowBook(user_name)
            else:
                return
        else:
            return

    # takes a borrowing id and returns the book
    # ************ list your books shouldnt return book ************ 
    def returnBook(self, user_name):
        """
        Prints the menu console for listing the user's books and returning a book.
            ("--- Return a book ---")
            ("1. List your books")
            ("2. Return your book")
            ("3. Exit")
        
        The first function lists all the books that the current user has not returned. 
        The second function allows the user return a book by entering bookID. 
        If the bookID is not found or does not belong to the user, returns to ReturnBook menu.
        Upon successful return, removes the event on the Google Calendar of the library.  
            param1: 'user_name' is the username that receives from the socket and used to return userID
        """
        print("--- Return a book ---")
        print("1. List your books")
        print("2. Return your book")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # get userId later
            res = self.db.getBorrowedBooksByUserID(
                self.db.getUserIDByUserName(user_name))
            for row in res:
                self.output.displayBorrowedBook(row)
            self.returnBook(user_name)
        if choice == "2":
            borrowedBookID = input("Enter your Borrowed Book ID: ")
            book = self.db.getBorrowedBookByBorrowedBookID(borrowedBookID)
            if(book == None):
                print("No Book Found!")
                self.returnBook(user_name)
            else:
                self.db.setReturnedBook(borrowedBookID)
                print("Book has been returned!")
                self.returnBook(user_name)
            # e = Calendar()
            # e.removeEvent()
        if choice == "3":
            # self.initialise()
            return

    def logout(self):
        """
        Sends logout message from MasterPi to ReceptionPi
        """
        MasterPiSocket.sendMessageLogoutSocket(self)
        # self.initialise()
        time.sleep(2)
        return

    # get user name from reception pi through sockets

    #************ FIX userName to user_name ********
    def returnUserID(self, userName):
        """
        Returns UserID of the current user 
            param1: 'user_name' is the username that receives from the socket and used to return userID
        """
        return self.db.getUserIDByUserName(userName)


consoleMP()