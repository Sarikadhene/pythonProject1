# Task #10 -
# ✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

i = int(input("Enter the number  :"))

j=1
print(i,end="! --> ")
for i in range(i,0, -1):
    print(i,end="")
    j=j*i
print(" -> ", j)


