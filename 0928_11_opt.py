# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 23:06:17 2022

@author: user
"""

times = 3

class Solution():
    def __init__(self, classInfo):
        self.classInfo = classInfo
        self.classTime = [0]*60
        self.className = list(classInfo.keys())
    def reslut(self):
        for i in range(times):
            index = self.className[i]
            for elem in self.classInfo[index]:
                if(self.classTime[int(elem)]):
                    print(f'{self.classTime[int(elem)]} and {index} conflict on {elem}')
                else:
                    self.classTime[int(elem)] = int(self.className[i])
                    
def main():
    #classInfo = {'1001': {'13', '12', '11'}, '1002': {'23', '21', '22'}, '1003': {'32', '31', '13'}}
    
    classInfo = dict()
    for i in range(times):
        index = input()
        classInfo[index] = list()
        hours = int(input())
        for j in range(hours):
            classInfo[index].append(input())
    
    sol = Solution(classInfo)
    sol.reslut()
    
if __name__ == '__main__':
    main()