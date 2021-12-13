# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 10:39:35 2021

@author: User
"""

import requests
import socks
import socket
from bs4 import BeautifulSoup
from stem.control import Controller
from stem import Signal
import subprocess

def get_tor_session():
    # инициализировать сеанс запросов
    session = requests.Session()
    # установка прокси для http и https на localhost: 9050
    # для этого требуется запущенная служба Tor на вашем компьютере и прослушивание порта 9050 (по умолчанию)
    session.proxies = {"http": "socks5://localhost:9050", "https": "socks5://localhost:9050"}
    return session

def renew_connection():
    with Controller.from_port(port=9051) as c:
        c.authenticate("1982god39")
        # отправить сигнал NEWNYM для установления нового чистого соединения через сеть Tor
        c.signal(Signal.NEWNYM)

def checkIP():
    ip = requests.get('http://checkip.dyndns.org').content
    soup = BeautifulSoup(ip, 'html.parser')
    print(soup.find('body').text)

#socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
#socket.socket = socks.socksocket
#checkIP()

def get_ip_test():
    s = get_tor_session()
    ip = s.get("http://checkip.dyndns.org").text
    print("IP:", ip)
    s.close()

get_ip_test()
#subprocess.call(['.././tor_reip.sh'])
renew_connection()
get_ip_test()



