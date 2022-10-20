# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 00:06:09 2022

@author: user
"""

clas=[i*0 for i in range(60)]
time=3
for i in range(time):
    classname=int(input())
    h=int(input())
    for j in range(h):
        ct=int(input())
        if clas[ct]==0:
            clas[ct]=classname
        else:
            print(str(clas[ct])+" and "+str(classname)+" conflict on "+str(ct))