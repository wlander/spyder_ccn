#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:03:10 2021

@author: gravicapa
"""

import time
import utils as ut
import pars_templates as ptmpl
import spyder_cian as sp
import proxxx
import tor_express as tr

tr.check_curr_ip()
tr.tor_reconnect()
time.sleep(3)
tr.check_curr_ip()

