# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 00:04:08 2022

@author: user
"""

class Solution():
    def __init__(self, A, B, x, y):
        self.A = A
        self.B = B
        self.x = x
        self.y = y
        self.C = A+B
        self.D = self.C.replace(x, y)
        self.E = self.D[:3] + self.D[-3:]
    def result(self):
        print(f'{len(self.C)+len(self.D)}\n{self.E*3}')
    
def main():
    sol = Solution(input(), input(), input(), input())
    sol.result()
    
if __name__ == '__main__':
    main()