# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:37:27 2022

@author: user
"""

def mySum(m, n, step):
    sum = 0
    for i in range(m, n+1, step):
        sum += i
    return sum 
def main():
    m = int(input("Input a min number:"))
    n = int(input("Input a max number:"))
    step = int(input("Input a step number:"))
    main_sum = mySum(m, n, step)
    print('sum (%d ~ %d)= %d' %(m, n, main_sum))
main()