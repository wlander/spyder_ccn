#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:23:26 2021

@author: gravicapa
"""
import requests
import re
import time
import numpy as np
import json
import pars_templates as pt 
import utils
import proxxx as prx

class spyder_cian:

    
    def __init__(self, proxy_file = None):
        
        self.proxy_d = prx.proxy_distr()
        
        if isinstance(proxy_file, str):  self.proxy_d = prx.proxy_distr(proxy_file)
        else: self.proxy_d = prx.proxy_distr()
        
        self.fillter_cian = custom_filter_cian()
        self.pages_info = {'total_num_pages': 0, 'total_offers': 0, 'page_len': 0, 'page_data': "0"} 
        self.offers_list = []

        
    def get_json_data(rsp):
        
        data_str = rsp.text                
        str_json = pt.json_start + data_str[data_str.find(pt.json_start)+len(pt.json_start):data_str.find(pt.json_stop)].strip() + ':{}}]'             
        return json.loads(str_json)
 
       
    def get_reguest(self, num_page, header = utils.get_header(), prox = None):
        
        set_url = pt.base_url+pt.custom_req_url
        
        hr = header
        if header is None: hr = pt.url_headers[0] #if header is undefined - header = define header
        
        if prox is not None: response = requests.get(set_url.format(num_page), headers=hr, proxies=prox)
        else: response = requests.get(set_url.format(num_page), headers=hr)        

        if(response.status_code==200):
            return response            
        else:
            utils.msgo.msg("response.status_code: " + response.status_code, ", def - get_page_data")          
            return 0

        
    def get_page_data(self, response):
            
        data_str = response.text
                
        str_json = pt.json_start + data_str[data_str.find(pt.json_start)+len(pt.json_start):data_str.find(pt.json_stop)].strip() + ':{}}]'             
            
        offers_str = pt.open_json + str_json[str_json.find(pt.offers_start)+len(pt.offers_start):str_json.find(pt.offers_stop)].strip()
            
        return offers_str

    def offer_check_filter(self, offer):
        
        dt = str(offer['creationDate'])
        dt = dt.partition('T')[0]
        
        if(dt>self.fillter_cian.base_filter['creationDate']):
            if(self.fillter_cian.base_filter['sort']=='creation_date_desc'): return 2
            else: return 1
        
        return 0

    
    def get_pages_info(self):
        
        #get first page
        rsp = self.get_reguest(0, utils.get_header(), self.proxy_d.get_proxy())
        total_num_pages = 0
                
        if rsp!=0:
            
            json_data = self.get_json_data(rsp)       
            sign_num =  len(json_data)-1              
            total_offers = json_data[sign_num]['value']['results']['totalOffers']   #num total offers from json           
            page_len = len(json_data[sign_num]['value']['results']['offers'])       #num offers in the page
            total_num_pages = int(total_offers/page_len)   #calcultate num pages  
            
            #saving of first page data into gloabal class value 
            self.pages_info =  {'total_num_pages': total_num_pages, 'total_offers': total_offers, 'page_len': page_len, 'page_data': json_data} 
            
        return total_num_pages

    
    def get_page_offers(self, p):
    
        rsp = self.get_reguest(p, utils.get_header(), self.proxy_d.get_proxy())
                    
        if rsp!=0:
                        
            json_data = self.get_json_data(rsp)
            sign_num =  len(json_data)-1
            page_len = len(json_data[sign_num]['value']['results']['offers'])
                        
            for p in range(page_len):
                flf = self.offer_check_filter(json_data[sign_num]['value']['results']['offers'][p])
                if(flf==2): return 1
                elif(flf==0): self.offers_list.append(json_data[sign_num]['value']['results']['offers'][p])          
        
            return 1
    
        return 0
    
   
    def spyder_all_pages(self):
                                          
        self.get_pages_info()
        
        if(self.pages_info['page_len']>0):
            
            sign_num =  len(self.pages_info['data'])-1 
            #first page to the out list with check filter out
            for p in range(self.pages_info['page_len']):
                flf = self.offer_check_filter(self.pages_info['data'][sign_num]['value']['results']['offers'][p])
                if(flf==2): return 1
                elif(flf==0): self.offers_list.append(self.pages_info['data'][sign_num]['value']['results']['offers'][p])    
            
            if(self.pages_info['total_num_pages']>1):
                
                for p in range(1,self.pages_info['total_num_pages']):
                    self.get_page_offers(p)
                
                return 1
            
        return 0


    
class custom_filter_cian:

    
    def __init__(self):   
        
        self.base_filter = {'region': "4885", 'deal_type': "sale", 'offer_type': "flat",\
                            'creationDate': "2021-10-01", 'price': 0, 'sort':"creation_date_desc"}

        self.room = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 9:1}
        
        self.custom_req_url = 'deal_type=%s&engine_version=2&offer_type=%s&p=%d&region=%s\
            &room1=%d&room2=%d&room3=%d&room4=%d&room5=%d&room6=%d&room7=%d&room9=%d&sort=%s'
            
        
        self.url_cian = self.set_url()

        
    def set_url(self, page=1):
        
        p = page
        if(page<2): p = 1
        
        create_url =  pt.base_url + (self.custom_req_url % (self.base_filter['deal_type'], self.base_filter['offer_type'], p,\
                                    self.base_filter['region'], self.room[1],  self.room[2], self.room[3],\
                                    self.room[4], self.room[5], self.room[6], self.room[7], self.room[9], self.base_filter['sort']))
        
        if(p==1): create_url = create_url.replace('&p=1', '')                              
        
        self.url_cian = create_url
        
        return create_url
    
        #print(self.url_cian, "/ ", p)