# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 23:03:10 2022

@author: user
"""
import unittest
import week0503_testcase
class Test14(unittest.TestCase):
    def test(self):
        self.assertEqual(week0503_testcase.homework14(2, ['I have a pen I have an apple', 'Pen pineapple apple pen']), 'haveapenhaveanappleenpineappleapplepen\n3\n51\npineapple')
        self.assertEqual(week0503_testcase.homework14(5, ["There's a growing trend among teenagers", 'A dead duck does not fly backward', 'I would be delighted', "A song can make or ruin a person’s day", 'The pigs were insulted']), 'heresagrowingtrendamongteenagersdeadduckdoesnotflybackwardwouldbedelightedsongcanmakeorruinapersonsdayhepigswereinsulted\n5\n152\nteenagers')
        self.assertEqual(week0503_testcase.homework14(2, ['THE END OF THE WORLD', 'FINALE OF THE SHOW']), 'No lowercase letters\n31\n38\nFINALE')
        self.assertEqual(week0503_testcase.homework14(2, ['*&^$(*#&%*#&$^&%*@^&', '*&%#(*&#%(*&%Cry*$&%(&$%']), 'ry\n1\n44\n*&%#(*&#%(*&%Cry*$&%(&$%')
