# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 22:45:42 2022

@author: user
"""

class Solution():
    def __init__(self, m, n, a, b):
        self.m = int(m)
        self.n = int(n)
        self.a = int(a)
        self.b = int(b)
        self.alist = self.calList(self.a)
        self.blist = self.calList(self.b)
    def calList(self, x):
        xlist = []
        for i in range(self.m, self.n+1, x):
            xlist.append(i)
        return xlist
    def result(self):
        total = 1
        for i in self.blist:
            total *= i
        print(f'{sum(self.alist)}\n{total}')
    
def main():
    sol = Solution(input(), input(), input(), input())
    sol.result()
    
if __name__ == '__main__':
    main()