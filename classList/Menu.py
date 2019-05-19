from classList.Database import Database
from classList.User import User
import hashlib
import getpass
import re
from SocketPi.MasterPiSocket import MasterPiSocket

from SocketPi.ReceptionPiSocket import ReceptionPiSocket

class Menu():
    def __init__(self):
        while(True):
            choice = 0
            while(choice != "1" and choice != "2" and choice != "3"):
                print("1. Create a new account")
                print("2. Log in")
                print("3. Quit")

                choice = input("Enter your choice: ")

            if(choice == "1"):
                self.registerUser()
            elif(choice == "2"):
                self.loginUser()
            elif(choice == "3"):
                pass

    def registerUser(self):
        db = Database()

        username = ""
        while(username == ""):
            username = input("Enter username: ")
            if(db.findUserByUsername(username) != None):
                username = ""
                print("This username already exists.")
                continue

        firstName = ""
        while(firstName == ""):
            firstName = input("Enter first name: ")
            if not firstName.isalpha():
                firstName = ""
                print("Input is invalid!")
                continue

        lastName = ""
        while(lastName == ""):
            lastName = input("Enter last name: ")
            if not lastName.isalpha():
                lastName = ""
                print("Input is invalid!")
                continue

        # will validate email later
        email = ""
        while(email == ""):
            email = input("Enter email: ")
            if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
                email = ""
                print("Email is not valid")
                continue

        # will validate password later
        hashedPassword = ""

        password = ""
        while(password == ""):
            password = getpass.getpass("Enter password: ")

        password2 = ""
        while(password2 == ""):
            password2 = getpass.getpass("Confirm password: ")
            if(password2 != password):
                password2 = ""
                print("Passwords do not match")
                continue
            else:
                hashedPassword = hashlib.sha256(password.encode()).hexdigest()

        # may use try-catch later
        user = User(username, hashedPassword, firstName, lastName, email)
        db.insertUser(user)
        print(username + " has been registered!")
        
    def loginUser(self):
        username = ""
        while(username == ""):
            username = input("Enter username: ")

        password = ""
        while(password == ""):
            password = getpass.getpass("Enter password: ")

        db = Database()

        hashedPassword = hashlib.sha256(password.encode()).hexdigest()

        user = db.findUserByUsernameAndPassword(username, hashedPassword)
        if(user == None):
            print("Wrong login credentials")
            Menu()
        else:
            print("Logged in successfully")

            # use socket here
            #ReceptionPiSocket.sendMessageLoginSocket(self, username)
            

        # return user
