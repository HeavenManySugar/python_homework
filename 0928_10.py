# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 08:45:50 2022

@author: user
"""

class Solution():
    def __init__(self, playerCards):
        cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0.5, 0.5, 0.5]
        self.cardPoints = dict(zip(cards, points))
        self.playerCards = playerCards
    def result(self):
        point = [0, 0]
        for playerIndex in range(len(self.playerCards)):
            for card in self.playerCards[playerIndex]:
                point[playerIndex] += self.cardPoints[card]
            if point[playerIndex]>10.5:
                point[playerIndex] = 0
            print(point[playerIndex])
        print('A Win' if point[0]>point[1] else 'B Win' if point[0]<point[1] else 'Tie')
def main():
    playerCards = [list(), list()]
    for i in range(2):
        for j in range(3):
            playerCards[i].append(input())
    sol = Solution(playerCards)
    sol.result()
    
if __name__ == '__main__':
    main()