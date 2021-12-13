# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 10:39:35 2021

@author: User
"""

import requests
from stem.control import Controller
from stem import Signal
import time
from stem.util.log import get_logger  

logger = get_logger()
logger.propagate = False
      
tor_proxy = {'http': 'socks5://localhost:9050', 'https': 'socks5://localhost:9050'}
tor_paswwd = "1982god39"

def get_tor_session():
    # инициализировать сеанс запросов
    session = requests.Session()
    # tor must be runned!
    session.proxies = tor_proxy
    return session

def tor_reconnect():
    with Controller.from_port(port=9051) as c:
        c.authenticate(tor_paswwd)
        c.signal(Signal.NEWNYM)

def check_curr_ip():
    s = get_tor_session()
    ip_str = s.get("http://checkip.dyndns.org").text
    s.close()
    #print("IP:", ip_str)
    return ip_str


#check_curr_ip()
#subprocess.call(['.././tor_reip.sh'])
#tor_reconnect()
#time.sleep(3)
#check_curr_ip()
#tor_reconnect()
#time.sleep(3)
#check_curr_ip()

#renew_connection()
#get_ip_test()



