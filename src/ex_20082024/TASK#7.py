### Task #7
#✅ Leap Year Checker:
#Create a program that determines whether a given year is a leap year.
#A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#Use an if-else statement to make this determination.

year = int(input("Enter the year : "))

leapyear = year % 4

leapyear1 = year %100

leapyear2 = year %400

if leapyear == 0 and leapyear1 !=0 and leapyear2 !=0 :
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
