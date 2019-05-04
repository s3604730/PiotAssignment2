# pip install MySQL-python

import MySQLdb

class Database:
    HOST = "35.201.14.167"
    USER = "piotassignment1234@gmail.com"
    PASSWORD = "iwanttodropout"
    DATABASE = "piotassignment2"

    def __init__(self, connection = None):
        if(connection == None):
            connection = MySQLdb.connect(Database.HOST, Database.USER,
                Database.PASSWORD, Database.DATABASE)
        self.connection = connection    

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def createLmsUserTable(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists LmsUser (
	                LmsUserID int not null auto_increment,
                    UserName nvarchar(256) not null,
                    Name text not null,
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
            cursor.execute("insert into LmsUser (UserName,Name) values (%s,%s)", (username, name))
        self.connection.commit()

# get user
    def getUser(self):
        with self.connection.cursor() as cursor:
            return cursor.fetchall()
            cursor.execute("select LmsUserID, UserName, Name from LmsUser")

# insert book
    def insertBook(self, title, author, publishedDate):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into Book (Title, Author, PublishedDate) values (%s,%s,%s)", (title, author, publishedDate))
        self.connection.commit()        

# get book
    def getBook(self):
        with self.connection.cursor() as cursor:
            return cursor.fetchall()
            cursor.execute("select BookID, Title, Author, PublishedDate from Book")
    
# insert borrowed book
    def insertBorrowedBook(self, lmsuserID, bookID, status, borrowedDate, returnedDate):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into BorrowedBook (LmsUserID, BookID, Status, BorrowedDate, ReturnedDate) values (%s,%s,%s,%s,%s)", (lmsuserID, bookID, status, borrowedDate, returnedDate))
        self.connection.commit()     

# get borrowed book
    def getBorrowedBook(self):
        with self.connection.cursor() as cursor:
            return cursor.fetchall()
            cursor.execute("select BorrowedBookID, LmsUserID, BookID, Status, BorrowedDate, ReturnedDate from BorrowedBook")