# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 00:14:56 2022

@author: user
"""

class Solution():
    def __init__(self, drawType, n):
        self.drawType = drawType
        self.n = n
        self.function = {1: self.type1, 2: self.type2, 3: self.type3}
    '''
    def genNumber(self, cur, ntype):
        cur += (ntype+1)
        if cur%2:
            return ''.join(map(str, range(self.n, 0, -1)))
        else:
            return ''.join(map(str, range(1, self.n+1)))
    '''
    def type1(self, cur):
        underscore = '_'*(self.n-1)
        #number = self.genNumber(cur, 1)
        if cur%2:
            number = ''.join(map(str, range(self.n, 0, -1)))
        else:
            number = ''.join(map(str, range(1, self.n+1)))
        return underscore[:(self.n-1-cur)] + number[:] + underscore[(self.n-1-cur):]
    def type2(self, cur):
        return self.type1(cur)[::-1]
        '''
        underscore = '_'*(self.n-1)
        number = self.genNumber(cur, 2)
        return underscore[(self.n-1-cur):] + number[:] + underscore[:(self.n-1-cur)]
        '''
    def type3(self, cur):
        number = ''.join(map(str, range((self.n//2+1), 0, -1))) + ''.join(map(str, range(2, (self.n//2+1)+1)))
        halfN = self.n//2
        magicNumber = max((min(cur, halfN)-cur//(halfN)*(cur-halfN)), 0)
        underscore = '_' * magicNumber
        return underscore + number[magicNumber:self.n-magicNumber] + underscore
    def result(self):
        if self.drawType == 3 and self.n%2 == 0:
            print('ERROR')
            return
        for i in range(self.n):
            print(self.function[self.drawType](i))  
    
def main():
    sol = Solution(int(input()), int(input()))
    sol.result()
    
if __name__ == '__main__':
    main()
