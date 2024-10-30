"""
Module for classifying types of triangles based on side lengths.
"""

def classify_triangle(a, b, c):
    """
    Classifies a triangle based on the lengths of its sides.

    Parameters:
    a, b, c (int or float): The lengths of the triangle's three sides.

    Returns:
    str: A description of the triangle type (e.g., 'Equilateral', 'Isosceles and Right').
    """

    a, b, c = sorted([a, b, c])

    # Check if the sides form a valid triangle using the triangle inequality theorem
    if a + b <= c:
        return "Not a triangle"
    # Classify the triangle type
    if a == b == c:
        triangle_type = "Equilateral"
    elif b in (a, c):
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    # Check if it's a right triangle
    if round(a**2 + b**2, 6) == round(c**2, 6):
        triangle_type += " and Right"
    return triangle_type
