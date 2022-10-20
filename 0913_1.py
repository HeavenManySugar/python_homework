# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 00:36:59 2022

@author: user
"""

class Students:
    def __init__(self, name: str, std_id: str, score_list: list):
        self.name = name
        self.std_id = std_id
        self.score_list = score_list
        self.total = 0
        
    def output(self):
        print(f'Name:{self.name}\nID:{self.std_id}')
        for score in self.score_list:
            self.total += score
        print(f'Average:{self.total//3}\nTotal:{self.total}')

def main():
    std = Students(input(), input(), [eval(input()), eval(input()), eval(input())])
    std.output()
    
if __name__ == '__main__':
    main()