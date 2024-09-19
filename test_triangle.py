import unittest  #Import the Unittest module
from triangle import classify_triangle  # Import the function from your triangle module.

class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(10, 10, 10), "Equilateral")
    
    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(7, 7, 10), "Isosceles")
    
    def test_another_scalene(self):
        self.assertEqual(classify_triangle(8, 7, 10), "Scalene")
    
    def test_right_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 7.07106781187), "Isosceles and Right")

    def test_large_right_triangle(self):
        self.assertEqual(classify_triangle(6, 8, 10), "Scalene and Right")

    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle( 2,3,6), "Not a triangle")
    
    def test_large_right_triangle_alt(self):
        self.assertEqual(classify_triangle(9,12,15), "Scalene and Right")
    
    

if __name__ == '__main__':
    unittest.main(exit=False)  # Prevents the test from causing the interpreter to exit
