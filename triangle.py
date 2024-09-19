def classify_triangle(a, b, c):
    # Sort the sides to simplify right triangle check (no need to check multiple Pythagorean conditions)
    a, b, c = sorted([a, b, c])

    # Check if the sides form a valid triangle using the triangle inequality theorem
    if a + b <= c:
        return "Not a triangle"

    # classify  the triangle type
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Check if it's a right triangle (since the sides are sorted, we only need to check a^2 + b^2 == c^2)
    #Also check the decimals point untill 6 digits so that we can get correct results for right triangle
    if round(a**2 + b**2, 6) == round(c**2, 6):
        triangle_type += " and Right"


    return triangle_type

