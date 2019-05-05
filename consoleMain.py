import book, 


#stays idle if no message is sent from Reception Pi
class consoleMP:
    def __init__(self):
        self.initilaise()


    def initialise(self):
        print("1: Search a book")
        print("2: Borrow a book")
        print("3: Return a book")
        print("4: Logout")

        choice = input("Enter your choice")

        if choice == "1":
            self.searchBook()
        elif choice == "2":
            print("Input Book Title")
            bookTitle = input(bookName)
            self.findBook(input(bookTitle))
        elif choice == "3":
            self.returnBook()
        elif choice == "4":
            self.logout()



    #searches for a book and returns its the top 5 results with id, book and author
    def searchBook(self, bookName):

              



    #takes the id of a book and returns a borrowing id if it's available
    def borrowBook()

    #takes a borrowing id and returns the book
    def returnBook()