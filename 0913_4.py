# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 01:25:51 2022

@author: user
"""

class Solution():
    def __init__(self, price, x, y, z):
        self.price = price
        self.x = x
        self.y = y
        self.z = z
        self.ans = x*price[0]+y*price[1]+z*price[2]
    def result(self):
        print(f'{self.ans}')
    
def main():
    sol = Solution([380, 1200, 180], eval(input()), eval(input()), eval(input()))
    sol.result()
    
if __name__ == '__main__':
    main()