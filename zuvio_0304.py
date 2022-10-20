# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:37:58 2022

@author: user
"""
  
def middleNumber(a, b, c):
    d = [a, b, c]
    d.sort()
    return d[1]
    
print(middleNumber(123213, 1, 2))