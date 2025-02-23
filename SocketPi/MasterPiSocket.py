#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html
# DISCLAIMER, REFERENCED BY echo_client.py AND echo_server.py BY RMIT

from SocketPi.AbstractSocket import AbstractSocket
import socket
import json

class MasterPiSocket(AbstractSocket):
    """
    This class acts as a socket for communication for the Master pi
    This class includes the functions
        - Send logout message through Socket
        - Receive message login socket with username
    

    """
    def __init__(self):
        pass
    # skip because master pi doesn't send login username

    def sendMessageLoginSocket(self, userName):
        pass
    # Master pi receiving a login message from reception pi

    def receiveMessageLoginSocket(self):
        """
        This method receives the login username socket

        """
        HOST = ""

        # Note "0.0.0.0" also works but only with IPv4.
        PORT = 65000  # Port to listen on (non-privileged ports are > 1023).
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
                    userNameRequestMessage = "Give Username"
                    conn.sendall(userNameRequestMessage.encode())

                    # receive userName
                    data = conn.recv(4096)
                    # set userName
                    userName = data.decode()
                    print(userName)

                    # send success message back saying login was successful
                    successMessage = "Successfully logged into MASTER PI"
                    conn.sendall(successMessage.encode())
                    #break
                    return userName

                print("Disconnecting from client.")
        print("Closing listening socket.")
        print("Done.")
        

    # Master pi sends a logout message to the reception pi
    def sendMessageLogoutSocket(self):
        """
        This method sends a logout message towards the reception pi
        """
        HOST = '10.132.81.57'  # The server's hostname or IP address.
        PORT = 65001         # The port used by the server. s
        ADDRESS = (HOST, PORT)
        # sending message
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Connecting to {}...".format(ADDRESS))
            s.connect(ADDRESS)
            print("Connected.")
            logout_message = "Logout Successful"
            # Send a message for logout
            loginMsg = "Logout Successful!"
            s.sendall(loginMsg.encode())

            # Receive a message requesting for logout message
            data = s.recv(4096)
            print(data.decode())

            # send the logout message
            s.sendall(logout_message.encode())

            # receive success message
            data = s.recv(4096)

            print("{}", data.decode())

        print("Done.")
        return True

    def receiveMessageLogoutSocket(self, userName):
        pass


