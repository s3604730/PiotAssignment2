# pip install MySQL-python

import mysql.connector


class Database:
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
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    # create table user
    def createTableUser(self):
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
        self.cursor.execute(
            "insert into LmsUser (UserName) values (%s)", (username, ))
        self.connection.commit()

    # get all users
    def getAllUsers(self):
        self.cursor.execute("select * from LmsUser ORDER BY LmsUserID")
        res = self.cursor.fetchall()
        return res

    # get user ID
    def getUserIDByUserName(self, userName):
        self.cursor.execute(
            "SELECT LmsUserID FROM LmsUser WHERE UserName = %s", (userName,))
        res = self.cursor.fetchone()
        
        
        if res is None:
            return "None"
        else:
            return res[0]

    # get all books
    def getAllBooks(self):
        self.cursor.execute(
            "select * from Book")
        res = self.cursor.fetchall()
        return res

    def getBookByBookID(self, bookID):
        self.cursor.execute(
            "SELECT * FROM Book WHERE BookID = %s", (bookID,))
        res = self.cursor.fetchone()
        return res

    # searchBook
    def searchBooks(self, bookDetail):
        sql_select = "select * from Book Where Title like %s OR Author like %s"
        val = ("%" + str(bookDetail) + "%", "%" + str(bookDetail) + "%",)
        self.cursor.execute(sql_select, val)
        res = self.cursor.fetchall()
        return res

    # insert borrowed book
    def insertBorrowedBook(self, lmsuserID, bookID, borrowedDate, returnedDate):
        self.cursor.execute("insert into BookBorrowed (LmsUserID, BookID, Status, BorrowedDate, ReturnedDate) values (%s,%s,'borrowed',%s,%s)",
                            (lmsuserID, bookID, borrowedDate, returnedDate))
        self.connection.commit()

    # get borrowed book
    def getBorrowedBooksByUserID(self, lmsUserID):
        self.cursor.execute(
            "SELECT * FROM BookBorrowed WHERE LmsUserID = %s AND status = 'borrowed'", (lmsUserID,))
        res = self.cursor.fetchall()
        return res

    def getBorrowedBookByBookID(self, bookID):
        self.cursor.execute(
            "SELECT * FROM BookBorrowed WHERE BookID = %s AND status = 'borrowed'", (bookID,))
        res = self.cursor.fetchone()
        return res

    # searches for borrowed book specified in parameter
    def getBorrowedBookByBorrowedBookID(self, bookBorrowedID):
        self.cursor.execute(
            "SELECT * FROM BookBorrowed WHERE BookBorrowedID = %s AND status = 'borrowed'", (bookBorrowedID,))
        res = self.cursor.fetchone()
        return res

    # set status to "returned", may update return date later
    def setReturnedBook(self, bookBorrowedID):
        self.cursor.execute("UPDATE BookBorrowed SET Status = 'returned' WHERE BookBorrowedID = %s",
                            (bookBorrowedID,))
        self.connection.commit()

    def clearTable(self, tableName):
        self.cursor.execute("DELETE FROM " + tableName)
        self.connection.commit()


# db = Database()
# print(db.getBookByBookID("fesad"))
