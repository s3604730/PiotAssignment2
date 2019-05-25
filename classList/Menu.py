from classList.Database import Database
from classList.User import User
import hashlib
import getpass
import re
import time
from SocketPi.MasterPiSocket import MasterPiSocket

from SocketPi.ReceptionPiSocket import ReceptionPiSocket
from classList.CaptureCam import CaptureCam
from classList.EncodeCam import EncodeCam
from classList.RecogniseCam import RecogniseCam

class Menu():
    def __init__(self):
        while(True):
            choice = 0
            while(choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"):
                print("1. Create a new account")
                print("2. Log in")
                print("3. Register user face to account")
                print("4. Login using face")
                print("5. Quit")

                choice = input("Enter your choice: ")

            if(choice == "1"):
                self.registerUser()
            elif(choice == "2"):
                self.loginUser()
                time.sleep(2)
                # socket for waiting for logout socket
                ReceptionPiSocket.receiveMessageLogoutSocket(self)

            elif(choice == "3"):
                user_name = self.register_user_face()
                if (user_name != "None"):
                    CaptureCam.capture(self, user_name)
                    EncodeCam()
                    print(user_name)
                

            elif(choice == "4"):
                user_name = RecogniseCam.running_Recognise_Cam(self)
                print(user_name)
                ReceptionPiSocket.sendMessageLoginSocket(self, user_name)
                time.sleep(2)
                ReceptionPiSocket.receiveMessageLogoutSocket(self)
                
            elif(choice == "5"):
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
            ReceptionPiSocket.sendMessageLoginSocket(self, username)

        # return user

    def login_User_Face(self):
        username = ""
        
        while(username == ""):
            username = input("Enter username: ")
        db = Database()
        a = db.findUserByUsername(username)
        if a == "None":
            print("Cannot find user")
            return "None"
        else:
            print("Found user")
        return username
        pass
    
    def register_user_face(self):
        username = ""
        
        while(username == ""):
            username = input("Enter username: ")
        db = Database()
        a = db.findUserByUsername(username)
        if str(a) == "None":
            print("Cannot find user")
            
            return "None"
        else:
            print("Found user")
            username = str(a[1])
            return username
        
        
        
        
