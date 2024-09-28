#Task #11 -
#✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

fibo= int(input("Enter number for Fibonaci series "))

num1=0
num2 =1
for fibo in range(fibo,0,-1) :
    num3=num1+num2
    print(num1 , end=" ")
    num1=num2
    num2=num3




