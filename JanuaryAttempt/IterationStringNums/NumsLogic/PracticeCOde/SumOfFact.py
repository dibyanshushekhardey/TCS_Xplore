# write a program to print the sum of 1/1!  2/2! + ...
num = 1
sum = 0.0

while num <= 7:
    fact = 1
    for i in range(1, num+1):
        fact *= i
        i += 1
    sum = sum + (num/fact)
    num += 1

print("Sum of the series is {}".format(round(sum, 5)))
