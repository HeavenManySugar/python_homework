# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 09:27:48 2022

@author: user
"""

print((lambda temperature, humidity, wind:18 if temperature>=50 else 'Today is cool' if temperature<25 else 24 if (temperature>=30 and wind==0) or humidity>=85 else 27 if (25<=temperature<=29) and ((60<=humidity<=84 and wind==1) or (humidity<60 and wind==0)) else 'Today is cool')(int(input()), int(input()), int(input())))