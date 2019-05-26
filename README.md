# Programming Internet Of Things Assignment 2
Smart Library
Application for book borrowing service which uses two raspberry pi's to communicate through sockets.
Written in Python.

# Authors
Tony Tran<br/>
Woon Ye Wyn<br/>
Harry Le<br/>
Robin Kwan<br/>

# Hardware Used
* 2x Raspberry Pi 3 b+
* Microsoft LifeCam HD-3000

# Software Used
* Flask
* OpenCV
* Sphinx
* MySQL Database
* Google Data Studio
* Google Cloud Platform
* Google Calendar API(Python)

# Packages Installation Instructions
* pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
* pip3 install flask flask_sqlalchemy flask_marshmallow marshmallow-sqlalchemy
* sudo apt-get install mysql-server python-mysqldb
* pip3 install sphinx==1.6.6
* https://www.pyimagesearch.com/2017/10/09/optimizing-opencv-on-the-raspberry-pi/
* python3 -m pip install PyMySQL

# How To Run It
* Run consoleMain.py and then run main.py on the pi. ConsoleMain will remain idle while the user interacts with the menu in main.py.
