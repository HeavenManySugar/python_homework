# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:47:22 2022

@author: user
"""

def printOneRow(m, n, s, mark):
    for y in range(m, n, s):
        if mark.isdigit():
            print(y, end='')
        else:
            print(mark, end='')
            
def sol(n):
    for i in range(n):
        printOneRow(2*(n-i-1), -1, -2, '0')
        if i!=n-1:
            printOneRow(0, 1, 1, '#')
        print()
        
sol(5)
'''
def sol(n):
    ans = ''
    temp = ''
    lastn = 1
    for i in range(n):
        temp = str(lastn) + temp 
        lastn = lastn+lastn
        if i == 0: 
            ans = temp + '\n' + ans
        else:
            ans = temp + '#\n' + ans
    printOneRow(0, 1, 1, ans)
    
sol(4)
'''
'''
def sol(n):
    if n == 1:
        print(n)
        return
    
    num = n
    while num>=0:
        if num >= 1:
            printOneRow(num, num+1, 1, '0')
        else:
            printOneRow(0, 1, 1, '#')
            break
        num = num//2
    print()
    sol(n//2)
sol(8)
'''
