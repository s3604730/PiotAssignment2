# pip install MySQL-python

import mysql.connector


class Database:
    """
    This class connects with the Google Cloud database. 
    It includes all the functions related to the Cloud database. 
    """
    HOST = "35.201.14.167"
    USER = "root"
    PASSWORD = ""
    DATABASE = "piotassignment2"

    def __init__(self, connection=None):
        if(connection == None):
            connection = mysql.connector.connect(
                host=self.HOST, user=self.USER, password=self.PASSWORD, database=self.DATABASE)
        self.connection = connection
        self.cursor = connection.cursor()

        self.createTableUser()
        self.createTableBook()
        self.createTableBookBorrowed()

    def close(self):
        """
        Close the database connection
        """
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    # create table user
    def createTableUser(self):
        """
        Create LmsUser table (LmsUserID, UserName)
        """
        self.cursor.execute("""
            create table if not exists LmsUser (
                LmsUserID int not null auto_increment,
                UserName nvarchar(256) not null,
                constraint PK_LmsUser primary key (LmsUserID),
                constraint UN_UserName unique (UserName)
            );
        """)
        self.connection.commit()

    # create table book
    def createTableBook(self):
        """
        Create Book table (BookID,Title,Author,PublishedDate)
        """
        self.cursor.execute("""
            create table if not exists Book (
                BookID int not null auto_increment,
                Title text not null,
                Author text not null,
                PublishedDate date not null,
                constraint PK_Book primary key (BookID)
            );
        """)
        self.connection.commit()

    # create table book borrowed
    def createTableBookBorrowed(self):
        """
        Create BookBorrowed table (BookBorrowedID, LmsUserID, BookID, Status, BorrowedDate, ReturnedDate)
        """
        self.cursor.execute("""
            create table if not exists BookBorrowed (
                BookBorrowedID int not null auto_increment,
                LmsUserID int not null,
                BookID int not null,
                Status enum ('borrowed', 'returned'),
                BorrowedDate date not null,
                ReturnedDate date null,
                constraint PK_BookBorrowed primary key (BookBorrowedID),
                constraint FK_BookBorrowed_LmsUser foreign key (LmsUserID) references LmsUser (LmsUserID),
                constraint FK_BookBorrowed_Book foreign key (BookID) references Book (BookID)
            );
        """)
        self.connection.commit()

    # insert user
    def insertUser(self, username):
        """
        Insert 'username' parameter into UserName in LmsUser table 

            param1: 'username' 
        """
        self.cursor.execute(
            "insert into LmsUser (UserName) values (%s)", (username, ))
        self.connection.commit()

    # get all users
    def getAllUsers(self):
        """
        Return all the users from LmsUser table 
        """
        self.cursor.execute("select * from LmsUser ORDER BY LmsUserID")
        res = self.cursor.fetchall()
        return res

    # get user ID
    def getUserIDByUserName(self, userName):
        """
        Return an LmsUserID that the username = 'userName' parameter.
        If not found, returns "none".

            param1: 'userName' 
        """
        self.cursor.execute(
            "SELECT LmsUserID FROM LmsUser WHERE UserName = %s", (userName,))
        res = self.cursor.fetchone()
        
        
        if res is None:
            return "None"
        else:
            return res[0]

    # get all books
    def getAllBooks(self):
        """
        Return all the books in Book table 
        """
        self.cursor.execute(
            "select * from Book")
        res = self.cursor.fetchall()
        return res

    def getBookByBookID(self, bookID):
        """
        Return a book with the BookID = 'bookID' parameter. 

            param1: 'bookID'
        """
        self.cursor.execute(
            "SELECT * FROM Book WHERE BookID = %s", (bookID,))
        res = self.cursor.fetchone()
        return res

    # searchBook
    def searchBooks(self, bookDetail):
        """
        Return books that contain of 'bookDetail' parameter.

            param1: 'bookDetail'
        """
        sql_select = "select * from Book Where Title like %s OR Author like %s"
        val = ("%" + str(bookDetail) + "%", "%" + str(bookDetail) + "%",)
        self.cursor.execute(sql_select, val)
        res = self.cursor.fetchall()
        return res

    # insert borrowed book
    def insertBorrowedBook(self, lmsuserID, bookID, borrowedDate, returnedDate):
        """
        Insert 
        'lmsuserID' into LmsUserID, 
        'bookID' into BookID, 
        'borrowedDate' into BorrowedDate, 
        'returnedDate' into ReturnedDate 
        and set Status of the row to 'borrowed' in BorrowedBook table.

            param1: 'lmsuserID'
            param2: 'bookID'
            param3: 'borrowedDate'
            param4: 'returnDate'
        """
        self.cursor.execute("insert into BookBorrowed (LmsUserID, BookID, Status, BorrowedDate, ReturnedDate) values (%s,%s,'borrowed',%s,%s)",
                            (lmsuserID, bookID, borrowedDate, returnedDate))
        self.connection.commit()

    # get borrowed book
    def getBorrowedBooksByUserID(self, lmsUserID):
        """
        Return all the books that the LmsUserID = 'lmsUserID' parameter 
        and the status = 'borrowed'.

            param1: 'lmsUserID'
        """
        self.cursor.execute(
            "SELECT * FROM BookBorrowed WHERE LmsUserID = %s AND status = 'borrowed'", (lmsUserID,))
        res = self.cursor.fetchall()
        return res

    def getBorrowedBookByBookID(self, bookID):
        """
        Return all the books that the BookID = 'bookID' parameter
        and the status = 'borrowed'.

            param1: 'bookID'
        """
        self.cursor.execute(
            "SELECT * FROM BookBorrowed WHERE BookID = %s AND status = 'borrowed'", (bookID,))
        res = self.cursor.fetchone()
        return res

    # searches for borrowed book specified in parameter
    def getBorrowedBookByBorrowedBookID(self, bookBorrowedID):
        """
        Return all the books that the BookBorrowedID = 'bookBorrowedID' parameter
        and the status = 'borrowed'.

            param1: 'bookBorrowedID'
        """
        self.cursor.execute(
            "SELECT * FROM BookBorrowed WHERE BookBorrowedID = %s AND status = 'borrowed'", (bookBorrowedID,))
        res = self.cursor.fetchone()
        return res

    # set status to "returned", may update return date later
    def setReturnedBook(self, bookBorrowedID):
        """
        Set Status (of a book) that the BookBorrowedID = 'bookBorrowedID' parameter to 'returned'. 

            param1: 'bookBorrowedID'
        """ 
        self.cursor.execute("UPDATE BookBorrowed SET Status = 'returned' WHERE BookBorrowedID = %s",
                            (bookBorrowedID,))
        self.connection.commit()

    def clearTable(self, tableName):
        """
        Clear 'tableName' table 

            param1: 'tableName'
        """
        self.cursor.execute("DELETE FROM " + tableName)
        self.connection.commit()

# db = Database()
# print(db.getBookByBookID("fesad"))
