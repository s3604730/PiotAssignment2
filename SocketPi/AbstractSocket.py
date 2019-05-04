#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html
from abc import ABC, ABCMeta, abstractmethod
import socket

class AbstractSocket(ABC):
 def __init(self):
  pass

 #abstract method for sending message socket login
 def sendMessageLoginSocket(self):
  pass

 #abstract method for receiving message socket login
 def receiveMessageLoginSocket(self):
  pass

 #abstract method for sending message socket logout
 def sendMessageLogoutSocket(self):
  pass
 
 #abstract method for receiving message socket logout
 def receiveMessageLogoutSocket(self):
  pass

 
