import mysql.connector
import json
from datetime import datetime
from classList.User import User


class Database():
    # mysql config of Pi
    #iot2user for tony database
    #otherwise root for everyone else
    host = "localhost"
    user = "iot2user"
    password = ""
    database = "iot2"

    def __init__(self, testing=False):
        # populate database and tables if they don't exist
        if(testing == True):
            self.database = "testing"
        self.createDatabase()
        self.createTableUser()

        # connect to database
        con = mysql.connector.connect(
            host=self.host, user=self.user, password=self.password, database=self.database)
        self.cursor = con.cursor()
        self.con = con

    # createDatabase
    def createDatabase(self):
        con = mysql.connector.connect(
            host=self.host, user=self.user, password=self.password)
        stm = "CREATE DATABASE IF NOT EXISTS iot2"
        con.cursor().execute(stm)
        con.commit()

    # create table users
    def createTableUser(self):
        con = mysql.connector.connect(
            host=self.host, user=self.user, password=self.password, database=self.database)
        stm = "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255),password VARCHAR(255), firstName VARCHAR(255), lastName VARCHAR(255), email VARCHAR(255))"
        con.cursor().execute(stm)
        con.commit()

    # insert user
    def insertUser(self, user):
        try:
            stm = (
                "INSERT INTO users(username, password, firstName, lastName, email) VALUES (%s, %s, %s, %s, %s)")

            val = (user.getUsername(),  user.getPassword(), user.getFirstName(), user.getLastName(),
                   user.getEmail())

            self.cursor.execute(stm, val)

            self.con.commit()
            return True
        except:
            return False

    # find user by user name to for register part

    def findUserByUsername(self, username):
        stm = ("SELECT * FROM users WHERE username = %s")
        val = (username, )

        self.cursor.execute(stm, val)

        res = self.cursor.fetchone()

        return res

    # find user by credentials to verify login details
    def findUserByUsernameAndPassword(self, username, password):
        stm = ("SELECT * FROM users WHERE username = %s AND password = %s")
        val = (username, password)

        self.cursor.execute(stm, val)

        res = self.cursor.fetchone()

        return res
