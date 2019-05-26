# Abstract use class
from abc import ABC, ABCMeta, abstractmethod


# Abstract Class


class UserSkeleton(ABC):
    def __init__(self, username, password, firstName, lastName, email):
        super().__init__()
        self.__username = username
        self.__password = password
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getEmail(self):
        return self.__email
