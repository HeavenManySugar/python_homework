# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:31:47 2022

@author: user
"""
"""
def opAirConOn(temperature, wind, humidity):
    return '開冷氣' if temperature>30 and wind==0 or humidity>85 else '不開冷氣'

print(opAirConOn(32, 0, 50))
print(opAirConOn(28, 0, 90))
print(opAirConOn(25, 0, 70))
print(opAirConOn(31, 1, 80))
"""

def opAirConOn(temperature, wind, humidity):
    return '開冷氣' if temperature>30 and wind==0 or humidity>85 else ''

print(opAirConOn(32, 0, 50))
print(opAirConOn(28, 0, 90))
print(opAirConOn(31, 1, 87))
