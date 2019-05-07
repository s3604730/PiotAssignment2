from Database import Database

#stays idle if no message is sent from Reception Pi
class consoleMP:
    def __init__(self):
        with Database() as db:
            db.createTables()
        self.initilaise()


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

    def searchBook(self, bookDetail):
        print("---Search Results:----")
        print("{:<15} {}".format("Book ID", "Title","Author", "Publish Date"))
        with Database() as db:
            for books in db.getBook():
                print("{:<15} {}".format(books[0], books[1]))



    #takes the id of a book and returns a borrowing id if it's available
    def borrowBook(self,bookID):
        print("--- Borrow a book ---")
        bookID = input("Enter the ID of the book: ")
        with Database() as db:
            


            m.create_event(calendar_id='<your calendar id>',
            start= datetime.utcnow().isoformat() + "Z",
            end='2017,12,5,15,15,00'




    #takes a borrowing id and returns the book
    def returnBook()