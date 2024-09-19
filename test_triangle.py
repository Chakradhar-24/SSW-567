import unittest
from triangle import classify_triangle  # Import the function from your triangle function.

class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")
    
    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")
    
    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right")
    
    def test_right_isosceles_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 1.414213), "Isosceles and Right")
    
    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle")
    
    def test_large_right_triangle(self):
        self.assertEqual(classify_triangle(6, 8, 10), "Scalene and Right")
    
    def test_another_scalene(self):
        self.assertEqual(classify_triangle(7, 5, 9), "Scalene")

if __name__ == '__main__':
    unittest.main(exit=False)  # Prevents the test from causing the interpreter to exit
