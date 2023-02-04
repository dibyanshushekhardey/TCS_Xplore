# WAP to print sum of even and odd digits
# of a number separately
# (Take a number as input from user)

number = int(input("Enter a number: "))

sum_even = 0
sum_odd = 0

while number > 0:
    rem = number % 10
    if rem % 2 == 0:
        sum_even = sum_even + rem
    else:
        sum_odd = sum_odd + rem
    number = number // 10

print("Sum of even digits: {}".format(sum_even))
print("Sum of odd digits: {}".format(sum_odd))