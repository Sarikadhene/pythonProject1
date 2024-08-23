### Task #8
# ✅ Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

side1 = float(input("Enter 1st side of triangle : "))
side2 = float(input("Enter 2nd side of triangle : "))
side3 = float(input("Enter 3rd side of triangle : "))

if side1 == side2 == side3:
    print("Length of All sides of triangle are equal therefore this is equilateral triangle")
elif side1 == side2 :
    print("two sides of triangle are equal therefore this is isosceles triangle")
elif side1 == side3 :
    print("two sides of triangle are equal therefore this is isosceles triangle")
elif side2 == side3:
    print("two sides of triangle are equal therefore this is isosceles triangle")
else :
    print("All sides of triangle are unequal therefore this is scalene triangle")
