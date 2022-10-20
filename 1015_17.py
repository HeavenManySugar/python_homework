# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 23:35:49 2022

@author: user
"""

class Solution():
    def __init__(self, drawType, n):
        self.drawType = drawType
        self.n = n
        self.function = {1: self.type1, 2: self.type2, 3: self.type3}
    def type1(self, cur):
        return ''.join(map(str, range(1, cur+2)))+''.join(map(str, range(cur, 0, -1)))
    def type2(self, cur):
        return '_'*(self.n-cur-1)+self.type1(cur)+'_'*(self.n-cur-1)
    def type3(self, cur):
        return self.type2(self.n-cur-1)
    def result(self):
        for i in range(self.n):
            print(self.function[self.drawType](i))  
    
def main():
    sol = Solution(int(input()), int(input()))
    sol.result()
    
if __name__ == '__main__':
    main()
