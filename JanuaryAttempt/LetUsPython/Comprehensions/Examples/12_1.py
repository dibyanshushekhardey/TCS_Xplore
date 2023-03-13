'''
Using list comprehension, write a program to generate a list of numbers
in the range 2 to 50 that are divisible by 2 and 4
'''

l = [num for num in range(2, 51) if num % 2 == 0 and num % 4 == 0]
print(l)