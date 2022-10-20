# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 21:13:04 2022

@author: user
"""

import math
'''
def isPrime(n):
    if n==2 or n==3:
        return True
    elif n>4:
        m = n % 6
        if m != 1 and m!=5: #prime must be 6n+1 or 6n+5
            return False
        for i in range(5, math.sqrt(n), 6):
            if n%i==0 or n%(i+2)==0: #n%i:6n+5 n%(i+2):6n+1
                return False
        return True
    else:
        return False
'''
def createPrimeList(n):
    prime = []
    primeBool = [True]*(n)
    primeBool[0] = False
    primeBool[1] = False
    for i in range(int(math.sqrt(n))):
        if(primeBool[i]):
            for j in range(i*i, n, i):
                primeBool[j] = False
    for i in range(n):
        if(primeBool[i]):
            prime.append(i)
    return prime

print(sum(createPrimeList(int(input())+1)))