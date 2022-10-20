# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 09:13:25 2022

@author: user
"""

class Solution():
    def __init__(self, temperature, humidity, wind):
        self.temperature = int(temperature)
        self.humidity = int(humidity)
        self.wind = int(wind)
    def result(self):
        if self.temperature>=50:
            result = 18
        elif self.temperature<25:
            result = 'Today is cool'
        elif (self.temperature>=30 and self.wind==0) or self.humidity>=85:
            result = 24
        elif (25<=self.temperature<=29) and ((60<=self.humidity<=84 and self.wind==1)\
                                         or (self.humidity<60 and self.wind==0)):
            result = 27
        else:
            result = 'Today is cool'
        print(result)
    
def main():
    sol = Solution(input(), input(), input())
    sol.result()
    
if __name__ == '__main__':
    main()