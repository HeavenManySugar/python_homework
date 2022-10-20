# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 15:14:56 2022

@author: user
"""

#(lambda x, y: print(f'Name:{x[0]}\nID:{x[1]}\nAverage:{sum(y)//3}\nTotal:{sum(y)}'))([input(), input()], [eval(input()), eval(input()), eval(input())])
o = list(map(print, (lambda x, y, z: (lambda a, b: [f'{a[i]}:{b[i]}' for i in range(len(a))])(z, (lambda c, d: [c[0], c[1], d//3, d])(x, sum(y))))([input(), input()], [eval(input()), eval(input()), eval(input())], ['Name', 'ID', 'Average', 'Total'])))
