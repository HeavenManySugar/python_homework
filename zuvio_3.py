# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 16:35:29 2022

@author: user
"""

def calc(number, birth):
    result = (number*2+5)*50+1770-birth
    return result//100, result%100

print(calc(3, 2004))
