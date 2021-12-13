#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 13:47:30 2021

@author: wlander
"""

import requests
from stem.control import Controller
from stem import Signal
from stem.util.log import get_logger
import random as rnd
import utils
from fake_useragent import UserAgent

logger = get_logger()
logger.propagate = False
 
uagent = UserAgent()
uagent.update()
          
class proxy_distr:
        
    def __init__(self):
        
        self.proxy_file = "data/proxy_full.txt"
        self.tor = True
        self.num_tor_reip = 3
        self.cnt_reip = 0        
        self.check_proxy_num = 100
        self.proxy_list = self.get_proxy_from_file(self.proxy_file)
        self.tor_proxy = {'http': 'socks5://localhost:9050', 'https': 'socks5://localhost:9050'}
        self.tor_paswwd = "1982god39"    
 
        self.uagent_file = "data/user_agents/user_agents.txt"
        self.uagent_list = self.get_proxy_from_file(self.uagent_file)
        self.ua_file = True
        
        
#reading proxy list file        
    def get_list_from_file(self, f):

        try:
            with open(f, "r") as file:
                lst = file.readlines()
                #print("list len: ",len(self.proxy_list))
            return lst
        except:
            utils.msgo.msg("error file opened", "def - get_list_from_file, class - proxy_distr")           
            return []

        
#get random along proxy        
    def get_proxy(self, num = None):
        
        if self.tor is False:
            if num is None:
                pr = self.proxy_list[rnd.randint(0, len(self.proxy_list))]
            else:
                pr = [self.proxy_list[rnd.randint(0, len(self.proxy_list))] for i in range(num)]
            
            pr = pr.replace('\n', '')
            return ({'http': 'http://'+pr, 'https': 'https://'+pr})
        else:
            self.cnt_reip+=1
            if (self.cnt_reip==self.num_tor_reip): self.tor_re_connect()
            return self.tor_proxy

            
    def get_header(self, num = None):
        
        if self.ua_file is False:
            if num is None:
                pr = self.uagent_list[rnd.randint(0, len(self.uagent_list))]
            else:
                pr = [self.uagent_list[rnd.randint(0, len(self.uagent_list))] for i in range(num)]
                
            pr = pr.replace('\n', '')
    
            return ({'User-Agent': pr})
        else:
            return ({'User-Agent': UserAgent().chrome})

            
#get and check out one proxy. it is locked while it wouldn't be check out    
    def get_check_proxy(self):
        
        pr = 0
        for i in range(self.check_proxy_num):
            pr = self.get_proxy()
            response = requests.get(pr)
            if(response.status_code!=200): break
        
        if(pr): return ({'http': pr, 'https': pr})
        else: return 0        

    
    def tor_re_connect(self):
        with Controller.from_port(port=9051) as c:
            c.authenticate(self.tor_paswwd)
            c.signal(Signal.NEWNYM)

    
    def tor_check_ip(self):
        s = self.get_tor_session()
        ip_str = s.get("http://checkip.dyndns.org").text
        s.close()
        #print("IP:", ip_str)
        return ip_str

    
    def get_tor_session(self):
        # инициализировать сеанс запросов
        session = requests.Session()
        # tor must be runned!
        session.proxies = self.tor_proxy
        return session    