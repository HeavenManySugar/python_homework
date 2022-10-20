# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 23:01:06 2022

@author: user
"""

class Solution():
    def __init__(self, istr):
        self.istr = istr
        self.lower = ''
        self.upper = 0
        self.strsplit = self.istr.split()
        self.strlen = len(self.istr)
        self.longest = ''
        self.init()
    def init(self):
        for elem in self.istr:
            if elem.islower():
                self.lower += elem
            elif elem.isupper():
                self.upper += 1
        for elem in self.strsplit:
            if len(elem)>len(self.longest):
                self.longest = elem
    
def homework14(n, str_in):
    lower = ''
    upper = 0
    lenTotal = 0
    longest = ''
    for i in range(n):
        sol = Solution(str_in[i])
        lower += sol.lower
        upper += sol.upper
        lenTotal += sol.strlen
        if len(sol.longest)>len(longest):
            longest = sol.longest
    
    return f'{"No lowercase letters" if len(lower) == 0 else lower}\n{upper}\n{lenTotal}\n{longest}'
