# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 23:40:56 2022

@author: user
"""

class Solution():
    def __init__(self, drawType, n):
        self.drawType = drawType
        self.n = n
    def type1(self, cur):
        #return '*' * (cur+1) if cur<self.n//2+1 else '*' * int(self.n//2-cur%(self.n//2+1))
        return '*' * (cur+1) if cur<self.n//2+1 else '*' * self.n-cur
    def dot(self, cur):
        return '.' * int(abs(self.n//2-cur)%(self.n//2+1))
    def type2(self, cur):
        return self.dot(cur) + self.type1(cur)
    def type3(self, cur):
        return self.type2(cur) + self.type1(cur)[1:] + self.dot(cur)
    def result(self):
        if(self.drawType == 1):
            function = self.type1
        elif(self.drawType == 2):
            function = self.type2
        else:
            function = self.type3
        for i in range(self.n):
            print(function(i))
    
def main():
    sol = Solution(int(input()), int(input()))
    if bool(sol.n%2):
        sol.result()
    else:
        print('ERROR')
    
if __name__ == '__main__':
    main()
