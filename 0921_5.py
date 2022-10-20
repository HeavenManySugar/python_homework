# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 23:52:45 2022

@author: user
"""

class Solution():
    def __init__(self, heightCentimeter, weightKilogram):
        self.heightCentimeter = heightCentimeter
        self.heightMeter = heightCentimeter/100
        self.weightKilogram = weightKilogram
        self.bmi = weightKilogram / (self.heightMeter * self.heightMeter)
    
def main():
    sol = Solution(eval(input()), eval(input()))
    print(f'{sol.bmi:.1f}')
    
if __name__ == '__main__':
    main()