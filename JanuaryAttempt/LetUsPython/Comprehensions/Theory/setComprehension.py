# generate a set containing square of all numbers between 0 and 10
a={x**2 for x in range(10)}
print(a)

# from a set delete all numbers between 20 and 50
a={num for num in a if num > 20 and num < 50}
print(a)