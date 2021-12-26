# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:42:56 2021

@author: User
"""
#import sys
#sys.path.append("../")
import requests
import re
import time
import numpy as np
import json
import utils as ut
import pars_templates as ptmpl
import spyder_cian as sp
import proxxx


url = 'https://cian.ru'

prx = proxxx.proxy_distr()
spy = sp.spyder_cian()
hd = ut.get_header()


def check_spy_ccn():
    
    num_pages = spy.get_pages_info()
    print("num_pages: ", num_pages)
    
    for p in range(3):
        time.sleep(np.random.randint(5,10))
        stat = spy.get_page_offers(p)
        print("stat: ", stat, ", page: ", p)

check_spy_ccn()
#spy.write_offers_to_file_as_json()
  



#def check_ccn():
def check_proxy_ccn():
    for i in range(10):   
        print(spy.proxy_d.get_proxy())
        time.sleep(1) 
        
    
def check_tor():
    prx.tor_re_connect()
    print(prx.tor_check_ip())
    time.sleep(3)
    prx.tor_re_connect()
    print(prx.tor_check_ip())

def test_proxy():   
    prx = ut.proxy_distr()  
    for i in range(10):    
        time.sleep(3)
        print(prx.get_proxy())   

#check_proxy_ccn()
    
#rsp = spy.get_reguest(0, ut.get_header())
#r = requests.get("https://nazarklinok.ru/", headers = ut.get_header(), proxies = spy.proxy_d.get_proxy())
#print(str(rsp.status_code))
#print(r.text, utf-8)