# armstrong number
number = int(input("Enter a number: "))
sum = 0
temp = number
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if number == sum:
    print("{} is an Armstrong number".format(number))
else:
    print("{} is not an Armstrong number".format(number))