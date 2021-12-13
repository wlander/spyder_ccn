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

#def check_ccn():
def check_proxy_ccn():
    
    

def check_tor():
    prx.tor_re_connect()
    print(prx.tor_check_ip())
    time.sleep(3)
    prx.tor_re_connect()
    print(prx.tor_check_ip())

def test_proxy():
    
    prx = ut.proxy_distr()
    
    #for i in range(10):        
    print(prx.get_proxy(10))   