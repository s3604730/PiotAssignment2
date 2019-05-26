#!/usr/bin/env python3
import json
import os
from SocketPi.MasterPiSocket import MasterPiSocket

from SocketPi.ReceptionPiSocket import ReceptionPiSocket
#get relative path
path = os.path.abspath(os.path.dirname(__file__))
os.chdir(path)



  

 
from classList.Menu import Menu


class Main():
    def __init__(self):
        Menu()


Main()
