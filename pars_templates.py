#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:36:14 2021

@author: gravicapa
"""

import json

base_url = 'https://nn.cian.ru/cat.php?'

custom_req_url = 'deal_type=sale&engine_version=2&offer_type=flat&p={}&region=4885\
&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&room7=1&room9=1&sort=creation_date_desc'

url_headers = [
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'},
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.13'}
    ]


open_json = '[{'
close_json = '}]'

first_page = '"page1":'
next_page = ',"page{}":'

json_start = '[{"key":'
json_stop = ':{}}];'

offers_start = ',"offers":[{'
offers_stop = ',"aggregatedOffers"'

#template json custom filter from cian (filter field from cian json)
with open("/home/gravicapa/projects/spyders/projects/spyder_ccn/data/templates/template_filters.json", "r", encoding="utf8") as f:  
    custom_filter_cian = json.loads(f.read())
    f.close()



