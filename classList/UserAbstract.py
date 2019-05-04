# Abstract use class
from abc import ABC, ABCMeta, abstractmethod


# Abstract Class


class UserSkeleton(ABC):
    def __init__(self, userName, passWord, firstName, lastName, email):
        super().__init__()
        self.__userName = userName
        self.__passWord = passWord
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email

    def getUserName(self):
        return self.__userName

    def getPassWord(self):
        return self.__passWord

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getEmail(self):
     return self.__email
