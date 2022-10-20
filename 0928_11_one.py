# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 00:37:23 2022

@author: user
"""

(lambda classInfo:(lambda classInfo, className, classTime:[[(print(f'{className[i]} and {className[j]} conflict on {list(classTime[i]&classTime[j])[0]}') if len(classTime[i]&classTime[j]) else 0) for j in range(i+1, 3)] for i in range(3)])(classInfo, list(classInfo.keys()), list(classInfo.values())))(dict([(lambda index:[index, {input() for j in range(int(input()))}])(input()) for i in range(3)]))