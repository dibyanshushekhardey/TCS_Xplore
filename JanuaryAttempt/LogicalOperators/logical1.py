# combining conditions
n = int(input("Enter the number:\n"))


# check if the number is natural and if it is even
if n > 0 and n % 2 == 0:
    print("AND: {number} is even natural".format(number=n))
else:
    print("AND: {number} is odd".format(number=n))

# check is number is natural and of it is even
if n > 0 and n % 2 == 1:
    print("OR: {number} is odd natural".format(number=n))
else:
    print("OR: {number} is even".format(number=n))
