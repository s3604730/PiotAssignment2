#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

# DISCLAIMER, REFERENCED BY echo_client.py AND echo_server.py BY RMIT
import socket
from AbstractSocket import AbstractSocket

# class for reception pi based on abstract


class ReceptionPiSocket(AbstractSocket):
    def __init__(self):
        pass
    # send message from reception pi to master pi

    def sendMessageLoginSocket(self, userName):
        HOST = "10.132.132.187"  # The server's hostname or IP address.
        PORT = 65000         # The port used by the server. s
        ADDRESS = (HOST, PORT)

        # sending message
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Connecting to {}...".format(ADDRESS))
            s.connect(ADDRESS)
            print("Connected.")


            # Send a message for login successful
            yeet = "Login Successful!"
            s.sendall(yeet.encode())

            # Receive a message requesting for Username
            data = s.recv(4096)
            print(data.decode())

            # send the username
            s.sendall(userName.encode())

            # receive success message
            data = s.recv(4096)

            print("{}", data.decode())

        print("Done.")

    # abstract method, skip because reception pi doesn't do this
    def receiveMessageLoginSocket(self, userName):
        pass
    # abstract method, skip because reception pi doesn't do this

    def sendMessageLogoutSocket(self, userName):
        pass

    # reception pi receives the logout message and the username
    def receiveMessageLogoutSocket(self, userName):
        # Empty string means to listen on all IP's on the machine, also works with IPv6.
        HOST = ""

        # Note "0.0.0.0" also works but only with IPv4.
        PORT = 65000  # Port to listen on (non-privileged ports are > 1023).
        ADDRESS = (HOST, PORT)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(ADDRESS)
            s.listen()
            # waiting to receive a message from any address at port 65000

            print("Listening on {}...".format(ADDRESS))
            conn, addr = s.accept()
            with conn:
                # when a connection has been connected to
                print("Connected to {}".format(addr))
                data = conn.recv(4096)
                # get username variable
                userName = data.decode()
                print(userName)

                while True:
                    # receive the message sent
                    data = conn.recv(4096)
                    if(not data):
                        break
                    # print decoded message
                    print("Received {} bytes of data decoded to: '{}'".format(
                        len(data), data.decode()))
                    # send back a message to indicate that the logout message has been received
                    print("Sending data back.")
                    conn.sendall(data)

                print("Disconnecting from client.")
            print("Closing listening socket.")
        print("Done.")
