# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:42:56 2021

@author: User
"""

import requests
import re
import time
import numpy as np
import json
import utils as ut
import pars_templates as ptmpl
import spyder_cian as sp


def test_read_json():
    data_str = ""
    
    with open("data/templates/template_cian2.json", "r", encoding="utf8") as f:  
        data_str = f.read()
    f.close()
    data_str = '['+data_str+']'
    
    json_data = json.loads(data_str)
    
    #for i in range(len(json_data)):
    #    print(json_data[i]['key'])
    print(json_data[len(json_data)-1]['value']['results']['totalOffers'])
    print(len(json_data[len(json_data)-1]['value']['results']['offers']))
    #get_json_data = json_data[len(json_data)-1]['value']['filters'] 
    #jj = json.dumps(get_json_data)

    #with open("data/templates/template_filters.json", "w", encoding="utf8") as f:
    #    f.write(str(jj))  
        
    #with open("data/templates/template_filters.json", 'w', encoding='utf8') as json_file:
    #    json.dump(get_json_data, json_file, ensure_ascii=False)    

#test_read_json()


def test_pars_json():
    #f = open("out/template_cian.json", "r")
    data_str = ""
    
    with open("out/sheet_1.txt", "r", encoding="utf8") as f:  
        data_str = f.read()
    f.close()
    
    start_json = '[{'
    stop_json = '}]'
    start_page = '"page1":'
    next_page = ',"page{}":'
    
    start_pos = '[{"key":'
    stop_pos = ':{}}];'      
    str_json = '[{"key":' + data_str[data_str.find(start_pos)+len(start_pos):data_str.find(stop_pos)].strip() + ':{}}]'
        
    start_pos = ',"offers":[{'
    stop_pos = ',"aggregatedOffers"'    
    offers_str = '[{' + str_json[str_json.find(start_pos)+len(start_pos):str_json.find(stop_pos)].strip()
    
    all_offers_str = start_json
    
    for i in range(1,3):
        if(i==1): all_offers_str+=start_page+offers_str 
        else: all_offers_str+=next_page.format(i)+offers_str   
        
    all_offers_str+=stop_json
    
    with open("out/data_cian.json", "w", encoding="utf8") as f:
        f.write(all_offers_str)     
    
    print("OK")
    #json_data = json.loads(offers_str)
    #print(len(json_data))

