from classList.Database import Database
from classList.User import User


class Menu():
    def __init__(self):
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

        lastName = ""
        while(lastName == ""):
            lastName = input("Enter last name: ")

        # will validate email later
        email = ""
        while(email == ""):
            email = input("Enter email: ")

        # will validate password later
        password = ""
        while(password == ""):
            password = input("Enter password: ")

        password2 = ""
        while(password2 == ""):
            password2 = input("Confirm password: ")
            if(password2 != password):
                password2 = ""
                print("Passwords do not match")
                continue

        # may use try-catch later
        user = User(username, password, firstName, lastName, email)
        db.insertUser(user)
        return user

    def loginUser(self):
        username = ""
        while(username == ""):
            username = input("Enter username: ")

        password = ""
        while(password == ""):
            password = input("Enter password: ")

        db = Database()

        user = db.findUserByUsernameAndPassword(username, password)
        if(user == None):
            print("Wrong login credentials")
            Menu()
        else:
            print("Loged in successfully")
        # use socket here

        # return user
