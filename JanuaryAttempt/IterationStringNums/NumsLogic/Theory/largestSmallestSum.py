# get the largest, smallest and sum of the digits in number

num = int(input("Enter the number: "))
largest_num = 0
smallest_num = 9
count = 0

while num > 0:
    remainder = num%10
    count = count + remainder
    if largest_num < remainder:
        largest_num = remainder
    elif smallest_num > remainder:
        smallest_num = remainder
    num = int(num/10)

print("Largest digit: {}".format(largest_num))
print("Smallest digit: {}".format(smallest_num))
print("Sum of digit: {}".format(count))