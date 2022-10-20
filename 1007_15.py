# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 23:52:45 2022

@author: user
"""

class Solution():
    def __init__(self, name, weightKilogram, heightMeter):
        self.name = name
        #self.heightCentimeter = heightCentimeter
        #self.heightMeter = heightCentimeter/100
        self.heightMeter = heightMeter
        self.weightKilogram = weightKilogram
        self.bmi = weightKilogram / (self.heightMeter ** 2)
    
def main():
    a = Solution(input(), eval(input()), eval(input()))
    b = Solution(input(), eval(input()), eval(input()))
    print(f'Hi {a.name}, Your BMI: {a.bmi:.2f}{" too HIGH." if a.bmi>24 else " too LOW." if a.bmi<18.5 else "."}')
    print(f'Hi {b.name}, Your BMI: {b.bmi:.2f}{" too HIGH." if b.bmi>24 else " too LOW." if b.bmi<18.5 else "."}')
    print(f"{a.name if a.bmi>b.bmi else b.name}'s BMI is larger than {a.name if a.bmi<b.bmi else b.name}.")
    
if __name__ == '__main__':
    main()