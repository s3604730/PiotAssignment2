#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

# DISCLAIMER, REFERENCED BY echo_client.py AND echo_server.py BY RMIT
import socket
from SocketPi.AbstractSocket import AbstractSocket
import json


# class for reception pi based on abstract


class ReceptionPiSocket(AbstractSocket):
    """
    This class acts as a socket for communication for the reception pi
    This class includes the functions 
        - Send a login message through Socket
        - Receive message logout socket
    """

    def __init__(self):
        pass
    # send message from reception pi to master pi

    def sendMessageLoginSocket(self, userName):

        """
        This method sends a login message through sockets to master
        pi and sends the username. 

        param1: 'user_name' username is sent to the receiving socket



        """
        HOST = '10.132.136.92'  # The server's hostname or IP address.
        PORT = 65000         # The port used by the server. s
        ADDRESS = (HOST, PORT)

        # sending message
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Connecting to {}...".format(ADDRESS))
            s.connect(ADDRESS)
            print("Connected.")

            # Send a message for login successful
            loginMsg = "Login Successful!"
            s.sendall(loginMsg.encode())

            # Receive a message requesting for Username
            data = s.recv(4096)
            print(data.decode())

            # send the username
            s.sendall(userName.encode())

            # receive success message
            data = s.recv(4096)

            print("{}", data.decode())

        print("Done.")
        return True

    # abstract method, skip because reception pi doesn't do this
    def receiveMessageLoginSocket(self, userName):
        pass
    # abstract method, skip because reception pi doesn't do this

    def sendMessageLogoutSocket(self, userName):
        pass

    # reception pi receives the logout message and the username
    def receiveMessageLogoutSocket(self):
        """
        This method receives a message for logout 

        """
        HOST = ""

        # Note "0.0.0.0" also works but only with IPv4.
        PORT = 65001  # Port to listen on (non-privileged ports are > 1023).
        ADDRESS = (HOST, PORT)
        # Initialise and wait for connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(ADDRESS)
            s.listen()

            print("Listening on {}...".format(ADDRESS))
            conn, addr = s.accept()
            # when a connection has been established
            with conn:
                while True:

                    print("Connected to {}".format(addr))
                    # Receive message that login is sucessful
                    data = conn.recv(4096)
                    coolMessage = data.decode()
                    print(coolMessage)
                    # send success message back requesting for username
                    logoutRequestMessage = "LogoutMessageReceived"
                    conn.sendall(logoutRequestMessage.encode())

                    # receive userName
                    data = conn.recv(4096)
                    # set userName
                    logoutMessageSecond = data.decode()
                    print(logoutMessageSecond)

                    # send success message back saying logout was successful
                    successMessage = "Successfully logged out"
                    conn.sendall(successMessage.encode())
                    break

                print("Disconnecting from client.")
        print("Closing listening socket.")
        print("Done.")
