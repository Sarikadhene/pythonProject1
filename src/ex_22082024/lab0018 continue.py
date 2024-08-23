#continue statement skips the currnet iteration of loop and
#moves to next iteration

for num in range(10):
    if num%2 ==0 :
        continue  #continue back to above for loop
    else :
        print(num, end=" " )

for num in range(10):
    if num % 2 == 0:
        pass  # continue back to above for loop
    else:
        print(num, end="")