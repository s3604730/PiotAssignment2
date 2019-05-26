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
    def __init__(self):
        self.db = Database()
        self.output = Output()
        self.cal = Calendar()
        self.initialise()

    def initialise(self):
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
        res = self.db.searchBooks(input)
        for row in res:
            self.output.displayBook(row)

        return
    # takes the id of a book and returns a borrowing id if it's available

    def borrowBook(self, user_name):
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
                self.cal.addEvent(bookID,user_name)
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
    def returnBook(self, user_name):
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
                self.cal.removeEvent(self.db.getBookIDByBorrowedBookID(borrowedBookID))
                self.db.setReturnedBook(borrowedBookID)
                print("Book has been returned!")
                self.returnBook(user_name)
            # e = Calendar()
            # e.removeEvent()
        if choice == "3":
            # self.initialise()
            return

    def logout(self):
        # TODO
        '''sends logout message from MP to RP'''
        MasterPiSocket.sendMessageLogoutSocket(self)
        # self.initialise()
        time.sleep(2)
        print("yeet")
        return

    # get user name from reception pi through sockets
    def returnUserID(self, userName):
        return self.db.getUserIDByUserName(userName)


consoleMP()
