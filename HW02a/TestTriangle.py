# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

   # Test for right triangles
    def testRightTriangles(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(8,6,10), 'Right', '8,6,10 should be a Right triangle')
        self.assertEqual(classifyTriangle(12,5,13), 'Right', '12,5,13 should be a Right triangle')
   

 # Test for isosceles triangles 
    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles', '2,2,3 should be Isosceles')
        self.assertEqual(classifyTriangle(10, 10, 5), 'Isoceles', '10,10,5 should be Isosceles')
 
   # Test for scalene triangles
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 should be Right triangle')
        self.assertEqual(classifyTriangle(5, 6, 7), 'Scalene', '5,6,7 should be Scalene')

  # Test for equilateral triangles
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    # Test for invalid input
    def testInvalidTriangles(self):
        self.assertEqual(classifyTriangle(10, 0, 5), 'InvalidInput', '10,0,5 should be InvalidInput')
        self.assertEqual(classifyTriangle(3, 2, 500), 'InvalidInput', 'Sides > 200 are invalid')
        self.assertEqual(classifyTriangle(2, -3, 4), 'InvalidInput', '2,-3,4 should be InvalidInput')
        self.assertEqual(classifyTriangle(9, 'x', 4), 'InvalidInput', 'Non-integer inputs are invalid')
        
    # Test for "Not a triangle" cases
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(3,4,7), 'NotATriangle', '3,4,7 should be NotATriangle')
        self.assertEqual(classifyTriangle(20,2,2), 'NotATriangle', '20,2,2 should be NotATriangle')





if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

