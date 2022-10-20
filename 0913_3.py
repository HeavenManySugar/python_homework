# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 01:14:58 2022

@author: user
"""

class Solution():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.sum = num1 + num2
        self.diff = num1 - num2
        self.prod = num1 * num2
        self.quot = num1 / num2
        self.result_name = ['Sum', 'Difference', 'Product', 'Quotient']
        self.result_value = [self.sum, self.diff, self.prod, self.quot]
    def result(self):
        for i in range(len(self.result_name)):
            print(f'{self.result_name[i]}:{self.result_value[i]:.2f}')
    
def main():
    sol = Solution(eval(input()), eval(input()))
    sol.result()
    
if __name__ == '__main__':
    main()