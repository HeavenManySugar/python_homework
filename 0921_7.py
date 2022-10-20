# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 00:15:19 2022

@author: user
"""

class Solution():
    def __init__(self, sentence, vocabulary):
        self.sentence = sentence
        self.vocabulary = vocabulary
        self.sentenceSplit = sentence.split(vocabulary)
    def result(self):
        print(f'{len(self.sentence)}\n{self.sentenceSplit}')
    
def main():
    sol = Solution(input(), input())
    sol.result()
    
if __name__ == '__main__':
    main()