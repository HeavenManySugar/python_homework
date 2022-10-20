# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 23:06:17 2022

@author: user
"""

times = 3

class Solution():
    def __init__(self, classInfo):
        self.classInfo = classInfo
    def reslut(self):
        keys = list(self.classInfo.keys())
        values = list(self.classInfo.values())
        for i in range(times-1):
            for j in range(i+1, times):
                #print(len(values[i]&values[j]))
                conflict = values[i]&values[j]
                if len(conflict):
                    print(f'{keys[i]} and {keys[j]} conflict on ', end='')
                    for elem in conflict:
                        print(elem, end='')
    
def main():
    classInfo = dict()
    for i in range(times):
        index = input()
        classInfo[index] = set()
        loop = int(input())
        for j in range(loop):
            classInfo[index].add(input())
    #classInfo = {'1001': {'13', '12', '11'}, '1002': {'23', '21', '22'}, '1003': {'32', '31', '13'}}
    
    sol = Solution(classInfo)
    sol.reslut()
    
if __name__ == '__main__':
    main()