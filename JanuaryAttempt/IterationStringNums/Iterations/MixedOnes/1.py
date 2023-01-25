n = int(input())

# condition 1
if n > 0:
    if n % 2 == 0:
        print("{} is an even natural number".format(n))
    else:
        print("{} is an odd natural number".format(n))
else:
    if n % 2 == 0:
        print("{} is an even number".format(n))
    else:
        print("{} is an odd number".format(n))