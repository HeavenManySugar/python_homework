# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 00:53:58 2022

@author: user
"""

class Solution():
    def __init__(self, n):
        self.n = n
    ### from 1007_17 HomeWork
    #def type1(self, cur):
    def draw(self, cur, size, char):
        return char * (cur*2+1) if cur<size//2+1 else char * ((size-cur-1)*2+1)
    #def dot(self, cur):
    def space(self, cur, size):
        return ' ' * int(abs(size//2-cur)%(size//2+1)) * 2
    ### have some change
    def drawTail(self, cur, size, char):
        if cur == 0 or cur == size-1:
            return ''
        else:
            tcur = cur-1
            tsize = size-2
            return self.space(cur, size) + self.space(tcur, tsize) + self.draw(tcur, tsize, char)
    def drawFish(self, cur, size, char):
        return self.space(cur, size) + self.draw(cur, size, char) + self.draw(cur, size, char)[1:]
    def result(self):
        if self.n%2==0:
            print('ERROR')
            return
        for i in range(self.n):
            print(self.drawFish(i, self.n, '*')+self.drawTail(i, self.n, '+'))  
    
def main():
    sol = Solution(int(input()))
    sol.result()
    
if __name__ == '__main__':
    main()
