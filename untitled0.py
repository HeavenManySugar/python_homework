# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:02:41 2022

@author: user
"""

def myPrint1(num):
    for x in range(1, num+1):
        for y in range(num, x, -1):

            s = '({0},{1})'.format(x,y)
            print(s, end=';')
        for y in range(1, 2*x, 1):
            s = '({0},{1})'.format(x,y)

            print(s, end=',')
        print()
myPrint1(4)
