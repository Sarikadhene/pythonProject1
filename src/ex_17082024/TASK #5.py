# Task #5
# Create a program that takes two numbers as input
# and prints whether the first number is greater than, less than, or equal to the second number.

num1 = int(input("Enter 1st number for comparision : "))
num2 = int(input("Enter 2nd number for comparision : "))

if (num1 > num2) :
    print(f"{num1} is greater than {num2} ")
elif (num1 < num2) :
    print(f"{num1} is less than {num2}")
else :
    print(f" {num1} is equal to {num2} ")
