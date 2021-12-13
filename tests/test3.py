#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 08:53:49 2021

@author: wlander
"""

import stem
from stem import Signal
from stem.control import Controller
from stem.connection import connect
import time
#
# Create a new controller 
#
controller = Controller.from_port()
Password = "1982god39"
#
def renew_tor():
    global controller
    global Password
    print ('Renewing Tor Circuit')
    if "stem.control.Controller" not in str(controller):
      #if global controller exist no more
      controller = Controller.from_port()
    # debug output
    print (controller)
    # authenticare the connection with the server control port 
    controller.authenticate(Password)
    print ('Tor running version is : %s' % controller.get_version() )
    # force a new circuit
    controller.signal(Signal.NEWNYM)
    # wait for new circuit
    time.sleep(10)
    print ('New Tor circuit estabilished')



if __name__ == "__main__":
    for i in range (10):
      print ( " Attempt n. : %i " % i)  
      renew_tor()
