#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:45:58 2021

@author: gravicapa
"""

import sys
import requests
import time
import logging
import random as rnd
from pars_templates import url_headers

class Msg_out:
    def __init__(self, out_type):  
        self.out_type = out_type
        self.file_log = "log.out"
        
    def msg(self, msg, src):
        if self.out_type=="console":
            print(msg)
        elif self.out_type=="log":
            try:
                #try open file for log
                print("Log to file will be here soon!")
            except: FileNotFoundError


    def set_file_log(self, fl):
        self.file_log  = fl
        
msgo = Msg_out("console") 


def timer(f):
    def wrap_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        delta = time.time() - start
        print (f'Время выполнения функции {f.__name__} составило {delta} секунд')
        return result
    return wrap_timer

    def msg(self, msg, src):
        if self.out_type=="console":
            print(msg)
        elif self.out_type=="log":
            try:
                #try open file for log
                print("Log to file will be here soon!")
            except: FileNotFoundError

def log(f):
    def wrap_log(*args, **kwargs):
        logging.info(f"Запущена функция {f.__doc__}")
        result = f(*args, **kwargs)
        logging.info(f"Результат: {result}")
        return result
    return wrap_log

logging.basicConfig(level=logging.INFO)


def get_header():
    return url_headers[rnd.randint(0, len(url_headers)-1)]    
         
    