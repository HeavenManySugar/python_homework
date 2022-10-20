# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 01:03:40 2022

@author: user
"""
from math import sqrt

class Solution():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.x1 = ((-b)+sqrt(b*b-4*a*c))/(2*a)
        self.x2 = ((-b)-sqrt(b*b-4*a*c))/(2*a)
    def result(self):
        print(f'{self.x1:.1f}\n{self.x2:.1f}')
    
def main():
    sol = Solution(eval(input()), eval(input()), eval(input()))
    sol.result()
    
if __name__ == '__main__':
    main()