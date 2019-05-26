# Programming Internet Of Things Assignment 2
Smart Library
Application for book borrowing service which uses two raspberry pi's to communicate through sockets.<br/>
Written in Python.

# Authors
Tony Tran<br/>
Woon Ye Wyn<br/>
Harry Le<br/>
Robin Kwan<br/>

# Hardware Used
* 2x Raspberry Pi 3 B+
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
* Configure MasterPiSocket.py and ReceptionPiSocket.py to both pi's private ip
* Run consoleMain.py and enter authentication key given from browser prompt
* Run consoleMain.py on the reception Pi and main.py on the master pi.
* The reception pi remains idle while the user interacts with the master pi
* For admin privileges, run flask_main.py 



# Trello Link:
* https://trello.com/b/9jqOaddC/piotassignment2
# Github Link:
* https://github.com/s3604730/PiotAssignment2
# Flask Link:
* https://github.com/harryleau/flask-app-iot
