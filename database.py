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
        print(connection)

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def createTables(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists LmsUser (
	                LmsUserID int not null auto_increment,
                    UserName nvarchar(256) not null,
                    constraint PK_LmsUser primary key (LmsUserID),
                    constraint UN_UserName unique (UserName)
                );

                create table if not exists Book (
	                BookID int not null auto_increment,
                    Title text not null,
                    Author text not null,
                    PublishedDate date not null,
                    constraint PK_Book primary key (BookID)
                );

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
    def insertUser(self, username, name):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "insert into LmsUser (UserName,Name) values (%s,%s)", (username, name))
        self.connection.commit()

# get user
    def getUser(self):
        with self.connection.cursor() as cursor:
            return cursor.fetchall()
            cursor.execute("select LmsUserID, UserName, Name from LmsUser")

    def getUserID(self, userName):

        self.cursor.execute(
            "SELECT * FROM Book WHERE BookID = %s", (userName,))
        userID = self.cursor.fetchall()

        return userID


# insert book


    def insertBook(self, title, author, publishedDate):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "insert into Book (Title, Author, PublishedDate) values (%s,%s,%s)", (title, author, publishedDate))
        self.connection.commit()

# get book
    def getBook(self):
        self.cursor.execute(
            "select BookID, Title, Author, PublishedDate from Book")
        res = self.cursor.fetchall()
        return res

    def searchBook(self, bookDetail):

        sql_select = "select * from Book Where Title like %s OR Author like %s"
        val = ("%" + str(bookDetail) + "%", "%" + str(bookDetail) + "%",)
        self.cursor.execute(sql_select, val)
        res = self.cursor.fetchall()
        # for row in res:
        #     print("Book ID: ", row[0])
        #     print("Title: ", row[1])
        #     print("Author: ", row[2])
        print(res)
# insert borrowed book

    def insertBorrowedBook(self, lmsuserID, bookID, status, borrowedDate, returnedDate):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into BorrowedBook (LmsUserID, BookID, Status, BorrowedDate, ReturnedDate) values (%s,%s,%s,%s,%s)",
                           (lmsuserID, bookID, status, borrowedDate, returnedDate))
        self.connection.commit()

# get borrowed book
    def getBorrowedBook(self, LmsID):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM BookBorrowed WHERE LmsID = %s", (LmsID,))
            for row in self.getBook():
                print("Book Borrowed ID: ", row[0], )
                print("LMS User ID ", row[1], )
                print("BookID: ", row[2], )
                print("Status: ", row[4])
                print("Borrow Date", row[5])
                print("Return Date", row[6])

# searches for borrowed book specified in parameter
    def searchBorrowedBook(self, bookBorrowedID):
        with self.connection.cursor() as cursor:
            sql_select = "SELECT * FROM BookBorrowed WHERE BookBorrowedID = %s"
            cursor.execute(sql_select, bookBorrowedID,)
            for row in self.getBook():
                print("Book Borrowed ID: ", row[0],)
                print("LMS User ID ", row[1],)
                print("BookID: ", row[2],)
                print("Status: ", row[4])
                print("Borrow Date", row[5])
                print("Return Date", row[6])


db = Database()
db.searchBook("Mario")
