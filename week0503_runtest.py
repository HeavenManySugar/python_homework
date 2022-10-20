# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 23:03:10 2022

@author: user
"""

import coverage
import unittest

cov = coverage.coverage(branch=True, source=['week0503_testcase'])
cov.start()
suite = unittest.defaultTestLoader.discover("./", "week0503_testdriver.py") 
unittest.TextTestRunner().run(suite) 
cov.stop() 
cov.save() 
cov.report() 
cov.html_report(directory='cov') 