#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 14:00:09 2021

@author: gravicapa
"""

import spyder_cian as sp

class spyder_cnn_iface:
    
    def __init__(self, nums_thr = 1):
        
        self.spy_lst = []
        for i in range(nums_thr): self.spy_lst.append(sp.spyder_cian())
    
    def spy(self, spyder_num):
        jd = self.spy_lst[spyder_num].get_json_data()
        return jd