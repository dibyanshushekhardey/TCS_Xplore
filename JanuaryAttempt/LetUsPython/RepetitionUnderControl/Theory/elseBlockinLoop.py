num = int(input("Enter an inetger: "))
i = 2
while i <= num - 1:
    if num % i == 0:
        print(num, 'is not a prime number')
        break
    i += 1
else:
    print(num, 'is a prime number')