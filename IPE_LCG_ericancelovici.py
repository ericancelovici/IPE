# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 02:25:22 2018
Method of Linear Congruence 
IPE - ericancelovici
@author: eancelov
"""

def lcg(x):
    a = 22695477
    b = 1
    m = 2**32
    random = (a * x + b) % m
    if random <= 2**31:
        return 0
    else:
        return 1 
 

