# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 08:17:43 2022

@author: user
"""
class Solution():
    def __init__(self, appleNum, kiwiNum, pineappleNum):
        self.buyNum = {'apple':int(appleNum), 'kiwi':int(kiwiNum), 'pineapple':int(pineappleNum)}
        self.price = {'apple':30, 'kiwi':70, 'pineapple':40}
        self.fruitDiscount = {'apple':[1, 1, 0.95, 0.9, 0.8, 0.8], 'kiwi':[1, 1, 0.9, 0.85, 0.75, 0.75], 'pineapple':[1, 1, 0.85, 0.8, 0.8, 0.8]}
        self.discount30 = 0.87
    def result(self):
        priceTotal = 0
        buyTotal = 0
        for fruit in list(self.buyNum.keys()):
            if self.buyNum[fruit]<30:
                discount = self.fruitDiscount[fruit][int((self.buyNum[fruit]-1)/5)]
            else:
                discount = self.fruitDiscount[fruit][-1]
            priceTotal += self.buyNum[fruit]*self.price[fruit]*discount
        for num in list(self.buyNum.values()):
            buyTotal += num
        priceTotal *= self.discount30 if buyTotal>=30 else 1
        print(f'{int(priceTotal)}')
        
def main():
    sol = Solution(input(), input(), input())
    sol.result()
    
if __name__ == '__main__':
    main()