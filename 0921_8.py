# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 00:18:40 2022

@author: user
"""

class Solution():
    def __init__(self, FullName, yyyymmdd):
        self.FullName = FullName
        self.FirstName = FullName.split(' ')[0]
        self.LastName = FullName.split(' ')[1]
        self.yyyymmdd = yyyymmdd
        self.yyyy = yyyymmdd.split('/')[0]
        self.mm = yyyymmdd.split('/')[1]
        self.dd = yyyymmdd.split('/')[2]
    def result(self):
        print(f'{self.FirstName} is born at year {self.yyyy} month {self.mm} day {self.dd} in {self.LastName} family.')
    
def main():
    sol = Solution(input(), input())
    sol.result()
    
if __name__ == '__main__':
    main()