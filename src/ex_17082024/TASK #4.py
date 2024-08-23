# - Write a Python program to calculate the area of a circle given its radius using the formula
#  area=π×r^2``` ( Take pie as 3.14)

pi = 3.14
radius = float(input("enter the radius of circle : "))

Area = pi * pow(radius, 2)

print(f"Area of circle with the radius {radius} : {Area:.2f} square units")
