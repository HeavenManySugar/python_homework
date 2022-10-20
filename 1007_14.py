# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 23:01:06 2022

@author: user
"""

class Solution():
    def __init__(self, istr):
        self.istr = istr
    def result(self):
        lower = ''
        upper = 0
        strsplit = self.istr.split()
        strlen = len(self.istr)
        longest = ''
        for elem in self.istr:
            if elem.islower():
                lower += elem
            elif elem.isupper():
                upper += 1
        for elem in strsplit:
            if len(elem)>len(longest):
                longest = elem
        return (lower, upper, strlen, longest)
    
def main():
    n = int(input())
    lower = ''
    upper = 0
    lenTotal = 0
    longest = ''
    for i in range(n):
        sol = Solution(input())
        result = sol.result()
        lower += result[0]
        upper += result[1]
        lenTotal += result[2]
        if len(result[3])>len(longest):
            longest = result[3]
    
    print(f'{"No lowercase letters" if len(lower) == 0 else lower}\n{upper}\n{lenTotal}\n{longest}')
    
if __name__ == '__main__':
    main()