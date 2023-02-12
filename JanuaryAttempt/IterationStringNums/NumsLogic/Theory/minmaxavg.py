# WAP to print the minimum and maximum number of all the numbers
# also print the average of all numbers entered
number = int(input("Enter the count you need: "))
total = 0.0
count = 0
maximum = 0
minimum = 0

print("Enter the numbers: ")
for i in range(number):
    num = int(input())
    count += 1
    total += num

    if i == 0:
        minimum = num
    if num < minimum:
        minimum = num
    elif num > maximum:
        maximum = num

print("Average: {}".format(total/number))
print("Maximum number: {}".format(maximum))
print("Minimum number: {}".format(minimum))