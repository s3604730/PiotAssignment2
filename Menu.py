from Database import Database

class Menu:
    def main(self):
        with Database() as db:
            db.createTables()
        self.runMenu()

    def runMenu(self):
        while(True):
            print()
            print("1. Search book")
            print("2. Borrow book")
            print("3. Return book")
            print("4. Exit")
            selection = input("Select an option: ")
            print()

            if(selection == "1"):
                self.SearchBook()
            elif(selection == "2"):
                self.BorrowBook()
            elif(selection == "3"):
                self.ReturnBook()
            elif(selection == "4"):
                print("Goodbye!")
                break    
            else:
                print("Invalid input - please try again.")

    def SearchBook(self):
        print("--- BookList ---")
        bookID = input("Enter the book name: ")
        print("{:<15} {}".format("Book ID", "Title", "Author", "Published Date"))
        with Database() as db:
            for book in db.getBook(booktitle):
                if db.getBook(booktitle) != ""
                    print("{:<15} {}".format(book[0], book[1]), book[2], book[3])
                else
                    print("Not found !")
                    return

# To Do 
    def BorrowBook(self):
        print("--- Borrow a book ---")
        bookID = input("Enter the ID of the book: ")
        with Database() as db:
        #Find a book by bookID.
        #Print the book properties
        #Ask for confirmation
        #Assign the bookID < BookID >  
        #Assign the current userID < LmsUserID > 
        #Assign status enum 'borrowed' 
        #Assign borrowedDate
        #Assign returnedDate + 7 days + add the event on google calendar
            if(db.insertBorrowedBook(bookID)):


    def ReturnBook(self):
        print("--- Return a book ---")
        #Track all the books the current user hasn't returned by the current userID < LmsUserID > 
        print("1. List your books")

        #Find returning book by the borrowedBookID < BorrowedBookID > 
        #Check if borrowedBookID belongs to the current user and hasn't been returned 
        #Assign status enum 'returned' 
        #Remove the event from the user's google calendar
        print("2. Return your book")
        print("3. Exit")
        
    if __name__ == "__main__":
        Menu().main()
