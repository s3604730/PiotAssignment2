from Database import Database
from calendar_api.calendar_api import google_calendar_api

#stays idle if no message is sent from Reception Pi
class consoleMP:
    def __init__(self):
        with Database() as db:
            db.createTables()
        self.initilaise()
        m=google_calendar_api()

    def initialise(self):
        print("1: Search a book")
        print("2: Borrow a book")
        print("3: Return a book")
        print("4: Logout")

        choice = input("Enter your choice")
        print()
        if choice == "1":
            bookTitle = input("Input Book TItle")
            self.searchBook(bookTitle)
        elif choice == "2":
            self.borrowBook()
        elif choice == "3":
            self.returnBook()
        elif choice == "4":
            self.logout()
        else:
            print("Invalid Input!")

    #takes the id of a book and returns a borrowing id if it's available
    def borrowBook(self,bookID,LmsUserID):
        exit = false
        print("--- Borrow a book ---")
        bookID = input("Enter the ID of the book: ")
        with Database() as db:
            searchBook(bookID)
            choice = input("Do you want to borrow this book? \n Y/N")
            if choice == 'Y':
                while (exit != true):
                    insertBorrowedBook(bookID,LmsUserID)
                    m.create_event(calendar_id='primary',)
                    start = datetime.utcnow().isoformat() + "Z",
                    e = GCAL.events().insert(calendarId='primary', 
                    sendNotifications=True, body=EVENT).execute()
                    if input("Do you want to borrow another book? \n Y/N") == "N":
                        exit = true
            
        
        
        
        #Find a book by bookID. 
        #Print the book properties
        #Ask for confirmation
        #Assign the bookID < BookID >  
        #Assign the current userID < LmsUserID > 
        #Assign status enum 'borrowed' 
        #Assign borrowedDate
        #Assign returnedDate + 7 days + add the event on google calendar

    #takes a borrowing id and returns the book
    def returnBook():
        print("--- Return a book ---")
        print("1. List your books")
        #Find returning book by the borrowedBookID < BorrowedBookID > 
        #Check if borrowedBookID belongs to the current user and hasn't been returned 
        #Assign status enum 'returned' 
        #Remove the event from the user's google calendar
        print("2. Return your book")
        print("3. Exit")